import asyncio
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest
from pydantic import ValidationError
from rich.console import Console

from src.models import (
    AIConfig,
    CategoryGroupConfig,
    ClassificationResult,
    Config,
    ContentAnalysis,
    ContentItem,
    DigestConfig,
    ProcessingConfig,
    ProcessingResult,
    ProfileSettingsConfig,
    SourceType,
    SourcesConfig,
)
from src.orchestrator import HorizonOrchestrator, _build_post_front_matter
from src.processing import ProfileRegistry


def make_item(item_id: str, score: float, category: str | None) -> ContentItem:
    metadata = {"category": category} if category is not None else {}
    return ContentItem(
        id=item_id,
        source_type=SourceType.RSS,
        title=item_id,
        url=f"https://example.com/{item_id}",
        published_at=datetime.now(timezone.utc),
        metadata=metadata,
        profile="tech-news",
        processing=ProcessingResult(
            classification=ClassificationResult(
                profile="tech-news", method="source_override"
            ),
            analysis=ContentAnalysis(
                score=score, reason="test", summary=item_id
            ),
        ),
    )


def make_orchestrator(digest: DigestConfig) -> HorizonOrchestrator:
    orchestrator = HorizonOrchestrator.__new__(HorizonOrchestrator)
    orchestrator.config = SimpleNamespace(
        digest=digest,
        processing=ProcessingConfig(
            profile_settings={
                "tech-news": ProfileSettingsConfig(threshold=7.0),
                "tech-blog": ProfileSettingsConfig(
                    threshold=4.0, topic_dedup=False
                ),
                "finance-news": ProfileSettingsConfig(threshold=7.0),
            }
        ),
    )
    orchestrator.console = Console(record=True)
    return orchestrator


def test_unconfigured_balanced_digest_preserves_old_behavior() -> None:
    items = [make_item("lower", 7.0, "ai"), make_item("higher", 9.0, "finance")]
    result = make_orchestrator(DigestConfig()).apply_balanced_digest(items)

    assert result.enabled is False
    assert result.items is items


def test_category_groups_apply_limits_and_default_group_limit() -> None:
    filtering = DigestConfig(
        category_groups={
            "ai": CategoryGroupConfig(limit=2, categories=["ai", "ml"]),
            "finance": CategoryGroupConfig(limit=1, categories=["finance"]),
        },
        default_group_limit=1,
    )
    items = [
        make_item("ai-low", 7.0, "ai"),
        make_item("finance-low", 6.0, "finance"),
        make_item("other-high", 9.5, "world"),
        make_item("ai-high", 9.0, "ml"),
        make_item("finance-high", 8.5, "finance"),
        make_item("ai-mid", 8.0, "ai"),
        make_item("other-low", 5.0, None),
    ]

    result = make_orchestrator(filtering).apply_balanced_digest(items)

    assert [item.id for item in result.items] == [
        "other-high",
        "ai-high",
        "finance-high",
        "ai-mid",
    ]
    assert result.group_counts == {"other": 1, "ai": 2, "finance": 1}


def test_max_items_applies_after_group_limits() -> None:
    filtering = DigestConfig(
        max_items=2,
        category_groups={
            "ai": CategoryGroupConfig(limit=2, categories=["ai"]),
            "finance": CategoryGroupConfig(limit=2, categories=["finance"]),
        },
    )
    items = [
        make_item("finance", 8.0, "finance"),
        make_item("ai-top", 10.0, "ai"),
        make_item("ai-second", 9.0, "ai"),
    ]

    result = make_orchestrator(filtering).apply_balanced_digest(items)

    assert [item.id for item in result.items] == ["ai-top", "ai-second"]
    assert result.group_counts == {"ai": 2}


def test_max_items_works_without_category_groups() -> None:
    filtering = DigestConfig(max_items=1)
    items = [make_item("lower", 7.0, None), make_item("higher", 9.0, None)]

    result = make_orchestrator(filtering).apply_balanced_digest(items)

    assert [item.id for item in result.items] == ["higher"]


