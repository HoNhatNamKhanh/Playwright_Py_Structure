from pages.base_page import BasePage

class LoginPage(BasePage):

    # Locators
    username_input = "User_mail"
    password_input = "User_Password"
    login_button = "Locator"

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
