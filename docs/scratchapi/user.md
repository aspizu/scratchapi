# User

[Scratchapi Index](../README.md#scratchapi-index) /
[Scratchapi](./index.md#scratchapi) /
User

> Auto-generated documentation for [scratchapi.user](../../scratchapi/user.py) module.

- [User](#user)
  - [BaseUser](#baseuser)
    - [BaseUser.api_get_curating_studios](#baseuserapi_get_curating_studios)
    - [BaseUser.api_get_favorite_projects](#baseuserapi_get_favorite_projects)
    - [BaseUser.api_get_followers](#baseuserapi_get_followers)
    - [BaseUser.api_get_following](#baseuserapi_get_following)
    - [BaseUser.api_get_message_count](#baseuserapi_get_message_count)
    - [BaseUser.api_get_projects](#baseuserapi_get_projects)
    - [BaseUser.api_post_comment](#baseuserapi_post_comment)
    - [BaseUser.api_report](#baseuserapi_report)
    - [BaseUser().follow](#baseuser()follow)
    - [BaseUser().get_curating_studios](#baseuser()get_curating_studios)
    - [BaseUser().get_favorite_projects](#baseuser()get_favorite_projects)
    - [BaseUser().get_followers](#baseuser()get_followers)
    - [BaseUser().get_following](#baseuser()get_following)
    - [BaseUser().get_message_count](#baseuser()get_message_count)
    - [BaseUser().get_projects](#baseuser()get_projects)
    - [BaseUser().post_comment](#baseuser()post_comment)
    - [BaseUser().promote](#baseuser()promote)
    - [BaseUser().report](#baseuser()report)
    - [BaseUser().unfollow](#baseuser()unfollow)
  - [User](#user-1)

## BaseUser

[Show source in user.py:15](../../scratchapi/user.py#L15)

User object as returned by most API endpoints.

#### Signature

```python
class BaseUser:
    def __init__(self, data: Any, session: Session):
        ...
```

### BaseUser.api_get_curating_studios

[Show source in user.py:61](../../scratchapi/user.py#L61)

Returns a list of studios curated by the user given by username.

#### Signature

```python
@staticmethod
def api_get_curating_studios(
    session: Session, username: str, limit: int | None = None, offset: int | None = None
):
    ...
```

### BaseUser.api_get_favorite_projects

[Show source in user.py:80](../../scratchapi/user.py#L80)

Returns a list of projects favorited by the user given by username.

#### Signature

```python
@staticmethod
def api_get_favorite_projects(
    session: Session, username: str, limit: int | None = None, offset: int | None = None
):
    ...
```

### BaseUser.api_get_followers

[Show source in user.py:103](../../scratchapi/user.py#L103)

Returns a list of users following the user given by username.

#### Signature

```python
@staticmethod
def api_get_followers(
    session: Session, username: str, limit: int | None = None, offset: int | None = None
):
    ...
```

### BaseUser.api_get_following

[Show source in user.py:122](../../scratchapi/user.py#L122)

Returns a list of users that the user given by username is following.

#### Signature

```python
@staticmethod
def api_get_following(
    session: Session, username: str, limit: int | None = None, offset: int | None = None
):
    ...
```

### BaseUser.api_get_message_count

[Show source in user.py:141](../../scratchapi/user.py#L141)

Returns the number of messages in the user's inbox given by username.

#### Signature

```python
@staticmethod
def api_get_message_count(session: Session, username: str) -> int:
    ...
```

### BaseUser.api_get_projects

[Show source in user.py:42](../../scratchapi/user.py#L42)

Returns a list of projects shared by the user given by username.

#### Signature

```python
@staticmethod
def api_get_projects(
    session: Session, username: str, limit: int | None = None, offset: int | None = None
):
    ...
```

### BaseUser.api_post_comment

[Show source in user.py:152](../../scratchapi/user.py#L152)

Post a comment on user's profile given by username.

#### Signature

```python
@staticmethod
def api_post_comment(session: Session, username: str, content: str):
    ...
```

### BaseUser.api_report

[Show source in user.py:170](../../scratchapi/user.py#L170)

Report the user for a violation in the given section given by username

#### Signature

```python
@staticmethod
def api_report(session: Session, username: str, section: Literal["username"]):
    ...
```

### BaseUser().follow

[Show source in user.py:184](../../scratchapi/user.py#L184)

Follow the user.

#### Signature

```python
def follow(self):
    ...
```

### BaseUser().get_curating_studios

[Show source in user.py:76](../../scratchapi/user.py#L76)

Return a list of studios curated by the user.

#### Signature

```python
def get_curating_studios(self, limit: int | None = None, offset: int | None = None):
    ...
```

### BaseUser().get_favorite_projects

[Show source in user.py:95](../../scratchapi/user.py#L95)

Returns a list of projects favorited by the user.

#### Signature

```python
def get_favorite_projects(self, limit: int | None = None, offset: int | None = None):
    ...
```

### BaseUser().get_followers

[Show source in user.py:118](../../scratchapi/user.py#L118)

Return a list of users following the user.

#### Signature

```python
def get_followers(self, limit: int | None = None, offset: int | None = None):
    ...
```

### BaseUser().get_following

[Show source in user.py:137](../../scratchapi/user.py#L137)

Return a list of users that the user is following.

#### Signature

```python
def get_following(self, limit: int | None = None, offset: int | None = None):
    ...
```

### BaseUser().get_message_count

[Show source in user.py:148](../../scratchapi/user.py#L148)

Returns the number of messages in the user's inbox.

#### Signature

```python
def get_message_count(self) -> int:
    ...
```

### BaseUser().get_projects

[Show source in user.py:57](../../scratchapi/user.py#L57)

Returns a list of projects shared by the user.

#### Signature

```python
def get_projects(self, limit: int | None = None, offset: int | None = None):
    ...
```

### BaseUser().post_comment

[Show source in user.py:166](../../scratchapi/user.py#L166)

Post a comment on user's profile

#### Signature

```python
def post_comment(self, content: str):
    ...
```

### BaseUser().promote

[Show source in user.py:38](../../scratchapi/user.py#L38)

Promote this BaseUser to a User object.

#### Signature

```python
def promote(self) -> User:
    ...
```

#### See also

- [User](#user)

### BaseUser().report

[Show source in user.py:180](../../scratchapi/user.py#L180)

Report the user for a violation in the given section

#### Signature

```python
def report(self, section: Literal["username"]):
    ...
```

### BaseUser().unfollow

[Show source in user.py:188](../../scratchapi/user.py#L188)

Unfollow the user.

#### Signature

```python
def unfollow(self):
    ...
```



## User

[Show source in user.py:193](../../scratchapi/user.py#L193)

User object as returned by the get_user API endpoint.

#### Signature

```python
class User(BaseUser):
    def __init__(self, data: Any, session: Session):
        ...
```

#### See also

- [BaseUser](#baseuser)