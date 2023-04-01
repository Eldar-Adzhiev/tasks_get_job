from api.user import Users
from jsonschema import validate
from api.schemas.crud_user import *
from ui.pages.main_page import MainPage


def test_create_user():
    user = Users()
    response = user.create_user()
    validate(instance=response.json(), schema=create_user_schems)
    assert response.status_code == 201, "Incorrect status code"


def test_compare_respons_ui_api(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.scroll_page_to_element(MainPage.CREATE_USER)
    main_page.get_element(MainPage.CREATE_USER).click()


