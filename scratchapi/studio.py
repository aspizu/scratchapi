from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .lib import print  # type: ignore
from .lib import timestamp_to_datetime

if TYPE_CHECKING:
    from .session import Session


class Studio:
    """Studio"""

    def __init__(self, data: Any, session: Session):
        self.session = session
        self.id: int = data["id"]
        self.title: str = data["title"]
        self.description: str = data["description"]
        self.visibility: str = data["visibility"]
        self.is_public: bool = data["public"]
        self.is_open_to_all: bool = data["open_to_all"]
        self.has_comments_enabled: bool = data["comments_allowed"]
        self.thumbnail: str = data["image"]
        self.created = timestamp_to_datetime(data["history"]["created"])
        self.modified = timestamp_to_datetime(data["history"]["modified"])
