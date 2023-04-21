import pytest
from playwright.sync_api import sync_playwright, Browser

from modules.api_client import APIClient
from settings import HASH_VALUE


@pytest.fixture(scope="session")
def browser() -> Browser:
    """
    Fixture to provide a browser instance for testing. Runs once per execution session.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def context(browser):
    """Fixture to provide a browser context for testing."""
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="module")
def context_mod(browser):
    """
    Fixture to provide a shared browser context for testing.
    Will run once per module of tests.
    """
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context):
    """Fixture to provide a new page in the browser context for testing."""
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="module")
def page_mod(context_mod):
    """
    Fixture to provide a shared new page in the browser context for testing.
    Will run once per module of tests.
    """
    page = context_mod.new_page()
    yield page
    page.close()


@pytest.fixture(scope="module")
def indexer_payload() -> dict:
    """
    Returns indexer response object. Pass this to the tests for atomic asserts.
    Will run once per module and can be shared between tests.
    """
    client = APIClient()
    response = client.post(tx_hash=HASH_VALUE)
    assert (
        response.status_code == 200
    )  # this will serve as precondition for all tests in the suite
    return response.json()
