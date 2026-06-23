from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = "#first-name"
        self.last_name_input = "#last-name"
        self.postal_code_input = "#postal-code"
        self.continue_button = "#continue"
        self.finish_button = "#finish"
        self.complete_header = ".complete-header"

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code_input, postal_code)
        self.page.click(self.continue_button)

    def finish_order(self):
        self.page.click(self.finish_button)

    def get_success_message(self) -> str:
        return self.page.text_content(self.complete_header)