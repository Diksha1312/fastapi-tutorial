from ..models import Todos
from .utils import *
from fastapi import status
from ..routers.todos import get_db, get_current_user

app.dependency_overrides[get_db] = override_get_db # swaps dependencies during testing
app.dependency_overrides[get_current_user] = override_get_current_user

def test_read_all_authenticated(test_todo):
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{'title':'Learn fastapi','description':'deadline approaching', 'id': 1,
                                'priority':3,'complete':False,'owner_id':1}]
    
def test_read_one_authenticated(test_todo):
    response = client.get('/todo/1')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'title':'Learn fastapi','description':'deadline approaching', 'id': 1,
                                'priority':3,'complete':False,'owner_id':1}

def test_read_one_authenticated_not_found(test_todo):
    response = client.get('/todo/99')
    assert response.status_code == 404
    assert response.json() == {'detail': 'ID not found'}

def test_create_todo(test_todo):
    request_data = {
        'title': 'New Todo!',
        'description': "Testing new todo",
        'priority': 3,
        'complete': False,
    }
    response = client.post('/todo', json=request_data)
    assert response.status_code == status.HTTP_201_CREATED
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 2).first()
    assert model.description == request_data.get('description')
    assert model.title == request_data.get('title')
    assert model.complete == request_data.get('complete')
    assert model.priority == request_data.get('priority')

def test_update_todo(test_todo):
    request_data = {
        'title': 'Changing todo to check test update todo',
        'description': "deadline approaching",
        'priority': 3,
        'complete': False,
    }
    response = client.put('/todo/1', json=request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model.title == request_data.get('title')

def test_update_todo_not_found():
    request_data = {
        'title': 'Changing todo to check test update todo',
        'description': "Testing new todo",
        'priority': 3,
        'complete': False,
    }
    response = client.put('/todo/99', json=request_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'ID not found'}

def test_delete_todo(test_todo):
    response = client.delete('/todo/1')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None

def test_delete_todo_not_found():
    response = client.delete('/todo/99')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'ID not found'}