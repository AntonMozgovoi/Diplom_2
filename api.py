import requests
from Urls import Urls
from data import LoginUser, UpdateUser, DeleteUser
from helper import DataHelper


class UserApi:
    @staticmethod
    def creation_user(body):
        req_body = requests.post(Urls.BASE_URL + Urls.REGISTRATION_USER, json=body)
        return req_body

    @staticmethod
    def login_user():
        req = requests.post(Urls.BASE_URL + Urls.LOGIN_USER, data=LoginUser.LOGIN_USER)
        return req


