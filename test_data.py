
BASE_URL = "https://stellarburgers.nomoreparties.site"
API_URL = f"{BASE_URL}/api"

urls = {
    "registration": f"{API_URL}/auth/register",
    "login": f"{API_URL}/auth/login",
    'edit': f"{API_URL}/auth/user",
    "user": f"{API_URL}/auth/user",
    "delete": f"{API_URL}/auth/user",
    "orders": f"{API_URL}/orders"
}

# Заголовки по умолчанию
DEFAULT_HEADERS = {
    "Content-Type": "application/json"
}

# Словарь для хранения токенов
tokens = {
    "accessToken": '',
    "refreshToken": ''
}

test_ingredients = {
    "ingredients": ["61c0c5a71d1f82001bdaaa75", "61c0c5a71d1f82001bdaaa6c"]
}

no_ingredients = {
    "ingredients": []
}

invalid_ingredient = {
    "ingredients": ["test_fake"]
}


# Неверные данные пользователя
wrong_data = {
            "email": "test@example.com",
            "password": "wrong_password"
        }