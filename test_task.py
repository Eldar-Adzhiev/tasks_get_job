from pages.incoming_messages_page import IncomingMessages
import time
import allure

@allure.suite("Тестовое задание")
def test_login_and_send_new_message(browser):
    link = "https://mail.google.com/"
    task = IncomingMessages(browser, link)
    task.login()
    count = task.get_count_of_messages()
    task.click_write_new_message()
    task.input_to()
    task.input_count_of_message(count)
    task.input_topic()
    task.click_send()
    time.sleep(5)

