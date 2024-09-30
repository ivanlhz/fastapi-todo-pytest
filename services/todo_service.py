from repositories.todo_repository import TodoRepository, TodoCreate, Todo

# Los servicios se encargan de la logica de negocio, es decir funcionalidades y operaciones requeridas por la aplicacion
# en este caso no es mas que un intermediario ya que no tenemos logica propia de negocio
# aqui podriamos parsear los datos que vienen directamente de la DB a otro formato de datos que espera el front, formatear una fecha...
class TodoService():
    def __init__(self):
        self.todo_repository = TodoRepository()

    def create_todo(self, todo: TodoCreate)-> Todo:
        return self.todo_repository.create_todo(todo)
    
    def get_todos(self) -> list[Todo]:
        return self.todo_repository.get_todos()
    
    def get_todo(self, todo_id: int) -> Todo | None:
        return self.todo_repository.get_todo(todo_id)
    
    def update_todo(self, todo_id: int, todo: TodoCreate) -> Todo | None:
        return self.todo_repository.update_todo(todo_id, todo)
    
    def delete_todo(self, todo_id) -> bool:
        return self.todo_repository.delete_todo(todo_id)