import allure
import pytest
import requests
import test_data as TD
from helpers import user_data


class TestUserLogin:
    def test_login_existing_user(self, registration_user):
        """Тест входа существующего пользователя"""
        user = user_data()
        response = registration_user(user)
        assert response.status_code == 200
        login_data = {
            "email": user["email"],
            "password": user["password"]
        }
        response = requests.post(TD.urls["login"], json=login_data, headers=TD.DEFAULT_HEADERS)
        assert response.status_code == 200
        assert "accessToken" in response.json()

    def test_login_wrong_credentials(self):
        """Тест входа с неверными учетными данными"""
        response = requests.post(TD.urls["login"], json=TD.wrong_data, headers=TD.DEFAULT_HEADERS)
        assert response.status_code == 401
        assert "email or password are incorrect" in response.json()["message"] 