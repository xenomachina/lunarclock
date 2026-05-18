# Outside of CI, we try to fix auto-fixable problems. In CI, we don't and instead fail.
FORMAT_FLAGS := $(if $(CI),--check)
LINT_FLAGS   := $(if $(CI),,--fix)

.PHONY: all mypy format lint deptry test

all: test lint format deptry

mypy:
	uv run mypy .

format:
	uvx ruff format $(FORMAT_FLAGS) --config pyproject.toml .

lint:
	uvx ruff check $(LINT_FLAGS) --config pyproject.toml .

deptry:
	uv run deptry --config pyproject.toml .

test: mypy
	uv run pytest $(PYTEST_ARGS)
