""" Базовый класс для работы с API """

import requests
from requests import Response


class BaseApi():
    BASE_URL = 'https://restful-booker.herokuapp.com'
    HEADERS = {"Content-Type": "application/json"}

    @staticmethod
    def post(**kwargs) -> Response:
        url = BaseApi.BASE_URL + kwargs.get('url')
        response = requests.post(url, json=kwargs.get('data'))

        return response

    @staticmethod
    def get(**kwargs) -> Response:
        url = BaseApi.BASE_URL + kwargs.get('url')
        response = requests.get(url=url, json=kwargs.get('data'))

        return response

    @staticmethod
    def put(**kwargs) -> Response:
        url = BaseApi.BASE_URL + kwargs.get('url')
        result = requests.put(url=url, json=kwargs.get('data'), headers=kwargs.get('cookies'))

        return result

    @staticmethod
    def patch(**kwargs) -> Response:
        url = BaseApi.BASE_URL + kwargs.get('url')
        result = requests.patch(url=url, json=kwargs.get('data'), headers=kwargs.get('cookies'))

        return result

    @staticmethod
    def delete(**kwargs) -> Response:
        url = BaseApi.BASE_URL + kwargs.get('url')
        result = requests.delete(url=url, headers=kwargs.get('cookies'))

        return result