def test_filter_items_skips_ai_topic_dedup_for_disabled_profile(monkeypatch) -> None:
    orchestrator = make_orchestrator(DigestConfig())
    orchestrator.profiles = ProfileRegistry.load(
        Path(__file__).resolve().parents[1] / "profiles", "tech-news"
    )
    items = [make_item("first", 9.0, "blog"), make_item("second", 8.0, "blog")]
    for item in items:
        item.profile = "tech-blog"
        item.processing.classification.profile = "tech-blog"

    async def unexpected_dedup(input_items, *, log=True):  # type: ignore[no-untyped-def]
        raise AssertionError("AI topic dedup must be skipped for tech-blog")

    monkeypatch.setattr(orchestrator, "merge_topic_duplicates", unexpected_dedup)

    result = asyncio.run(
        orchestrator.filter_items(items, topic_dedup=True, apply_balance=False, log=False)
    )

    assert [item.id for item in result.items] == ["first", "second"]


def test_runtime_threshold_override_takes_priority() -> None:
    orchestrator = make_orchestrator(DigestConfig())
    item = make_item("item", 7.5, "ai")

    assert orchestrator.passes_profile_filter(item)
    assert not orchestrator.passes_profile_filter(item, threshold=8.0)


def test_profile_without_threshold_bypasses_score_filter() -> None:
    orchestrator = make_orchestrator(DigestConfig())
    orchestrator.config.processing.profile_settings = {}

    assert orchestrator.passes_profile_filter(make_item("item", 1.0, "ai"))


def test_rejects_settings_for_unknown_profile() -> None:
    config = Config(
        ai=AIConfig(
            provider="openai",
            model="test",
            api_key_env="TEST_API_KEY",
        ),
        sources=SourcesConfig(),
        processing=ProcessingConfig(
            profile_settings={
                "missing": ProfileSettingsConfig(threshold=7.0)
            }
        ),
    )

    with pytest.raises(ValueError, match="Unknown processing profile: missing"):
        HorizonOrchestrator(config, SimpleNamespace())


def test_appends_profiles_missing_from_configured_order() -> None:
    config = Config(
        ai=AIConfig(
            provider="openai",
            model="test",
            api_key_env="TEST_API_KEY",
        ),
        sources=SourcesConfig(),
        digest=DigestConfig(profile_order=["tech-news", "tech-blog"]),
    )

    HorizonOrchestrator(config, SimpleNamespace())

    assert config.digest.profile_order == [
        "tech-news",
        "tech-blog",
        "ai-creator",
        "finance-news",
    ]


def test_rejects_unknown_profile_order() -> None:
    profile_order = ["tech-news", "tech-blog", "finance-news", "missing"]
    config = Config(
        ai=AIConfig(
            provider="openai",
            model="test",
            api_key_env="TEST_API_KEY",
        ),
        sources=SourcesConfig(),
        digest=DigestConfig(profile_order=profile_order),
    )

    with pytest.raises(ValueError, match="contains unknown profiles.*missing"):
        HorizonOrchestrator(config, SimpleNamespace())


def test_duplicate_category_warns_and_first_group_wins() -> None:
    filtering = DigestConfig(
        category_groups={
            "first": CategoryGroupConfig(limit=1, categories=["shared"]),
            "second": CategoryGroupConfig(limit=2, categories=["shared"]),
        }
    )
    orchestrator = make_orchestrator(filtering)

    result = orchestrator.apply_balanced_digest(
        [make_item("top", 9.0, "shared"), make_item("second", 8.0, "shared")]
    )

    assert [item.id for item in result.items] == ["top"]
    assert result.duplicate_categories == ["shared"]
    assert "using 'first'" in orchestrator.console.export_text()


@pytest.mark.parametrize(
    "kwargs",
    [
        {"max_items": 0},
        {"max_items_per_source": 0},
        {"max_watch_items": -1},
        {"default_group_limit": 0},
        {"category_groups": {"ai": {"limit": 0, "categories": ["ai"]}}},
        {"category_groups": {"ai": {"limit": 1, "categories": []}}},
        {"profile_order": ["tech-news", "tech-news"]},
        {"profile_order": ["tech-news", ""]},
    ],
)
def test_digest_config_rejects_invalid_values(kwargs) -> None:
    with pytest.raises(ValidationError):
        DigestConfig(**kwargs)


