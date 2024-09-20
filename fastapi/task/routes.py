# Rutas de pedido en el Navegador, tambien se conoce como CONTROLADOR
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from task.dto import *
from task.service import *
from user.service import getUser

task = APIRouter()

# Metodo o Controlador
@task.get('/', response_model=List[TaskDTO], status_code=200)
def tasks():
    try:
        tasks = getTasks()
        if tasks:
            return tasks
        return JSONResponse(content=f'Tareas no econtrados', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al recuperar Tareas: {e}', status_code=500)

@task.get('/{id}', response_model=TaskDTO, status_code=200)
def get_task(id: int):
    try:
        task = getTask(id=id)
        if task:
            return task
        return JSONResponse(content=f'Tarea no econtrado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al recuperar Tarea: {e}', status_code=500)

@task.post('/', response_model=TaskDTO, status_code=200)
def create(taskpost: CreateTask):
    try:
        # Verificamos si existe el Usuario
        user = getUser(id=taskpost.user_id)
        if user:
            task_new = createTask(task=taskpost)
            if task_new:
                return task_new
            return JSONResponse(content=f'Tarea no Creada', status_code=404)
        return JSONResponse(content=f'Usuario no Existe', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al Crear Tarea: {e}', status_code=500)

@task.put('/', response_model=TaskDTO, status_code=200)
def update(taskupdate: UpdateTaskDTO):
    try:
        task_update = updateTask(taskupdate=taskupdate)
        if task_update:
            return task_update
        return JSONResponse(content=f'Tarea no actualizado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al actualizar el Tarea: {e}', status_code=500)

@task.delete('/', response_model=TaskDTO, status_code=200)
def delete(taskdelete: DeleteTaskDTO):
    try:
        task_delete = deleteTask(taskdelete=taskdelete) 
        if task_delete:
            return task_delete
        return JSONResponse(content=f'Tarea no Eliminado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al eliminar el Tarea: {e}', status_code=500)

