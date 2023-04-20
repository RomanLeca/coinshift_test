import pytest

from settings import HASH_VALUE, TO_ADDRESS, FROM_ADDRESS, BASE_URL, FE_PORT


@pytest.fixture(scope="module")
def indexer_search_page(page_mod):
    """
    Open the indexer search in a browser window.
    """
    page = page_mod
    page.goto(f"{BASE_URL}:{FE_PORT}")
    yield page

@pytest.fixture(scope="module")
def indexer_search_result(indexer_search_page):
    """
    Search for the transaction by hash and pass it to the tests.
    """
    page = indexer_search_page
    SEARCH_FIELD = page.get_by_role("textbox")
    SEARCH_FIELD.click()
    SEARCH_FIELD.fill(HASH_VALUE)
    page.get_by_role("button", name="Submit").click()
    yield page


def test_page_title(indexer_search_page):
    page = indexer_search_page
    PAGE_TITLE = page.get_by_role("heading", name="Interview Automation Engineer")
    assert PAGE_TITLE.is_visible()


@pytest.mark.parametrize("text_value", [HASH_VALUE, FROM_ADDRESS, TO_ADDRESS])
def test_transaction_values(indexer_search_result, text_value):
    """
    These tests will check various static values matches
    """
    page = indexer_search_result
    page.get_by_text(text_value).is_visible()


def test_frontend_and_api_are_in_sync(indexer_search_result, indexer_payload):
    """
    This test can compare web search results and api payload results and make sure all values match.
    The api payload can optionally be passed in as a dictionary to parametrize, thus avoiding loops in tests.
    This will keep every assertion independent, but also increase the overall number of reported tests.
    """
    page = indexer_search_result
    for key, value in indexer_payload.items():
        page.get_by_text(f"{key} - {value}").is_visible()
