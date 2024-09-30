from fastapi import APIRouter

router = APIRouter(prefix='api')

@router.post('/todos')
def create_todo():
    pass

@router.get('/todos')
def get_todos():
    pass

@router.get('/todo/{todo_id}')
def get_todo(todo_id: int):
    pass

@router.path('/todos/{todo_id}')
def update_todos(todo_id: int):
    pass

@router.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    pass