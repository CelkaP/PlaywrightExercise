from src.page_object.pages.base_page import BasePage
from src.page_object.locators import Locator


class BlogPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @property
    def accept_cookies_button(self):
        return self.find_element(Locator.cookies_agree_button)

    @property
    def leadership_link(self):
        return self.find_element(Locator.leadership_under_about)

    @property
    def filter_by(self):
        return self.find_element(Locator.filter_by)

    @property
    def cloud_and_dev_ops_filter(self):
        return self.find_element(Locator.cloud_and_dev_ops_filter)

    @property
    def articles(self):
        return self.find_elements(Locator.articles)

    @property
    def all_topics(self):
        return self.find_elements(Locator.all_topics)

    @property
    def top_articles(self):
        return self.find_elements(Locator.top_articles)

    @property
    def get_in_touch_button(self):
        return self.find_element(Locator.get_in_touch_button)

    def click_get_in_touch_btn(self):
        self.get_in_touch_button.click()

    def click_accept_cookies_button(self):
        self.accept_cookies_button.click()

    def click_leadership_link(self):
        self.leadership_link.click()

    def click_filter_by(self):
        self.filter_by.click()

    def click_all_topics(self):
        self.all_topics.click()

    def click_cloud_and_dev_ops_filter(self):
        self.cloud_and_dev_ops_filter.click()

    def get_selected_category(self):
        return self.filter_by.get_attribute("class")

    def get_selected_all_topics_class(self):
        return self.all_topics.get_attribute("class")

    def get_cloud_and_dev_ops_filter_class(self):
        return self.cloud_and_dev_ops_filter.get_attribute("class")