def test_run_applies_balanced_digest_before_enrichment(tmp_path, monkeypatch) -> None:
    config = Config(
        ai=AIConfig(
            provider="openai",
            model="test",
            api_key_env="TEST_API_KEY",
            languages=[],
        ),
        sources=SourcesConfig(),
        processing=ProcessingConfig(
            profile_settings={
                "tech-news": ProfileSettingsConfig(threshold=7.0)
            }
        ),
        digest=DigestConfig(
            max_items=1,
            category_groups={
                "ai": CategoryGroupConfig(limit=1, categories=["ai"]),
                "finance": CategoryGroupConfig(limit=1, categories=["finance"]),
            },
        ),
    )
    storage = SimpleNamespace()
    orchestrator = HorizonOrchestrator(config, storage)
    items = [
        make_item("ai", 9.0, "ai"),
        make_item("finance", 8.0, "finance"),
        make_item("below-threshold", 6.0, "ai"),
    ]
    enriched_ids: list[str] = []

    async def fetch_all_sources(since):  # type: ignore[no-untyped-def]
        return items

    async def analyze_content(input_items):  # type: ignore[no-untyped-def]
        return input_items

    async def merge_topic_duplicates(input_items, *, log=True):  # type: ignore[no-untyped-def]
        return input_items

    async def expand_twitter_discussion(input_items):  # type: ignore[no-untyped-def]
        return None

    async def enrich_important_items(input_items):  # type: ignore[no-untyped-def]
        enriched_ids.extend(item.id for item in input_items)

    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)
    monkeypatch.setattr(orchestrator, "analyze_items", analyze_content)
    monkeypatch.setattr(orchestrator, "merge_topic_duplicates", merge_topic_duplicates)
    monkeypatch.setattr(orchestrator, "_expand_twitter_discussion", expand_twitter_discussion)
    monkeypatch.setattr(orchestrator, "enrich_items", enrich_important_items)
    monkeypatch.chdir(tmp_path)

    asyncio.run(orchestrator.run())

    assert enriched_ids == ["ai"]


def test_run_balances_after_twitter_reanalysis(tmp_path, monkeypatch) -> None:
    config = Config(
        ai=AIConfig(
            provider="openai",
            model="test",
            api_key_env="TEST_API_KEY",
            languages=[],
        ),
        sources=SourcesConfig(),
        digest=DigestConfig(max_items=1),
    )
    orchestrator = HorizonOrchestrator(config, SimpleNamespace())
    items = [make_item("first", 9.0, "ai"), make_item("second", 8.0, "ai")]
    enriched_ids: list[str] = []

    async def fetch_all_sources(since):  # type: ignore[no-untyped-def]
        return items

    async def analyze_content(input_items):  # type: ignore[no-untyped-def]
        return input_items

    async def merge_topic_duplicates(input_items, *, log=True):  # type: ignore[no-untyped-def]
        return input_items

    async def expand_twitter_discussion(input_items):  # type: ignore[no-untyped-def]
        input_items[0].processing.analysis.score = 7.0
        input_items[1].processing.analysis.score = 10.0
        input_items.sort(
            key=lambda item: item.processing.analysis.score or 0,
            reverse=True,
        )

    async def enrich_important_items(input_items):  # type: ignore[no-untyped-def]
        enriched_ids.extend(item.id for item in input_items)

    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)
    monkeypatch.setattr(orchestrator, "analyze_items", analyze_content)
    monkeypatch.setattr(orchestrator, "merge_topic_duplicates", merge_topic_duplicates)
    monkeypatch.setattr(orchestrator, "_expand_twitter_discussion", expand_twitter_discussion)
    monkeypatch.setattr(orchestrator, "enrich_items", enrich_important_items)
    monkeypatch.chdir(tmp_path)

    asyncio.run(orchestrator.run())

    assert enriched_ids == ["second"]


def test_fill_remaining_slots_prevents_today_digest_from_stopping_at_six() -> None:
    filtering = DigestConfig(
        max_items=20,
        fill_remaining_slots=True,
        category_groups={
            "focus": CategoryGroupConfig(limit=12, categories=["ai"]),
            "discovery": CategoryGroupConfig(limit=2, categories=["discovery"]),
            "engineering": CategoryGroupConfig(
                limit=3,
                categories=["engineering"],
                allow_backfill=True,
            ),
        },
    )
    items = [make_item("focus", 10.0, "ai")]
    items.extend(
        make_item(f"discovery-{index}", 9.9 - index * 0.1, "discovery")
        for index in range(5)
    )
    items.extend(
        make_item(f"engineering-{index}", 9.4 - index * 0.1, "engineering")
        for index in range(8)
    )

    result = make_orchestrator(filtering).apply_balanced_digest(items)

    assert len(result.items) == 11
    assert result.group_counts == {"focus": 1, "discovery": 2, "engineering": 8}
    assert result.backfill_count == 5


