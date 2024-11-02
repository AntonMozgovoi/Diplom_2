import allure
import requests
from Urls import Urls
from data import CreateOrder, LoginUser


class TestCreateOrder:
    @allure.title('Создание заказа неавторизованным рользователем')
    @allure.description('проверка успешного создания заказа неавторизованным поьзователем')
    def test_create_success_non_auth_order(self):
        create_request = requests.post(Urls.BASE_URL + Urls.CREATE_ORDER, data=CreateOrder.CREATE_ORDER)
        assert  create_request.status_code == 200

    @allure.title('Создание заказа без ингридиентов')
    @allure.description('проверка неуспешного создания заказа без игридиентов')
    def test_create_order_without_ingredients(self):
        create_request = requests.post(Urls.BASE_URL + Urls.CREATE_ORDER, data=CreateOrder.CREATE_ORDER_EMPTY)
        assert create_request.status_code == 400
    @allure.title('Создание заказа с неверным хешем')
    @allure.description('проверка неуспешного создания заказа при указании неверного хеша')
    def test_create_order_wrong_hash(self):
        create_request = requests.post(Urls.BASE_URL + Urls.CREATE_ORDER, data=CreateOrder.CREATE_ORDER_WRONG_HASH)
        assert create_request.status_code == 500
    @allure.title('Создание заказа авторизованным пользователем')
    @allure.description('проверка успешного создания заказа авторизованным пользователем ')
    def test_create_success_auth_order(self):
        req_order=requests.post(Urls.BASE_URL + Urls.LOGIN_USER, data=LoginUser.LOGIN_USER)
        token = req_order.json()['accessToken']
        create_request = requests.post(Urls.BASE_URL + Urls.CREATE_ORDER, data=CreateOrder.CREATE_ORDER, headers={'Authorization': f'{token}'})
        assert create_request.status_code == 200