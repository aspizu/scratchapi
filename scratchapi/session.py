from __future__ import annotations

from typing import Any, BinaryIO, Callable, Literal, TypeVar

import requests

from .exceptions import *
from .lib import print  # type: ignore
from .lib import API, HOST, SITEAPI, USER_AGENT
from .project import Project
from .user import User

T = TypeVar("T")


class Session(requests.Session):
    """
    A session object for logging in to Scratch and accessing API endpoints for the
    current user.
    """

    def __init__(self, username: str, password: str):
        """
        Start a session by logging in to the Scratch API.

        Raises:
            InvalidCredentialsError: If the username or password is incorrect.
        """
        super().__init__()
        # self.cookies["scratchlanguage"] = "en"
        self.headers.update(
            {
                "User-Agent": USER_AGENT,
                "Accept": "text/html, */*; q=0.01",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-CSRFToken": "a",
                "X-Requested-With": "XMLHttpRequest",
                "DNT": "1",
                "Connection": "keep-alive",
                "Referer": HOST,
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            }
        )
        self.username = username
        self.login(password)
        del password
        self.user = self.get_user(self.username)

    def __rich_repr__(self):
        yield None, self.user

    def get_list(
        self,
        endpoint: str,
        limit: int | None,
        offset: int | None,
        middleware: Callable[[Any], T],
    ) -> list[T]:
        """
        Fetch a list of data from the API.

        Args:
            endpoint: The API endpoint to request.
            limit: The maximum number of items to return. Defaults to 20.
            offset: The number of items to skip before starting to return results. Defaults to 0.
            middleware: A function that will be applied to each item in the response before returning.
        """
        limit = limit or 20
        offset = offset or 0
        response = self.get(
            f"{API}/{endpoint}", params={"limit": limit, "offset": offset}
        )
        response.raise_for_status()
        return [middleware(each) for each in response.json()]

    def login(self, password: str):
        """
        Log in to the Scratch API.

        Raises:
            InvalidCredentialsError: If username or password is incorrect.
        """
        response = self.post(
            f"{HOST}/accounts/login/",
            json={"username": self.username, "password": password, "useMessages": True},
            cookies={"scratchcsrftoken": "a"},
        )
        data = response.json()[0]
        if data["success"] == 0:
            raise InvalidCredentialsError(data)
        response.raise_for_status()
        self.session_id: str = self.cookies["scratchsessionsid"]
        self.token: str = data["token"]
        self.headers["X-Token"] = self.token
        self.CSRF_token: str = self.cookies["scratchcsrftoken"]
        self.headers["X-CSRFToken"] = self.CSRF_token
        self.cookies["scratchsessionsid"] = self.session_id

    def logout(self):
        """Log out of the Scratch API."""
        response = self.post(
            f"{HOST}/accounts/logout/", data={"csrfmiddlewaretoken": self.CSRF_token}
        )
        response.raise_for_status()

    def get_user(self, username: str):
        """
        Get a user object from username.

        Raises:
            NotFoundError: If the user is not found.
        """
        response = self.get(f"{API}/users/{username}/")
        if response.status_code == 404:
            raise NotFoundError(username)
        response.raise_for_status()
        return User(response.json(), self)

    def toggle_profile_comments(self):
        """Toggle comments for the user's profile."""
        response = self.post(
            f"{SITEAPI}/comments/user/{self.username}/toggle-comments/"
        )
        response.raise_for_status()
        assert response.text == "ok"

    def follow_user(self, username: str):
        """
        Follow a user.

        Raises:
            NotFoundError: If the user to follow is not found.
        """
        response = self.put(
            f"{SITEAPI}/users/followers/{username}/add/",
            params={"usernames": self.username},
        )
        if response.status_code == 404:
            raise NotFoundError(username)
        response.raise_for_status()

    def unfollow_user(self, username: str):
        """
        Unfollow a user.

        Raises:
            NotFoundError: If the user to unfollow is not found.
        """
        response = self.put(
            f"{SITEAPI}/users/followers/{self.username}/remove/",
            params={"usernames": username},
        )
        if response.status_code == 404:
            raise NotFoundError(username)
        response.raise_for_status()
        print(response.json())

    def get_project(self, id: int):
        """
        Get a project object from id.

        Raises:
            NotFoundError: If the project is not found.
        """
        response = self.get(f"{API}/projects/{id}/")
        if response.status_code == 404:
            raise NotFoundError(id)
        response.raise_for_status()
        return Project(response.json(), self)

    def edit_profile(
        self,
        bio: str | None = None,
        status: str | None = None,
        featured_project_id: str | None = None,
        featured_project_label: Literal["featured_project"]
        | Literal["featured_tutorial"]
        | Literal["work_in_progress"]
        | Literal["remix_this"]
        | Literal["my_favorite_things"]
        | Literal["why_i_scratch"]
        | None = None,
    ):
        """
        Edit the user's profile by updating given parameters.

        Args:
            bio: If given, the user's "About me" section will be updated.
            status: If given, the user's "What I'm working on" section will be updated.
            featured_project_id: If given, the featured project will be updated.
            featured_project_label: Label for featured project.

        Raises:
            SyntaxError: If `featured_project_label` is not passed.
        """
        payload = {}
        if bio:
            payload["bio"] = bio
            self.user.bio = bio
        if status:
            payload["status"] = status
            self.user.status = status
        if featured_project_id:
            if not featured_project_label:
                raise SyntaxError(
                    "Keyword argument `featured_project_label` must be "
                    "passed if `featured_project_id` is passed."
                )
            payload["featured_project"] = featured_project_id
            payload["featured_project_label"] = {
                "featured_project": "",
                "featured_tutorial": 0,
                "work_in_progress": 1,
                "remix_this": 2,
                "my_favorite_things": 3,
                "why_i_scratch": 4,
            }[featured_project_label]
        response = self.put(f"{SITEAPI}/users/all/{self.username}/", json=payload)
        response.raise_for_status()

    def upload_avatar(self, image: BinaryIO):
        response = self.post(
            f"{SITEAPI}/users/all/{self.username}/",
            files={"file": ("avatar.png", image, "image/png")},
        )
        print(response.text)
        response.raise_for_status()
