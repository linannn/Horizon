import json
from pathlib import Path


def test_daily_config_caps_repository_release_monitoring() -> None:
    config = json.loads(Path("data/config.github.json").read_text(encoding="utf-8"))
    github_sources = [source for source in config["sources"]["github"] if source["enabled"]]
    filtering = config["filtering"]
    releases_group = filtering["category_groups"]["releases"]
    changelog = next(
        source
        for source in config["sources"]["rss"]
        if source["name"] == "GitHub Changelog"
    )

    assert {source["category"] for source in github_sources} == {"release-monitoring"}
    assert changelog["category"] == "release-monitoring"
    assert filtering["watch_score_threshold"] == 4.0
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
    filtering = config["filtering"]
    aihot = next(
        source for source in config["sources"]["rss"] if source["name"] == "AI 热榜"
    )

    assert aihot == {
        "name": "AI 热榜",
        "url": "https://aihot.virxact.com/feed/full.xml",
        "enabled": True,
        "category": "major-ai",
        "original_link_text": "阅读原文",
    }
    assert filtering["category_groups"]["major-ai"] == {
        "name": "Major AI Events",
        "limit": 5,
        "categories": ["major-ai"],
    }
    assert any("Major AI model" in topic for topic in filtering["focus_topics"])