def test_balanced_digest_limits_items_from_one_source() -> None:
    filtering = DigestConfig(max_items=20, max_items_per_source=2)
    items = [
        make_item("decoder-top", 10.0, "ai-news"),
        make_item("decoder-second", 9.0, "ai-news"),
        make_item("decoder-third", 8.0, "ai-news"),
        make_item("other", 7.0, "ai-news"),
    ]
    for item in items[:3]:
        item.metadata["feed_name"] = "The Decoder"
    items[3].metadata["feed_name"] = "Other"

    result = make_orchestrator(filtering).apply_balanced_digest(items)

    assert [item.id for item in result.items] == [
        "decoder-top",
        "decoder-second",
        "other",
    ]
    assert result.source_limit_removed == 1


def test_aggregated_feed_source_limit_uses_original_sources() -> None:
    filtering = DigestConfig(max_items=20, max_items_per_source=2)
    items = [
        make_item("qwen", 10.0, "major-ai"),
        make_item("xai", 9.0, "major-ai"),
        make_item("anthropic", 8.0, "major-ai"),
    ]
    for item, source in zip(items, ["Qwen", "xAI", "Anthropic"]):
        item.metadata["feed_name"] = "AI 热榜"
        item.metadata["origin_domain"] = "x.com"
        item.metadata["origin_source"] = source

    result = make_orchestrator(filtering).apply_balanced_digest(items)

    assert [item.id for item in result.items] == ["qwen", "xai", "anthropic"]
    assert result.source_limit_removed == 0


def test_filter_items_requires_reader_focus_relevance() -> None:
    orchestrator = make_orchestrator(DigestConfig(max_watch_items=0))
    orchestrator.config.processing.profile_settings["tech-news"] = ProfileSettingsConfig(
        threshold=5.0, focus_topics=["AI coding tools"]
    )
    relevant = make_item("relevant", 5.0, "ai-coding")
    relevant.processing.analysis.focus_relevant = True
    relevant.processing.analysis.substantive = True
    unrelated = make_item("unrelated", 10.0, "ai-news")
    unrelated.processing.analysis.focus_relevant = False
    unknown = make_item("unknown", 10.0, "ai-news")

    result = asyncio.run(
        orchestrator.filter_items(
            [unrelated, unknown, relevant],
            topic_dedup=False,
            log=False,
        )
    )

    assert [item.id for item in result.items] == ["relevant"]
    assert result.focus_relevance_count == 1
    assert result.focus_relevance_removed == 2


def test_filter_items_rejects_non_substantive_vibe_demo() -> None:
    orchestrator = make_orchestrator(DigestConfig(max_watch_items=0))
    orchestrator.config.processing.profile_settings["tech-news"] = ProfileSettingsConfig(
        threshold=5.0, focus_topics=["AI coding tools"]
    )
    useful = make_item("useful", 5.0, "ai-coding")
    useful.processing.analysis.focus_relevant = True
    useful.processing.analysis.substantive = True
    demo = make_item("tolkien-to-3d-vibe-test", 10.0, "ai-coding")
    demo.title = "Karpathy turns Tolkien into a 3D scene as a vibe test"
    demo.processing.analysis.focus_relevant = True
    demo.processing.analysis.substantive = False

    result = asyncio.run(
        orchestrator.filter_items(
            [demo, useful],
            topic_dedup=False,
            log=False,
        )
    )

    assert [item.id for item in result.items] == ["useful"]
    assert result.substantive_count == 1
    assert result.substantive_removed == 1


