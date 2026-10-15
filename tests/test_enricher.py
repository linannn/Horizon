import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest

from src.ai.enricher import ContentEnricher
from src.ai.prompting.enrichment import GROUNDING_RULES
from src.models import (
    ArtifactSource,
    ClassificationResult,
    ContentAnalysis,
    ContentArtifact,
    ContentBlock,
    ContentItem,
    ProcessingResult,
    SourceType,
)
from src.processing import ProfileRegistry
from src.processing.profiles import LoadedProfile
from src.processing.tools import ToolRegistry, ToolResult


PROFILES = ProfileRegistry.load(
    Path(__file__).resolve().parents[1] / "profiles", "tech-news"
)


def make_item() -> ContentItem:
    return ContentItem(
        id="rss:test:item",
        source_type=SourceType.RSS,
        title="A technical release",
        url="https://example.com/item",
        content="A project released a new architecture.",
        published_at=datetime.now(timezone.utc),
        profile="tech-news",
        processing=ProcessingResult(
            classification=ClassificationResult(
                profile="tech-news", method="source_override"
            ),
            analysis=ContentAnalysis(
                score=8.5,
                reason="Important release",
                summary="A new architecture was released.",
                tags=["systems"],
            ),
        ),
    )


def make_tool_only_profiles() -> ProfileRegistry:
    profile = PROFILES.get("tech-news")
    background = next(
        block for block in profile.definition.enrichment.blocks
        if block.id == "background"
    )
    enrichment = profile.definition.enrichment.model_copy(update={"blocks": [background]})
    definition = profile.definition.model_copy(update={"enrichment": enrichment})
    tool_only_profile = LoadedProfile(
        definition=definition,
        match_prompt=profile.match_prompt,
        analysis_prompt=profile.analysis_prompt,
        enrichment_prompt=profile.enrichment_prompt,
    )
    return ProfileRegistry({profile.id: tool_only_profile}, profile.id)


def queued_ai(responses):
    requests = []
    responses = iter(responses)

    async def complete(**kwargs):
        requests.append(kwargs)
        return next(responses)

    return SimpleNamespace(complete=complete), requests


class RecordingTools:
    names = {"web_search", "history_search"}

    def __init__(self):
        self.calls = []

    async def execute(self, request_id, block_id, tool, arguments, current_item=None):
        self.calls.append((block_id, tool, arguments))
        return ToolResult(request_id, block_id, tool, [])


class FakeTools:
    names = {"web_search", "history_search"}

    async def execute(self, request_id, block_id, tool, arguments, current_item=None):
        assert block_id == "background"
        assert tool == "web_search"
        assert arguments["query"] in {"A technical release", "project architecture"}
        return ToolResult(
            request_id=request_id,
            block_id=block_id,
            tool=tool,
            results=[
                {
                    "title": "Project documentation",
                    "url": "https://docs.example.com/project",
                    "text": "Architecture background.",
                }
            ],
        )


