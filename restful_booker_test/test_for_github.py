import requests

BASE_URl = 'https://restful-booker.herokuapp.com/'


def create_booker(url: str, booking_data):
    response = requests.post(
        f"{url}/booking",
        json=booking_data,
        headers={
            "Content-Type": "application/json",
            'Accept': 'application/json'
    })

    return response

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

def test_for_github():
    response = create_booker(BASE_URl, data)
    assert response.status_code == 200