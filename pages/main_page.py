import allure
from selenium.webdriver.common.by import By
import re

from utils.csv_file import FileUtil


class MainPage:

    USER_NAME = (By.XPATH, '//*[contains(@class,"fontBig")]')
    TRANSACTIONS = (By.XPATH, '//button[@ng-click="transactions()"]')
    DEPOSIT = (By.XPATH, '//button[@ng-click="deposit()"]')
    WITHDRAW = (By.XPATH, '//button[@ng-click="withdrawl()"]')

    INPUT_SUM_FIELD = (By.XPATH, '//input[@ng-model="amount"]')
    BUTTON_SUBMIT_SUM = (By.XPATH, '//button[contains(@class, "btn-default")]')
    INPUT_SUM_FIELD_LABEL = (By.XPATH, '//div[@class="form-group"]/label')
    BALANCE = (By.XPATH, '//strong[@class="ng-binding"][2]')
    MESSAGE = (By.XPATH, '//span[@ng-show="message"]')
    BUTTON_BACK = (By.XPATH, '//button[@ng-click="back()"]')

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

    def is_transaction_present(self, index):
        with allure.step("Get transaction"):
            return self.app.is_element_present(By.XPATH, f'//tbody/tr[{index}]')

    def click_button_back(self):
        with allure.step("Click button back"):
            self.app.get_element(MainPage.BUTTON_BACK).click()

    def is_message_present(self, text):
        with allure.step("Check message about transaction"):
            return self.app.is_text_present(MainPage.MESSAGE, text)

    def get_transactions(self):
        with allure.step("Get transactions"):
            return self.app.get_elements((By.XPATH, '//tbody/tr[contains(@id, "anchor")]'))

    def get_date(self, row):
        with allure.step("Get data"):
            data: str = self.app.get_element((By.XPATH, f'//tbody/tr[@id="anchor{row}"]/td[@class="ng-binding"][1]')).text
            data_list = re.split(r"[, ]", data)
            return data_list[1] + " " + data_list[0] + " " + data_list[3] + " " + data_list[4]

    def get_amount(self, row):
        with allure.step("Get amount"):
            return self.app.get_element((By.XPATH, f'//tbody/tr[@id="anchor{row}"]/td[@class="ng-binding"][2]')).text

    def get_transaction_type(self, row):
        with allure.step("Get transaction type"):
            return self.app.get_element((By.XPATH, f'//tbody/tr[@id="anchor{row}"]/td[@class="ng-binding"][3]')).text

    def write_transactions_to_csv(self, transactions_count):
        date = []
        for i in range(transactions_count):
            date_list = []
            date_list.append(self.get_date(i))
            date_list.append(self.get_amount(i))
            date_list.append(self.get_transaction_type(i))
            date.append(date_list)
        a = FileUtil()
        a.write_csv("test", date)