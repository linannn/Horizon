import asyncio
from datetime import datetime, timezone
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from src.ai.enricher import EnrichmentBatchResult
from src.models import (
    AIConfig,
    ClassificationResult,
    Config,
    ContentAnalysis,
    ContentArtifact,
    ContentBlock,
    ContentItem,
    ProcessingResult,
    SourcesConfig,
)
from src.orchestrator import HorizonOrchestrator
from src.storage.manager import StorageManager


def make_item(item_id):
    return ContentItem(
        id=item_id,
        source_type="rss",
        title=item_id,
        url=f"https://example.com/{item_id}",
        published_at=datetime.now(timezone.utc),
        profile="tech-news",
        processing=ProcessingResult(
            classification=ClassificationResult(profile="tech-news", method="source_override"),
            analysis=ContentAnalysis(score=8, reason="Release", summary="English fallback must not be published"),
        ),
    )


@pytest.mark.parametrize("all_failed", [False, True])
def test_daily_run_publishes_only_enriched_items_and_preserves_previous_post_on_failure(
    tmp_path, monkeypatch, all_failed
):
    config = Config(
        ai=AIConfig(provider="minimax", model="test", api_key_env="TEST_KEY", languages=["zh"]),
        sources=SourcesConfig(),
    )
    storage = StorageManager(str(tmp_path / "data"))
    orchestrator = HorizonOrchestrator(config, storage)
    notifier = SimpleNamespace(send_daily_summary=AsyncMock(), send_failure=AsyncMock())
    orchestrator.webhook_notifier = notifier
    items = [make_item("good"), make_item("failed")]
    monkeypatch.setattr(orchestrator, "fetch_all_sources", AsyncMock(return_value=items))

    async def unchanged(items, **kwargs):
        return items

    async def enrich(items):
        if all_failed:
            return EnrichmentBatchResult(failures={item.id: "Invalid artifact" for item in items})
        items[0].processing.artifacts["zh"] = ContentArtifact(
            language="zh",
            title="有效的中文资讯",
            blocks=[ContentBlock(id="summary", title="摘要", content="这是一条经过校验的中文摘要。", primary=True)],
        )
        return EnrichmentBatchResult(succeeded_ids=[items[0].id], failures={items[1].id: "Invalid tool plan"})

    monkeypatch.setattr(orchestrator, "analyze_items", unchanged)
    monkeypatch.setattr(orchestrator, "merge_topic_duplicates", unchanged)
    monkeypatch.setattr(orchestrator, "enrich_items", enrich)
    monkeypatch.chdir(tmp_path)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    post = tmp_path / "docs" / "_posts" / f"{today}-summary-zh.md"
    post.parent.mkdir(parents=True)
    post.write_text("Previously published digest", encoding="utf-8")

    if all_failed:
        with pytest.raises(RuntimeError, match="enrichment failed"):
            asyncio.run(orchestrator.run())
        assert post.read_text(encoding="utf-8") == "Previously published digest"
        assert not list(storage.summaries_dir.glob("*.md"))
        notifier.send_daily_summary.assert_not_awaited()
        notifier.send_failure.assert_awaited_once()
    else:
        asyncio.run(orchestrator.run())
        published = post.read_text(encoding="utf-8")
        assert "从 2 条内容中筛选出 1 条重要资讯" in published
        assert "有效的中文资讯" in published
        assert "English fallback" not in published
        assert "https://example.com/failed" not in published
        delivered = notifier.send_daily_summary.await_args.kwargs["important_items"]
        assert [item.id for item in delivered] == ["good"]
