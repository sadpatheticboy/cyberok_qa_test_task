""" Фикстуры для работы с API """

import pytest

from api.auth.auth_api import AuthApi
from api.ping.ping_api import PingApi
from api.booking.booking_api import BookingApi


@pytest.fixture(scope='module')
def auth_api(account_api_session):
    yield AuthApi(session=account_api_session)


@pytest.fixture(scope='module')
def booking_api(account_api_session):
    yield BookingApi(session=account_api_session)


@pytest.fixture(scope='module')
def ping_api(account_api_session):
    yield PingApi(session=account_api_session)
