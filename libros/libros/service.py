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

def crear_libro(db: Session, titulo: str, autor: str, publicado_en: str, isbn: str):
    db_libro = Libro(
        titulo=titulo,
        autor=autor,
        publicado_en=publicado_en,
        isbn=isbn,
    )
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    return db_libro

def obtener_libros(db: Session):
    return db.query(Libro).all()

def obtener_libro_por_id(db: Session, libro_id: uuid.UUID):
    return db.query(Libro).filter(Libro.id == libro_id).first()

def actualizar_libro(db: Session, libro_id: uuid.UUID, titulo: str, autor: str, publicado_en: str, isbn: str):
    db_libro = obtener_libro_por_id(db, libro_id)
    if db_libro:
        db_libro.titulo = titulo
        db_libro.autor = autor
        db_libro.publicado_en = publicado_en
        db_libro.isbn = isbn
        db.commit()
        db.refresh(db_libro)
    return db_libro

def eliminar_libro(db: Session, libro_id: uuid.UUID):
    db_libro = obtener_libro_por_id(db, libro_id)
    if db_libro:
        db.delete(db_libro)
        db.commit()
    return db_libro
