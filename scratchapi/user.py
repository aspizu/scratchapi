from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, TypeVar

from .exceptions import CommentsDisabledError
from .lib import print  # type: ignore
from .lib import API, SITEAPI, timestamp_to_datetime
from .project import Project
from .studio import Studio

if TYPE_CHECKING:
    from .session import Session

T = TypeVar("T")


class User:
    """User"""

    def __init__(self, data: Any, session: Session):
        self.session = session
        self.id: int = data["id"]
        self.username: str = data["username"]
        self.is_scratch_team: bool = data["scratchteam"]
        self.joined = timestamp_to_datetime(data["history"]["joined"])
        self.status: str = data["profile"]["status"]
        self.bio: str = data["profile"]["bio"]
        self.country: str = data["profile"]["country"]

    def __repr__(self):
        return (
            f"[User]\n"
            f"  username:        {self.username!r}\n"
            f"  is_scratch_team: {self.is_scratch_team!r}\n"
            f"  joined:          {self.joined!r}"
        )

    def _fetch_list(
        self, endpoint: str, limit: int, offset: int, middleware: Callable[[Any], T]
    ) -> list[T]:
        """
        Wrap GET endpoints that take in a limit and offset and return a list of objects
        """
        response = self.session.get(
            f"{API}/{endpoint}", params={"limit": limit, "offset": offset}
        )
        response.raise_for_status()
        return [middleware(each) for each in response.json()]

    def get_projects(self, limit: int = 20, offset: int = 0):
        """Returns a list of projects shared by the user"""
        return self._fetch_list(
            f"users/{self.username}/projects",
            limit,
            offset,
            lambda item: Project(item, self.session),
        )

    def get_curating_studios(self, limit: int = 20, offset: int = 20):
        """Returns a list of studios curated by the user"""
        return self._fetch_list(
            f"users/{self.username}/studios/curate",
            limit,
            offset,
            lambda item: Studio(item, self.session),
        )

    def get_favorite_projects(self, limit: int = 20, offset: int = 0):
        """Returns a list of projects favorited by the user"""
        return self._fetch_list(
            f"users/{self.username}/favorites",
            limit,
            offset,
            lambda item: Project(item, self.session),
        )

    def get_followers(self, limit: int = 20, offset: int = 0):
        """Returns a list of users following the user"""
        return self._fetch_list(
            f"users/{self.username}/followers",
            limit,
            offset,
            lambda item: User(item, self.session),
        )

    def get_following(self, limit: int = 20, offset: int = 0):
        """Returns a list of users followed by the user"""
        return self._fetch_list(
            f"users/{self.username}/following",
            limit,
            offset,
            lambda item: User(item, self.session),
        )

    def get_message_count(self) -> int:
        response = self.session.get(f"{API}/users/{self.username}/messages/count")
        response.raise_for_status()
        return response.json()["count"]

    def post_comment(self, content: str, parent_id: str = "", commentee_id: str = ""):
        response = self.session.post(
            f"{SITEAPI}/comments/user/{self.username}/add/",
            json={
                "content": content,
                "parent_id": parent_id,
                "commentee_id": commentee_id,
            },
        )
        response.raise_for_status()
        if (
            response.text.strip()
            == '<script id="error-data" type="application/json">{"error": "isDisallowed"}</script>'
        ):
            raise CommentsDisabledError
