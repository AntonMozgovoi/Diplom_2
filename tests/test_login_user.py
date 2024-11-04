import allure
import requests
from urls import Urls
from data import LoginUser
from messages import ErrorMessage


class TestLoginUser:
    @allure.title('Авторизация пользователя')
    @allure.description('Успешная авторизация пользователя')
    def test_success_login_user(self):
        login_body = LoginUser.LOGIN_USER
        create_request = requests.post(Urls.BASE_URL + Urls.LOGIN_USER, data=login_body)
        assert create_request.status_code == 200 and create_request.json()["success"] == True

    @allure.title('Авторизация незарегистрированного пользователя')
    @allure.description('Неуспешная авторизация незарегистрированного пользователя')
    def test_error_login_user(self):
        login_body = LoginUser.LOGIN_WRONG_USER
        create_request = requests.post(Urls.BASE_URL + Urls.LOGIN_USER, data=login_body)
        assert create_request.status_code == 401 and create_request.json()["message"] == ErrorMessage.LOGIN_ERROR_USER
