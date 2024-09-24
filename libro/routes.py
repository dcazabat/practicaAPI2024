from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from libro.dto import *
from libro.service import *

libro = APIRouter()

@libro.get('/', response_model=List[LibroDTO], status_code=200, summary="Obtener todos los libros", description="Devuelve una lista de todos los libros almacenados.", tags=["Libros"])
def libros():
    try:
        libros = get_all_libros()
        if libros:
            return libros
        return JSONResponse(content='Libros no encontrados', status_code=404)
    except Exception as e:
        raise HTTPException(detail=f'Error al recuperar Libros: {e}', status_code=500)
    
@libro.get('/{id}', response_model=LibroDTO, status_code=200, summary="Obtener libro por ID", description="Devuelve un libro específico basado en su ID.", tags=["Libros"])
def get_libro(id: UUID):
    try:
        libro = get_libro_by_id(id=id)
        if libro:
            return libro
        return JSONResponse(content='Libro no encontrado', status_code=404)
    except Exception as e:
        raise HTTPException(detail=f'Error al recuperar libro: {e}', status_code=500)