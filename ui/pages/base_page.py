from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser, url="https://reqres.in/"):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def wait_element(self, locator):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element

    def get_element(self, locator):
        return self.browser.find_element(locator)

    def scroll_page_to_element(self, element):
        self.browser.execute_script("scrollIntoView();", element)



