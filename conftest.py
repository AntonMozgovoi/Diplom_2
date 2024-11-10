import allure
import pytest
import requests
from urls import Urls
from data import DeleteUser, UpdateUser
from helper import DataHelper
from tests.test_update_user import TestUpdateUser


@pytest.fixture
def create_user():
    requests.post(Urls.BASE_URL + Urls.REGISTRATION_USER, data=UpdateUser.CREATE_FOR_UPDATE)
    req_log = requests.post(Urls.BASE_URL + Urls.LOGIN_USER, data=UpdateUser.LOGIN_FOR_UPDATE)
    token = req_log.json()['accessToken']
    yield token
    requests.delete(Urls.BASE_URL + Urls.DELETE_USER, json=DeleteUser.DELETE_USER,
                    headers={'Authorization': f'{token}'})


@pytest.fixture
def create_user_not_auth():
    req_upd = requests.post(Urls.BASE_URL + Urls.REGISTRATION_USER, data=UpdateUser.CREATE_FOR_UPDATE)
    token = req_upd.json()['accessToken']
    yield token
    requests.delete(Urls.BASE_URL + Urls.DELETE_USER, json=UpdateUser.CREATE_FOR_UPDATE,
                    headers={'Authorization': f'{token}'})