from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = "#add-to-cart-sauce-labs-backpack"
        self.cart_badge = ".shopping_cart_badge"
        self.cart_link = ".shopping_cart_link"

    def add_product_to_cart(self):
        self.page.click(self.add_to_cart_button)

    def get_cart_count(self) -> str:
        return self.page.text_content(self.cart_badge)
    
    def go_to_cart(self):
        self.page.click(self.cart_link)
        self.page.wait_for_selector("**/cart.html", timeout=10000)