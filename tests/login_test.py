from playwright.sync_api import Page 
from pages.login_page import LoginPage

def test_login_page(page: Page):
    page.goto("https://practice.automationtesting.in/my-account/")
    
    login = LoginPage(page)

    # login.enter_username("kaceho@game.id")
    # login.enter_password("password")
    # login.click_login()
    
    login.login("kaceho@id.game", "kaceho@id.game1")
    page.wait_for_timeout(1000)