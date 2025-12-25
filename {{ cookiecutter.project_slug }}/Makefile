.PHONY: setup_lint lint format test

lint:
	uv run lintrunner
	uv run ty check src

format:
	uv run lintrunner format

test:
	uv run pytest ./tests

