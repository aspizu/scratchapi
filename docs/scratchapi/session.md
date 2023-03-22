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
    - [Session().get_news](#session()get_news)
    - [Session().get_project](#session()get_project)
    - [Session().get_studio](#session()get_studio)
    - [Session().get_user](#session()get_user)
    - [Session().login](#session()login)
    - [Session().logout](#session()logout)
    - [Session().toggle_profile_comments](#session()toggle_profile_comments)
    - [Session().unfollow_user](#session()unfollow_user)
    - [Session().upload_avatar](#session()upload_avatar)

## Session

[Show source in session.py:18](../../scratchapi/session.py#L18)

A session object for logging in to Scratch and accessing API endpoints for the
current user.

#### Signature

```python
class Session(requests.Session):
    def __init__(self, username: str, password: str):
        ...
```

### Session().edit_profile

[Show source in session.py:201](../../scratchapi/session.py#L201)

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

[Show source in session.py:139](../../scratchapi/session.py#L139)

Follow a user.

#### Raises

- `NotFoundError` - If the user to follow is not found.

#### Signature

```python
def follow_user(self, username: str):
    ...
```

### Session().get_list

[Show source in session.py:66](../../scratchapi/session.py#L66)

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

### Session().get_news

[Show source in session.py:196](../../scratchapi/session.py#L196)

#### Signature

```python
def get_news(self, limit: int | None = None, offset: int | None = None):
    ...
```

### Session().get_project

[Show source in session.py:170](../../scratchapi/session.py#L170)

Get a project object from id.

#### Raises

- `NotFoundError` - If the project is not found.

#### Signature

```python
def get_project(self, id: int):
    ...
```

### Session().get_studio

[Show source in session.py:183](../../scratchapi/session.py#L183)

Get a studio object from id.

#### Raises

- `NotFoundError` - If the project is not found.

#### Signature

```python
def get_studio(self, id: int):
    ...
```

### Session().get_user

[Show source in session.py:118](../../scratchapi/session.py#L118)

Get a user object from username.

#### Raises

- `NotFoundError` - If the user is not found.

#### Signature

```python
def get_user(self, username: str):
    ...
```

### Session().login

[Show source in session.py:88](../../scratchapi/session.py#L88)

Log in to the Scratch API.

#### Raises

- `InvalidCredentialsError` - If username or password is incorrect.

#### Signature

```python
def login(self, password: str):
    ...
```

### Session().logout

[Show source in session.py:111](../../scratchapi/session.py#L111)

Log out of the Scratch API.

#### Signature

```python
def logout(self):
    ...
```

### Session().toggle_profile_comments

[Show source in session.py:131](../../scratchapi/session.py#L131)

Toggle comments for the user's profile.

#### Signature

```python
def toggle_profile_comments(self):
    ...
```

### Session().unfollow_user

[Show source in session.py:154](../../scratchapi/session.py#L154)

Unfollow a user.

#### Raises

- `NotFoundError` - If the user to unfollow is not found.

#### Signature

```python
def unfollow_user(self, username: str):
    ...
```

### Session().upload_avatar

[Show source in session.py:251](../../scratchapi/session.py#L251)

#### Signature

```python
def upload_avatar(self, image: BinaryIO):
    ...
```