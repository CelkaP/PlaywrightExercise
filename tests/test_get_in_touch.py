import pytest

from src.page_object.pages.blog_page import BlogPage
from src.page_object.pages.get_in_touch_page import GetInTouch


def test_is_submit_btn_inactive(page):
    bp = BlogPage(page)
    bp.click_accept_cookies_button()
    bp.click_get_in_touch_btn()
    gt = GetInTouch(page)
    gt.enter_first_name("Anna")
    gt.enter_last_name("Smith")
    gt.enter_email("annasmith@griddynamics.com")
    gt.accept_newsletter()
    gt.accept_terms()
    gt.click_interested_in()
    gt.click_careers_employment()

    assert gt.submit_btn_class == "get-in-touch-form__field submit disabled"
