# pytemplate

pytemplate is a basic python project template (mainly trageted for ML experiments)

# Usage
Install [`cookiecutter`](https://cookiecutter.readthedocs.io/en/stable/installation.html#install-cookiecutter)

Run and answer prompts:
```bash
cookiecutter pytemplate
```

# What you get

pytemplate is basic python project template that configures the following:

* `pyproject.toml`:
    * build backend is set to [`setuptools`](https://setuptools.pypa.io/en/latest/index.html)

* Lint and format:

    * `Makefile` tragets: setup_lint, lint, format
    * [`lintrunner`](https://github.com/suo/lintrunner)
    * [`pylint`](https://pylint.org/) with [google style](https://google.github.io/styleguide/pyguide.html) config (except indent which is set to 4)
    * [`ruff`](https://github.com/astral-sh/ruff) formatting and linting

* Testing:
    * [pytest](https://docs.pytest.org)
