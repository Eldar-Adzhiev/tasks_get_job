import pytest
from selenium import webdriver

from utils.random_utils import RandomData


@pytest.fixture(scope="function")
def browser():

    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture
def username():
    username = RandomData()
    return username.get_random_fullname()


@pytest.fixture
def mail():
    username = RandomData()
    return username.get_random_mail()


@pytest.fixture
def current_address():
    username = RandomData()
    return username.get_random_address()


@pytest.fixture
def permanent_address():
    username = RandomData()
    return username.get_random_address()
