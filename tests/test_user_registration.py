import allure
import pytest
import requests
import test_data as TD
from helpers import user_data


class TestUserRegistration:
    def test_create_unique_user(self, registration_user):
        """Тест создания уникального пользователя"""
        payload = user_data()
        response = registration_user(payload)
        assert response.status_code == 200
        assert "accessToken" in response.json()

    def test_create_existing_user(self, registration_user):
        """Тест создания уже существующего пользователя"""
        payload = user_data()
        response = registration_user(payload)
        assert response.status_code == 200
        response = registration_user(payload)
        assert response.status_code == 403
        assert "User already exists" in response.json()["message"]

    def test_create_user_missing_field(self, registration_user):
        """Тест создания пользователя без обязательного поля"""
        payload = user_data()
        payload.pop("name")  # Удаляем обязательное поле
        response = registration_user(payload)
        assert response.status_code == 403
        assert "Email, password and name are required fields" in response.json()["message"] 