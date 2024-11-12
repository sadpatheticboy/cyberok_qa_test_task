""" Тесты для проверки бронирования """

import allure

from api.auth.auth_api import AuthApi
from configs.marks import booking_api
from snippets.base_checks import BaseChecks
from api.booking.booking_api import BookingApi
from data.test_data import credentials_for_booking, expected_fields_booking, credentials_for_update_booking, \
    credentials_for_partial_update_booking

pytest_mark = [booking_api]


@allure.feature("API")
@allure.story("API 'restful-booker'")
@allure.epic("Бронирование")
@allure.suite("Бронирование")
@allure.parent_suite("Позитивные тесты")
@allure.title('Тест на отправку запроса на получение списка бронирований')
def test_booking_get_list_of_bookings():
    with allure.step("Отправляем запрос на получение списка бронирований"):
        response = BookingApi.get_booking_ids(firstname='John')

    with allure.step("В ответе сообщение с токеном"):
        BaseChecks.check_field_exist(response=response, field='bookingid')


@allure.feature("API")
@allure.story("API 'restful-booker'")
@allure.epic("Бронирование")
@allure.suite("Бронирование")
@allure.parent_suite("Позитивные тесты")
@allure.title('Тест на отправку запроса на получение конкретного бронирования по заданному ID')
def test_booking_get_current_booking_by_ids():
    with allure.step("Отправляем запрос на получение бронирования по заданному ID"):
        response = BookingApi.get_booking_by_id(booking_id=21)

    with allure.step("ОР:"):
        with allure.step('В ответе присутствуют все ожидаемые поля'):
            BaseChecks.check_fields_exist(response=response, fields=expected_fields_booking)


@allure.feature("API")
@allure.story("API 'restful-booker'")
@allure.epic("Бронирование")
@allure.suite("Бронирование")
@allure.parent_suite("Позитивные тесты")
@allure.title('Тест на создание бронирования')
def test_booking_get_current_booking_by_id():
    with allure.step("Отправляем запрос на создание бронирования"):
        response = BookingApi.post_create_booking(**credentials_for_booking)

    with allure.step('ОР:'):
        with allure.step('Бронь создалась'):
            BaseChecks.check_field_exist(response=response, field='bookingid')

        with allure.step('В ответе присутствуют все ожидаемые поля'):
            BaseChecks.check_fields_exist(response=response.get('booking'), fields=expected_fields_booking)


@allure.feature("API")
@allure.story("API 'restful-booker'")
@allure.epic("Бронирование")
@allure.suite("Бронирование")
@allure.parent_suite("Позитивные тесты")
@allure.title('Тест на обновление бронирования')
def test_booking_put_update_current_booking_by_id():
    with allure.step('Подготовка данных'):
        with allure.step("Отправляем запрос на получение доступа"):
            response = AuthApi.create_auth_token(username='admin', password='password123')
            token_auth = response.get('token')

        with allure.step("Отправляем запрос на создание бронирования"):
            response = BookingApi.post_create_booking(**credentials_for_booking)
            response_bookingid = response.get('bookingid')

    with allure.step("Отправляем запрос на обновление бронирования"):
        response_new = BookingApi.put_update_booking(booking_id=response_bookingid, token_auth=token_auth,
                                                     **credentials_for_update_booking)

    with allure.step('ОР:'):
        with allure.step('Бронь обновилась'):
            assert response_new != response, 'Бронь не обновилась'


@allure.feature("API")
@allure.story("API 'restful-booker'")
@allure.epic("Бронирование")
@allure.suite("Бронирование")
@allure.parent_suite("Позитивные тесты")
@allure.title('Тест на частичное обновление бронирования')
def test_booking_patch_update_current_booking_by_id():
    with allure.step('Подготовка данных'):
        with allure.step("Отправляем запрос на получение доступа"):
            response = AuthApi.create_auth_token(username='admin', password='password123')
            token_auth = response.get('token')

        with allure.step("Отправляем запрос на создание бронирования"):
            response = BookingApi.post_create_booking(**credentials_for_booking)
            response_bookingid = response.get('bookingid')

    with allure.step("Отправляем запрос на частичное обновление бронирования"):
        response_new = BookingApi.patch_partial_update_booking(booking_id=response_bookingid, token_auth=token_auth,
                                                               **credentials_for_partial_update_booking)


    with allure.step('ОР:'):
        with allure.step('Бронь обновилась'):
            assert response_new != response, 'Бронь не обновилась'


@allure.feature("API")
@allure.story("API 'restful-booker'")
@allure.epic("Бронирование")
@allure.suite("Бронирование")
@allure.parent_suite("Позитивные тесты")
@allure.title('Тест на удаление бронирования')
def test_booking_delete_current_booking_by_id():
    with allure.step('Подготовка данных'):
        with allure.step("Отправляем запрос на получение доступа"):
            response = AuthApi.create_auth_token(username='admin', password='password123')
            token_auth = response.get('token')

        with allure.step("Отправляем запрос на создание бронирования"):
            response = BookingApi.post_create_booking(**credentials_for_booking)
            response_bookingid = response.get('bookingid')

    with allure.step("Отправляем запрос на удаление бронирования"):
        response_code = BookingApi.delete_booking(booking_id=response_bookingid, token_auth=token_auth)

    with allure.step('ОР:'):
        with allure.step('Бронь удалена'):
            assert response_code == 201, 'Бронь не удалена'



@allure.feature("API")
@allure.story("API 'restful-booker'")
@allure.epic("Бронирование")
@allure.suite("Бронирование")
@allure.parent_suite("Негативные тесты")
@allure.title('Тест на удаление бронирования без токена авторизациии')
def test_booking_delete_current_booking_by_id():
    with allure.step('Подготовка данных'):
        with allure.step("Отправляем запрос на создание бронирования"):
            response = BookingApi.post_create_booking(**credentials_for_booking)
            response_bookingid = response.get('bookingid')

    with allure.step("Отправляем запрос на удаление бронирования"):
        response_code = BookingApi.delete_booking(booking_id=response_bookingid)

    with allure.step('ОР:'):
        with allure.step('Бронь удалена'):
            assert response_code == 403, 'Не удалось совершить действие'