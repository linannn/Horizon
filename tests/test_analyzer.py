import asyncio
import json
from datetime import datetime, timezone
from types import SimpleNamespace

import pytest
import src.ai.analyzer as analyzer_module
from src.ai.analyzer import ContentAnalyzer
from src.ai.prompts import CONTENT_ANALYSIS_SYSTEM, TOPIC_DEDUP_SYSTEM
from src.models import ContentItem, SourceType


def _make_item(item_id: str) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=SourceType.RSS,
        title=f"Item {item_id}",
        url="https://example.com/item",
        published_at=datetime(2026, 4, 26, tzinfo=timezone.utc),
    )


def test_analyze_batch_does_not_sleep_by_default(monkeypatch):
    analyzer = ContentAnalyzer(SimpleNamespace())
    items = [_make_item("rss:test:1"), _make_item("rss:test:2")]
    sleep_calls = []

    async def fake_analyze_item(item):
        item.ai_score = 8.0

    async def fake_sleep(seconds):
        sleep_calls.append(seconds)

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)
    monkeypatch.setattr(analyzer_module.asyncio, "sleep", fake_sleep)

    result = asyncio.run(analyzer.analyze_batch(items))

    assert len(result) == 2
    assert sleep_calls == []


def test_analyze_batch_sleeps_between_items_when_throttle_configured(monkeypatch):
    client = SimpleNamespace(config=SimpleNamespace(throttle_sec=1.5))
    analyzer = ContentAnalyzer(client)
    items = [_make_item("rss:test:1"), _make_item("rss:test:2"), _make_item("rss:test:3")]
    sleep_calls = []

    async def fake_analyze_item(item):
        item.ai_score = 8.0

    async def fake_sleep(seconds):
        sleep_calls.append(seconds)

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)
    monkeypatch.setattr(analyzer_module.asyncio, "sleep", fake_sleep)

    asyncio.run(analyzer.analyze_batch(items))

    assert sleep_calls == [1.5, 1.5]


def test_analyze_batch_concurrent_processing(monkeypatch):
    """Verify that higher concurrency allows overlapping item processing."""
    client = SimpleNamespace(config=SimpleNamespace(analysis_concurrency=3))
    analyzer = ContentAnalyzer(client)
    items = [_make_item(f"rss:test:{i}") for i in range(5)]
    active_count = 0
    max_active = 0

    async def fake_analyze_item(item):
        nonlocal active_count, max_active
        active_count += 1
        max_active = max(max_active, active_count)
        await asyncio.sleep(0.05)  # Small delay to allow overlap
        active_count -= 1

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)

    asyncio.run(analyzer.analyze_batch(items))

    assert max_active == 3
    assert all(item.ai_score is None for item in items)  # None because fake_analyze_item doesn't set it


def test_analyze_batch_concurrent_preserves_order(monkeypatch):
    """Verify that analyze_batch preserves input order in results."""
    client = SimpleNamespace(config=SimpleNamespace(analysis_concurrency=3))
    analyzer = ContentAnalyzer(client)
    items = [_make_item(f"rss:test:{i}") for i in range(5)]

    async def fake_analyze_item(item):
        item.ai_score = float(item.id.split(":")[-1]) * 10

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)

    result = asyncio.run(analyzer.analyze_batch(items))

    assert [item.id for item in result] == [item.id for item in items]


def test_analyze_item_accepts_valid_result():
    result = {
        "score": 8.5,
        "focus_relevant": True,
        "substantive": True,
        "reason": "Relevant",
        "summary": "A useful update",
        "tags": ["ai", "research"],
    }
    client = SimpleNamespace(complete=lambda **kwargs: None)

    async def complete(**kwargs):
        return json.dumps(result)

    client.complete = complete
    item = _make_item("rss:test:valid")

    asyncio.run(ContentAnalyzer(client)._analyze_item(item))

    assert item.ai_score == 8.5
    assert item.ai_focus_relevant is True
    assert item.ai_substantive is True
    assert item.ai_reason == "Relevant"
    assert item.ai_summary == "A useful update"
    assert item.ai_tags == ["ai", "research"]


