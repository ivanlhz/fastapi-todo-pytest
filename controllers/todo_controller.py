from fastapi import HTTPException
from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str

class Todo(TodoCreate):
    id: int
    completed: bool = False


class TodoController():
    def __init__(self):
        self.todos = []

    def create_todo(self, todo: TodoCreate):
        new_todo = (Todo(id = len(self.todos) + 1, **todo.model_dump()))
        self.todos.append(new_todo)
        return new_todo

    def get_todos(self):
        return self.todos

    def get_todo(self, todo_id: int):    
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        raise HTTPException(status_code=404, detail="Todo not found")


    def update_todo(self, todo_id: int, updated_todo: TodoCreate):
        for todo in self.todos:
            if todo.id == todo_id:
                todo.title = updated_todo.title
                return todo
        raise HTTPException(status_code=404, detail="Todo not found")

    def delete_todo(self, todo_id: int):
        for index,todo in enumerate(self.todos):
            if (todo.id == todo_id):
                del self.todos[index]
                return {"message": "✔️Todo deleted successfully"}
        raise HTTPException(status_code=404, detail="Todo not found")