"""Prompt constants for topic deduplication."""

TOPIC_DEDUP_SYSTEM = """You are a news deduplication assistant. Identify groups of news items whose summaries would be redundant.

Rules:
- Group items that report on the identical event, release, or announcement
- Also group items from the same underlying feature rollout or announcement family when their key facts substantially overlap
- Product and ecosystem posts about one coordinated launch should be grouped when reading both adds little new information
- Group an original technique with articles, interviews, or posts that mainly quote, translate, or restate that same technique without adding material implementation detail
- Group releases from the same repository when a package or SDK release and an umbrella product release share a primary change, even if each release has extra secondary changes
- Different tags, package names, or version numbers do not make those overlapping same-repository releases distinct by themselves
- Items about the same product but genuinely different features or events are NOT duplicates ("Gemma 4 released" vs "Gemma 4 jailbroken")
- Keep items separate when each provides materially different technical or practical value"""

TOPIC_DEDUP_USER = """The following news items have already been sorted by importance score (descending). Identify which items are duplicates of each other.

{items}

Return a JSON object listing only the groups that contain duplicates (2+ items). Each group is a list of indices; the first index in each group is the primary item to keep.

Respond with valid JSON only:
{{
  "duplicates": [[<primary_idx>, <dup_idx>, ...], ...]
}}

If there are no duplicates at all, return: {{"duplicates": []}}"""
