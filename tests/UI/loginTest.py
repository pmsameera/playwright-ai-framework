from pages.loginPage import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.openURL()
    login.login("standard_user", "secret_sauce")