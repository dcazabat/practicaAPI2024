from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from user.dto import *
from user.service import *

user = APIRouter()

# Ruta para obtener todos los usuarios
@user.get('/', response_model=List[UserDTO], status_code=200, summary="Obtener todos los usuarios", description="Devuelve una lista de todos los usuarios registrados.", tags=["Usuarios"])
def users():
    try:
        users = getUsers()
        if users:
            return users
        return JSONResponse(content='Usuarios no encontrados', status_code=404)
    except Exception as e:
        raise HTTPException(detail=f'Error al recuperar Usuarios: {e}', status_code=500)

# Ruta para obtener un usuario por ID
@user.get('/{id}', response_model=UserDTO, status_code=200, summary="Obtener usuario por ID", description="Devuelve un usuario específico basado en su ID.", tags=["Usuarios"])
def get_user(id: int):
    try:
        user = getUser(id=id)
        if user:
            return user
        return JSONResponse(content='Usuario no encontrado', status_code=404)
    except Exception as e:
        raise HTTPException(detail=f'Error al recuperar Usuario: {e}', status_code=500)

# Ruta para crear un nuevo usuario
@user.post('/', response_model=UserDTO, status_code=201, summary="Crear un nuevo usuario", description="Crea un nuevo usuario en el sistema con los datos proporcionados.", tags=["Usuarios"], responses={201: {"description": "Usuario creado con éxito"}, 404: {"description": "Usuario no creado"}, 500: {"description": "Error interno del servidor"}})
def create(userpost: CreateUser):
    try:
        user_new = createUser(user=userpost)
        if user_new:
            return user_new
        return JSONResponse(content='Usuario no creado', status_code=404)
    except Exception as e:
        raise HTTPException(detail=f'Error al crear Usuario: {e}', status_code=500)

# Ruta para actualizar un usuario
@user.put('/{id}', response_model=UserDTO, status_code=200, summary="Actualizar un usuario", description="Actualiza la información de un usuario existente en el sistema.", tags=["Usuarios"])
def update(userupdate: UpdateUserDTO, id: int):
    try:
        user_update = updateUser(userupdate=userupdate, id=id)
        if user_update:
            return user_update
        return JSONResponse(content='Usuario no actualizado', status_code=404)
    except Exception as e:
        raise HTTPException(detail=f'Error al actualizar el Usuario: {e}', status_code=500)

# Ruta para eliminar un usuario
@user.delete('/', response_model=UserDTO, status_code=200, summary="Eliminar un usuario", description="Elimina un usuario existente del sistema.", tags=["Usuarios"])
def delete(userdelete: DeleteUserDTO):
    try:
        user_delete = deleteUser(userdelete=userdelete)
        if user_delete:
            return user_delete
        return JSONResponse(content='Usuario no eliminado', status_code=404)
    except Exception as e:
        raise HTTPException(detail=f'Error al eliminar el Usuario: {e}', status_code=500)
