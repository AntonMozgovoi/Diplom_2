class CreateUser:
    REGISTER_USER = {
    "email": "antosha123@yandex.ru",
    "password": "123456",
    "name": "Username"
    }

    REGISTER_USER_WITHOUT_FIELD = {
    "email": "",
    "password": "123456",
    "name": "Username"
    }

class LoginUser:
    LOGIN_USER = {
    "email": "user_for_test@yandex.ru",
    "password": "123456"
    }

    LOGIN_WRONG_USER = {
        "email": "xxxx@xx.xx",
        "password": "123456"
    }
class UpdateUser:
    CREATE_FOR_UPDATE = {
        "email": "first_email_user@yandex.ru",
        "password": "123456",
        "name": "Username"
    }
    LOGIN_FOR_UPDATE = {
        "email": "first_email_user@yandex.ru",
        "password": "123456",
    }

    UPDATE_USER = {
        "email": "updating_user@yandex.ru",
        "password": "123456"
    }

    UPDATE_USER_PASS = {
        "email": "first_email_user@yandex.ru",
        "password": "updating_pass"
    }
class DeleteUser:
    DELETE_USER = {
        "email": "updating_user@yandex.ru",
        "password": "123456",
    }

    DELETE_USER_PASS = {
        "email": "first_email_user@yandex.ru",
        "password": "updating_pass",
    }

class CreateOrder:
    CREATE_ORDER = {
    "ingredients": ["61c0c5a71d1f82001bdaaa76", "61c0c5a71d1f82001bdaaa6e"]
    }

    CREATE_ORDER_EMPTY = {
        "ingredients": []
    }

    CREATE_ORDER_WRONG_HASH = {
        "ingredients": ["xxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxx"]
    }