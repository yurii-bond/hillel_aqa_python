import requests

from lecture_23.hillel_api import API

s = requests.session()

def test_signin_positive():
    # GIVEN
    user_data = {
        "email": "qweerty83588@mail.com",
        "password": "Test1234",
        "remember": False
    }

    # WHEN
    response = API.auth.signin(s=s, request_body=user_data)
    response_json = response.json()

    # THEN
    print(response_json)
    assert response.status_code == 200, "Wrong status code"
    assert response_json['status'] == "ok", "Key 'status' is not ok"

def test_get_current_user_positive():

    r = API.users.current(s)
    r_json = r.json()

    assert r.status_code == 200
    assert r_json['status'] == "ok", "Key 'status' is not ok"