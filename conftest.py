import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():

    print("\nstart chrome browser for test..")
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Remote(command_executor="http://localhost:4444",
                               options=chrome_options)
    browser.maximize_window()

    yield browser

    browser.quit()
