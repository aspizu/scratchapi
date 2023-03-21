from __future__ import annotations

import requests

from .exceptions import InvalidCredentialsError
from .lib import print  # type: ignore
from .lib import API, HOST, USER_AGENT
from .user import User


class Session(requests.Session):
    def __init__(self, username: str, password: str):
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

    def __repr__(self):
        return f"Session(username={self.username!r})"

    def login(self, password: str):
        """Log in to the Scratch API"""
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
        """Log out of the Scratch API"""
        response = self.post(
            f"{HOST}/accounts/logout/", data={"csrfmiddlewaretoken": self.CSRF_token}
        )
        response.raise_for_status()

    def get_user(self, username: str):
        """Get a user object from username"""
        response = self.get(f"{API}/users/{username}/")
        response.raise_for_status()
        return User(response.json(), self)
