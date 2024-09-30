from todo_repository import Todo, TodoCreate, TodoRepository

repository = TodoRepository()
created_todo: TodoCreate  = {"id": 1 ,"title": "test","completed": False}

def test_get_todos():
    assert repository.get_todos() == []

def test_create_todo():
    response = repository.create_todo(created_todo)
    assert response.model_dump() == created_todo

def test_get_todo():
    response = repository.get_todo(1)
    assert response.model_dump() == created_todo

def test_get_todo_None():
    response = repository.get_todo(2)
    assert response == None

def test_update_todo():
    response = repository.update_todo(1, TodoCreate(title="Hola"))
    assert response == Todo(id = 1, title="Hola", completed=False)

def test_update_todo_None():
    response = repository.update_todo(2, TodoCreate(title="Hola"))
    assert response == None

def test_delete_todo():
    assert repository.delete_todo(1) == True

def test_delete_todo_false():
    assert repository.delete_todo(2) == False
