from api.base_request import BaseRequest
import json


class Users(BaseRequest):

    def get_list_users(self, page: int):
        return self.get(end_point="api/users",
                        params={
                             "page": f"{page}"
                         })

    def get_user(self, id: int):
        return self.get(end_point=f"api/users/{id}")

    def create_user(self):
        return self.post(end_point="api/users",
                         data={
                             "name": "morpheus",
                             "job": "leader"
                         },
                         check_status=False, jsonify=False)

    def update_user(self):
        return self.put(end_point="api/users/2",
                        data={
                             "name": "morpheus",
                             "job": "zion resident"
                         })

    def delete_user(self):
        return self.delete(end_point="api/users/2")

    def register(self):
        return self.post(end_point="api/register",
                         data={
                             "email": "eve.holt@reqres.in",
                             "password": "pistol"
                         })

    def login(self):
        return self.post(end_point="api/login",
                         data={
                             "email": "eve.holt@reqres.in",
                             "password": "cityslicka"
                         })
