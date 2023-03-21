# Session

[Scratchapi Index](../README.md#scratchapi-index) /
[Scratchapi](./index.md#scratchapi) /
Session

> Auto-generated documentation for [scratchapi.session](../../scratchapi/session.py) module.

- [Session](#session)
  - [Session](#session-1)
    - [Session().get_user](#session()get_user)
    - [Session().login](#session()login)
    - [Session().logout](#session()logout)
    - [Session().user_post_comment](#session()user_post_comment)

## Session

[Show source in session.py:11](../../scratchapi/session.py#L11)

#### Signature

```python
class Session(requests.Session):
    def __init__(self, username: str, password: str):
        ...
```

### Session().get_user

[Show source in session.py:65](../../scratchapi/session.py#L65)

Get a user object from username

#### Signature

```python
def get_user(self, username: str):
    ...
```

### Session().login

[Show source in session.py:40](../../scratchapi/session.py#L40)

Log in to the Scratch API

#### Signature

```python
def login(self, password: str):
    ...
```

### Session().logout

[Show source in session.py:58](../../scratchapi/session.py#L58)

Log out of the Scratch API

#### Signature

```python
def logout(self):
    ...
```

### Session().user_post_comment

[Show source in session.py:71](../../scratchapi/session.py#L71)

Post a comment on user's profile

#### Signature

```python
def user_post_comment(self, username: str, content: str):
    ...
```