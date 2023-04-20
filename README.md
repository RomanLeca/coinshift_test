## Project Overview
This project contains code for testing a web application and an API. 
The web application is a search page for a blockchain indexer, and the API provides transaction data for the indexer. 
The tests are written in Python using the Pytest framework and Playwright for browser automation.
Poetry is used as the package manager for the project dependencies.

## Files
### ./modules/api_client.py 
Contains a class for interacting with the blockchain indexer API.
### ./conftest.py
Contains fixtures and configuration for Pytest.
### ./tests/frontend/test_indexer_page.py
Contains tests for the web search page.
### ./tests/api/test_indexer_payload.py
Contains tests for the API response payload.
### ./pyproject.toml
Contains project dependencies
### ./poetry.lock
Automatically generated. manages the dependencies from pyproject.toml 
### ./settings.py
Contains some constant values (url data, string values, etc)
## How to Run the Tests
1. If required:
- Install Python (3.8 or higher) and configure the interpreter
- Install Poetry via
  - `curl -sSL https://install.python-poetry.org | python3 -`
or follow any other instructions from https://python-poetry.org/docs/#installing-with-the-official-installer

2. Then:
- Clone this repository and navigate to the project directory.
- Create a virtual environment and install dependencies inside: 
  - `poetry shell`
  - `poetry install`
- Install Playwright binaries:
  - `poetry run playwright install`

- Start the nodejs web application and API (I could've persisted these in a docker image, but it felt wrong since your projects are not public)
- Inside poetry shell, run the 11 tests in parallel with: 
  - `poetry run pytest --verbose -n 11`

### Future potential improvements
- Run tests in a docker environment
- Add Allure reporting (looks nice and allows for a "BDD-ish" layer)
- Add a page object layer to DRY page locators in code