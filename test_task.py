import time

import allure

from pages.base_page import BasePage
from pages.main_page import MainPage
from utils.config_parser import ConfigParser


@allure.suite("Тестовое задание")
def test_login_and_send_new_message(browser):
    link = ConfigParser("config.json").get_config()["url"]
    page = BasePage(browser, link)
    page.open()
    page.auth_page.login()
    assert page.is_element_present(*MainPage.USER_NAME), "Main page don't open"
    assert page.main_page.get_user_name().text == "Harry Potter", "Incorrect username."

    date = page.get_date()
    balance = page.fibonacci(date+1)
    page.main_page.click_button_deposit()
    assert page.main_page.is_field_text_present("Amount to be Deposited :"), "Field has incorrect label"

    page.main_page.input_balance(balance)
    page.main_page.click_button_submit_sum()
    assert int(page.main_page.get_balance()) == balance, "Incorrect balance"
    time.sleep(2)
    page.main_page.click_button_withdraw()
    assert page.main_page.is_field_text_present("Amount to be Withdrawn :"), "Field has incorrect label"

    page.main_page.input_balance(balance)
    page.main_page.click_button_submit_sum()
    assert page.main_page.get_balance() == '0', "Incorrect balance"
    time.sleep(2)
    page.main_page.click_button_transactions()
    time.sleep(15)
