import allure
import requests
from data import UpdateUser
from urls import Urls
from messages import ErrorMessage


class TestUpdateUser:
    @allure.title('Обновление пароля')
    @allure.description('Проверка обновления пароля неавторизованного пользователя')
    def test_update_non_auth_user_pass(self, create_user_not_auth):
        update_request = requests.patch(Urls.BASE_URL + Urls.UPDATE_USER, data=UpdateUser.UPDATE_USER_PASS)
        assert update_request.status_code == 401 and update_request.json()["message"] == ErrorMessage.UPDATE_USER

    @allure.title('Обновление e-mail')
    @allure.description('Проверка обновления email авторизованного пользователя')
    def test_update_non_auth_user_email(self, create_user_not_auth):
        update_request = requests.patch(Urls.BASE_URL + Urls.UPDATE_USER, data=UpdateUser.UPDATE_USER)
        assert update_request.status_code == 401 and update_request.json()["message"] == ErrorMessage.UPDATE_USER

    @allure.title('Обновление пароля')
    @allure.description('Проверка обновления пароля авторизованного пользователя')
    def test_success_update_password(self, create_user):       # Проверка успешного обновления password авторизованного пользователя
        update_request = requests.patch(Urls.BASE_URL + Urls.UPDATE_USER, data=UpdateUser.UPDATE_USER_PASS,
                                        headers={'Authorization': f'{create_user}'})
        assert update_request.status_code == 200 and update_request.json()["success"] == True

    @allure.title('Обновление e-mail')
    @allure.description('Проверка обновления email авторизованного пользователя')
    def test_success_update_email(self, create_user):
        update_request = requests.patch(Urls.BASE_URL + Urls.UPDATE_USER, data=UpdateUser.UPDATE_USER,
                                        headers={'Authorization': f'{create_user}'})
        assert update_request.status_code == 200 and update_request.json()["success"] == True