def test_analyze_item_includes_reader_focus_and_source_category():
    result = {
        "score": 8.0,
        "focus_relevant": True,
        "substantive": True,
        "reason": "Directly relevant",
        "summary": "A useful coding-agent update",
        "tags": ["ai-coding", "agents"],
    }
    captured = {}

    async def complete(**kwargs):
        captured.update(kwargs)
        return json.dumps(result)

    item = _make_item("rss:test:focused")
    item.metadata["category"] = "ai-coding"

    asyncio.run(
        ContentAnalyzer(
            SimpleNamespace(complete=complete),
            focus_topics=["AI coding tools", "MCP"],
        )._analyze_item(item)
    )

    assert "Source Category: ai-coding" in captured["user"]
    assert "Reader Focus: AI coding tools, MCP" in captured["user"]
    assert "Set focus_relevant to true only" in captured["system"]
    assert "must score 5 or lower" in captured["system"]
    assert "actionable tool, workflow, or engineering technique" in captured["system"]
    assert '"focus_relevant"' in captured["user"]
    assert '"substantive"' in captured["user"]
    assert "demos or vibe experiments" in captured["system"]
    assert (
        "Treat ordinary bug fixes, dependency updates, and releases whose only "
        "change is adding model or provider support as routine maintenance"
        in captured["system"]
    )
    assert (
        "Unless routine maintenance fixes a critical security, data-loss, "
        "compatibility, or measured performance problem, set substantive to false "
        "and score it 3 or lower"
        in captured["system"]
    )


def test_topic_dedup_prompt_collapses_overlapping_announcement_families():
    assert "same underlying feature rollout or announcement family" in TOPIC_DEDUP_SYSTEM
    assert "key facts substantially overlap" in TOPIC_DEDUP_SYSTEM
    assert "quote, translate, or restate that same technique" in TOPIC_DEDUP_SYSTEM
    assert "same repository" in TOPIC_DEDUP_SYSTEM
    assert "package or SDK release" in TOPIC_DEDUP_SYSTEM


def test_analysis_prompt_excludes_adjacent_ai_security_from_reader_focus():
    assert "General-purpose AI product vulnerabilities" in CONTENT_ANALYSIS_SYSTEM
    assert "enterprise AI monitoring or gateway products" in CONTENT_ANALYSIS_SYSTEM
    assert "Security fixes to AI coding tools" in CONTENT_ANALYSIS_SYSTEM
    assert "concrete design primitives" in CONTENT_ANALYSIS_SYSTEM


def test_analysis_prompt_keeps_major_ai_events_with_developer_impact():
    assert "major AI model, research, or product announcement" in CONTENT_ANALYSIS_SYSTEM
    assert "developer tool choices, agent capabilities" in CONTENT_ANALYSIS_SYSTEM
    assert "open-source availability, cost, context, or deployment" in (
        CONTENT_ANALYSIS_SYSTEM
    )


@pytest.mark.parametrize(
    "result",
    [
        {"score": 11, "reason": "high", "summary": "summary", "tags": []},
        {"score": float("nan"), "reason": "bad", "summary": "summary", "tags": []},
        {"score": 5, "reason": 123, "summary": "summary", "tags": []},
        {"score": 5, "reason": "ok", "summary": "summary", "tags": ["ok", 1]},
        {"score": 5, "reason": "ok", "tags": []},
    ],
)
def test_analyze_item_malformed_json_result_uses_fallback(result):
    async def complete(**kwargs):
        return json.dumps(result)

    item = _make_item("rss:test:invalid")

    asyncio.run(ContentAnalyzer(SimpleNamespace(complete=complete))._analyze_item(item))

    assert item.ai_score == 0.0
    assert item.ai_substantive is False
    assert item.ai_reason == "Analysis response parse failed"
    assert item.ai_summary == item.title
    assert item.ai_tags == []
