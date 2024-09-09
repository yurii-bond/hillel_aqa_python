from lecture_23.hillel_api import API
import requests

s = requests.session()


def test_sigin_delete_and_cant_resign():
    """E2E test example"""
    # Створення даних користувача для тестування
    user_data = {
        "email": "qweerty31574@mail.com",
        "password": "Test1234",
        "remember": False
    }

    # Автентифікація користувача
    r = API.auth.signin(s, user_data)
    r_json = r.json()

    # Перевірка успішності автентифікації
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"

    # Видалення користувача
    r = API.users.users(s)
    r_json = r.json()

    # Перевірка успішності видалення користувача
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"

    # Спроба повторного входу після видалення користувача (має бути помилка)
    r = API.auth.signin(s, user_data)
    r_json = r.json()

    # Перевірка невдалої спроби входу після видалення користувача
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'error' expected"