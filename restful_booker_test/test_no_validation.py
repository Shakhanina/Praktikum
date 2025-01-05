import json
import pytest
from ..rest.main import *

BASE_URl = 'https://restful-booker.herokuapp.com/'

file_auth = open('restful_booker_test/not_valid_auth.json', 'r')
file_create = open('restful_booker_test/not_valid_create.json', 'r')

auth_data = json.load(file_auth)
create_data = json.load(file_create)

file_auth.close()
file_create.close()

@pytest.mark.parametrize("data", auth_data)
def test_not_valid_auth(data):
    auth_response = auth(BASE_URl, data)
    assert auth_response != 200


@pytest.mark.parametrize("data", create_data)
def test_not_valid_create(data):
    create_response = create_booker(BASE_URl, data)
    assert create_response != 200