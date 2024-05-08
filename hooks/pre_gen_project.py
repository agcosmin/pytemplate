"""Cookiecutter pre-generation hooks."""

import ast
import sys
import subprocess


def have_git() -> bool:
    """Check if git is available if git repository must be initialized."""
    require_git = ast.literal_eval("{{ cookiecutter.init_repo }}")
    if require_git:
        return subprocess.run(["git", "--version"], capture_output=True).returncode == 0

    return True


if __name__ == "__main__":
    if not have_git():
        print("ERROR: Git is not installed.")
        sys.exit(1)
