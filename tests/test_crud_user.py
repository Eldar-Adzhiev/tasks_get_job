from api.user import Users
from jsonschema import validate
from api.schemas.crud_user import *


def test_create_user():
    user = Users()
    response = user.create_user()
    validate(instance=response.json(), schema=create_user_schems)
    assert response.status_code == 201, "Incorrect status code"


