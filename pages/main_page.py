import allure
from selenium.webdriver.common.by import By


class MainPage:

    USER_NAME = (By.XPATH, '//*[contains(@class,"fontBig")]')
    TRANSACTIONS = (By.XPATH, '//button[@ng-click="transactions()"]')
    DEPOSIT = (By.XPATH, '//button[@ng-click="deposit()"]')
    WITHDRAW = (By.XPATH, '//button[@ng-click="withdrawl()"]')

    INPUT_SUM_FIELD = (By.XPATH, '//input[@ng-model="amount"]')
    BUTTON_SUBMIT_SUM = (By.XPATH, '//button[contains(@class, "btn-default")]')
    INPUT_SUM_FIELD_LABEL = (By.XPATH, '//div[@class="form-group"]/label')
    BALANCE = (By.XPATH, '//strong[@class="ng-binding"][2]')

    def __init__(self, app):
        self.app = app

    def get_user_name(self):
        with allure.step("Get username"):
            return self.app.get_element(MainPage.USER_NAME)

    def click_button_transactions(self):
        with allure.step("Click button transactions"):
            self.app.get_element(MainPage.TRANSACTIONS).click()

    def click_button_deposit(self):
        with allure.step("Click button deposit"):
            self.app.get_element(MainPage.DEPOSIT).click()

    def click_button_withdraw(self):
        with allure.step("Click button withdraw"):
            self.app.get_element(MainPage.WITHDRAW).click()

    def input_balance(self, key):
        with allure.step("Input balance"):
            field = self.app.get_element(MainPage.INPUT_SUM_FIELD)
            field.click()
            field.clear()
            field.send_keys(key)

    def click_button_submit_sum(self):
        with allure.step("Click button submit sum"):
            self.app.get_element(MainPage.BUTTON_SUBMIT_SUM).click()

    def get_input_field_name(self):
        with allure.step("Get input field name"):
            return self.app.get_element(MainPage.INPUT_SUM_FIELD_LABEL).text

    def is_field_text_present(self, text):
        with allure.step("Get input field text"):
            return self.app.is_text_present(MainPage.INPUT_SUM_FIELD_LABEL, text)

    def get_balance(self):
        with allure.step("Get balance"):
            return self.app.get_element(MainPage.BALANCE).text
