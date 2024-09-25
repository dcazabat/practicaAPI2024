# Rutas de pedido en el Navegador, tambien se conoce como CONTROLADOR
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from libros.dto import *
from libros.service import *

libroos = APIRouter()

@libroos.post('/', response_model=LibroDTO, status_code=200)
def create(libropost: CreateLibro):
    try:
        libro_new = createLibro(libro=libropost)
        if libro_new:
            return libro_new
        return JSONResponse(content=f'Libro no Creado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al Crear Libro: {e}', status_code=500)
    
@libroos.get('/', response_model=List[LibroDTO], status_code=200)
def libros():
    try:
        libros = getLibros()
        if libros:
            return libros
        return JSONResponse(content=f'Libros no econtrados', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al recuperar Libros: {e}', status_code=500)

@libroos.get('/{id}', response_model=LibroDTO, status_code=200)
def get_libro(id: int):
    try:
        libro = getLibro(id=id)
        if libro:
            return libro
        return JSONResponse(content=f'Libro no econtrado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al recuperar Libro: {e}', status_code=500)

@libroos.put('/', response_model=LibroDTO, status_code=200)
def update(libroupdate: UpdateLibroDTO):
    try:
        libro_update = updateLibro(libroupdate=libroupdate)
        if libro_update:
            return libro_update
        return JSONResponse(content=f'Libro no actualizado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al actualizar el Libro: {e}', status_code=500)

@libroos.delete('/', response_model=LibroDTO, status_code=200)
def delete(librodelete: DeleteLibroDTO):
    try:
        libro_delete = deleteLibro(librodelete=librodelete) 
        if libro_delete:
            return libro_delete
        return JSONResponse(content=f'Libro no Eliminado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al eliminar el Libro: {e}', status_code=500)