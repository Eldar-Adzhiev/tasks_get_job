from api.base_request import BaseRequest
import json


class Users(BaseRequest):

    def get_list_users(self, page: int):
        return self.get(end_point="api/users",
                        params={
                            "page": f"{page}"
                        },
                        check_status=False,
                        jsonify=False)

    def get_user(self, user_id: int):
        return self.get(end_point=f"api/users/{user_id}",
                        check_status=False,
                        jsonify=False)

    def create_user(self, name="morpheus", job="leader"):
        return self.post(end_point="api/users",
                         data={
                             "name": name,
                             "job": job
                         },
                         check_status=False,
                         jsonify=False)

    def update_user(self, user_id=2, name="morpheus", job="zion resident"):
        return self.put(end_point=f"api/users/{user_id}",
                        data={
                            "name": name,
                            "job": job
                        },
                        check_status=False,
                        jsonify=False)

    def delete_user(self, user_id=2):
        return self.delete(end_point=f"api/users/{user_id}",
                           check_status=False,
                           jsonify=False)

    def register(self, email="eve.holt@reqres.in", password="pistol"):
        return self.post(end_point="api/register",
                         data={
                             "email": email,
                             "password": password
                         },
                         check_status=False,
                         jsonify=False)

    def login(self, email="eve.holt@reqres.in", password="cityslicka"):
        return self.post(end_point="api/login",
                         data={
                             "email": email,
                             "password": password
                         },
                         check_status=False,
                         jsonify=False)


def get_user(user_id):
    users = Users()
    page_number = 1
    list_of_users = users.get_list_users(page_number)
    for page_count in range(list_of_users.json()["total_pages"]):
        list_of_users = users.get_list_users(page_number)
        page_number += 1
        for user_count in range(len(list_of_users.json()["data"])):
            if list_of_users.json()["data"][user_count]["id"] == user_id:
                return list_of_users.json()["data"][user_count]
    return False
