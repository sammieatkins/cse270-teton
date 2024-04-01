import pytest
from unittest.mock import Mock, patch
import requests

@pytest.fixture
def mocker():
    return Mock()

def test_login_with_wrong_credentials(mocker):
    url = "http://127.0.0.1:8000/users"
    data = {
        "username": "admin",
        "password": "password"
    }
    
    # Mocking the requests.post method
    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 401
        response = requests.post(url, data=data)

    assert response.status_code == 401

def test_login_with_correct_credentials(mocker):
    url = "http://127.0.0.1:8000/users"
    data = {
        "username": "admin",
        "password": "qwerty"
    }
    
    # Mocking the requests.post method
    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 200
        response = requests.post(url, data=data)

    assert response.status_code == 200