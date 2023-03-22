from __future__ import annotations

from typing import TYPE_CHECKING, Any

from . import user
from .exceptions import *
from .lib import print  # type: ignore
from .lib import API, timestamp_to_datetime

if TYPE_CHECKING:
    from .session import Session
    from .user import User


class ProjectComment:
    """Project comment object as returned by the get_comment API endpoint."""

    def __init__(self, data: Any, session: Session, project: Project | None = None):
        self.session = session
        self.project = project
        print(data)


class Project:
    """Project object as returned by the get_project API endpoint."""

    def __init__(self, data: Any, session: Session, author: User | None = None):
        self.session = session
        self.author = author or user.BaseUser(data["author"], session)
        self.id: int = data["id"]
        self.title: str = data["title"]
        self.description: str = data["description"]
        self.instructions: str = data["instructions"]
        self.visibility: str = data["visibility"]
        self.is_public: bool = data["public"]
        self.has_comments_enabled: bool = data["comments_allowed"]
        self.is_published: bool = data["is_published"]
        self.thumbnail: str = data["image"]
        """The URL to the project's thumbnail."""
        self.created = timestamp_to_datetime(data["history"]["created"])
        self.modified = timestamp_to_datetime(data["history"]["modified"])
        self.shared = timestamp_to_datetime(data["history"]["shared"])
        self.view_count: int = data["stats"]["views"]
        self.love_count: int = data["stats"]["loves"]
        self.favorite_count: int = data["stats"]["favorites"]
        self.remix_count: int = data["stats"]["remixes"]
        self.is_remix: bool = data["remix"]["parent"] is not None
        self.remix_parent_id: int | None = data["remix"]["parent"]
        """Id of the project this project is a remix of."""
        self.remix_root_id: int | None = data["remix"]["root"]
        """Id of the top-most project this project is a remix of."""

    def __rich_repr__(self):
        yield "title", self.title
        yield "author", self.author.username
        yield "id", self.id
        yield "description", self.description, None
        yield "instructions", self.instructions, None
        yield "visibility", self.visibility
        yield "public", self.is_public, False
        yield "comments_allowed", self.has_comments_enabled, False
        yield "is_published", self.is_published, False
        yield "thumbnail", self.thumbnail, None
        yield "created", self.created
        yield "modified", self.modified
        yield "shared", self.shared
        yield "view_count", self.view_count
        yield "love_count", self.love_count
        yield "favorite_count", self.favorite_count
        yield "remix_count", self.remix_count
        yield "is_remix", self.is_remix, False
        yield "remix_parent_id", self.remix_parent_id, None
        yield "remix_root_id", self.remix_root_id, None

    __rich_repr__.angular = True  # type: ignore

    @staticmethod
    def api_get_comment(
        session: Session, username: str, project_id: int, comment_id: int
    ):
        response = session.get(
            f"{API}/users/{username}/projects/{project_id}/comments/{comment_id}/"
        )
        if response.status_code == 404:
            raise NotFoundError(username, project_id, comment_id)
        response.raise_for_status()
        return ProjectComment(response.json(), session)

    def get_comment(self, comment_id: int):
        return Project.api_get_comment(
            self.session, self.author.username, self.id, comment_id
        )
