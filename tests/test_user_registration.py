import allure
import pytest
import requests
import test_data as TD
from helpers import user_data


class TestUserRegistration:
    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, registration_user):
        payload = user_data()
        response = registration_user(payload)
        assert response.status_code == 200
        assert "accessToken" in response.json()

    @allure.title("Создание уже существующего пользователя")
    def test_create_existing_user(self, registration_user):
        payload = user_data()
        response = registration_user(payload)
        assert response.status_code == 200
        response = registration_user(payload)
        assert response.status_code == 403
        assert "User already exists" in response.json()["message"]

    @allure.title("Создание пользователя без обязательного поля")
    def test_create_user_missing_field(self, registration_user):
        payload = user_data()
        payload.pop("name")  # Удаляем обязательное поле
        response = registration_user(payload)
        assert response.status_code == 403
        assert "Email, password and name are required fields" in response.json()["message"] 