def test_enrichment_generates_blocks_and_validated_sources():
    responses = iter(
        [
            json.dumps(
                {
                    "tool_requests": [
                        {
                            "block_id": "background",
                            "tool": "web_search",
                            "arguments": {"query": "project architecture"},
                            "purpose": "Explain the existing architecture",
                        }
                    ]
                }
            ),
            json.dumps(
                {
                    "title": "新架構發佈",
                    "blocks": [
                        {
                            "id": "summary",
                            "title": "摘要",
                            "content": "項目發佈了新的架構，它改變了系統設計，並採用了新的邊界。",
                            "source_refs": [],
                        }
                    ],
                }
            ),
            json.dumps(
                {
                    "title": "新架構發佈",
                    "blocks": [
                        {
                            "id": "summary",
                            "type": "section",
                            "title": "摘要",
                            "content": "项目发布了新的架构，它改变了系统设计，并采用了新的边界。",
                            "source_refs": [],
                        },
                        {
                            "id": "background",
                            "type": "section",
                            "title": "未隔离的背景",
                            "content": "这个版本应被丢弃。",
                            "source_refs": [],
                        },
                    ],
                }
            ),
            json.dumps(
                {
                    "title": "",
                    "block": {
                        "id": "background",
                        "type": "section",
                        "title": "背景",
                        "content": "旧架构的背景信息。",
                        "source_refs": ["tool-1"],
                    },
                }
            ),
        ]
    )
    requests = []

    async def complete(**kwargs):
        requests.append(kwargs)
        return next(responses)

    item = make_item()
    enricher = ContentEnricher(
        SimpleNamespace(complete=complete),
        PROFILES,
        ["zh"],
        tools=FakeTools(),
    )
    asyncio.run(enricher._enrich_item(item))

    artifact = item.processing.artifacts["zh"]
    assert artifact.title == "新架构发布"
    assert artifact.blocks[0].content == "项目发布了新的架构，它改变了系统设计，并采用了新的边界。"
    assert [block.id for block in artifact.blocks] == [
        "summary",
        "background",
    ]
    assert artifact.blocks[-1].title == "背景"
    assert artifact.blocks[0].primary is True
    assert artifact.blocks[1].primary is False
    assert artifact.blocks[-1].source_refs == ["tool-1-1"]
    assert artifact.sources[0].url == str(item.url)
    assert artifact.sources[1].url == "https://docs.example.com/project"
    assert len(requests) == 4
    assert "explicitly mentioned in the item" in requests[0]["system"]
    assert "Treat the source item as the primary account" in requests[1]["system"]
    assert "Simplified Chinese (language tag `zh`)" in requests[1]["system"]
    assert "Treat the source item as the primary account" in requests[3]["system"]
    assert "https://docs.example.com/project" not in requests[1]["user"]
    assert "https://docs.example.com/project" in requests[3]["user"]
    assert "# Already generated blocks" in requests[3]["user"]
    assert "項目發佈了新的架構，它改變了系統設計，並採用了新的邊界。" in requests[3]["user"]


def test_enrichment_rejects_tool_on_unapproved_block():
    response = json.dumps(
        {
            "tool_requests": [
                {
                    "block_id": "summary",
                    "tool": "web_search",
                    "arguments": {"query": "unapproved"},
                    "purpose": "Rewrite the news",
                }
            ]
        }
    )
    ai_client, requests = queued_ai([response, response])

    enricher = ContentEnricher(
        ai_client,
        PROFILES,
        ["zh"],
        tools=FakeTools(),
    )

    with pytest.raises(ValueError, match="Invalid enrichment tool plan") as exc_info:
        asyncio.run(enricher._enrich_item(make_item()))

    assert len(requests) == 2
    assert "not allowed" in str(exc_info.value.__cause__)
    assert "not allowed" in requests[1]["user"]


def test_enrichment_repairs_invalid_tool_plan_before_executing_any_tool():
    responses = iter(
        [
            json.dumps({"tool_requests": [
                {
                    "block_id": "background",
                    "tool": "web_search",
                    "arguments": {"query": "project architecture"},
                    "purpose": "Find project context",
                },
                {
                    "block_id": "summary",
                    "tool": "web_search",
                    "arguments": {"query": "unapproved"},
                    "purpose": "Rewrite the news",
                },
            ]}),
            json.dumps({"tool_requests": [
                {
                    "block_id": "background",
                    "tool": "web_search",
                    "arguments": {"query": "project architecture"},
                    "purpose": "Find project context",
                }
            ]}),
        ]
    )
    ai_client, requests = queued_ai(responses)
    tools = RecordingTools()

    enricher = ContentEnricher(
        ai_client, PROFILES, ["en"], tools=tools
    )

    results = asyncio.run(
        enricher._plan_and_execute_tools(make_item(), PROFILES.get("tech-news"))
    )

    assert len(requests) == 2
    assert "not allowed" in requests[1]["user"]
    assert [call[0] for call in tools.calls] == ["background", "background"]
    assert all(call[0] != "summary" for call in tools.calls)
    assert [result.block_id for result in results] == ["background", "background"]


