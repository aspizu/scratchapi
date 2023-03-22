from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .lib import print  # type: ignore
from .lib import timestamp_to_datetime

if TYPE_CHECKING:
    from .session import Session


class Message:
    def __init__(self, data: Any, session: Session):
        self.session = session
        self.id: int = data["id"]
        self.created = timestamp_to_datetime(data["datetime_created"])
        self.actor_username: str = data["actor_username"]
        self.actor_id: int = data["actor_id"]

    @staticmethod
    def new(data: Any, session: Session) -> Message:
        if data["type"] == "addcomment":
            return AddCommentMessage(data, session)
        elif data["type"] == "studioactivity":
            return StudioActivityMessage(data, session)
        elif data["type"] == "favoriteproject":
            return FavoriteProjectMessage(data, session)
        elif data["type"] == "loveproject":
            return LoveProjectMessage(data, session)
        elif data["type"] == "followuser":
            return FollowUserMessage(data, session)
        print("Please create an issue at: https://github.com/aspizu/scratchapi/issues")
        raise ValueError(data)


class AddCommentMessage(Message):
    def __init__(self, data: Any, session: Session):
        super().__init__(data, session)
        self.comment_type: int = data["comment_type"]
        self.comment_obj_id: int = data["comment_obj_id"]
        self.comment_fragment: str = data["comment_fragment"]
        self.comment_obj_title: str = data["comment_obj_title"]
        self.commentee_username: str = data["commentee_username"]


class StudioActivityMessage(Message):
    def __init__(self, data: Any, session: Session):
        super().__init__(data, session)
        self.gallery_id: int = data["gallery_id"]
        self.title: str = data["title"]


class FavoriteOrLoveProjectMessage(Message):
    def __init__(self, data: Any, session: Session, is_love: bool = False):
        super().__init__(data, session)
        self.project_id: int = data["project_id"]
        self.title: str = data["title"] if is_love else data["project_title"]


class FavoriteProjectMessage(FavoriteOrLoveProjectMessage):
    ...


class LoveProjectMessage(FavoriteOrLoveProjectMessage):
    def __init__(self, data: Any, session: Session):
        super().__init__(data, session, True)


class FollowUserMessage(Message):
    def __init__(self, data: Any, session: Session):
        super().__init__(data, session)
        self.followed_user_id: int = data["followed_user_id"]
        self.followed_username: str = data["followed_username"]
