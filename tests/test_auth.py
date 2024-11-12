""" Тесты для проверки авторизации """

import allure
import pytest

from configs.marks import auth_api
from api.auth.auth_api import AuthApi
from snippets.base_checks import BaseChecks

pytest_mark = [auth_api]


@allure.feature("API")
@allure.story("API 'restful-booker'")
@allure.epic("Аккаунт")
@allure.suite("Авторизация")
@allure.parent_suite("Позитивные тесты")
@allure.title('Тест на отправку верного запроса на авторизацию')
def test_auth_with_valid_credentials():
    with allure.step("Отправляем запрос на получение доступа"):
        response = AuthApi.create_auth_token(username='admin', password='password123')

    with allure.step("В ответе сообщение с токеном"):
        BaseChecks.check_field_exist(response=response, field='token')


@allure.feature("API")
@allure.story("API 'restful-booker'")
@allure.epic("Аккаунт")
@allure.suite("Авторизация")
@allure.parent_suite("Негативные тесты")
@allure.title('Тест на отправку неверного запроса на авторизацию')
@pytest.mark.parametrize('credentials', [('admin',), ('admin', 'wrong_password')])
def test_auth_with_invalid_credentials(credentials):
    with allure.step("Отправляем запрос на получение доступа"):
        response = AuthApi.create_auth_token(*credentials)

    with allure.step("В ответе сообщение о неправильных данных"):
        BaseChecks.check_error(response=response, error='Bad credentials')