def test_enrichment_repairs_invalid_web_search_query_before_execution():
    responses = iter(
        [
            json.dumps({"tool_requests": [
                {
                    "block_id": "background",
                    "tool": "web_search",
                    "arguments": {"query": "   "},
                    "purpose": "Find project context",
                }
            ]}),
            json.dumps({"tool_requests": []}),
        ]
    )
    ai_client, requests = queued_ai(responses)
    tools = RecordingTools()

    enricher = ContentEnricher(
        ai_client, PROFILES, ["en"], tools=tools
    )

    results = asyncio.run(
        enricher._plan_and_execute_tools(make_item(), PROFILES.get("tech-news"))
    )

    assert len(requests) == 2
    assert "non-empty query" in requests[1]["user"]
    assert tools.calls == []
    assert results == []


def test_enrichment_rejects_malformed_tool_plan():
    async def complete(**kwargs):
        return "[]"

    enricher = ContentEnricher(
        SimpleNamespace(complete=complete),
        PROFILES,
        ["zh"],
        tools=FakeTools(),
    )

    with pytest.raises(ValueError, match="tool plan"):
        asyncio.run(enricher._enrich_item(make_item()))


def test_enrichment_repairs_malformed_tool_plan_once():
    responses = iter(
        [
            "[]",
            json.dumps({"tool_requests": []}),
            json.dumps(
                {
                    "title": "Technical release",
                    "blocks": [
                        {
                            "id": "summary",
                            "type": "section",
                            "title": "Summary",
                            "content": "A complete summary.",
                            "source_refs": [],
                        },
                        {
                            "id": "background",
                            "type": "section",
                            "title": "Background",
                            "content": "Context for the release.",
                            "source_refs": [],
                        }
                    ],
                }
            ),
        ]
    )
    requests = []

    async def complete(**kwargs):
        requests.append(kwargs)
        return next(responses)

    item = make_item()
    enricher = ContentEnricher(
        SimpleNamespace(complete=complete),
        PROFILES,
        ["en"],
        tools=FakeTools(),
    )

    asyncio.run(enricher._enrich_item(item))

    assert len(requests) == 3
    assert all(request["temperature"] == 0 for request in requests)
    assert requests[1]["temperature"] == 0
    assert item.processing.artifacts["en"].blocks[0].id == "summary"
    assert [source.url for source in item.processing.artifacts["en"].sources] == [
        str(item.url)
    ]


def _artifact_response(invalid_field=None):
    title = "AI release"
    summary_title = "AI update"
    summary_content = "A new version is available."
    if invalid_field == "artifact_title":
        title = "…"
    elif invalid_field == "block_title":
        summary_title = "…"
    elif invalid_field == "block_content":
        summary_content = "..."
    return json.dumps({
        "title": title,
        "blocks": [
            {
                "id": "summary",
                "title": summary_title,
                "content": summary_content,
                "source_refs": [],
            },
            {
                "id": "background",
                "title": "Background",
                "content": "The release changes the system architecture.",
                "source_refs": [],
            },
        ],
    })


@pytest.mark.parametrize(
    ("invalid_field", "persistent"),
    [
        (field, persistent)
        for field in ("artifact_title", "block_title", "block_content")
        for persistent in (False, True)
    ],
)
def test_enrichment_repairs_or_rejects_ellipsis_artifact_fields(
    invalid_field, persistent
):
    ai_client, requests = queued_ai([
        json.dumps({"tool_requests": []}),
        _artifact_response(invalid_field),
        _artifact_response(invalid_field if persistent else None),
    ])
    item = make_item()
    enricher = ContentEnricher(
        ai_client, PROFILES, ["en"], tools=FakeTools()
    )

    if persistent:
        with pytest.raises(ValueError, match="Invalid enrichment artifact"):
            asyncio.run(enricher._enrich_item(item))
    else:
        asyncio.run(enricher._enrich_item(item))

    assert len(requests) == 3
    assert "not satisfy the output contract" in requests[2]["user"]
    assert "only punctuation" in requests[2]["user"]
    if persistent:
        assert "en" not in item.processing.artifacts
    else:
        assert item.processing.artifacts["en"].title == "AI release"


