import allure
import pytest
import requests
from helpers import user_data, random_name, random_password, random_email
import test_data as TD


class TestUserUpdate:

    def test_update_user_name_with_auth(self, registration_user):
        payload = user_data()
        registration_user(payload)
        headers = {
            'Authorization': f'Bearer {TD.tokens["accessToken"]}'
        }

        # Обновляем имя
        new_name = random_name()
        response = requests.patch(TD.urls["edit"], json={"name": new_name}, headers=headers)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == new_name

    def test_update_user_email_with_auth(self, registration_user):
        payload = user_data()
        registration_user(payload)
        headers = {
            'Authorization': f'Bearer {TD.tokens["accessToken"]}'
        }

        # Обновляем email
        new_email = random_email()
        response = requests.patch(TD.urls["edit"], json={"email": new_email}, headers=headers)
        assert response.status_code == 200
        assert response.json()["user"]["email"] == new_email

    def test_update_user_password_with_auth(self, registration_user):
        payload = user_data()
        registration_user(payload)
        headers = {
            'Authorization': f'Bearer {TD.tokens["accessToken"]}'
        }

        # Обновляем пароль
        new_password = random_password()
        response = requests.patch(TD.urls["edit"], json={"password": new_password}, headers=headers)
        assert response.status_code == 200

    def test_update_user_without_auth(self):
        update_data = {"name": "New Name"}
        response = requests.patch(TD.urls["edit"], json=update_data, headers=TD.DEFAULT_HEADERS)
        assert response.status_code == 401
        assert "You should be authorised" in response.json()["message"]