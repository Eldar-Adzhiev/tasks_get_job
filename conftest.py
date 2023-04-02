import pytest
from selenium import webdriver

from api.user import Users


@pytest.fixture(scope="function")
def browser():
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture()
def create_user():
    response = Users().create_user()
    return response.json()
