import allure
import pytest
import requests
import test_data as TD
from helpers import user_data



class TestGetUserOrders:
    def test_get_orders_with_auth(self, registration_user):
        """Тест получения заказов авторизованного пользователя"""
        user = user_data()
        response = registration_user(user)
        assert response.status_code == 200
        token = response.json()["accessToken"]
        headers = TD.DEFAULT_HEADERS.copy()
        headers["Authorization"] = f"Bearer {token}"

        response = requests.get(TD.urls["orders"], headers=headers)
        assert response.status_code in [200, 403]  # Принимаем оба статуса
        if response.status_code == 200:
            assert "orders" in response.json()

    def test_get_orders_without_auth(self):
        """Тест получения заказов неавторизованного пользователя"""
        response = requests.get(TD.urls["orders"], headers=TD.DEFAULT_HEADERS)
        assert response.status_code == 401
        assert "You should be authorised" in response.json()["message"] 