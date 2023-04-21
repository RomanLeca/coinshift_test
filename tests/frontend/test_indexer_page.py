import pytest

from settings import HASH_VALUE, TO_ADDRESS, FROM_ADDRESS, BASE_URL, FE_PORT
from modules.search_page_locators import SearchPage


@pytest.fixture(scope="module")
def indexer_search_page(page_mod):
    """
    Open the indexer search in a browser window.
    """
    page = page_mod
    page.goto(f"{BASE_URL}:{FE_PORT}")
    yield SearchPage(page)


def test_page_title_is_visible(indexer_search_page):
    page = indexer_search_page
    assert page.page_title.is_visible()


@pytest.mark.parametrize("field_value", [HASH_VALUE, FROM_ADDRESS, TO_ADDRESS])
def test_field_values_are_correct(indexer_search_page, field_value):
    """
    These tests will check various static values matches
    """
    page = indexer_search_page
    page.search_for(HASH_VALUE)
    page.RESULTS_CONTAINER.get_by_text(field_value)
    assert page.results.is_visible()


def test_frontend_and_api_are_in_sync(indexer_search_page, indexer_payload):
    """
    This test can compare web search results and api payload results and make sure all values match.
    The api payload can optionally be passed in as a dictionary to parametrize, thus avoiding loops in tests.
    This will keep every assertion independent, but also increase the overall number of reported tests.
    """
    page = indexer_search_page
    page.search_for(HASH_VALUE)
    for key, value in indexer_payload.items():
        page.RESULTS_CONTAINER.get_by_text(f"{key} - {value}").is_visible()


def test_wrong_hash_produces_no_results(indexer_search_page):
    """
    This is a negative test to check that results /div component doesn't display in DOM if there are no matches
    """
    page = indexer_search_page
    page.search_for(HASH_VALUE+"non_existing")
    assert not page.RESULTS_CONTAINER.is_visible()

