from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = "#checkout"

    def proceed_to_checkout(self):
        self.page.wait_for_selector("#checkout", state="visible")
        self.page.click(self.checkout_button)