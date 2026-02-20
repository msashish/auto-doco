# Automate docs on Static site

## Developer guide

1. Create your virtual environment and configure poetry

    poetry init
    python -m venv .venv-doco
    poetry config virtualenvs.in-project true
    source .venv-doco/bin/activate
    poetry env use /Users/msashish/msashishgit/auto-doco/.venv-doco/bin/python3.11

2. Install packages

    poetry add mkdocs
    poetry add mkdocs-material

3. Initialise mkdocs

    mkdocs new .