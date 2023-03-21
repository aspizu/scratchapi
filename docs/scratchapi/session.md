# Session

[Scratchapi Index](../README.md#scratchapi-index) /
[Scratchapi](./index.md#scratchapi) /
Session

> Auto-generated documentation for [scratchapi.session](../../scratchapi/session.py) module.

- [Session](#session)
  - [Session](#session-1)
    - [Session().get_list](#session()get_list)
    - [Session().get_user](#session()get_user)
    - [Session().login](#session()login)
    - [Session().logout](#session()logout)

## Session

[Show source in session.py:15](../../scratchapi/session.py#L15)

#### Signature

```python
class Session(requests.Session):
    def __init__(self, username: str, password: str):
        ...
```

### Session().get_list

[Show source in session.py:44](../../scratchapi/session.py#L44)

Wrap GET endpoints that take in a limit and offset and return a list of objects

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

[Show source in session.py:87](../../scratchapi/session.py#L87)

Get a user object from username

#### Signature

```python
def get_user(self, username: str):
    ...
```

### Session().login

[Show source in session.py:62](../../scratchapi/session.py#L62)

Log in to the Scratch API

#### Signature

```python
def login(self, password: str):
    ...
```

### Session().logout

[Show source in session.py:80](../../scratchapi/session.py#L80)

Log out of the Scratch API

#### Signature

```python
def logout(self):
    ...
```