def _header_response(invalid_field=None):
    title = "AI release"
    block_title = "Background"
    block_content = "The earlier system architecture provides useful context."
    if invalid_field == "header_title":
        title = "…"
    elif invalid_field == "block_title":
        block_title = "!!!"
    elif invalid_field == "block_content":
        block_content = "..."
    return json.dumps({
        "title": title,
        "block": {
            "id": "background",
            "title": block_title,
            "content": block_content,
            "source_refs": [],
        },
    })


@pytest.mark.parametrize(
    ("invalid_field", "persistent"),
    [
        (field, persistent)
        for field in ("header_title", "block_title", "block_content")
        for persistent in (False, True)
    ],
)
def test_enrichment_repairs_or_rejects_ellipsis_header_fields(
    invalid_field, persistent
):
    ai_client, requests = queued_ai([
        json.dumps({"tool_requests": [{
            "block_id": "background",
            "tool": "web_search",
            "arguments": {"query": "project architecture"},
            "purpose": "Find project context",
        }]}),
        _header_response(invalid_field),
        _header_response(invalid_field if persistent else None),
    ])
    item = make_item()
    tools = RecordingTools()
    enricher = ContentEnricher(
        ai_client,
        make_tool_only_profiles(),
        ["en"],
        tools=tools,
    )

    if persistent:
        with pytest.raises(ValueError, match="Invalid enrichment block: background"):
            asyncio.run(enricher._enrich_item(item))
    else:
        asyncio.run(enricher._enrich_item(item))

    assert len(requests) == 3
    assert "not satisfy the output contract" in requests[2]["user"]
    assert "only punctuation" in requests[2]["user"]
    assert len(tools.calls) == 2
    if persistent:
        assert "en" not in item.processing.artifacts
    else:
        assert item.processing.artifacts["en"].title == "AI release"
        assert item.processing.artifacts["en"].blocks[0].title == "Background"


def test_enrichment_repairs_empty_blog_block_once():
    responses = iter(
        [
            json.dumps(
                {
                    "title": "A technical story",
                    "blocks": [
                        {
                            "id": "background",
                            "title": " ",
                            "content": "",
                            "source_refs": [],
                        },
                        {
                            "id": "solution",
                            "title": "Solution and results",
                            "content": "The author explains the implementation.",
                            "source_refs": [],
                        },
                        {
                            "id": "takeaway",
                            "title": "Takeaway",
                            "content": "The approach is useful in bounded cases.",
                            "source_refs": [],
                        }
                    ],
                }
            ),
            json.dumps(
                {
                    "title": "A technical story",
                    "blocks": [
                        {
                            "id": "background",
                            "title": "Background",
                            "content": "The author frames the original problem and constraints.",
                            "source_refs": [],
                        },
                        {
                            "id": "solution",
                            "title": "Solution and results",
                            "content": "The author explains the implementation and its effects.",
                            "source_refs": [],
                        },
                        {
                            "id": "takeaway",
                            "title": "Takeaway",
                            "content": "The approach is useful in bounded cases.",
                            "source_refs": [],
                        }
                    ],
                }
            ),
        ]
    )
    requests = []

    async def complete(**kwargs):
        requests.append(kwargs)
        return next(responses)

    item = make_item()
    item.profile = "tech-blog"
    item.processing.classification.profile = "tech-blog"
    enricher = ContentEnricher(
        SimpleNamespace(complete=complete),
        PROFILES,
        ["en"],
        tools=FakeTools(),
    )

    asyncio.run(enricher._enrich_item(item))

    assert len(requests) == 2
    assert requests[1]["temperature"] == 0
    assert "corrected JSON object" in requests[1]["user"]
    assert [
        block.id for block in item.processing.artifacts["en"].blocks
    ] == ["background", "solution", "takeaway"]
    assert all(
        not block.primary for block in item.processing.artifacts["en"].blocks
    )


