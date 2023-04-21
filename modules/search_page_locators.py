from playwright.sync_api import Page


class SearchPage:
    """
    All relevant locators and methods to access them are stored here.
    Locators are accessed as property attributes.
    Actions are accessed as normal method functions.
    """
    def __init__(self, page: Page):
        self.page = page
        self.PAGE_TITLE = page.get_by_role("heading", name="Interview Automation Engineer")
        self.SEARCH_FIELD = page.get_by_role("textbox")
        self.SUBMIT_BTN = page.get_by_role("button", name="Submit")
        self.RESULTS_CONTAINER = page.locator('xpath=//body/main/div/div')

    @property
    def page_title(self):
        return self.PAGE_TITLE

    def search_for(self, query: str):
        self.SEARCH_FIELD.fill(query)
        self.SUBMIT_BTN.click()

    @property
    def results(self):
        return self.RESULTS_CONTAINER
