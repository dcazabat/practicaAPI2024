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