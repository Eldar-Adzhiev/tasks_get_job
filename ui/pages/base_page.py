from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser, url="https://reqres.in/"):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def get_element(self, locator):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element




