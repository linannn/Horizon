"""Prompt construction for profile-driven content analysis."""

from typing import Optional, Sequence

from ...models import ContentItem
from ...processing.profiles import LoadedProfile
from .common import EVIDENCE_RULES, UNTRUSTED_INPUT_RULE

ANALYSIS_RULES = f"""You are a content curator evaluating an item under the supplied processing profile.

- {UNTRUSTED_INPUT_RULE}
- Base the analysis only on the supplied item and its metadata.
{EVIDENCE_RULES}
- Apply the profile's evaluation policy consistently."""


FOCUS_RULES = """When Reader Focus is provided:
- Judge focus relevance separately from general importance
- Source Category is only a routing hint and is not proof of focus relevance
- Set focus_relevant to true only when the item directly provides an AI coding tool, coding-agent capability, MCP/agent ecosystem update, practical AI engineering workflow, or developer-facing AI tool release
- A major AI model, research, or product announcement is focus relevant when it materially changes developer tool choices, agent capabilities, open-source availability, cost, context, or deployment decisions
- General AI industry news, model-only news, and AI security news are not focus relevant unless they materially change a coding or agent workflow
- General-purpose AI product vulnerabilities, enterprise AI monitoring or gateway products, and standalone safety or moderation models are not focus relevant, even when technically substantive
- Security fixes to AI coding tools and coding agents are focus relevant when they directly affect a developer's coding workflow
- Reusable security architecture for developers building agents may be focus relevant only when it provides concrete design primitives, not merely a vendor security product
- Pure model launches, pricing, benchmarks, or comparisons without material developer or agent impact must score 5 or lower
- Broad conceptual or theoretical AI pieces without an actionable tool, workflow, or engineering technique must score 6 or lower
- Scores of 7 or higher require an actionable tool, workflow, engineering technique, or decision-relevant major AI development directly relevant to the reader's focus
- Prefer practical releases, techniques, limitations, and engineering practices within the reader's focus

Judge substantive value separately:
- Set substantive to true only when the item contains at least one concrete, reusable, or decision-relevant takeaway backed by specific details
- Concrete product changes, reusable workflows, implementation details, measured engineering lessons, and specific limitations can be substantive
- Major releases or research with concrete capability, availability, cost, context, or deployment details can be substantive because they inform engineering decisions
- Set substantive to false for demos or vibe experiments without reusable implementation detail, promotional or opinion-only posts, and release entries whose body contains no meaningful changelog
- Treat ordinary bug fixes, dependency updates, and releases whose only change is adding model or provider support as routine maintenance
- Unless routine maintenance fixes a critical security, data-loss, compatibility, or measured performance problem, set substantive to false and score it 3 or lower
- A fun prototype or impressive output alone is not substantive
- Non-substantive items must score 4 or lower"""


def analysis_system_prompt(
    profile: LoadedProfile, focus_topics: Optional[Sequence[str]] = None
) -> str:
    focus_section = f"\n\n# Reader focus policy\n\n{FOCUS_RULES}" if focus_topics else ""
    focus_fields = (
        '\n  "focus_relevant": <true-or-false>,\n  "substantive": <true-or-false>,'
        if focus_topics else ""
    )
    return f"""{ANALYSIS_RULES}

# Profile policy

{profile.analysis_prompt}{focus_section}

# Output contract

Return valid JSON only:
{{
  "score": <number from 0 to 10>,{focus_fields}
  "reason": "<concise explanation>",
  "summary": "<one-sentence summary>",
  "tags": ["<tag>", "..."]
}}"""


def analysis_user_prompt(
    item: ContentItem,
    content_section: str,
    discussion_section: str,
    focus_topics: Optional[Sequence[str]] = None,
) -> str:
    focus_section = f"\nReader Focus: {', '.join(focus_topics)}" if focus_topics else ""
    return f"""Analyze the following content.

Title: {item.title}
Source: {item.source_type.value}
Source Category: {item.metadata.get("category") or "Unspecified"}
Author: {item.author or "Unknown"}
URL: {item.url}{focus_section}
{content_section}
{discussion_section}"""
