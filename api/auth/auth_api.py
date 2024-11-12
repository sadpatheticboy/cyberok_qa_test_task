""" Эндпоинты для работы с авторизацией """

from typing import Optional
from api.base_api import BaseApi


class AuthApi:

    def __init__(self, session) -> None:
        self.session = session

    @staticmethod
    def create_auth_token(username: Optional[str] = None, password: Optional[str] = None, **kwargs) -> dict:
        """
        Отправляет запрос для создания токена авторизации
        :param username: Логин для авторизации
        :param password: Пароль для авторизации
        :return: Ответ сервера
        """

        data = {
            'username': username,
            'password': password
        }

        response = BaseApi.post(url='/auth', data=data, **kwargs)

        return response.json()
