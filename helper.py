import allure
import requests
from faker import Faker

from urls import Urls
from data import CreateUser, UpdateUser


class DataHelper:
    @staticmethod
    def modify_registration_body_request(key, value):
        body = CreateUser.REGISTER_USER.copy()
        body[key] = value
        return body


    @staticmethod
    def generate_registration_body():
        fake = Faker()
        return DataHelper.modify_registration_body_request('email', fake.email())

