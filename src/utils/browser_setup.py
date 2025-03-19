import pytest
from playwright.sync_api import sync_playwright
from src.config.settings import BROWSER, BROWSER_OPTIONS, WEBSITE_URL


@pytest.fixture(scope="module")
def setup_browser():
    with sync_playwright() as pw:
        browser = getattr(pw, BROWSER).launch(**BROWSER_OPTIONS)
        context = browser.new_context()
        page = context.new_page()
        page.goto(WEBSITE_URL)
        yield page

        page.close()
        browser.close()
