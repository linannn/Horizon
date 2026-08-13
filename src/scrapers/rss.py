"""RSS feed scraper implementation."""

import calendar
import hashlib
import logging
import os
import re
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import List, Optional
from urllib.parse import urlparse

import feedparser
import httpx
from bs4 import BeautifulSoup

from .base import BaseScraper
from ..extractors import ExtractorRegistry
from ..models import ContentItem, SourceType, RSSSourceConfig

logger = logging.getLogger(__name__)


class RSSScraper(BaseScraper):
    """Scraper for RSS/Atom feeds."""

    def __init__(
        self,
        sources: List[RSSSourceConfig],
        http_client: httpx.AsyncClient,
        extractors: Optional[ExtractorRegistry] = None,
    ):
        """Initialize RSS scraper.

        Args:
            sources: List of RSS feed configurations
            http_client: Shared async HTTP client
            extractors: Optional registry of content extractors for full article fetching
        """
        super().__init__({"sources": sources}, http_client)
        self._extractors = extractors

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch RSS feed items.

        Args:
            since: Only fetch items published after this time

        Returns:
            List[ContentItem]: Fetched content items
        """
        items = []
        sources = self.config["sources"]

        for source in sources:
            if not source.enabled:
                continue

            feed_items = await self._fetch_feed(source, since)
            items.extend(feed_items)

        return items

    async def _fetch_feed(
        self, source: RSSSourceConfig, since: datetime
    ) -> List[ContentItem]:
        """Fetch items from a single RSS feed.

        Args:
            source: RSS feed configuration
            since: Only fetch items after this time

        Returns:
            List[ContentItem]: Feed content items
        """
        items = []

        try:
            # Expand environment variables in URL (e.g. ${LWN_TOKEN})
            feed_url = re.sub(
                r"\$\{(\w+)\}",
                lambda m: os.environ.get(m.group(1), m.group(0)).strip(),
                str(source.url),
            )

            # Fetch feed content
            response = await self.client.get(feed_url, follow_redirects=True)
            response.raise_for_status()

            # Parse feed
            feed = feedparser.parse(response.text)

            for entry in feed.entries:
                # Parse published date
                published_at = self._parse_date(entry)
                if not published_at or published_at < since:
                    continue

                # Generate unique ID from feed URL and entry ID
                feed_id = str(source.url).split("//")[1].replace("/", "_")
                entry_id = entry.get("id", entry.get("link", ""))
                entry_hash = hashlib.sha256(str(entry_id).encode("utf-8")).hexdigest()[
                    :16
                ]

                # Extract content
                content = self._extract_content(entry)
                aggregation_url = entry.get("link", str(source.url))
                item_url = self._extract_original_link(
                    entry, source.original_link_text
                ) or str(aggregation_url)
                author = entry.get("author", source.name)

                if source.content_extractor and self._extractors:
                    extractor = self._extractors.get(source.content_extractor)
                    if extractor:
                        if item_url:
                            full = await extractor.extract(item_url, self.client)
                            if full:
                                content = full

                metadata = {
                    "feed_name": source.name,
                    "category": source.category,
                    "tags": [tag.term for tag in entry.get("tags", [])],
                }
                if item_url != str(aggregation_url):
                    metadata["aggregation_url"] = str(aggregation_url)
                    origin_domain = urlparse(item_url).hostname
                    if origin_domain:
                        metadata["origin_domain"] = origin_domain
                    author_detail = entry.get("author_detail", {})
                    origin_source = author_detail.get("name")
                    if origin_source:
                        metadata["origin_source"] = origin_source
                        author = origin_source

                item = ContentItem(
                    id=self._generate_id("rss", feed_id, entry_hash),
                    source_type=SourceType.RSS,
                    title=entry.get("title", "Untitled"),
                    url=item_url,
                    content=content,
                    author=author,
                    published_at=published_at,
                    metadata=metadata,
                )
                items.append(item)

        except httpx.HTTPError as e:
            logger.warning("Error fetching RSS feed %s: %s", source.name, e)
        except Exception as e:
            logger.warning("Error parsing RSS feed %s: %s", source.name, e)

        return items

    @staticmethod
    def _extract_original_link(entry: dict, link_text: Optional[str]) -> Optional[str]:
        """Extract a linked original article from an aggregator feed entry."""
        if not link_text:
            return None

        content = RSSScraper._extract_content(entry)
        soup = BeautifulSoup(content, "html.parser")
        for link in soup.find_all("a", href=True):
            if link.get_text(strip=True) != link_text:
                continue
            href = str(link["href"])
            if urlparse(href).scheme in {"http", "https"}:
                return href
        return None

    def _parse_date(self, entry: dict) -> datetime:
        """Parse publication date from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            datetime: Parsed publication date or None
        """
        # Try different date fields
        for field in ["published", "updated", "created"]:
            if field in entry:
                try:
                    # Try parsing structured time first
                    if f"{field}_parsed" in entry and entry[f"{field}_parsed"]:
                        return datetime.fromtimestamp(
                            calendar.timegm(entry[f"{field}_parsed"]), tz=timezone.utc
                        )
                    # Fallback to string parsing
                    date_str = entry[field]
                    return parsedate_to_datetime(date_str)
                except Exception:
                    continue

        return None

    @staticmethod
    def _extract_content(entry: dict) -> str:
        """Extract text content from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            str: Extracted text content
        """
        # Try different content fields
        if "summary" in entry:
            return entry.summary
        if "description" in entry:
            return entry.description
        if "content" in entry and entry.content:
            # content is usually a list
            return entry.content[0].get("value", "")

        return ""
