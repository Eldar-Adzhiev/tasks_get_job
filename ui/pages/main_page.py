from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class MainPage(BasePage):
    CREATE_USER = (By.CSS_SELECTOR, "[data-id='post']")
    RESPONSE_CODE = (By.CSS_SELECTOR, "[data-key='response-code']")
    RESPONSE_BODY = (By.CSS_SELECTOR, "[data-key='output-response']")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_status_code(self):
        return self.wait_element(self.RESPONSE_CODE)

    def get_response_body(self):
        return self.wait_element(self.RESPONSE_BODY)