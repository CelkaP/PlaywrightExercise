from src.page_object.locators import Locator
from src.page_object.pages.base_page import BasePage


class LeadershipPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @property
    def leonard(self):
        return self.find_element(Locator.leonard)

    @property
    def leonard_position(self):
        return self.find_element(Locator.leonard_position).text_content()

    @property
    def leonard_bio(self):
        return self.find_element(Locator.leonard_bio).text_content()

    def click_on_leonard(self):
        self.leonard.click()
