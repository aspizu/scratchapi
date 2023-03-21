from __future__ import annotations

try:
    from rich import print  # type: ignore
except ImportError:
    pass

from datetime import datetime
from typing import TypeAlias, Union

JSON: TypeAlias = dict[
    Union[str, int, float, bool], Union["JSON", str, bool, int, float, list["JSON"]]
]
HOST = "https://scratch.mit.edu"
SITEAPI = f"{HOST}/site-api"
API = "https://api.scratch.mit.edu"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"


def timestamp_to_datetime(timestamp: str):
    """Parses a string timestamp in ISO-8601 format and returns a datetime object."""
    return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
