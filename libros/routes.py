from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from libros.dto import *
from libros.service import *


libro = APIRouter()



@libro.get('/',response_model=List[LibroDTO],status_code=200,summary="Toda la libreria",description="Devuelve toda la lista de los libros registrados",tags=["Libros"])
def libros():
    try:
        libros = getLibros()
        if libros:
            return libros
        return JSONResponse(content='Libros robados', status_code=404)
    except Exception as err:
        raise HTTPException(detail=f'Error al recuperar Libros: {err}', status_code=500)

@libro.get('/{id}',response_model=LibroDTO,status_code=200,summary="Obtener un libro por id",description="Devuelve un libro específico basado en su ID.",tags=["Libros"])
def getLibro(id: int):
    try:
        libro = getLibro(id=id)
        if libro:
            return libro
        return JSONResponse(content='Libro robado', status_code=404)
    except Exception as err:
        raise HTTPException(detail=f'Error al recuperar Libro: {err}', status_code=500)


@libro.post('/', response_model=LibroDTO, status_code=201, summary="Crear un nuevo libro", description="Crea un nuevo libro en el sistema con los datos proporcionados.", tags=["Libros"], responses={201: {"description": "Libro creado con éxito"}, 404: {"description": "Libro no creado"}, 500: {"description": "Error interno del servidor"}})
def create(libropost: CreateLibro):
    try:
        libroNew = createLibro(libro=libropost)
        if libroNew:
            return libroNew
        return JSONResponse(content='Libro robado', status_code=404)
    except Exception as err:
        raise HTTPException(detail=f'Error al crear Libro: {err}', status_code=500)


@libro.put('/{id}', response_model=LibroDTO, status_code=200, summary="Actualizar un libro", description="Actualiza la información de un libro libro en el sistema.", tags=["Libros"])
def update(updateLibro1: UpdateLibro, id: int):
    try:
        libroUpdate = updateLibro(updateLibro1=updateLibro1, id=id)
        if libroUpdate:
            return libroUpdate
        return JSONResponse(content='Libro no actualizado', status_code=404)
    except Exception as err:
        raise HTTPException(detail=f'Error al actualizar el Libro: {err}', status_code=500)

@libro.delete('/', response_model=LibroDTO, status_code=200, summary="Eliminar un Libro", description="Elimina un libro existente del sistema.", tags=["Libros"])
def delete(librodelete: DeleteLibroDTO):
    try:
        libroDelete = deleteLibro(librodelete=librodelete)
        if libroDelete:
            return libroDelete
        return JSONResponse(content='Libro no eliminado', status_code=404)
    except Exception as err:
        raise HTTPException(detail=f'Error al eliminar el Libro: {err}', status_code=500)