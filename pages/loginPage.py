from pages.basePage import BasePage

class LoginPage(BasePage):

    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def openURL(self):
        self.goto("https://www.saucedemo.com")

    def login(self, userName, passWord):
        self.fill(self.USERNAME, userName)
        self.fill(self.PASSWORD, passWord)
        self.clickBtn(self.LOGIN_BUTTON)