def test_filter_items_adds_bounded_lower_priority_focus_updates() -> None:
    orchestrator = make_orchestrator(DigestConfig(max_watch_items=3))
    orchestrator.config.processing.profile_settings["tech-news"] = ProfileSettingsConfig(
        threshold=5.0, focus_topics=["AI coding tools"], watch_score_threshold=4.0
    )
    core = make_item("core", 7.0, "ai-coding")
    core.processing.analysis.focus_relevant = True
    core.processing.analysis.substantive = True
    watch_high = make_item("watch-high", 4.8, "ai-coding")
    watch_high.processing.analysis.focus_relevant = True
    watch_high.processing.analysis.substantive = False
    watch_middle = make_item("watch-middle", 4.5, "engineering-practice")
    watch_middle.processing.analysis.focus_relevant = True
    watch_middle.processing.analysis.substantive = True
    watch_low = make_item("watch-low", 4.0, "agent-ecosystem")
    watch_low.processing.analysis.focus_relevant = True
    watch_low.processing.analysis.substantive = False
    watch_overflow = make_item("watch-overflow", 4.0, "ai-coding")
    watch_overflow.processing.analysis.focus_relevant = True
    watch_overflow.processing.analysis.substantive = False
    below_watch = make_item("below-watch", 3.9, "ai-coding")
    below_watch.processing.analysis.focus_relevant = True
    below_watch.processing.analysis.substantive = False
    inconsistent_demo = make_item("inconsistent-demo", 10.0, "ai-coding")
    inconsistent_demo.processing.analysis.focus_relevant = True
    inconsistent_demo.processing.analysis.substantive = False
    unrelated = make_item("unrelated", 4.9, "ai-news")
    unrelated.processing.analysis.focus_relevant = False
    unrelated.processing.analysis.substantive = True

    result = asyncio.run(
        orchestrator.filter_items(
            [
                unrelated,
                watch_low,
                watch_overflow,
                core,
                below_watch,
                watch_middle,
                inconsistent_demo,
                watch_high,
            ],
            topic_dedup=False,
            log=False,
        )
    )

    assert [item.id for item in result.items] == [
        "core",
        "watch-high",
        "watch-middle",
        "watch-low",
    ]
    assert result.threshold_count == 1
    assert result.watch_eligible_count == 4
    assert result.watch_selected_count == 3


def test_topic_dedup_uses_source_url_and_excerpt_for_reposted_technique(
    monkeypatch,
) -> None:
    filtering = DigestConfig()
    orchestrator = make_orchestrator(filtering)
    orchestrator.config.ai = SimpleNamespace()
    original = make_item("llm-open-source-tools", 8.0, "engineering-practice")
    original.title = "LLMs may make open-source developer tools more viable"
    original.content = (
        "Developers can keep local changes and use a nightly cron job to rebase "
        "them on upstream with an AI coding agent."
    )
    original.metadata["feed_name"] = "Simon Willison"
    original.processing.analysis.summary = "Use an agent in cron to maintain local tool forks."
    repost = make_item("crawshaw-cron", 7.0, "engineering-practice")
    repost.title = "David Crawshaw uses cron to let AI maintain software branches"
    repost.content = (
        "A reusable prompt fetches upstream, rebases local modifications, runs "
        "tests, and replaces the current version every night."
    )
    repost.metadata["feed_name"] = "Latent Space"
    repost.processing.analysis.summary = "A nightly coding agent rebases and tests a local fork."
    captured: dict[str, str] = {}

    async def complete(**kwargs):  # type: ignore[no-untyped-def]
        captured.update(kwargs)
        return '{"duplicates": [[0, 1]]}'

    monkeypatch.setattr(
        "src.orchestrator.create_ai_client",
        lambda config: SimpleNamespace(complete=complete),
    )

    result = asyncio.run(
        orchestrator.merge_topic_duplicates([original, repost], log=False)
    )

    assert [item.id for item in result] == ["llm-open-source-tools"]
    assert "Source: rss:Simon Willison" in captured["user"]
    assert "URL: https://example.com/llm-open-source-tools" in captured["user"]
    assert "Excerpt: Developers can keep local changes" in captured["user"]
    assert "Source: rss:Latent Space" in captured["user"]
    assert "Excerpt: A reusable prompt fetches upstream" in captured["user"]


