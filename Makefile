SCRIPT := lunarclock.py

# Outside of CI, we try to fix auto-fixable problems. In CI, we don't and instead fail.
FORMAT_FLAGS := $(if $(CI),--check)
LINT_FLAGS   := $(if $(CI),,--fix)

# PEP 723 inline-script dependencies from $(SCRIPT), as `--with` args for uvx.
WITH_DEPS := $(shell sed -n '/^\# dependencies = \[/,/^\# \]/p' $(SCRIPT) | grep -oE '"[^"]+"' | sed 's/^/--with /' | tr '\n' ' ')

.PHONY: all mypy format lint

all: lint format mypy

mypy:
	uvx $(WITH_DEPS) mypy --disallow-untyped-defs .

format:
	uvx ruff format $(FORMAT_FLAGS) .

lint:
	uvx ruff check $(LINT_FLAGS) .
