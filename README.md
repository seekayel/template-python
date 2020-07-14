# Template Python Project

This creates a template python project with Makefile, precommit hooks and pytest framework.

## Install

```sh
cd ~/git
pip show cookiecutter || pip install cookiecutter
cookiecutter template-python
```

### What is included

```sh
├── Makefile
├── Pipfile
├── src
└── tests
    └── unit
        ├── __init__.py
        └── test_handler.py
```
