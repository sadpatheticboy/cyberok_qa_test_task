""" Класс для базовых проверок """


class BaseChecks:

    @classmethod
    def check_field_exist(cls, response: dict | list, field: str) -> None:
        """
        Проверяет ответ на содержание заданного поля
        :param response: Ответ на запрос.
        :param field: Проверяемое поле
        """

        if isinstance(response, list):
            for item in response:
                assert item.get(field, None) is not None, f'В ответе нет поля {field!r}'

        else:
            assert response.get(field, None) is not None, f'В ответе нет поля {field!r}'

    @classmethod
    def check_fields_exist(cls, response: dict, fields: list[str]) -> None:
        """
        Проверяет ответ на наличие заданных полей
        :param response:  Ответ на запрос.
        :param fields: Проверяемые поля
        :return:
        """

        for field in fields:
            assert response.get(field, None) is not None, f'В ответе нет поля {field!r}'



    @classmethod
    def check_error(cls, response: dict, error: str) -> None:
        """
        Проверяет ответ на содержание определенной ошибки.
        :param response: Ответ на запрос.
        :param error: Текст ошибки.
        """
        assert response.get('reason', None) is not None, 'В ответе нет текста ошибки'
        assert response.get('reason').__eq__(error), ('Неправильный текст ошибки, имеется: '
                                                      f'{response.get("reason")} - требуется: {error}')
