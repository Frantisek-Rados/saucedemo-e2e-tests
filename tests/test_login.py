from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new.page()
        login_page = LoginPage(page)
        login_page.go_to()
        login_page.login("standart_user", "secret_sauce")
        assert page.url == "https://www.saucedemo.com/invertory.html"
        browser.close()
