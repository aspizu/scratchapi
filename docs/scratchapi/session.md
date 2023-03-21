# Session

[Scratchapi Index](../README.md#scratchapi-index) /
[Scratchapi](./index.md#scratchapi) /
Session

> Auto-generated documentation for [scratchapi.session](../../scratchapi/session.py) module.

- [Session](#session)
  - [Session](#session-1)
    - [Session().follow_user](#session()follow_user)
    - [Session().get_list](#session()get_list)
    - [Session().get_user](#session()get_user)
    - [Session().login](#session()login)
    - [Session().logout](#session()logout)
    - [Session().toggle_profile_comments](#session()toggle_profile_comments)
    - [Session().unfollow_user](#session()unfollow_user)

## Session

[Show source in session.py:15](../../scratchapi/session.py#L15)

#### Signature

```python
class Session(requests.Session):
    def __init__(self, username: str, password: str):
        ...
```

### Session().follow_user

[Show source in session.py:119](../../scratchapi/session.py#L119)

Follow a user.

#### Raises

- `NotFoundError` - If the user to follow is not found.

#### Signature

```python
def follow_user(self, username: str):
    ...
```

### Session().get_list

[Show source in session.py:44](../../scratchapi/session.py#L44)

Fetch a list of data from the API.

#### Arguments

- `endpoint` - The API endpoint to request.
- `limit` - The maximum number of items to return. Defaults to 20.
- `offset` - The number of items to skip before starting to return results. Defaults to 0.
- `middleware` - A function that will be applied to each item in the response before returning.

#### Signature

```python
def get_list(
    self,
    endpoint: str,
    limit: int | None,
    offset: int | None,
    middleware: Callable[[Any], T],
) -> list[T]:
    ...
```

#### See also

- [T](#t)

### Session().get_user

[Show source in session.py:98](../../scratchapi/session.py#L98)

Get a user object from username.

#### Raises

- `NotFoundError` - If the user is not found.

#### Signature

```python
def get_user(self, username: str):
    ...
```

### Session().login

[Show source in session.py:68](../../scratchapi/session.py#L68)

Log in to the Scratch API.

#### Raises

- `InvalidCredentialsError` - If username or password is incorrect.

#### Signature

```python
def login(self, password: str):
    ...
```

### Session().logout

[Show source in session.py:91](../../scratchapi/session.py#L91)

Log out of the Scratch API.

#### Signature

```python
def logout(self):
    ...
```

### Session().toggle_profile_comments

[Show source in session.py:111](../../scratchapi/session.py#L111)

Toggle comments for the user's profile.

#### Signature

```python
def toggle_profile_comments(self):
    ...
```

### Session().unfollow_user

[Show source in session.py:134](../../scratchapi/session.py#L134)

Unfollow a user.

#### Raises

- `NotFoundError` - If the user to unfollow is not found.

#### Signature

```python
def unfollow_user(self, username: str):
    ...
```