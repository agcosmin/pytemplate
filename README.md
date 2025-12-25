# pytemplate

pytemplate is a simple python project template.

# Usage
1. Install:
* [`cookiecutter`](https://cookiecutter.readthedocs.io/en/stable/installation.html#install-cookiecutter)
* [`uv`](https://docs.astral.sh/uv/)
    * If you have only dependencies from python indexes e.g. [pypi](https://pypi.org/)
    use any install method.
    * If you have dependencies that require a conda environment. Create your conda
    environment and install `uv` using pip.

2. Run `cookiecutter pytemplate` and answer prompts.
3. If using conda activate the environment.
4. Run `uv sync` to install dependencies
5. You are now ready to develop you project. If not familiar with `uv` read the
[docs](https://docs.astral.sh/uv/) to familiarize yourself with the `uv` workflow.

# What you get

pytemplate generates a python project directory tree configured for an workflow
with [`uv`](https://docs.astral.sh/uv/) python package and project manager,
[optional] [`conda`](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html)
environments, and [optional] tmux + neovim.

Example generated project directory tree:
```bash
.
├── .conda.env # contains conda env name for tmux + neovim session
├── .git # present if chose to init git repository
├── .gitignore
├── LICENSE # license file TBD option was not chosen
├── .lintrunner.toml # configuration for lintruner
├── Makefile # utility makefile tragets to run lint/format/test
├── .pylintrc # pylint config using [google style](https://google.github.io/styleguide/pyguide.html)
├── pyproject.toml # project configuration
├── README.md # base readme
├── src # packages sources
│   └── foobar
│       └── __init__.py
└── tests
    └── test_foobar.py # dumy tests
```


* Project configuration:
    * [`uv`](https://docs.astral.sh/uv/) project and package manager
    * [`setuptools`](https://setuptools.pypa.io/en/latest/index.html) build backend.
    * [`ruff`](https://github.com/astral-sh/ruff) config.
    * ML packages dependencies if selected - check and adjust package/versions as desired.

* Lint and format:
    * `Makefile` tragets: lint, format.
    * Uses [`lintrunner`](https://github.com/suo/lintrunner) to lint with:
    [`ruff`](https://github.com/astral-sh/ruff) and [`pylint`](https://pylint.org/),
    and to format with [`ruff`](https://github.com/astral-sh/ruff).
    * Uses [`ty`](https://github.com/astral-sh/ty) for type checking.
    * .pylintrc with [google style](https://google.github.io/styleguide/pyguide.html)

* Testing:
    * `Makefile` tragets: test.
    * [pytest](https://docs.pytest.org)

# `sesh`
`sesh` is a bash script, inspired by [ThePrimeagen's tmux-sessionizer](https://github.com/ThePrimeagen/.dotfiles/blob/master/bin/.local/scripts/tmux-sessionizer),
used to facilitate creation of a tmux session with neovim for development of
python projects generated from pytemplate (and other projects if setup accordingly).

To use `sesh` make it executable and place it somewhere in your `$PATH`.
Set the `$TMUX_SESSIONIZER_PATH` environment variable to full paths to be used
for project discovery. If not set, will default to "$HOME".

Run `sesh` and use the `fzf` to select your project. You will get a new `tmux`
session if one does not already exist. `sesh` will activate the `conda` environment
and the `uv .venv`. The conda environment name is sourced from `.conda.env` file
generated using pytemplate.
