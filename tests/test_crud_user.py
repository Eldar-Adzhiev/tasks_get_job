import time

import pytest

from api.user import Users, get_user
from jsonschema import validate
from api.schemas.crud_user import *
from ui.pages.main_page import MainPage
import json


@pytest.mark.parametrize("user", [
    (Users().create_user()),
    (Users().create_user(name="anotherName", job="AnotherJob")),
    (Users().create_user(name="", job=""))

])
def test_create_user(user):
    response = user
    print(response.json())
    validate(instance=response.json(), schema=create_user_schemas)
    assert response.status_code == 201, "Incorrect status code"


def test_compare_respons_ui_api(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.wait_element(MainPage.CREATE_USER).click()
    status_code_ui = main_page.get_status_code().text
    body_ui = json.loads(main_page.get_response_body().text)
    user = Users()
    response = user.create_user()
    status_code_api = response.status_code
    body_api = response.json()
    assert status_code_api == int(status_code_ui), "Status codes not equal on ui and api. " \
                                                   f"ui = {status_code_ui}." \
                                                   f"api = {status_code_api}"
    assert sorted(body_api.keys()) == sorted(body_ui.keys()), "Response body not equal. " \
                                                              f"ui = {sorted(body_ui.keys())}. " \
                                                              f"api = {sorted(body_api.keys())}"


def test_get_user_by_id(create_user):
    user = get_user(create_user["id"])
    assert user, "User doesn't found "
    assert user["name"] == create_user["name"], \
        "User name incorrect. " \
        f"Expected {create_user['name']} " \
        f"Actual {user['name']}"


@pytest.mark.parametrize("name, job", [
    ("", ""),
    ("AnotherName", "AnotherJob"),
    (1234, 1243),
    ("Name-with", "job-with"),
    ("N_ame", "J_ob")
])
def test_update_user(create_user, name, job):
    users = Users()
    response = users.update_user(create_user["id"], name, job)
    assert response.status_code == 200, "Incorrect status code " \
                                        f"Expected = {200} " \
                                        f"Actual = {response.status_code}"
    assert response.json()["name"] == name, "Incorrect name. " \
                                            f"Expected = {name} " \
                                            f"Actual = {response.json()['name']}"
    assert response.json()["job"] == job, "Incorrect name. " \
                                          f"Expected = {job} " \
                                          f"Actual = {response.json()['job']}"