def test_topic_dedup_merges_same_repo_semver_prereleases_before_ai(monkeypatch) -> None:
    filtering = DigestConfig()
    orchestrator = make_orchestrator(filtering)
    orchestrator.config.ai = SimpleNamespace()
    preview = make_item("preview", 8.0, "release-monitoring")
    preview.source_type = SourceType.GITHUB
    preview.content = "Preview fixes retry hangs."
    preview.metadata.update(
        {"repo": "google-gemini/gemini-cli", "tag": "v0.55.0-preview.1"}
    )
    nightly = make_item("nightly", 7.0, "release-monitoring")
    nightly.source_type = SourceType.GITHUB
    nightly.content = "Nightly adds PR generator infrastructure."
    nightly.metadata.update(
        {
            "repo": "google-gemini/gemini-cli",
            "tag": "v0.55.0-nightly.20260806.g761f604c1",
        }
    )
    next_version = make_item("next-version", 6.0, "release-monitoring")
    next_version.source_type = SourceType.GITHUB
    next_version.metadata.update(
        {"repo": "google-gemini/gemini-cli", "tag": "v0.56.0-preview.1"}
    )

    async def complete(**kwargs):  # type: ignore[no-untyped-def]
        return '{"duplicates": []}'

    monkeypatch.setattr(
        "src.orchestrator.create_ai_client",
        lambda config: SimpleNamespace(complete=complete),
    )

    result = asyncio.run(
        orchestrator.merge_topic_duplicates([preview, nightly, next_version], log=False)
    )

    assert [item.id for item in result] == ["preview", "next-version"]
    assert result[0].metadata["merged_release_tags"] == [
        "v0.55.0-preview.1",
        "v0.55.0-nightly.20260806.g761f604c1",
    ]
    assert "Nightly adds PR generator infrastructure." in (result[0].content or "")
    assert preview.content == "Preview fixes retry hangs."


def test_build_post_front_matter_localizes_chinese_page_metadata() -> None:
    result = _build_post_front_matter("2026-08-07", "zh")

    assert 'title: "Horizon 每日速递：2026-08-07"' in result
    assert 'description: "AI 精选的技术与研究日报"' in result
    assert "lang: zh" in result
    assert "locale: zh-CN" in result



@pytest.mark.parametrize("kwargs", [
    {"watch_score_threshold": 4.0},
    {"threshold": 5.0, "watch_score_threshold": 5.0},
])
def test_watch_threshold_requires_explicit_higher_profile_threshold(kwargs):
    with pytest.raises(ValidationError):
        ProfileSettingsConfig(**kwargs)


def test_topic_dedup_prompt_collapses_overlapping_announcement_families():
    from src.ai.prompting.deduplication import TOPIC_DEDUP_SYSTEM

    assert "same underlying feature rollout or announcement family" in TOPIC_DEDUP_SYSTEM
    assert "key facts substantially overlap" in TOPIC_DEDUP_SYSTEM
    assert "quote, translate, or restate that same technique" in TOPIC_DEDUP_SYSTEM
    assert "same repository" in TOPIC_DEDUP_SYSTEM
    assert "package or SDK release" in TOPIC_DEDUP_SYSTEM


def test_twitter_reanalysis_reapplies_focus_and_preserves_watch_items(monkeypatch):
    orchestrator = make_orchestrator(DigestConfig(max_watch_items=2))
    orchestrator.config.processing.profile_settings["tech-news"] = ProfileSettingsConfig(
        threshold=5.0, watch_score_threshold=4.0, focus_topics=["AI coding tools"]
    )
    primary = make_item("primary", 8.0, "ai")
    demoted = make_item("demoted", 7.0, "ai")
    watch = make_item("watch", 4.5, "ai")
    for item in (primary, demoted, watch):
        item.processing.analysis.focus_relevant = True
        item.processing.analysis.substantive = True
    watch.processing.analysis.substantive = False

    async def expand(items):
        primary.processing.analysis.focus_relevant = False
        demoted.processing.analysis.score = 4.8
        demoted.processing.analysis.substantive = False

    monkeypatch.setattr(orchestrator, "_expand_twitter_discussion", expand)
    result = asyncio.run(orchestrator.select_digest_items(
        [primary, demoted, watch], topic_dedup=False, log=False,
    ))
    assert [item.id for item in result.items] == ["demoted", "watch"]
    assert result.watch_selected_count == 2
    assert result.eligible_count == 2


def test_focus_gate_is_scoped_to_configured_profile():
    orchestrator = make_orchestrator(DigestConfig())
    orchestrator.config.processing.profile_settings["tech-news"] = ProfileSettingsConfig(
        threshold=5.0, focus_topics=["AI coding tools"]
    )
    focused = make_item("focused", 8.0, "ai")
    blog = make_item("blog", 6.0, "engineering")
    blog.processing.classification.profile = "tech-blog"
    result = asyncio.run(orchestrator.filter_items(
        [focused, blog], topic_dedup=False, log=False,
    ))
    assert [item.id for item in result.items] == ["blog"]
