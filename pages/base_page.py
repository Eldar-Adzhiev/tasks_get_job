import datetime
from typing import List

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)

    def open(self):
        self.browser.get(self.url)

    def refresh_page(self):
        self.browser.refresh()

    def get_element(self, locator, time=10) -> WebElement:
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def get_elements(self, locator, time=10) -> List:
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def is_element_present(self, how_search, what_search):
        try:
            self.browser.find_element(how_search, what_search)
        except NoSuchElementException:
            return False
        return True

    def is_text_present(self, locator, text, time=10):
        try:
            WebDriverWait(self.browser, time).until(EC.text_to_be_present_in_element(locator, text),
                                                    message=f"Can't find elements with {text}")
        except TimeoutException:
            return False
        return True

    @staticmethod
    def get_date():
        return int(str(datetime.date.today()).split("-")[-1])