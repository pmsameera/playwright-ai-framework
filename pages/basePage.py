class BasePage:

    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def clickBtn(self, locator):
        self.page.locator(locator).click()
