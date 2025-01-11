import requests

def delete_booker(url: str, booking_id: int, token: str):
    delete_response = requests.delete(
        f"{url}/booking/{booking_id}",
        headers={
            'Cookie': 'token='+token
        }
    )
    return delete_response


def create_booker(url: str, booking_data):
    response = requests.post(
        f"{url}/booking",
        json=booking_data,
        headers={
            "Content-Type": "application/json",
            'Accept': 'application/json'
    })

    return response


def auth(url: str, data):
    auth_response = requests.post(
        f'{url}/auth',
        json=data,
        headers={
            "Content-Type": "application/json"
        }
    )
    return auth_response