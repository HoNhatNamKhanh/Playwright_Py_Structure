from pages.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
    def __init__(self, page: Page):
            self.page = page
            # Set locators here
            self.username_input = "#username"
            self.password_input = "#password"
            self.login_button = 'input[value="Login"]'

    # Actions
    def enter_username(self, username: str):
        self.fill(self.username_input, username)

    def enter_password(self, password: str):
        self.fill(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
