import inspect
import requests


class BaseRequest:

    def __init__(self, url="https://reqres.in/"):
        self.session = requests.Session()
        self.__url = url

    def _request(self, method, end_point, headers=None, cookies=None, params=None, data=None, json_data=None,
                 files=None,
                 check_status=True, expect_status=200, jsonify=True):

        response = self.session.request(method, url=self.__url + end_point, params=params,
                                        data=data, json=json_data, files=files, cookies=cookies, headers=headers)

        if check_status:
            assert expect_status == response.status_code, \
                f"Класс = {self.__class__.__name__}, метод = {inspect.stack()[2][3]} \n" \
                f"Запрос на endpoint -  {end_point} \n" \
                f"Ожидаемый статус код = {expect_status} \n" \
                f"Фактический статус код = {response.status_code}\n" \
                f"Текст ошибки: {response.text}"

        if jsonify:
            return response.json()

        return response

    def get(self, **kwargs):
        return self._request(method="GET", **kwargs)

    def post(self, **kwargs):
        return self._request(method="POST", **kwargs)

    def put(self, **kwargs):
        return self._request(method="PUT", **kwargs)

    def delete(self, **kwargs):
        return self._request(method="DELETE", **kwargs)
