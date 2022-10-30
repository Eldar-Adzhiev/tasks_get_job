from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class Authorization(BasePage):
    EMAIL_OR_PHONE = (By.CSS_SELECTOR, "#identifierId")
    NEXT_BUTTON = (By.CSS_SELECTOR,
                   '[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]')
    PASSWORD = (By.CSS_SELECTOR, '[name="Passwd"]')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _input_email(self):
        with allure.step("Input email"):
            email_field = self.get_element(Authorization.EMAIL_OR_PHONE)
            email_field.send_keys("eldartestauto@gmail.com")

    def _click_next(self):
        with allure.step("Click next button"):
            next_button = self.get_element(Authorization.NEXT_BUTTON)
            next_button.click()

    def _input_password(self):
        with allure.step("Input password"):
            password = self.get_element(Authorization.PASSWORD)
            password.send_keys("dF9EfTLKH!JRhZf")

    def login(self):
        with allure.step("login in gmail"):
            login = Authorization(self.browser, self.url)
            login.open()
            login._input_email()
            login._click_next()
            login._input_password()
            login._click_next()


