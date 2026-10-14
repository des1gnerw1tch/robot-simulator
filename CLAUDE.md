# CLAUDE.md

## Ask before acting

- Never install system packages (`brew install`, `apt`, `npm -g`, `pipx`, downloading binaries onto the PATH, etc.) without explicit approval from the user first.

## Python

- Run all Python through `uv` (`uv run`, `uv add`, `uv sync`). Never call `python`/`pip` directly; pyenv's shims don't match the project's Python versions.