def test_enrichment_repairs_schema_type_used_as_blog_block_id():
    responses = iter(
        [
            json.dumps(
                {
                    "title": "A technical story",
                    "blocks": [
                        {
                            "id": "section",
                            "type": "section",
                            "title": "Background",
                            "content": "A complete but misidentified background block.",
                            "source_refs": [],
                        },
                        {
                            "id": "solution",
                            "title": "Solution and results",
                            "content": "The implementation produced a measured result.",
                            "source_refs": [],
                        },
                        {
                            "id": "takeaway",
                            "title": "Takeaway",
                            "content": "The method has a clear bounded use.",
                            "source_refs": [],
                        }
                    ],
                }
            ),
            json.dumps(
                {
                    "title": "A technical story",
                    "blocks": [
                        {
                            "id": "background",
                            "title": "Background",
                            "content": "The corrected background and constraints.",
                            "source_refs": [],
                        },
                        {
                            "id": "solution",
                            "title": "Solution and results",
                            "content": "The implementation produced a measured result.",
                            "source_refs": [],
                        },
                        {
                            "id": "takeaway",
                            "title": "Takeaway",
                            "content": "The method has a clear bounded use.",
                            "source_refs": [],
                        }
                    ],
                }
            ),
        ]
    )
    requests = []

    async def complete(**kwargs):
        requests.append(kwargs)
        return next(responses)

    item = make_item()
    item.profile = "tech-blog"
    item.processing.classification.profile = "tech-blog"
    enricher = ContentEnricher(
        SimpleNamespace(complete=complete),
        PROFILES,
        ["en"],
        tools=FakeTools(),
    )

    asyncio.run(enricher._enrich_item(item))

    assert len(requests) == 2
    assert "unknown blocks: section" in requests[1]["user"]
    assert item.processing.artifacts["en"].blocks[0].id == "background"


def test_failed_reenrichment_removes_stale_target_artifact():
    async def complete(**kwargs):
        return json.dumps(
            {
                "title": "A technical story",
                "blocks": [
                    {
                        "id": "story",
                        "type": "section",
                        "title": "",
                        "content": "",
                        "source_refs": [],
                    }
                ],
            }
        )

    item = make_item()
    item.profile = "tech-blog"
    item.processing.classification.profile = "tech-blog"
    item.processing.artifacts["en"] = ContentArtifact(
        language="en",
        title="Stale story",
    )
    enricher = ContentEnricher(
        SimpleNamespace(complete=complete),
        PROFILES,
        ["en"],
        tools=FakeTools(),
    )

    with pytest.raises(ValueError, match="Invalid enrichment artifact"):
        asyncio.run(enricher._enrich_item(item))

    assert "en" not in item.processing.artifacts


def test_enrichment_rejects_cross_block_source_reference():
    block = ContentBlock(
        id="summary",
        type="section",
        title="News",
        content="Content",
        source_refs=["tool-1-1"],
    )
    tool_result = ToolResult(
        request_id="tool-1",
        block_id="background",
        tool="web_search",
        results=[
            {
                "title": "Source",
                "url": "https://example.com/source",
                "text": "Context",
            }
        ],
    )

    with pytest.raises(ValueError, match="unknown source refs"):
        ContentEnricher._validate_blocks(
            [block], PROFILES.get("tech-news"), [tool_result]
        )


