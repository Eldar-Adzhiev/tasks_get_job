from selenium.webdriver.common.by import By
import allure

from pages.base_page import BasePage


class FormPage(BasePage):
    FIELD_USER_NAME = (By.CSS_SELECTOR, '#userName')
    FIELD_USER_EMAIL = (By.CSS_SELECTOR, "#userEmail")
    FIELD_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    FIELD_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#permanentAddress')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, '#submit')
    OUTPUT = (By.CSS_SELECTOR, '#output')
    OUTPUT_NAME = (By.CSS_SELECTOR, '#name')
    OUTPUT_EMAIL = (By.CSS_SELECTOR, '#email')
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#permanentAddress')

    def input_user_name(self, username):
        with allure.step("Input user name"):
            element = self.get_element(self.FIELD_USER_NAME)
            element.clear()
            element.send_keys(username)

    def input_user_email(self, user_email):
        with allure.step("Click next button"):
            element = self.get_element(self.FIELD_USER_EMAIL)
            element.clear()
            element.send_keys(user_email)

    def input_current_address(self, current_address):
        with allure.step("Click on Harry Potter user"):
            element = self.get_element(self.FIELD_CURRENT_ADDRESS)
            element.clear()
            element.send_keys(current_address)

    def input_permanent_address(self, permanent_address):
        with allure.step("Click login button"):
            element = self.get_element(self.FIELD_PERMANENT_ADDRESS)
            element.clear()
            element.send_keys(permanent_address)

    def click_submit_button(self):
        with allure.step("Click submit button"):
            button = self.get_element(self.BUTTON_SUBMIT)
            self.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            button.click()

    def is_output_message_present(self):
        with allure.step("Check that output message present"):
            return self.is_element_present(*self.OUTPUT)

    def get_name(self):
        with allure.step("Get name"):
            text = self.get_element(self.OUTPUT_NAME).text
            list_name = text.split(':')
            return list_name[1]

    def get_email(self):
        with allure.step("Get email"):
            text = self.get_element(self.OUTPUT_EMAIL).text
            list_email = text.split(':')
            return list_email[1]

    def get_current_address(self):
        with allure.step("Get current address"):
            element = self.get_elements(self.OUTPUT_CURRENT_ADDRESS)
            text = element[1].text
            list_current_address = text.split(':')
            return list_current_address[1]

    def get_permanent_address(self):
        with allure.step("Get permanent address"):
            element = self.get_elements(self.OUTPUT_PERMANENT_ADDRESS)
            text = element[1].text
            list_permanent_address = text.split(':')
            return list_permanent_address[1]
