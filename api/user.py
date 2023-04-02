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

    def update_user(self, name="morpheus", job="zion resident"):
        return self.put(end_point="api/users/2",
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
