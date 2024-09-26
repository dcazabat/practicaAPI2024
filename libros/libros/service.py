from sqlalchemy.orm import Session
import uuid
from typing import List
from config.cnx import sessionlocal
from libros.entity import Libro 
from libros.dto import *

#Trae todos los libros
def get_Libros():
    try:
        db = sessionlocal()
        libros = db.query(Libro).filter(Libro.deleted == False).all()
        if libros: 
           return libros
        return None
    except Exception as e:
        return f'Ocurrio un Error, {e}'
    finally:
        db.close

#Crea un libro 
def crear_libro(libros: CreateLibro):
    try:
        db = sessionlocal()
        libro_nuevo = Libro(
            titulo = Libro.titulo,
            autor = Libro.autor,
            publicado_en = Libro.publicado_en,
            isnb = Libro.isnb
        )
        db.add(libro_nuevo)
        db.commit()
        db.refresh(libro_nuevo)
        db.close()
        return libro_nuevo
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

    
def actualizar_libro(libro_update: UpdateLibroDTO, id: int):
    try:
        db = sessionlocal()
        libro_update = db.query(Libro).filter(Libro.id == id).first()
        if libro_update:
            libro_update.titulo = libro_update.titulo
            libro_update.autor = libro_update.autor
            db.commit()
            db.refresh(libro_update)
            return libro_update
        return None
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

def borrar_libro(libro_delete: DeleteLibroDTO, id: int):
    try:
        db = sessionlocal()
        libro_delete = db.query(Libro).filter(Libro.id == id).first()
        if libro_delete:
            libro_delete.deleted = libro_delete.deleted
            db.commit()
            db.refresh(libro_delete)
            return libro_delete
        return f'El libro fue eliminado correctamente'
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()