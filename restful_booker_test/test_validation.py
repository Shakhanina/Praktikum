import json
from jsonschema import validate
from ..rest.main import *
import pytest

BASE_URl = 'https://restful-booker.herokuapp.com/'
file = open('rest/Schema.json', 'r')
booking_schema = json.loads(file.read())

data = {
    'create_booking': {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-10-01",
            "checkout": "2023-10-10"
        },
        "additionalneeds": "Breakfast"
    },
    "auth": {
        'username': 'admin',
        'password': 'password123'
    }
}

@pytest.mark.parametrize("data", [data])
def test_valid_create(data):
    auth_data, create_data = data['auth'], data['create_booking']
    auth_response = auth(BASE_URl, auth_data)
    assert auth_response.status_code == 200
    token = auth_response.json()['token']

    create_response = create_booker(BASE_URl, create_data)
    assert create_response.status_code == 200
    validate(instance=create_response.json(), schema=booking_schema)
    bookingid = create_response.json()['bookingid']

    delete_response = delete_booker(BASE_URl, bookingid, token)
    assert delete_response.status_code == 201

file.close()