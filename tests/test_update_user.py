import allure
import requests
from data import UpdateUser
from Urls import Urls


class TestUpdateUser:
    @allure.title('Обновление пароля')
    @allure.description('Проверка обновления пароля неавторизованного пользователя')
    def test_update_non_auth_user_pass(self, update_user_not_auth):
        update_request = requests.patch(Urls.BASE_URL + Urls.UPDATE_USER, data=UpdateUser.UPDATE_USER_PASS)
        assert update_request.status_code == 401

    @allure.title('Обновление e-mail')
    @allure.description('Проверка обновления email авторизованного пользователя')
    def test_update_non_auth_user_email(self, update_user_not_auth):
        update_request = requests.patch(Urls.BASE_URL + Urls.UPDATE_USER, data=UpdateUser.UPDATE_USER)
        assert update_request.status_code == 401

    @allure.title('Обновление пароля')
    @allure.description('Проверка обновления пароля авторизованного пользователя')
    def test_success_update_password(self, update_user_password):       # Проверка успешного обновления password авторизованного пользователя
        update_request = requests.patch(Urls.BASE_URL + Urls.UPDATE_USER, data=UpdateUser.UPDATE_USER_PASS,
                                        headers={'Authorization': f'{update_user_password}'})
        assert update_request.status_code == 200

    @allure.title('Обновление e-mail')
    @allure.description('Проверка обновления email авторизованного пользователя')
    def test_success_update_email(self, update_user_email):
        update_request = requests.patch(Urls.BASE_URL + Urls.UPDATE_USER, data=UpdateUser.UPDATE_USER,
                                        headers={'Authorization': f'{update_user_email}'})
        assert update_request.status_code == 200
