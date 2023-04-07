from selenium.webdriver.common.by import By
import allure


class AuthorizationPage:
    CUSTOMER_LOGIN = (By.XPATH, '//button[@ng-click="customer()"]')
    DROP_DOWN_MENU = (By.TAG_NAME, "select")
    USER_HARRY_POTTER = (By.CSS_SELECTOR, "option:nth-child(3)")
    LOGIN_BUTTON = (By.XPATH, '//form[@name="myForm"]/button')

    def __init__(self, app):
        self.app = app

    def _click_customer_login(self):
        with allure.step("Click button customer login"):
            self.app.get_element(AuthorizationPage.CUSTOMER_LOGIN).click()

    def _click_on_drop_down_menu(self):
        with allure.step("Click next button"):
            self.app.get_element(AuthorizationPage.DROP_DOWN_MENU).click()

    def _click_on_harry_potter_user(self):
        with allure.step("Click on Harry Potter user"):
            self.app.get_element(AuthorizationPage.USER_HARRY_POTTER).click()

    def _click_login_button(self):
        with allure.step("Click login button"):
            self.app.get_element(AuthorizationPage.LOGIN_BUTTON).click()

    def login(self):
        with allure.step("login"):
            self._click_customer_login()
            self._click_on_drop_down_menu()
            self._click_on_harry_potter_user()
            self._click_login_button()
