from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from .exceptions import *
from .lib import print  # type: ignore
from .lib import API, SITEAPI, timestamp_to_datetime
from .project import Project
from .studio import Studio

if TYPE_CHECKING:
    from .session import Session


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
        self.avatar: str = data["profile"]["images"]["90x90"].replace(
            "90x90", "500x500"
        )

    def __rich_repr__(self):
        yield "id", self.id
        yield "username", self.username
        yield "is_scratch_team", self.is_scratch_team
        yield "joined", self.joined
        yield "status", self.status
        yield "bio", self.bio
        yield "country", self.country

    @staticmethod
    def api_get_projects(
        session: Session,
        username: str,
        limit: int | None = None,
        offset: int | None = None,
    ):
        """Returns a list of projects shared by the user given by username"""
        return session.get_list(
            f"users/{username}/projects",
            limit,
            offset,
            lambda item: Project(item, session),
        )

    def get_projects(self, limit: int | None = None, offset: int | None = None):
        """Returns a list of projects shared by the user"""
        return User.api_get_projects(self.session, self.username, limit, offset)

    @staticmethod
    def api_get_curating_studios(
        session: Session,
        username: str,
        limit: int | None = None,
        offset: int | None = None,
    ):
        """Returns a list of studios curated by the user given by username"""
        return session.get_list(
            f"users/{username}/studios/curate",
            limit,
            offset,
            lambda item: Studio(item, session),
        )

    def get_curating_studios(self, limit: int | None = None, offset: int | None = None):
        """Return a list of studios curated by the user"""
        return User.api_get_curating_studios(self.session, self.username, limit, offset)

    @staticmethod
    def api_get_favorite_projects(
        session: Session,
        username: str,
        limit: int | None = None,
        offset: int | None = None,
    ):
        """Returns a list of projects favorited by the user"""
        return session.get_list(
            f"users/{username}/favorites",
            limit,
            offset,
            lambda item: Project(item, session),
        )

    def get_favorite_projects(
        self, limit: int | None = None, offset: int | None = None
    ):
        """Returns a list of projects favorited by the user"""
        return User.api_get_favorite_projects(
            self.session, self.username, limit, offset
        )

    @staticmethod
    def api_get_followers(
        session: Session,
        username: str,
        limit: int | None = None,
        offset: int | None = None,
    ):
        """Returns a list of users following the user given by username"""
        return session.get_list(
            f"users/{username}/followers",
            limit,
            offset,
            lambda item: User(item, session),
        )

    def get_followers(self, limit: int | None = None, offset: int | None = None):
        """Return a list of users following the user"""
        return User.api_get_followers(self.session, self.username, limit, offset)

    @staticmethod
    def api_get_following(
        session: Session,
        username: str,
        limit: int | None = None,
        offset: int | None = None,
    ):
        """Returns a list of users that the user given by username is following"""
        return session.get_list(
            f"users/{username}/following",
            limit,
            offset,
            lambda item: User(item, session),
        )

    def get_following(self, limit: int | None = None, offset: int | None = None):
        """Return a list of users that the user is following"""
        return User.api_get_following(self.session, self.username, limit, offset)

    @staticmethod
    def api_get_message_count(session: Session, username: str) -> int:
        """Returns the number of messages in the user's inbox"""
        response = session.get(f"{API}/users/{username}/messages/count")
        response.raise_for_status()
        return response.json()["count"]

    def get_message_count(self) -> int:
        """Returns the number of messages in the user's inbox"""
        return User.api_get_message_count(self.session, self.username)

    @staticmethod
    def api_post_comment(session: Session, username: str, content: str):
        """Post a comment on user's profile given by username"""
        response = session.post(
            f"{SITEAPI}/comments/user/{username}/add/",
            json={"content": content, "parent_id": "", "commentee_id": ""},
        )
        response.raise_for_status()
        if (
            response.text.strip()
            == '<script id="error-data" type="application/json">{"error": "isDisallowed"}</script>'
        ):
            raise CommentsDisabledError

    def post_comment(self, content: str):
        """Post a comment on user's profile"""
        User.api_post_comment(self.session, self.username, content)

    @staticmethod
    def api_report(
        session: Session, username: str, section: Literal["username"]
    ):  # FIXME: add other sections
        """Report the user for a violation in the given section given by username"""
        response = session.post(
            f"{SITEAPI}/users/all/{username}/report", data={"selected_field": section}
        )
        response.raise_for_status()

    def report(self, section: Literal["username"]):  # FIXME: see User.api_report()
        """Report the user for a violation in the given section"""
        User.api_report(self.session, self.username, section)

    def follow(self):
        """Follow the user."""
        self.session.follow_user(self.username)

    def unfollow(self):
        """Unfollow the user."""
        self.session.unfollow_user(self.username)
