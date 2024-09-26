from sqlalchemy.orm import Session
from .models import Libro

def crear_libro(db: Session, titulo: str, autor: str, publicado_en, isbn: str):
    libro = Libro(titulo=titulo, autor=autor, publicado_en=publicado_en, isbn=isbn)
    db.add(libro)
    db.commit()
    db.refresh(libro)
    return libro

def obtener_libros(db: Session):
    return db.query(Libro).all()

def obtener_libro(db: Session, libro_id: str):
    return db.query(Libro).filter(Libro.id == libro_id).first()

def actualizar_libro(db: Session, libro_id: str, titulo: str = None, autor: str = None, publicado_en = None, isbn: str = None):
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if libro:
        if titulo:
            libro.titulo = titulo
        if autor:
            libro.autor = autor
        if publicado_en:
            libro.publicado_en = publicado_en
        if isbn:
            libro.isbn = isbn
        db.commit()
        db.refresh(libro)
    return libro

def eliminar_libro(db: Session, libro_id: str):
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if libro:
        db.delete(libro)
        db.commit()
    return libro

