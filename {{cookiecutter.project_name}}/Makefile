# This makefile has been created to help developers perform common actions.
# Most actions assume it is operating in a virtual environment where the
# python command links to the appropriate virtual environment Python.

VENVS_DIR := $(HOME)/.venvs
VENV_DIR := $(VENVS_DIR)/{{ cookiecutter.project_name }}

# Do not remove this block. It is used by the 'help' rule when
# constructing the help output.
# help:
# help: {{ cookiecutter.project_name }} Makefile help
# help:

# help: help                           - display this makefile's help information
.PHONY: help
help:
	@grep "^# help\:" Makefile | grep -v grep | sed 's/\# help\: //' | sed 's/\# help\://'

# help: install                        - create a virtual environment for development
.PHONY: install
install:
	@pipenv install --dev
	@pre-commit install

# help: clean                          - clean all files using .gitignore rules
.PHONY: clean
clean:
	# @git clean -X -f -d
	@git branch --merged| egrep -v "(^\*|master)" | xargs git branch -d


# help: scrub                          - clean all files, even untracked files
.PHONY: scrub
scrub:
	git clean -x -f -d
	@git branch --merged| egrep -v "(^\*|master)" | xargs git branch -d


# help: pre-commit                     - run pre-commit
.PHONY: pre-commit
pre-commit:
	@pipenv run pre-commit run

# help: pre-commit-all                 - run full pre-commit on all files
.PHONY: pre-commit-all
pre-commit-all:
	@pipenv run pre-commit run --all-files


# help: test                           - run tests
.PHONY: test
test:
	@pipenv run python -m unittest discover -s src


# help: test-verbose                   - run tests [verbosely]
.PHONY: test-verbose
test-verbose:
	@pipenv run python -m unittest discover -s src -v


# help: check-coverage                 - perform test coverage checks
.PHONY: check-coverage
check-coverage:
	@pipenv run coverage run -m unittest discover -s src
	@# produce html coverage report on modules
	@pipenv run coverage report --omit='*/virtualenvs/*','venv/*' --fail-under=80
	@pipenv run coverage html -d docs/source/coverage --include="src/ami_lookup/*"
	@# rename coverage html file for latter use with documentation
	@mv docs/source/coverage/index.html docs/source/coverage/coverage.html


# help: style                          - perform code format compliance check
.PHONY: style
style:
	@pipenv run black src/


# help: docs                           - generate project documentation
.PHONY: check-coverage
docs: check-coverage
	@cd docs; rm -rf source/api/ami_lookup*.rst source/api/modules.rst build/*
	@cd docs; make html
	@# Copy coverage output into docs build tree
	@cd docs; cp -R source/coverage build/html/.


# help: check-docs                     - quick check docs consistency
.PHONY: check-docs
check-docs:
	@cd docs; make dummy


# help: serve-docs                     - serve project html documentation
.PHONY: serve-docs
serve-docs:
	@cd docs/build; python -m http.server --bind 127.0.0.1


# help: build                          - build
.PHONY: build
build:
	@echo 'do build'

# help: deploy                         - deploy
.PHONY: deploy
deploy: build
	@echo 'do deploy'

# Keep these lines at the end of the file to retain nice help
# output formatting.
# help:
