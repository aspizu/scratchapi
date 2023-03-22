# Session

[Scratchapi Index](../README.md#scratchapi-index) /
[Scratchapi](./index.md#scratchapi) /
Session

> Auto-generated documentation for [scratchapi.session](../../scratchapi/session.py) module.

- [Session](#session)
  - [Session](#session-1)
    - [Session().edit_profile](#session()edit_profile)
    - [Session().follow_user](#session()follow_user)
    - [Session().get_list](#session()get_list)
    - [Session().get_messages](#session()get_messages)
    - [Session().get_news](#session()get_news)
    - [Session().get_project](#session()get_project)
    - [Session().get_studio](#session()get_studio)
    - [Session().get_user](#session()get_user)
    - [Session().login](#session()login)
    - [Session().logout](#session()logout)
    - [Session().toggle_profile_comments](#session()toggle_profile_comments)
    - [Session().unfollow_user](#session()unfollow_user)
    - [Session().upload_avatar](#session()upload_avatar)
    - [Session().username_available](#session()username_available)
    - [Session().username_exists](#session()username_exists)

## Session

[Show source in session.py:19](../../scratchapi/session.py#L19)

A session object for logging in to Scratch and accessing API endpoints for the
current user.

#### Signature

```python
class Session(requests.Session):
    def __init__(self, username: str, password: str):
        ...
```

### Session().edit_profile

[Show source in session.py:212](../../scratchapi/session.py#L212)

Edit the user's profile by updating given parameters.

#### Arguments

- `bio` - If given, the user's "About me" section will be updated.
- `status` - If given, the user's "What I'm working on" section will be updated.
- `featured_project_id` - If given, the featured project will be updated.
- `featured_project_label` - Label for featured project.

#### Raises

- `SyntaxError` - If `featured_project_label` is not passed.

#### Signature

```python
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
    ...
```

### Session().follow_user

[Show source in session.py:140](../../scratchapi/session.py#L140)

Follow a user.

#### Raises

- `NotFoundError` - If the user to follow is not found.

#### Signature

```python
def follow_user(self, username: str):
    ...
```

### Session().get_list

[Show source in session.py:67](../../scratchapi/session.py#L67)

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

### Session().get_messages

[Show source in session.py:203](../../scratchapi/session.py#L203)

Returns a list of messages in the current user's inbox.

#### Signature

```python
def get_messages(self, limit: int | None = None, offset: int | None = None):
    ...
```

### Session().get_news

[Show source in session.py:197](../../scratchapi/session.py#L197)

Returns a list of news.

#### Signature

```python
def get_news(self, limit: int | None = None, offset: int | None = None):
    ...
```

### Session().get_project

[Show source in session.py:171](../../scratchapi/session.py#L171)

Get a project object from id.

#### Raises

- `NotFoundError` - If the project is not found.

#### Signature

```python
def get_project(self, id: int):
    ...
```

### Session().get_studio

[Show source in session.py:184](../../scratchapi/session.py#L184)

Get a studio object from id.

#### Raises

- `NotFoundError` - If the project is not found.

#### Signature

```python
def get_studio(self, id: int):
    ...
```

### Session().get_user

[Show source in session.py:119](../../scratchapi/session.py#L119)

Get a user object from username.

#### Raises

- `NotFoundError` - If the user is not found.

#### Signature

```python
def get_user(self, username: str):
    ...
```

### Session().login

[Show source in session.py:89](../../scratchapi/session.py#L89)

Log in to the Scratch API.

#### Raises

- `InvalidCredentialsError` - If username or password is incorrect.

#### Signature

```python
def login(self, password: str):
    ...
```

### Session().logout

[Show source in session.py:112](../../scratchapi/session.py#L112)

Log out of the Scratch API.

#### Signature

```python
def logout(self):
    ...
```

### Session().toggle_profile_comments

[Show source in session.py:132](../../scratchapi/session.py#L132)

Toggle comments for the user's profile.

#### Signature

```python
def toggle_profile_comments(self):
    ...
```

### Session().unfollow_user

[Show source in session.py:155](../../scratchapi/session.py#L155)

Unfollow a user.

#### Raises

- `NotFoundError` - If the user to unfollow is not found.

#### Signature

```python
def unfollow_user(self, username: str):
    ...
```

### Session().upload_avatar

[Show source in session.py:262](../../scratchapi/session.py#L262)

Broken

#### Signature

```python
def upload_avatar(self, image: BinaryIO):
    ...
```

### Session().username_available

[Show source in session.py:276](../../scratchapi/session.py#L276)

Returns true if this username can be used to register a new account.

#### Signature

```python
def username_available(self, username: str) -> bool:
    ...
```

### Session().username_exists

[Show source in session.py:270](../../scratchapi/session.py#L270)

Returns true if an account with the given username exists.

#### Signature

```python
def username_exists(self, username: str) -> bool:
    ...
```