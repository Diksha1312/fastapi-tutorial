
from .utils import *
from ..routers.users import get_current_user, get_db
from fastapi import status


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get('/users')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'testClient'
    assert response.json()['first_name'] == 'test'
    assert response.json()['last_name'] == 'Client'
    assert response.json()['email'] == 'testClient@test.com'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '(123)-456-789'

def test_change_password_success(test_user):
    response = client.put('/users/password', json={"password": "test123", "new_password": "newtest123"})
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put('/users/password', json={"password": "test1234", "new_password": "newtest123"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}

def test_phone_number_success(test_user):
    response = client.put('/users/phone-number', json={'update_phone_number': '22222222'})
    assert response.status_code == status.HTTP_204_NO_CONTENT
