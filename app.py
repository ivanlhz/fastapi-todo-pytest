from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TodoCreate(BaseModel):
    title: str

class Todo(TodoCreate):
    id: int
    completed: bool = False

# To store our DB in memory (simulate a db)
todos = []

# create a new post
@app.post('/todos', response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo = (Todo(id = len(todos) + 1, **todo.model_dump()))
    todos.append(new_todo)
    return new_todo

# Fetch all todos
@app.get('/todos', response_model=list[Todo])
def get_todos():
    return todos

# Fetch a todo data
@app.get('/todos/{todo_id}', response_model=Todo)
def get_todo(todo_id: int):    
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# update the todo
@app.patch('/todos/{todo_id}')
def update_todo(todo_id: int, updated_todo: TodoCreate):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index].title = updated_todo.title
            return {"message", "Todo updated rightly!"}
    raise HTTPException(status_code=404, detail="Todo not found")

# Delete a todo from todos
@app.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    for index,todo in enumerate(todos):
        if (todo.id == todo_id):
            del todos[index]
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", port=8000, host='0.0.0.0', reload=True)