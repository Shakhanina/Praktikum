import json
from jsonschema import validate
from ..rest.main import *

BASE_URl = 'https://restful-booker.herokuapp.com/'
file = open('rest/Schema.json', 'r')
booking_schema = json.loads(file.read())


def test_creat_booking():
    data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-10-01",
            "checkout": "2023-10-10"
        },
        "additionalneeds": "Breakfast"
    }

    response = create_booker(BASE_URl, data)
    assert response.status_code == 200

    validate(instance=response.json(), schema=booking_schema)

    auth_data = {
        'username': 'admin',
        'password': 'password123'
    }

    auth_response = auth(BASE_URl, auth_data)

    token = auth_response.json()['token']
    booking_id = response.json()["bookingid"]

    delete_response = delete_booker(BASE_URl, booking_id, token)

    assert delete_response.status_code == 201

file.close()