from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class MainPage(BasePage):
    CREATE_USER = (By.CSS_SELECTOR, "[data-id='post']")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


