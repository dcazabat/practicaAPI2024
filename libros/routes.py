from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from libros.dto import *
from libros.service import *


libro = APIRouter()

@libro.get('/', response_model=List[LibroDTO], status_code=200, summary="Toda la libreria", tags=["Libros"])
def get_libros():
    try:
        libros_list = getLibros()
        if libros_list:
            return libros_list
        return JSONResponse(content='Libros robados', status_code=404)
    except Exception as err:
        raise HTTPException(status_code=500, detail=f'Error al recuperar Libros: {err}')


@libro.get('/{id}', response_model=LibroDTO, status_code=200, summary="Obtener un libro por id", tags=["Libros"])
def get_libro_by_id(id: int):
    try:
        libro_item = getLibro(id=id)  
        if libro_item:
            return libro_item
        return JSONResponse(content='Libro no encontrado', status_code=404)
    except Exception as err:
        raise HTTPException(status_code=500, detail=f'Error al recuperar Libro: {err}')


@libro.post('/', response_model=LibroDTO, status_code=201, summary="Crear un nuevo libro", tags=["Libros"])
def create(libropost: CreateLibro):
    try:
        libro_new = createLibro(libro=libropost)
        if libro_new:
            return libro_new  
        return JSONResponse(content='Libro no creado', status_code=404)
    except Exception as err:
        raise HTTPException(status_code=500, detail=f'Error al crear Libro: {err}')


@libro.put('/{id}', response_model=LibroDTO, status_code=200, summary="Actualizar un libro", tags=["Libros"])
def update_libro(libroUpdate1: UpdateLibro, id: int):
    try:
        libro_update = updateLibro(libroUpdate1=libroUpdate1, id=id)  
        if libro_update:
            return libro_update  
        return JSONResponse(content='Libro no actualizado', status_code=404)
    except Exception as err:
        raise HTTPException(status_code=500, detail=f'Error al actualizar el Libro: {err}')


@libro.delete('/', response_model=LibroDTO, status_code=200, summary="Eliminar un Libro", tags=["Libros"])
def delete_libro(librodelete: DeleteLibroDTO):
    try:
        libro_deleted = deleteLibro(librodelete=librodelete)
        if libro_deleted:
            return libro_deleted  
        return JSONResponse(content='Libro no eliminado', status_code=404)
    except Exception as err:
        raise HTTPException(status_code=500, detail=f'Error al eliminar el Libro: {err}')
