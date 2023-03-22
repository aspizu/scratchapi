# Message

[Scratchapi Index](../README.md#scratchapi-index) /
[Scratchapi](./index.md#scratchapi) /
Message

> Auto-generated documentation for [scratchapi.message](../../scratchapi/message.py) module.

- [Message](#message)
  - [AddCommentMessage](#addcommentmessage)
  - [FavoriteOrLoveProjectMessage](#favoriteorloveprojectmessage)
  - [FavoriteProjectMessage](#favoriteprojectmessage)
  - [FollowUserMessage](#followusermessage)
  - [LoveProjectMessage](#loveprojectmessage)
  - [Message](#message-1)
    - [Message.new](#messagenew)
  - [StudioActivityMessage](#studioactivitymessage)

## AddCommentMessage

[Show source in message.py:36](../../scratchapi/message.py#L36)

#### Signature

```python
class AddCommentMessage(Message):
    def __init__(self, data: Any, session: Session):
        ...
```

#### See also

- [Message](#message)



## FavoriteOrLoveProjectMessage

[Show source in message.py:53](../../scratchapi/message.py#L53)

#### Signature

```python
class FavoriteOrLoveProjectMessage(Message):
    def __init__(self, data: Any, session: Session, is_love: bool = False):
        ...
```

#### See also

- [Message](#message)



## FavoriteProjectMessage

[Show source in message.py:60](../../scratchapi/message.py#L60)

#### Signature

```python
class FavoriteProjectMessage(FavoriteOrLoveProjectMessage):
    ...
```

#### See also

- [FavoriteOrLoveProjectMessage](#favoriteorloveprojectmessage)



## FollowUserMessage

[Show source in message.py:69](../../scratchapi/message.py#L69)

#### Signature

```python
class FollowUserMessage(Message):
    def __init__(self, data: Any, session: Session):
        ...
```

#### See also

- [Message](#message)



## LoveProjectMessage

[Show source in message.py:64](../../scratchapi/message.py#L64)

#### Signature

```python
class LoveProjectMessage(FavoriteOrLoveProjectMessage):
    def __init__(self, data: Any, session: Session):
        ...
```

#### See also

- [FavoriteOrLoveProjectMessage](#favoriteorloveprojectmessage)



## Message

[Show source in message.py:12](../../scratchapi/message.py#L12)

#### Signature

```python
class Message:
    def __init__(self, data: Any, session: Session):
        ...
```

### Message.new

[Show source in message.py:20](../../scratchapi/message.py#L20)

#### Signature

```python
@staticmethod
def new(data: Any, session: Session) -> Message:
    ...
```



## StudioActivityMessage

[Show source in message.py:46](../../scratchapi/message.py#L46)

#### Signature

```python
class StudioActivityMessage(Message):
    def __init__(self, data: Any, session: Session):
        ...
```

#### See also

- [Message](#message)