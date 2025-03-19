import pytest

from src.page_object.pages.blog_page import BlogPage
from src.page_object.pages.leadership_page import LeadershipPage
from src.utils.browser_setup import setup_browser


@pytest.fixture(scope="module")
def page(setup_browser):
    return setup_browser


@pytest.fixture(scope="module")
def cached_leonard_info(page):
    bp = BlogPage(page)
    bp.click_accept_cookies_button()
    bp.click_leadership_link()
    lp = LeadershipPage(page)
    lp.click_on_leonard()
    return [lp.leonard_bio, lp.leonard_position]


@pytest.fixture(scope="module")
def articles_cached(page):
    bp = BlogPage(page)
    bp.click_accept_cookies_button()
    bp.click_filter_by()
    bp.click_cloud_and_dev_ops_filter()
    cloud_and_dev_ops_articles = bp.articles
    bp.click_filter_by()
    bp.click_all_topics()
    top_articles = bp.top_articles
    return [cloud_and_dev_ops_articles, top_articles]
