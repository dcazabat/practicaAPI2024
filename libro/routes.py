from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from libro.dto import *
from libro.service import *

libro = APIRouter()


@libro.get('/', response_model=List[LibroDTO], status_code=200, summary="Obtener todos los libros", description="Devuelve una lista de todos los libros.", tags=["Libros"])
def libros():
    try:
        libros = getLibros()
        if libros:
            return libros
        return JSONResponse(content='Libros no encontrados', status_code=404)
    except Exception as ex:
        raise HTTPException(detail=f'Ups, hubo un error al recuperar Libros: {ex}', status_code=500)


@libro.get('/{id}', response_model=LibroDTO, status_code=200, summary="Obtenemos un libro por ID", description="Devuelve un libro basado en su ID.", tags=["Libro"])
def get_libro(id: int):
    try:
        libro = getLibro(id=id)
        if libro:
            return libro
        return JSONResponse(content='Libro no encontrado', status_code=404)
    except Exception as ex:
        raise HTTPException(detail=f'Ups, hubo un error al recuperar Libro: {ex}', status_code=500)


@libro.post('/', response_model=LibroDTO, status_code=201, summary="Crear un nuevo libro", description="Crea un nuevo libro con datos proporcionados", tags=["Libros"], responses={201: {"description": "¡Bravo, libro creado con éxito!"}, 404: {"description": "Ups, libro no encontrado"}, 500: {"description": "Error interno del servidor"}})
def create(libropost: CreateLibro):
    try:
        libro_new = createLibro(libro=libropost)
        if libro_new:
            return libro_new
        return JSONResponse(content='Libro no creado', status_code=404)
    except Exception as ex:
        raise HTTPException(detail=f'Error al crear libro: {ex}', status_code=500)


@libro.put('/{id}', response_model=LibroDTO, status_code=200, summary="Actualizar un libro", description="Actualiza la información de un libro existente en el sistema.", tags=["Libros"])
def update(libroupdate: UpdateLibroDTO, id: int):
    try:
        libro_update = updateLibro(libroupdate=libroupdate, id=id)
        if libro_update:
            return libro_update
        return JSONResponse(content='Libro no actualizado', status_code=404)
    except Exception as ex:
        raise HTTPException(detail=f'Error al actualizar el Libro: {ex}', status_code=500)


@libro.delete('/', response_model=LibroDTO, status_code=200, summary="Eliminar un libro", description="Elimina un libro.", tags=["Libro"])
def delete(librodelete: DeleteLibroDTO):
    try:
        libro_delete = deleteLibro(librodelete=librodelete)
        if libro_delete:
            return libro_delete
        return JSONResponse(content='Libro no eliminado', status_code=404)
    except Exception as ex:
        raise HTTPException(detail=f'Error al eliminar el Libro: {ex}', status_code=500)