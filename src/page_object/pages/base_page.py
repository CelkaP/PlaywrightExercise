from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def find_element(self, locator):
        return self.page.locator(locator).first

    def find_elements(self, locator):
        return self.page.locator(locator).all()

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def check_checkbox(self, checkbox):
       if not checkbox.is_checked():
           checkbox.check()


    def uncheck_checkbox(self, checkbox):
        if checkbox.is_checked():
            checkbox.uncheck()