def test_enrichment_rejects_empty_required_block():
    block = ContentBlock(
        id="summary",
        type="section",
        title=" ",
        content="",
        source_refs=[],
    )

    with pytest.raises(ValueError, match="cannot be empty"):
        ContentEnricher._validate_blocks(
            [block], PROFILES.get("tech-news"), []
        )


@pytest.mark.parametrize(
    ("title", "content"),
    [("…", "Valid content."), ("Valid title", "!!!")],
)
def test_enrichment_rejects_placeholder_text_in_final_blocks(title, content):
    block = ContentBlock(
        id="background",
        type="section",
        title=title,
        content=content,
        source_refs=[],
    )

    with pytest.raises(ValueError, match="cannot be empty"):
        ContentEnricher._validate_blocks(
            [block], make_tool_only_profiles().get("tech-news"), []
        )


def test_enrichment_accepts_short_chinese_text_in_final_blocks():
    block = ContentBlock(
        id="background",
        type="section",
        title="AI",
        content="新",
        source_refs=[],
    )

    ContentEnricher._validate_blocks(
        [block], make_tool_only_profiles().get("tech-news"), []
    )


def test_enrichment_batch_reports_failure_without_discarding_successes():
    async def complete(**kwargs):
        raise RuntimeError("AI unavailable")

    successful_item = make_item()
    failed_item = make_item().model_copy(update={"id": "rss:test:failed"})
    enricher = ContentEnricher(
        SimpleNamespace(complete=complete),
        PROFILES,
        ["zh"],
        tools=FakeTools(),
    )

    async def enrich_item(item):  # type: ignore[no-untyped-def]
        if item.id == failed_item.id:
            raise RuntimeError("AI unavailable")

    enricher._enrich_item = enrich_item  # type: ignore[method-assign]

    result = asyncio.run(enricher.enrich_batch([successful_item, failed_item]))

    assert result.status == "partial_failure"
    assert result.succeeded_ids == [successful_item.id]
    assert result.failed_ids == [failed_item.id]
    assert result.failures[failed_item.id] == "RuntimeError: AI unavailable"


def test_history_search_reuses_one_call_for_both_languages(tmp_path, monkeypatch):
    (tmp_path / "horizon-2026-04-01-en.md").write_text(
        "### [Atlas preview](https://example.com/preview) ⭐️ 8/10\n\n"
        "Atlas preview requires manual batch configuration.\n\n---\n",
        encoding="utf-8",
    )
    tools = ToolRegistry(tmp_path)
    tool_calls = []
    execute = tools.execute

    async def record_execute(**kwargs):
        tool_calls.append(kwargs)
        return await execute(**kwargs)

    monkeypatch.setattr(tools, "execute", record_execute)
    requests = []

    async def complete(**kwargs):
        requests.append(kwargs)
        if kwargs["system"].startswith("# Tool planning"):
            return json.dumps({"tool_requests": [
                {"block_id": "background", "tool": "history_search",
                 "arguments": {"query": query}, "purpose": "Find the earlier version"}
                for query in ("Atlas preview", "Atlas batch")
            ]})
        if "Generate only block `background`" in kwargs["system"]:
            assert "Atlas preview requires manual batch configuration." in kwargs["user"]
            return json.dumps({"block": {
                "id": "background", "title": "Earlier coverage",
                "content": "The April 1 digest covered the preview's manual batch configuration.",
                "source_refs": ["tool-1-1"],
            }})
        assert "manual batch configuration" not in kwargs["user"]
        return json.dumps({"title": "Atlas release", "blocks": [{
            "id": "summary", "title": "Summary", "content": "Atlas now automates batching.",
        }]})

    item = make_item()
    item.published_at = datetime(2026, 4, 2, tzinfo=timezone.utc)
    enricher = ContentEnricher(SimpleNamespace(complete=complete), PROFILES, ["en", "zh"], tools=tools)

    asyncio.run(enricher._enrich_item(item))

    assert len(tool_calls) == 1
    assert tool_calls[0]["current_item"] is item
    # One existing planning call, then base and background generation per language.
    assert len(requests) == 5
    for language in ("en", "zh"):
        artifact = item.processing.artifacts[language]
        assert artifact.sources[0].url == str(item.url)
        assert artifact.sources[1].url == "https://example.com/preview"
        assert artifact.sources[1].title.startswith("2026-04-01")
        assert artifact.blocks[-1].source_refs == ["tool-1-1"]


