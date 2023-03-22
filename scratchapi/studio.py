from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .lib import print  # type: ignore
from .lib import timestamp_to_datetime

if TYPE_CHECKING:
    from .session import Session


class Studio:
    """Studio object as returned by the get_studio API endpoint."""

    def __init__(self, data: Any, session: Session):
        print(data)
        self.session = session
        self.id: int = data["id"]
        self.title: str = data["title"]
        self.description: str = data["description"]
        self.visibility: str = data["visibility"]
        self.is_public: bool = data["public"]
        self.is_open_to_all: bool = data["open_to_all"]
        self.has_comments_enabled: bool = data["comments_allowed"]
        self.thumbnail: str = data["image"]
        """The URL for the studio's thumbnail."""
        self.created = timestamp_to_datetime(data["history"]["created"])
        self.modified = timestamp_to_datetime(data["history"]["modified"])
        self.comment_count: int = data["stats"]["comments"]
        self.follower_count: int = data["stats"]["followers"]
        self.manager_count: int = data["stats"]["managers"]
        self.project_count: int = data["stats"]["projects"]

    def __rich_repr__(self):
        yield "id", self.id
        yield "title", self.title
        yield "description", self.description
        yield "visibility", self.visibility
        yield "is_public", self.is_public
        yield "is_open_to_all", self.is_open_to_all
        yield "has_comments_enabled", self.has_comments_enabled
        yield "thumbnail", self.thumbnail, None
        yield "created", self.created
        yield "modified", self.modified
        yield "comment_count", self.comment_count
        yield "follower_count", self.follower_count
        yield "manager_count", self.manager_count
        yield "project_count", self.project_count

    __rich_repr__.angular = True  # type: ignore
