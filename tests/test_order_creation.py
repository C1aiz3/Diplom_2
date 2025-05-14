import allure
import pytest
import requests
import test_data as TD
from helpers import user_data


class TestOrderCreation:
    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, registration_user):
        payload = user_data()
        registration_user(payload)
        headers = {
            'Authorization': f'Bearer {TD.tokens["accessToken"]}'
        }

        response = requests.post(TD.urls["orders"], json=TD.test_ingredients, headers=headers)
        assert response.status_code == 200
        assert "order" in response.json()

    @allure.title("Создание заказа неавторизованным пользователем")
    def test_create_order_without_auth(self):
        response = requests.post(TD.urls["orders"], json=TD.test_ingredients)
        assert response.status_code == 401 #здесь возвращает 200 как ни крути
        assert "You should be authorised" in response.json()["message"]

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, registration_user):
        payload = user_data()
        registration_user(payload)
        headers = {
            'Authorization': f'Bearer {TD.tokens["accessToken"]}'
        }

        response = requests.post(TD.urls["orders"], json=TD.no_ingredients, headers=headers)
        assert response.status_code == 400
        assert "Ingredient ids must be provided" in response.json()["message"]

    @allure.title("Создание заказа с неверным ингредиентом")
    def test_create_order_with_invalid_ingredient(self, registration_user):
        response = requests.post(TD.urls['orders'], json=TD.invalid_ingredient)
        assert response.status_code == 500