import allure
from selenium.webdriver.common.by import By
from pages.authorization_page import Authorization


class IncomingMessages(Authorization):

    COUNT_OF_MESSAGES = (By.XPATH, '//tr[last()]/td[@class="yX xY "]/div[2]/span[2]')
    BUTTON_WRITE_NEW_MESSAGE = (By.CSS_SELECTOR, '[class="T-I T-I-KE L3"]')
    TO = (By.CSS_SELECTOR, '[class="agP aFw"]')
    MESSAGE_FIELD = (By.CSS_SELECTOR, '[class="Am Al editable LW-avf tS-tW"]')
    SEND_BUTTON = (By.CSS_SELECTOR, '[class="dC"]>[class="T-I J-J5-Ji aoO v7 T-I-atl L3"]')
    TOPIC_FIELD = (By.CSS_SELECTOR, '[class="aoT"]')

    def get_count_of_messages(self):
        count = self.browser.find_element(*IncomingMessages.COUNT_OF_MESSAGES).text
        return count


    def click_write_new_message(self):
        with allure.step("Click write new message"):
            write_new_message = self.get_element(IncomingMessages.BUTTON_WRITE_NEW_MESSAGE)
            write_new_message.click()

    def input_to(self):
        with allure.step("Input email address to new message"):
            to = self.get_element(IncomingMessages.TO)
            to.send_keys("eldartestauto@gmail.com")

    def input_topic(self):
        with allure.step("Input topic to new message"):
            topic = self.get_element(IncomingMessages.TOPIC_FIELD)
            topic.send_keys("Simbirsoft Тестовое задание. Аджиев")

    def input_count_of_message(self, count):
        with allure.step("Input count of message in message field"):
            message_field = self.get_element(IncomingMessages.MESSAGE_FIELD)
            message_field.send_keys(count)

    def click_send(self):
        with allure.step("Click send"):
            send_message = self.get_element(IncomingMessages.SEND_BUTTON)
            send_message.click()
