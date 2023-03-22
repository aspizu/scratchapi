from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .lib import print  # type: ignore
from .lib import timestamp_to_datetime

if TYPE_CHECKING:
    from .session import Session


class News:
    """News object as returned by the get_news API endpoint."""

    def __init__(self, data: Any, session: Session):
        self.session = session
        self.id: int = data["id"]
        self.published = timestamp_to_datetime(data["stamp"])
        self.headline: str = data["headline"]
        """The title of the news article."""
        self.copy: str = data["copy"]
        """The description of the news article."""
        self.thumbnail: str = data["image"]
        """The URL to the news article's thumbnail."""
        self.url: str = data["url"]
        """The link which the news article points to."""

    def __rich_repr__(self):
        yield "id", self.id
        yield "published", self.published
        yield "headline", self.headline
        yield "copy", self.copy
        yield "thumbnail", self.thumbnail
        yield "url", self.url

    __rich_repr__.angular = True  # type: ignore
