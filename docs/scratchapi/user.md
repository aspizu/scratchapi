# User

[Scratchapi Index](../README.md#scratchapi-index) /
[Scratchapi](./index.md#scratchapi) /
User

> Auto-generated documentation for [scratchapi.user](../../scratchapi/user.py) module.

- [User](#user)
  - [User](#user-1)
    - [User.api_get_curating_studios](#userapi_get_curating_studios)
    - [User.api_get_favorite_projects](#userapi_get_favorite_projects)
    - [User.api_get_followers](#userapi_get_followers)
    - [User.api_get_following](#userapi_get_following)
    - [User.api_get_message_count](#userapi_get_message_count)
    - [User.api_get_projects](#userapi_get_projects)
    - [User.api_post_comment](#userapi_post_comment)
    - [User.api_report](#userapi_report)
    - [User().get_curating_studios](#user()get_curating_studios)
    - [User().get_favorite_projects](#user()get_favorite_projects)
    - [User().get_followers](#user()get_followers)
    - [User().get_following](#user()get_following)
    - [User().get_message_count](#user()get_message_count)
    - [User().get_projects](#user()get_projects)
    - [User().post_comment](#user()post_comment)
    - [User().report](#user()report)

## User

[Show source in user.py:15](../../scratchapi/user.py#L15)

User

#### Signature

```python
class User:
    def __init__(self, data: Any, session: Session):
        ...
```

### User.api_get_curating_studios

[Show source in user.py:55](../../scratchapi/user.py#L55)

Returns a list of studios curated by the user given by username

#### Signature

```python
@staticmethod
def api_get_curating_studios(
    session: Session, username: str, limit: int | None = None, offset: int | None = None
):
    ...
```

### User.api_get_favorite_projects

[Show source in user.py:74](../../scratchapi/user.py#L74)

Returns a list of projects favorited by the user

#### Signature

```python
@staticmethod
def api_get_favorite_projects(
    session: Session, username: str, limit: int | None = None, offset: int | None = None
):
    ...
```

### User.api_get_followers

[Show source in user.py:97](../../scratchapi/user.py#L97)

Returns a list of users following the user given by username

#### Signature

```python
@staticmethod
def api_get_followers(
    session: Session, username: str, limit: int | None = None, offset: int | None = None
):
    ...
```

### User.api_get_following

[Show source in user.py:116](../../scratchapi/user.py#L116)

Returns a list of users that the user given by username is following

#### Signature

```python
@staticmethod
def api_get_following(
    session: Session, username: str, limit: int | None = None, offset: int | None = None
):
    ...
```

### User.api_get_message_count

[Show source in user.py:135](../../scratchapi/user.py#L135)

Returns the number of messages in the user's inbox

#### Signature

```python
@staticmethod
def api_get_message_count(session: Session, username: str) -> int:
    ...
```

### User.api_get_projects

[Show source in user.py:36](../../scratchapi/user.py#L36)

Returns a list of projects shared by the user given by username

#### Signature

```python
@staticmethod
def api_get_projects(
    session: Session, username: str, limit: int | None = None, offset: int | None = None
):
    ...
```

### User.api_post_comment

[Show source in user.py:146](../../scratchapi/user.py#L146)

Post a comment on user's profile given by username

#### Signature

```python
@staticmethod
def api_post_comment(session: Session, username: str, content: str):
    ...
```

### User.api_report

[Show source in user.py:164](../../scratchapi/user.py#L164)

Report the user for a violation in the given section given by username

#### Signature

```python
@staticmethod
def api_report(session: Session, username: str, section: Literal["username"]):
    ...
```

### User().get_curating_studios

[Show source in user.py:70](../../scratchapi/user.py#L70)

Return a list of studios curated by the user

#### Signature

```python
def get_curating_studios(self, limit: int | None = None, offset: int | None = None):
    ...
```

### User().get_favorite_projects

[Show source in user.py:89](../../scratchapi/user.py#L89)

Returns a list of projects favorited by the user

#### Signature

```python
def get_favorite_projects(self, limit: int | None = None, offset: int | None = None):
    ...
```

### User().get_followers

[Show source in user.py:112](../../scratchapi/user.py#L112)

Return a list of users following the user

#### Signature

```python
def get_followers(self, limit: int | None = None, offset: int | None = None):
    ...
```

### User().get_following

[Show source in user.py:131](../../scratchapi/user.py#L131)

Return a list of users that the user is following

#### Signature

```python
def get_following(self, limit: int | None = None, offset: int | None = None):
    ...
```

### User().get_message_count

[Show source in user.py:142](../../scratchapi/user.py#L142)

Returns the number of messages in the user's inbox

#### Signature

```python
def get_message_count(self) -> int:
    ...
```

### User().get_projects

[Show source in user.py:51](../../scratchapi/user.py#L51)

Returns a list of projects shared by the user

#### Signature

```python
def get_projects(self, limit: int | None = None, offset: int | None = None):
    ...
```

### User().post_comment

[Show source in user.py:160](../../scratchapi/user.py#L160)

Post a comment on user's profile

#### Signature

```python
def post_comment(self, content: str):
    ...
```

### User().report

[Show source in user.py:174](../../scratchapi/user.py#L174)

Report the user for a violation in the given section

#### Signature

```python
def report(self, section: Literal["username"]):
    ...
```