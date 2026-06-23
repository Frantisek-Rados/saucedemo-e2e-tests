from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.header_page import HeaderPage

def test_full_purchase_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Prihlásenie
        login_page = LoginPage(page)
        login_page.go_to()
        login_page.login("standard_user", "secret_sauce")

        # 2. Pridanie produktu do košíka
        inventory_page = InventoryPage(page)
        inventory_page.add_product_to_cart()
        assert inventory_page.get_cart_count() == "1"

        # 3. Prechod do košíka – priamo cez URL
        page.goto("https://www.saucedemo.com/cart.html")
        page.wait_for_selector("#checkout", state="visible", timeout=10000)

        # 4. Prechod na checkout
        cart_page = CartPage(page)
        cart_page.proceed_to_checkout()

        # 5. Vyplnenie údajov a dokončenie objednávky
        checkout_page = CheckoutPage(page)
        checkout_page.fill_customer_info("František", "Radoš", "12345")
        checkout_page.finish_order()

        # 6. Overenie úspešného dokončenia
        assert checkout_page.get_success_message() == "Thank you for your order!"

        # 7. Odhlásenie
        header_page = HeaderPage(page)
        header_page.logout()

        # 8. Overenie presmerovania na login stránku
        assert page.url == "https://www.saucedemo.com/"

        browser.close()