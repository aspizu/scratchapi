from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .lib import print  # type: ignore
from .lib import timestamp_to_datetime

if TYPE_CHECKING:
    from .session import Session
    from .user import User


class Project:
    def __init__(self, data: Any, session: Session, author: User | None = None):
        self.session = session
        self.author = author
        self.id: int = data["id"]
        self.title: str = data["title"]
        self.description: str = data["description"]
        self.instructions: str = data["instructions"]
        self.visiblity: str = data["visibility"]
        self.is_public: bool = data["public"]
        self.has_comments_enabled: bool = data["comments_allowed"]
        self.is_published: bool = data["is_published"]
        self.created = timestamp_to_datetime(data["history"]["created"])
        self.modified = timestamp_to_datetime(data["history"]["modified"])
        self.shared = timestamp_to_datetime(data["history"]["shared"])
