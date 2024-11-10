import allure
import requests
from urls import Urls
from data import LoginUser



class UserApi:

    @staticmethod
    @allure.step('Создание тела запроса на регистрацию пользователя')
    def creation_user(body):
        req_body = requests.post(Urls.BASE_URL + Urls.REGISTRATION_USER, json=body)
        return req_body


