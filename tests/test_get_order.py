import allure
import requests
from urls import Urls
from data import LoginUser
from messages import ErrorMessage


class TestGetOder:
    @allure.title('Получение заказов без авторизации')
    @allure.description('Неуспешное получение заказов без авторизации')
    def test_order_non_auth(self):
        order = requests.get(Urls.BASE_URL + Urls.GET_ALL_ORDERS)
        assert order.status_code == 401 and order.json()["message"] == ErrorMessage.UPDATE_USER

    @allure.title('Получение заказов с авторизацией')
    @allure.description('Успешное получение заказов с авторизацией')
    def test_order_auth_user(self):
        req = requests.post(Urls.BASE_URL + Urls.LOGIN_USER, data=LoginUser.LOGIN_USER)
        token = req.json()['accessToken']
        order = requests.get(Urls.BASE_URL + Urls.GET_ALL_ORDERS, headers={'Authorization': f'{token}'})
        assert order.status_code == 200 and order.json()["success"] == True


