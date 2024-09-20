# Son las diferentes formas de aceptar o devolver los datos
from pydantic import BaseModel
from datetime import date
from typing import Optional

class CreateTask(BaseModel):
    titulo : str
    descripcion : str
    user_id : int
    
class TaskDTO(BaseModel):
    id: int
    titulo : str
    descripcion : str
    fecha : date
    user_id : int
    
class UpdateTaskDTO(BaseModel):
    id: int
    titulo : Optional[str] = None # Ejemplo de Valor Opcional
    descripcion : str
    
class DeleteTaskDTO(BaseModel):
    id: int
    deleted : bool