from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from book.dto import *
from book.service import *

book = APIRouter()

@book.get('/', response_model=List[BookDTO], status_code=200)
def books():
    try:
        books = getBooks()
        if books:
            return books
        return JSONResponse(content=f'Libros no econtrados', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al recuperar Libros: {e}', status_code=500)

@book.get('/{id}', response_model=BookDTO, status_code=200)
def get_book(id: int):
    try:
        book = getBook(id=id)
        if book:
            return book
        return JSONResponse(content=f'Libro no econtrado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al recuperar Libro: {e}', status_code=500)

@book.post('/', response_model=BookDTO, status_code=200)
def create(bookpost: CreateBook):
    try:
        book_new = createBook(book=bookpost)
        if book_new:
                return book_new
        return JSONResponse(content=f'Libro no Creado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al Crear Libro: {e}', status_code=500)

@book.put('/', response_model=BookDTO, status_code=200)
def update(bookupdate: UpdateBookDTO):
    try:
        book_update = updateBook(bookupdate=bookupdate)
        if book_update:
            return book_update
        return JSONResponse(content=f'Libro no actualizado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al actualizar el Libro: {e}', status_code=500)

@book.delete('/', response_model=BookDTO, status_code=200)
def delete(bookdelete: DeleteBookDTO):
    try:
        book_delete = deleteBook(bookdelete=bookdelete) 
        if book_delete:
            return book_delete
        return JSONResponse(content=f'Libro no Eliminado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al eliminar el Libro: {e}', status_code=500)