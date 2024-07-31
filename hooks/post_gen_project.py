"""cookiecutter post-generation hooks."""

import ast
import os
import subprocess
import sys


def remove_files() -> None:
    """Remove optional files."""
    files = ["{%- if cookiecutter.license == 'TBD' %}LICENSE{% endif -%}"]
    for file in files:
        if file != "":
            if os.path.isfile(file):
                os.remove(file)
            else:
                print(f"WARN: Could not find file {file} to remove.")


def hide_config_files() -> None:
    """Hide configuration files."""
    configs = ["gitignore", "lintrunner.toml", "pylintrc"]
    for file in configs:
        os.rename(file, f".{file}")


def intialize_repo() -> bool:
    """Intialize git repository."""
    init_repo = ast.literal_eval("{{ cookiecutter.init_repo }}")
    if init_repo:
        try:
            subprocess.run(["git", "init"], capture_output=True, check=True)
            subprocess.run(["git", "add", "--", "."], capture_output=True, check=True)
            subprocess.run(
                ["git", "commit", "-m", "Intial commit, project setup"],
                capture_output=True,
                check=True,
            )
        except subprocess.CalledProcessError as e:
            details = f"output:\n{e.output}\nstdout:\n{e.stdout}\nstderr:\n{e.stderr}"
            print(f"ERROR: Failed to initialize git repository. Details:\n{details}")
            return False
    return True


if __name__ == "__main__":
    remove_files()
    hide_config_files()
    if not intialize_repo():
        sys.exit(1)
