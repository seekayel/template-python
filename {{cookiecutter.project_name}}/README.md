# {{cookiecutter.project_nanme}}

TODO: one sentence decription of this project

## Orientation

This project was generated from https://github.com/seekayel/python-template

Frameworks of note:

- Pipenv: manages virtual envs for you. Wrap any python execution with `pipenv run ${CMD}`
- Makefile: to find out what can be done try `make help`
- Pre-commit: git pre-commit hooks that lint check validity try `make pre-commit-all`
- PyTest: `make test`

## Installation

`make install`

## Build

`make build`

## Test

`make test`

Unit Test Search Rules

- Required:
  - Filenames: test_*.py or *_test.py (or explicit mention in Make)
  - Function Names: `test*`
- Convention:
  - In: `tests/unit`
