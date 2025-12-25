"""Cookiecutter pre-generation hooks."""

import ast
import re
import sys
import subprocess


def have_git() -> bool:
    """Check if git is available if git repository must be initialized."""
    require_git = ast.literal_eval("{{ cookiecutter.init_repo }}")
    if require_git:
        have_git_cmd = (
            subprocess.run(["git", "--version"], capture_output=True).returncode
            == 0
        )
        if not have_git_cmd:
            print("ERROR: No git command found on path.")
            return False

    return True


def conda_env_name_is_valid() -> bool:
    conda_env_name = "{{ cookiecutter.conda_env_name }}"
    if not re.match(r"^[_a-zA-Z][_a-zA-Z0-9]+$", conda_env_name):
        print(f"ERROR: {conda_env_name} is not a valid conda environment name")
        return False

    return True


def package_name_is_valid() -> bool:
    package_name = "{{ cookiecutter.package_name }}"
    if not re.match(r"^[_a-z][_a-z0-9]+$", package_name):
        print(f"ERROR: {package_name} is not a valid PEP8 python pacakge name")
        return False

    return True


def project_name_is_valid() -> bool:
    project_name = "{{ cookiecutter.project_name }}"
    if not re.match(r"^[_a-zA-Z][_a-zA-Z0-9]+$", project_name):
        print(f"ERROR: {project_name} is not a valid PEP8 PyPI pacakge name")
        return False

    return True


if __name__ == "__main__":
    if (
        not have_git()
        or not conda_env_name_is_valid()
        or not package_name_is_valid()
        or not project_name_is_valid()
    ):
        sys.exit(1)
