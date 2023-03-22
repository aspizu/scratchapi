# Project

[Scratchapi Index](../README.md#scratchapi-index) /
[Scratchapi](./index.md#scratchapi) /
Project

> Auto-generated documentation for [scratchapi.project](../../scratchapi/project.py) module.

- [Project](#project)
  - [Project](#project-1)
    - [Project.api_get_comment](#projectapi_get_comment)
    - [Project().get_comment](#project()get_comment)
  - [ProjectComment](#projectcomment)

## Project

[Show source in project.py:24](../../scratchapi/project.py#L24)

Project object as returned by the get_project API endpoint.

#### Signature

```python
class Project:
    def __init__(self, data: Any, session: Session, author: User | None = None):
        ...
```

### Project.api_get_comment

[Show source in project.py:77](../../scratchapi/project.py#L77)

#### Signature

```python
@staticmethod
def api_get_comment(session: Session, username: str, project_id: int, comment_id: int):
    ...
```

### Project().get_comment

[Show source in project.py:89](../../scratchapi/project.py#L89)

#### Signature

```python
def get_comment(self, comment_id: int):
    ...
```



## ProjectComment

[Show source in project.py:15](../../scratchapi/project.py#L15)

Project comment object as returned by the get_comment API endpoint.

#### Signature

```python
class ProjectComment:
    def __init__(self, data: Any, session: Session, project: Project | None = None):
        ...
```