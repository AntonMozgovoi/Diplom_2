import allure
import requests
from Urls import Urls
from api import UserApi
from data import LoginUser, CreateUser
from helper import DataHelper
from messages import ErrorMessage


class TestCreateUser:
    @allure.title('Регистрация пользователя')
    @allure.description('Успешная регистрация пользователя')
    def test_success_create_user(self):
        registration_request = UserApi.creation_user(DataHelper.generate_registration_body())
        assert registration_request.status_code == 200

    @allure.title('Поворная регистрация пользователя')
    @allure.description('Неуспешная регистрация пользователя с одинаковой почтой')
    def test_double_create_user(self):
        create_body = CreateUser.REGISTER_USER
        requests.post(Urls.BASE_URL + Urls.REGISTRATION_USER, data=create_body)
        create_request = requests.post(Urls.BASE_URL + Urls.REGISTRATION_USER, data=create_body)
        assert create_request.status_code == 403 and create_request.json()["message"] == ErrorMessage.EXISTING_USER

    @allure.title('Регистрация пользователя без одного из полей')
    @allure.description('Неуспешная регистрация пользователя без одного из обязательных полей')
    def test_create_without_field_user(self):
        create_body = CreateUser.REGISTER_USER_WITHOUT_FIELD
        create_request = requests.post(Urls.BASE_URL + Urls.REGISTRATION_USER, data=create_body)
        assert create_request.status_code == 403 and create_request.json()["message"] == ErrorMessage.USER_WITHOUT_FIELD
