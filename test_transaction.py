import time

import allure

from pages.base_page import BasePage
from pages.main_page import MainPage
from utils.config_parser import ConfigParser
from utils.csv_file import FileUtil
from utils.help_functions import fibonacci
from utils.work_dir import get_absolute_path


@allure.suite("Тестовое задание")
def test_transactions(browser):
    link = ConfigParser("config.json").get_config()["url"]
    page = BasePage(browser, link)
    page.open()
    page.auth_page.login()
    assert page.is_element_present(*MainPage.USER_NAME), "Main page don't open"
    assert page.main_page.get_user_name().text == "Harry Potter", "Incorrect username."

    date = page.get_date()
    balance = fibonacci(date+1)
    page.main_page.click_button_deposit()
    assert page.main_page.is_field_text_present("Amount to be Deposited :"), "Field has incorrect label"

    page.main_page.input_balance(balance)
    page.main_page.click_button_submit_sum()
    assert int(page.main_page.get_balance()) == balance, "Incorrect balance"
    assert page.main_page.is_message_present("Deposit Successful"), "Message about Deposit Successful doesn't present"
    time.sleep(1)
    page.main_page.click_button_transactions()
    assert page.main_page.is_transaction_present(1), "Transaction not present"
    page.main_page.click_button_back()
    time.sleep(1)

    page.main_page.click_button_withdraw()
    assert page.main_page.is_field_text_present("Amount to be Withdrawn :"), "Field has incorrect label"

    page.main_page.input_balance(balance)
    page.main_page.click_button_submit_sum()
    assert page.main_page.get_balance() == '0', "Incorrect balance"
    assert page.main_page.is_message_present("Transaction successful"), \
        "Message about Transaction successful doesn't present"
    time.sleep(1)
    page.main_page.click_button_transactions()
    assert page.main_page.is_transaction_present(2), "Transaction not present"

    transactions_count = len(page.main_page.get_transactions())

    data = []
    for i in range(transactions_count):
        data_list = []
        data_list.append(page.main_page.get_date(i))
        data_list.append(page.main_page.get_amount(i))
        data_list.append(page.main_page.get_transaction_type(i))
        data.append(data_list)
    a = FileUtil()
    a.write_csv("test", data)

    allure.attach.file(get_absolute_path("generated_files/test.csv"))
