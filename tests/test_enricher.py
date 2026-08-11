import asyncio
import json
from datetime import datetime, timezone
from types import SimpleNamespace

from src.ai.enricher import ContentEnricher
from src.ai.prompts import CONTENT_ENRICHMENT_SYSTEM
from src.models import ContentItem, SourceType


def test_enrichment_searches_claim_first_and_keeps_primary_source(monkeypatch) -> None:
    calls = []

    async def complete(**kwargs):  # type: ignore[no-untyped-def]
        calls.append(kwargs)
        if len(calls) == 1:
            return json.dumps(
                {"queries": ["MCP stateless protocol", "MCP stateless protocol"]}
            )
        return json.dumps(
            {
                "title_en": "Stateless MCP reaches Workers",
                "title_zh": "无状态 MCP 可直接运行在 Workers 上",
                "whats_new_en": "MCP removed protocol sessions from the core request path.",
                "whats_new_zh": "MCP 从核心请求路径中移除了协议会话。",
                "why_it_matters_en": "Servers can use request-scoped infrastructure.",
                "why_it_matters_zh": "服务器可以使用请求级基础设施。",
                "key_details_en": "The change removes the required handshake.",
                "key_details_zh": "该变化移除了强制握手。",
                "background_en": "MCP connects agents to tools and data.",
                "background_zh": "MCP 用于连接智能体、工具和数据。",
                "community_discussion_en": "",
                "community_discussion_zh": "",
                "sources": [
                    "https://modelcontextprotocol.io/specification/2026-07-28",
                    "https://unrelated.example/article",
                ],
            }
        )

    client = SimpleNamespace(
        complete=complete,
        config=SimpleNamespace(enrichment_concurrency=1),
    )
    enricher = ContentEnricher(client)
    search_queries = []

    async def web_search(query, max_results=3):  # type: ignore[no-untyped-def]
        search_queries.append(query)
        if query == "MCP stateless protocol":
            return [
                {
                    "title": "MCP Specification",
                    "url": "https://modelcontextprotocol.io/specification/2026-07-28",
                    "body": "The protocol supports stateless requests.",
                }
            ]
        return []

    monkeypatch.setattr(enricher, "_web_search", web_search)
    item = ContentItem(
        id="rss:cloudflare:mcp-v2",
        source_type=SourceType.RSS,
        title="The next generation of MCP",
        url="https://blog.cloudflare.com/mcp-v2/",
        content="MCP is now a fully stateless protocol.",
        author="Cloudflare",
        published_at=datetime(2026, 8, 6, tzinfo=timezone.utc),
        ai_score=8.0,
        ai_reason="Directly relevant protocol update.",
        ai_summary="MCP now supports stateless server deployments.",
        ai_tags=["MCP", "Workers"],
    )

    asyncio.run(enricher._enrich_item(item))

    assert search_queries == ["The next generation of MCP", "MCP stateless protocol"]
    assert "**Primary Source:**" in calls[1]["user"]
    assert item.metadata["whats_new_zh"] == "MCP 从核心请求路径中移除了协议会话。"
    assert item.metadata["sources"] == [
        {
            "url": "https://blog.cloudflare.com/mcp-v2/",
            "title": "The next generation of MCP",
        },
        {
            "url": "https://modelcontextprotocol.io/specification/2026-07-28",
            "title": "MCP Specification",
        },
    ]


def test_enrichment_prompt_requires_numeric_and_source_consistency() -> None:
    assert "approved/rejected or detected/missed" in CONTENT_ENRICHMENT_SYSTEM
    assert "numerical and logical consistency" in CONTENT_ENRICHMENT_SYSTEM
    assert "Primary Source URL first" in CONTENT_ENRICHMENT_SYSTEM
    assert "non-overlapping" in CONTENT_ENRICHMENT_SYSTEM
