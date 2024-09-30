from fastapi.testclient import TestClient
from pytest import fixture

from app import app

client = TestClient(app)

@fixture(autouse=True)
def clear_todos():
    # Limpiar todos los "todos" antes de cada prueba
    response = client.get('/api/todos')
    todos = response.json()
    for todo in todos:
        client.delete(f'/api/todos/{todo["id"]}')

@fixture
def setup_todo():
    response = client.post('/api/todos', json={"title": "Comprar leche"})
    todo = response.json()
    expected_todo = {"id": todo["id"], "title": todo["title"], "completed": todo["completed"]}
    return expected_todo

def test_read_todos():
    response = client.get('/api/todos')
    assert response.status_code == 200
    assert response.json() == []

def test_create_todo():
    expected_todo = {"id": 1, "title": "Comprar leche", "completed": False}
    response = client.post('/api/todos', json={"title": expected_todo["title"]})
    assert response.status_code == 200
    assert response.json() == expected_todo
    get_response = client.get('/api/todos')
    assert get_response.status_code == 200
    assert get_response.json() == [expected_todo]

def test_read_todo(setup_todo):
    response = client.get('/api/todos/1')
    assert response.status_code == 200
    assert response.json() == setup_todo

def test_update_todo(setup_todo):
    response = client.patch('/api/todos/1', json={"title": setup_todo["title"]})
    assert response.status_code == 200
    assert response.json() == setup_todo

def test_delete_todo(setup_todo):   
    get_response = client.get('/api/todos')
    assert get_response.status_code == 200
    assert get_response.json() == [setup_todo]
    
    response = client.delete('/api/todos/' + str(setup_todo["id"]))
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted successfully ✔️"}
