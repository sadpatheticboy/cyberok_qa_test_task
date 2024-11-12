""" Тестовые данные для запросов """

expected_fields_booking = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates', 'additionalneeds']

credentials_for_booking = {
    'firstname': 'Timur',
    'lastname': 'Balkarov',
    'totalprice': 10000,
    'depositpaid': True,
    'bookingdates' : {
        "checkin" : "2024-01-01",
        "checkout" : "2024-11-11"
    },
    'additionalneeds': 'Breakfast'
}

credentials_for_update_booking = {
    'firstname': 'Timur',
    'lastname': 'Balkarov',
    'totalprice': 10000,
    'depositpaid': False,
    'bookingdates' : {
        "checkin" : "2024-01-01",
        "checkout" : "2024-12-12"
    },
    'additionalneeds': 'Dinner'
}


credentials_for_partial_update_booking = {
    'firstname': 'Netimur',
    'lastname': 'NeBalkarov'
}