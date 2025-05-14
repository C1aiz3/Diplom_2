import pytest
import requests
import test_data as TD


@pytest.fixture
def registration_user(request):
    def registration(payload):
        reg_response = requests.post(TD.urls["registration"], json=payload)
        reg_response_data = reg_response.json()
        
        if reg_response.status_code == 200:
            full_access_token = reg_response_data['accessToken']
            TD.tokens['accessToken'] = full_access_token[len("Bearer "):]
            TD.tokens['refreshToken'] = reg_response_data['refreshToken']

            def delete_user():
                headers = TD.DEFAULT_HEADERS.copy()
                headers['Authorization'] = f'Bearer {TD.tokens["accessToken"]}'
                requests.delete(TD.urls["delete"], headers=headers)

            request.addfinalizer(delete_user)
        
        return reg_response

    return registration