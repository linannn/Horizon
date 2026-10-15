import json
from pathlib import Path

from src.models import Config
from src.processing.profiles import ProfileRegistry


def test_daily_config_caps_repository_release_monitoring() -> None:
    config = json.loads(Path("data/config.github.json").read_text(encoding="utf-8"))
    github_sources = [source for source in config["sources"]["github"] if source["enabled"]]
    filtering = config["digest"]
    releases_group = filtering["category_groups"]["releases"]
    changelog = next(
        source
        for source in config["sources"]["rss"]
        if source["name"] == "GitHub Changelog"
    )

    assert {source["category"] for source in github_sources} == {"release-monitoring"}
    assert changelog["category"] == "release-monitoring"
    assert config["processing"]["profile_settings"]["tech-news"]["watch_score_threshold"] == 4.0
    assert filtering["max_watch_items"] == 4
    assert releases_group == {
        "name": "Project Releases",
        "limit": 2,
        "categories": ["release-monitoring"],
    }
    assert filtering["category_groups"]["discovery"]["limit"] == 4
    assert filtering["category_groups"]["engineering"]["limit"] == 4


def test_daily_config_includes_aihot_major_ai_feed() -> None:
    config = json.loads(Path("data/config.github.json").read_text(encoding="utf-8"))
    filtering = config["digest"]
    aihot = next(
        source for source in config["sources"]["rss"] if source["name"] == "AI 热榜"
    )

    assert aihot == {
        "name": "AI 热榜",
        "url": "https://aihot.virxact.com/feed/full.xml",
        "enabled": True,
        "category": "major-ai",
        "original_link_text": "阅读原文",
        "profile": "tech-news",
    }
    assert filtering["category_groups"]["major-ai"] == {
        "name": "Major AI Events",
        "limit": 5,
        "categories": ["major-ai"],
    }
    settings = config["processing"]["profile_settings"]["tech-news"]
    assert any("Major AI model" in topic for topic in settings["focus_topics"])


def test_daily_config_routes_sources_to_focused_profile_without_ai_classification() -> None:
    config = Config.model_validate_json(Path("data/config.github.json").read_text(encoding="utf-8"))
    profiles = ProfileRegistry.load(Path(config.processing.profiles_dir), config.processing.default_profile)
    profiles.validate_source_references(config.sources.model_dump(mode="json"))
    sources = [*config.sources.github, *config.sources.rss, config.sources.hackernews]
    for source in sources:
        if source.enabled:
            assert source.profile == "tech-news"
            assert config.processing.profile_settings[source.profile].focus_topics
    assert config.collection.time_window_hours == 24
    assert config.digest.max_items == 20
    assert config.digest.max_items_per_source == 2
    assert config.processing.profile_settings["tech-news"].threshold == 5.0
