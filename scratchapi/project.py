from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .lib import print  # type: ignore
from .lib import timestamp_to_datetime

if TYPE_CHECKING:
    from .session import Session
    from .user import User


class Project:
    """Project"""

    def __init__(self, data: Any, session: Session, author: User | None = None):
        self.session = session
        self.author = author
        self.id: int = data["id"]
        self.title: str = data["title"]
        self.description: str = data["description"]
        self.instructions: str = data["instructions"]
        self.visibility: str = data["visibility"]
        self.is_public: bool = data["public"]
        self.has_comments_enabled: bool = data["comments_allowed"]
        self.is_published: bool = data["is_published"]
        self.thumbnail: str = data["image"]
        self.created = timestamp_to_datetime(data["history"]["created"])
        self.modified = timestamp_to_datetime(data["history"]["modified"])
        self.shared = timestamp_to_datetime(data["history"]["shared"])
        self.view_count: int = data["stats"]["views"]
        self.love_count: int = data["stats"]["loves"]
        self.favorite_count: int = data["stats"]["favorites"]
        self.remix_count: int = data["stats"]["remixes"]
        self.is_remix: bool = data["remix"]["parent"] is not None
        self.remix_parent_id: int | None = data["remix"]["parent"]
        self.remix_root_id: int | None = data["remix"]["root"]

    def __rich_repr__(self):
        yield "id", self.id
        yield "title", self.title
        yield "description", self.description
        yield "instructions", self.instructions
        yield "visibility", self.visibility
        yield "is_public", self.is_public
        yield "has_comments_enabled", self.has_comments_enabled
        yield "is_published", self.is_published
        yield "created", self.created
        yield "modified", self.modified
        yield "shared", self.shared
        yield "view_count", self.view_count
        yield "love_count", self.love_count
        yield "favorite_count", self.favorite_count
        yield "remix_count", self.remix_count
