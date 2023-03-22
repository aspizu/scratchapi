# scratchapi
[type-safe](https://github.com/microsoft/pyright) API wrapper for [scratch.mit.edu](https://scratch.mit.edu) in [Python](https://www.python.org/).

## Quick Start

```py
from scratchapi import Session

session = Session(username='aspizu', password='rens2iskihuy')
session.get_user('Griffpatch').post_comment(f'My bio is: {session.user.bio}')
session.logout()
```

## Installation

```sh
cd ~/Downloads/Src/
git clone https://github.com/aspizu/scratchapi
cd scratchapi
python -m pip install -e . --config-settings editable_mode=strict
```

## Cloud Variables

Use [scratchcloudclient](https://github.com/xAspirus/scratchcloudclient) to deal with cloud variables.
It can be installed from PyPI using `pip install scratchcloudclient`.

## Documentation

View the API documentation [here](docs/README.md), generated using [Handsdown](https://github.com/vemel/handsdown).
