import allure

from pages.form_page import FormPage
from utils.config_parser import ConfigParser


@allure.suite("Тестовое задание")
def test_textform(browser, username, mail, current_address, permanent_address):
    link = ConfigParser("config.json").get_config()["url"]
    page = FormPage(browser, link)
    page.open()
    page.input_user_name(username)
    page.input_user_email(mail)
    page.input_current_address(current_address)
    page.input_permanent_address(permanent_address)
    page.click_submit_button()
    assert page.is_output_message_present(), "Output message doesn't present"

    assert page.get_name() == username, "Incorrect username \n" \
                                        f"Expected: {username}. \n" \
                                        f"Actual: {page.get_name()}"

    assert page.get_email() == mail, "Incorrect email \n" \
                                        f"Expected: {mail}. \n" \
                                        f"Actual: {page.get_email()}"

    assert page.get_current_address() == current_address, "Incorrect current address \n" \
                                        f"Expected: {current_address}. \n" \
                                        f"Actual: {page.get_current_address()}"

    assert page.get_permanent_address() == permanent_address, "Incorrect permanent address \n" \
                                        f"Expected: {permanent_address}. \n" \
                                        f"Actual: {page.get_permanent_address()}"
