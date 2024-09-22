from sqlalchemy.orm import Session
from models import Libro
import uuid

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
