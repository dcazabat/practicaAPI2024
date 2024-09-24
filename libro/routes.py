from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from libro.dto import *
from libro.service import *

libro = APIRouter()

@libro.get('/', response_model=List[LibroDTO], status_code=200, summary="Obtener todos los libros", description="Devuelve una lista de todos los libros almacenados.", tags=["Libros"])
def GetLibros():
    try:
        libros = get_all_libros()
        if libros:
            return libros
        return JSONResponse(content='Libros no encontrados', status_code=404)
    except Exception as e:
        raise HTTPException(detail=f'Error al recuperar Libros: {e}', status_code=500)
    
@libro.get('/{id}', response_model=LibroDTO, status_code=200, summary="Obtener libro por ID", description="Devuelve un libro específico basado en su ID.", tags=["Libros"])
def getLibro(id: UUID):
    try:
        libro = get_libro_by_id(id=id)
        if libro:
            return libro
        return JSONResponse(content='Libro no encontrado', status_code=404)
    except Exception as e:
        raise HTTPException(detail=f'Error al recuperar libro: {e}', status_code=500)
    
@libro.post('/', response_model=LibroDTO, status_code=201, summary="Crear un nuevo libro", description="Crea un nuevo libro en el sistema con los datos proporcionados.", tags=["Libros"], responses={201: {"description": "Libro creado con éxito"}, 404: {"description": "Libro no creado"}, 500: {"description": "Error interno del servidor"}})
def createLibro(libropost: CreateLibro):
    try:
        libro_new = create_libro(libro=libropost)
        if libro_new:
            return libro_new
        return JSONResponse(content='Libro no creado', status_code=404)
    except Exception as e:
        raise HTTPException(detail=f'Error al crear libro: {e}', status_code=500)
    
@libro.put('/{id}', response_model=LibroDTO, status_code=200, summary="Actualizar un libro", description="Actualiza la información de un libro existente en el sistema.", tags=["Libros"])
def updateLibro(libroupdate: UpdateLibroDTO, id: int):
    try:
        libro_update = update_libro(libroupdate=libroupdate, id=id)
        if libro_update:
            return libro_update
        return JSONResponse(content='Libro no actualizado', status_code=404)
    except Exception as e:
        raise HTTPException(detail=f'Error al actualizar el libro: {e}', status_code=500)

@libro.delete('/', response_model=LibroDTO, status_code=200, summary="Eliminar un libro", description="Elimina un libro existente del sistema.", tags=["Libros"])
def deleteLibro(librodelete: DeleteLibroDTO):
    try:
        libro_delete = delete_libro(librodelete=librodelete)
        if libro_delete:
            return libro_delete
        return JSONResponse(content='Usuario no eliminado', status_code=404)
    except Exception as e:
        raise HTTPException(detail=f'Error al eliminar el libro: {e}', status_code=500)