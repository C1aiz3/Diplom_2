import allure
import pytest
import requests

from data import NOT_AUTORISED
from helpers import user_data, random_name, random_password, random_email
import test_data as TD


class TestUserUpdate:
    @allure.title("Обновление имени пользователя с авторизацией")
    def test_update_user_name_with_auth(self, registration_user):
        payload = user_data()
        registration_user(payload)
        headers = {
            'Authorization': f'Bearer {TD.tokens["accessToken"]}'
        }

        new_name = random_name()
        response = requests.patch(TD.urls["edit"], json={"name": new_name}, headers=headers)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == new_name

    @allure.title("Обновление email пользователя с авторизацией")
    def test_update_user_email_with_auth(self, registration_user):
        payload = user_data()
        registration_user(payload)
        headers = {
            'Authorization': f'Bearer {TD.tokens["accessToken"]}'
        }

        new_email = random_email()
        response = requests.patch(TD.urls["edit"], json={"email": new_email}, headers=headers)
        assert response.status_code == 200
        assert response.json()["user"]["email"] == new_email

    @allure.title("Обновление пароля пользователя с авторизацией")
    def test_update_user_password_with_auth(self, registration_user):
        payload = user_data()
        registration_user(payload)
        headers = {
            'Authorization': f'Bearer {TD.tokens["accessToken"]}'
        }

        new_password = random_password()
        response = requests.patch(TD.urls["edit"], json={"password": new_password}, headers=headers)
        assert response.status_code == 200

    @allure.title("Обновление данных пользователя без авторизации")
    def test_update_user_without_auth(self):
        update_data = {"name": "New Name"}
        response = requests.patch(TD.urls["edit"], json=update_data, headers=TD.DEFAULT_HEADERS)
        assert response.status_code == 401
        assert NOT_AUTORISED in response.json()["message"]