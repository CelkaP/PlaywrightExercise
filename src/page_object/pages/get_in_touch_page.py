from src.page_object.locators import Locator
from src.page_object.pages.base_page import BasePage


class GetInTouch(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @property
    def first_name(self):
        return self.find_element(Locator.first_name)

    @property
    def last_name(self):
        return self.find_element(Locator.last_name)

    @property
    def email(self):
        return self.find_element(Locator.email)

    @property
    def interested_in(self):
        return self.find_element(Locator.interested_in)

    @property
    def careers_employment(self):
        return self.find_element(Locator.careers_employment)

    @property
    def terms_checkbox(self):
        return self.page.query_selector(Locator.terms_checkbox)

    @property
    def newsletter(self):
        return self.page.query_selector(Locator.newsletter)

    @property
    def submit_btn(self):
        return self.find_element(Locator.submit_btn)

    @property
    def submit_btn_class(self):
        return self.submit_btn.get_attribute("class")

    @property
    def accept_cookies_button(self):
        return self.find_element(Locator.cookies_agree_button)

    def click_accept_cookies_button(self):
        self.accept_cookies_button.click()

    def enter_first_name(self, first_name):
        self.first_name.fill(first_name)

    def enter_last_name(self, last_name):
        self.last_name.fill(last_name)

    def enter_email(self, email):
        self.email.fill(email)

    def click_interested_in(self):
        self.interested_in.click()

    def click_careers_employment(self):
        self.careers_employment.click()

    def accept_terms(self):
        self.check_checkbox(self.terms_checkbox)

    def accept_newsletter(self):
        self.check_checkbox(self.newsletter)