def test_enrichment_searches_claim_first_and_deduplicates_before_limit():
    queries = []

    async def complete(**kwargs):
        return json.dumps({"tool_requests": [
            {"block_id": "background", "tool": "web_search",
             "arguments": {"query": query}, "purpose": "Verify the release"}
            for query in (
                " a TECHNICAL   release ",
                "project architecture",
                " Project  Architecture ",
                "architecture limitations",
                "unneeded fourth query",
            )
        ]})

    class RecordingTools:
        names = {"web_search", "history_search"}

        async def execute(self, request_id, block_id, tool, arguments, current_item=None):
            queries.append(arguments["query"])
            return ToolResult(request_id, block_id, tool, [])

    enricher = ContentEnricher(
        SimpleNamespace(complete=complete), PROFILES, ["en"], tools=RecordingTools()
    )
    asyncio.run(enricher._plan_and_execute_tools(make_item(), PROFILES.get("tech-news")))

    assert queries == [
        "A technical release", "project architecture", "architecture limitations"
    ]


def test_enrichment_keeps_primary_and_all_cited_supporting_sources():
    item = make_item()
    sources = {
        source_id: ArtifactSource(id=source_id, title=source_id, url=url)
        for source_id, url in (
            ("tool-1-1", str(item.url)),
            ("tool-1-2", "https://docs.example.com/release"),
            ("tool-2-1", "https://docs.example.com/release"),
            ("tool-2-2", "https://docs.example.com/limitations"),
            ("tool-2-3", "https://example.com/extra"),
        )
    }
    blocks = [ContentBlock(
        id="background", title="Background", content="Grounded context.",
        source_refs=list(sources),
    )]

    selected = ContentEnricher._select_sources(item, blocks, sources)

    assert [source.url for source in selected] == [
        str(item.url), "https://docs.example.com/release",
        "https://docs.example.com/limitations", "https://example.com/extra",
    ]
    assert blocks[0].source_refs == ["primary", "tool-1-2", "tool-2-2", "tool-2-3"]


def test_enrichment_prompt_requires_numeric_and_source_consistency():
    assert "approved/rejected or detected/missed" in GROUNDING_RULES
    assert "numerical and logical consistency" in GROUNDING_RULES
    assert "Primary Source URL first" in GROUNDING_RULES
    assert "non-overlapping" in GROUNDING_RULES


def test_enrichment_preserves_same_query_evidence_for_separate_blocks():
    async def complete(**kwargs):
        return json.dumps({"tool_requests": [
            {"block_id": block_id, "tool": "web_search",
             "arguments": {"query": "project architecture"},
             "purpose": "Verify this block's facts"}
            for block_id in ("background", "impact")
        ]})

    class RecordingTools:
        names = {"web_search", "history_search"}

        async def execute(self, request_id, block_id, tool, arguments, current_item=None):
            return ToolResult(request_id, block_id, tool, [{
                "title": arguments["query"], "url": "https://docs.example.com/project",
                "text": "Architecture background.",
            }])

    enricher = ContentEnricher(
        SimpleNamespace(complete=complete), PROFILES, ["en"], tools=RecordingTools()
    )
    results = asyncio.run(
        enricher._plan_and_execute_tools(make_item(), PROFILES.get("tech-news"))
    )

    assert [(result.block_id, result.results[0]["title"]) for result in results] == [
        ("background", "A technical release"),
        ("background", "project architecture"),
        ("impact", "project architecture"),
    ]
