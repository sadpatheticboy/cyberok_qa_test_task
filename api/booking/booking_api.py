""" Эндпоинты для работы с бронированием """

from api.base_api import BaseApi


class BookingApi:

    def __init__(self, session):
        self.session = session

    @staticmethod
    def get_booking_ids(**kwargs) -> dict:
        """
        Отправляет запрос для получения списка бронирований
        Параметры (необязательные):
        - firstname: Имя
        - lastname: Фамилия
        - checkin: Дата заезда
        - checkout: Дата выезда
        :return: Словарь со списком бронирований
        """

        response = BaseApi.get(url="/booking", **kwargs)

        return response.json()

    @staticmethod
    def get_booking_by_id(booking_id: int, **kwargs) -> dict:
        """
        Отправляет запрос для получения бронирования по его ID
        :param booking_id: ID бронирования
        :return: Словарь с бронированием
        """
        response = BaseApi.get(url=f"/booking/{booking_id}", **kwargs)

        return response.json()

    @staticmethod
    def post_create_booking(firstname: str = None, lastname: str = None, totalprice: int = None,
                            depositpaid: bool = None, bookingdates: list = None,
                            additionalneeds: str = None, **kwargs) -> dict:
        """
        Отправляет запрос на создание нового бронирования
        :param firstname: Имя
        :param lastname: Фамилия
        :param totalprice: Общая стоимость бронирования
        :param depositpaid: Внесен депозит или нет
        :param bookingdates: Дата заезда и выезда
        :param additionalneeds: Любые другие потребности, которые есть у гостя
        :return: Словарь с созданной бронью
        """

        data = {"firstname": firstname,
                "lastname": lastname,
                "totalprice": totalprice,
                "depositpaid": depositpaid,
                'bookingdates': bookingdates,
                "additionalneeds": additionalneeds}

        response = BaseApi.post(url="/booking", data=data, **kwargs)

        return response.json()

    @staticmethod
    def put_update_booking(booking_id=int, firstname: str = None, lastname: str = None, totalprice: int = None,
                           depositpaid: bool = None, bookingdates: dict = None,
                           additionalneeds: str = None, **kwargs) -> dict:
        """
        Отправляет запрос на обновление бронирования
        :param booking_id: ID бронирования, которое нужно обновить
        :param firstname: Имя
        :param lastname: Фамилия
        :param totalprice: Общая стоимость бронирования
        :param depositpaid: Внесен депозит или нет
        :param bookingdates: Дата заезда и выезда
        :param additionalneeds: Любые другие потребности, которые есть у гостя
        :return: Словарь с обновленной бронью
        """

        data = {"firstname": firstname,
                "lastname": lastname,
                "totalprice": totalprice,
                "depositpaid": depositpaid,
                'bookingdates': bookingdates,
                "additionalneeds": additionalneeds}

        cookies = {"Cookie": f"token={kwargs.get('token_auth')}"}

        response = BaseApi.put(url=f"/booking/{booking_id}", data=data, cookies=cookies, **kwargs)

        return response.json()

    @staticmethod
    def patch_partial_update_booking(booking_id=int, firstname: str = None, lastname: str = None,
                                     totalprice: int = None,
                                     depositpaid: bool = None, bookingdates: dict = None,
                                     additionalneeds: str = None, **kwargs) -> dict:
        """
        Отправляет запрос на частичное обновление бронирования
        :param booking_id: ID бронирования, которое нужно обновить
        :param firstname: Имя
        :param lastname: Фамилия
        :param totalprice: Общая стоимость бронирования
        :param depositpaid: Внесен депозит или нет
        :param bookingdates: Дата заезда и выезда
        :param additionalneeds: Любые другие потребности, которые есть у гостя
        :return: Словарь с обновленной бронью
        """

        data = {}

        if firstname is not None:
            data.update({'firstname': firstname})

        if lastname is not None:
            data.update({'lastname': lastname})

        if totalprice is not None:
            data.update({'totalprice': totalprice})

        if depositpaid is not None:
            data.update({'depositpaid': depositpaid})

        if bookingdates is not None:
            data.update({'checkin': bookingdates.get('checkin')})
            data.update({'checkout': bookingdates.get('checkout')})

        if additionalneeds is not None:
            data.update({'additionalneeds': additionalneeds})

        cookies = {"Cookie": f"token={kwargs.get('token_auth')}"}

        response = BaseApi.patch(url=f"/booking/{booking_id}", data=data, cookies=cookies, **kwargs)

        return response.json()

    @staticmethod
    def delete_booking(booking_id=int, **kwargs) -> int:
        """
        Отправляет запрос на удаление бронирования
        :param booking_id: ID бронирования для удаления
        """

        cookies = {"Cookie": f"token={kwargs.get('token_auth')}"}

        response = BaseApi.delete(url=f"/booking/{booking_id}", cookies=cookies, **kwargs)

        return response.status_code
