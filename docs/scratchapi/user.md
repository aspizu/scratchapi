# User

[Scratchapi Index](../README.md#scratchapi-index) /
[Scratchapi](./index.md#scratchapi) /
User

> Auto-generated documentation for [scratchapi.user](../../scratchapi/user.py) module.

- [User](#user)
  - [User](#user-1)
    - [User().get_curating_studios](#user()get_curating_studios)
    - [User().get_favorite_projects](#user()get_favorite_projects)
    - [User().get_followers](#user()get_followers)
    - [User().get_following](#user()get_following)
    - [User().get_message_count](#user()get_message_count)
    - [User().get_projects](#user()get_projects)
    - [User().post_comment](#user()post_comment)

## User

[Show source in user.py:17](../../scratchapi/user.py#L17)

User

#### Signature

```python
class User:
    def __init__(self, data: Any, session: Session):
        ...
```

### User().get_curating_studios

[Show source in user.py:59](../../scratchapi/user.py#L59)

Returns a list of studios curated by the user

#### Signature

```python
def get_curating_studios(self, limit: int = 20, offset: int = 20):
    ...
```

### User().get_favorite_projects

[Show source in user.py:68](../../scratchapi/user.py#L68)

Returns a list of projects favorited by the user

#### Signature

```python
def get_favorite_projects(self, limit: int = 20, offset: int = 0):
    ...
```

### User().get_followers

[Show source in user.py:77](../../scratchapi/user.py#L77)

Returns a list of users following the user

#### Signature

```python
def get_followers(self, limit: int = 20, offset: int = 0):
    ...
```

### User().get_following

[Show source in user.py:86](../../scratchapi/user.py#L86)

Returns a list of users followed by the user

#### Signature

```python
def get_following(self, limit: int = 20, offset: int = 0):
    ...
```

### User().get_message_count

[Show source in user.py:95](../../scratchapi/user.py#L95)

#### Signature

```python
def get_message_count(self) -> int:
    ...
```

### User().get_projects

[Show source in user.py:50](../../scratchapi/user.py#L50)

Returns a list of projects shared by the user

#### Signature

```python
def get_projects(self, limit: int = 20, offset: int = 0):
    ...
```

### User().post_comment

[Show source in user.py:100](../../scratchapi/user.py#L100)

#### Signature

```python
def post_comment(self, content: str):
    ...
```