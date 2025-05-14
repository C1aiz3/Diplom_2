import allure
import pytest
import requests
import test_data as TD
from helpers import user_data



class TestGetUserOrders:
    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_with_auth(self, registration_user):
        payload = user_data()
        registration_user(payload)
        headers = {
            'Authorization': f'Bearer {TD.tokens["accessToken"]}'
        }

        response = requests.get(TD.urls["orders"], headers=headers)
        assert response.status_code == 200
        assert "orders" in response.json()

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_orders_without_auth(self):
        response = requests.get(TD.urls["orders"], headers=TD.DEFAULT_HEADERS)
        assert response.status_code == 401
        assert "You should be authorised" in response.json()["message"] 