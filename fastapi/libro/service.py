from sqlalchemy.orm import Session
from uuid import UUID
from libro.entity import Libro  
from libro.dto import CreateLibroDTO, UpdateLibroDTO, DeleteLibroDTO, LibroDTO  
from config.cnx import SessionLocal 

# Devuelve todos los libros activos (no eliminados)
def getLibros():
    try:
        db: Session = SessionLocal()
        libros = db.query(Libro).filter(Libro.deleted == False).all()
        if libros:
            return libros
        return None
    except Exception as e:
        return f"Ocurrió un error: {e}"
    finally:
        db.close()

# Devuelve todos los libros eliminados lógicamente
def getLibrosInactivos():
    try:
        db: Session = SessionLocal()
        libros = db.query(Libro).filter(Libro.deleted == True).all()
        if libros:
            return libros
        return None
    except Exception as e:
        return f"Ocurrió un error: {e}"
    finally:
        db.close()

# Devuelve los detalles de un libro por su ID
def getLibro(libro_id: UUID):
    try:
        db: Session = SessionLocal()
        libro = db.query(Libro).filter(Libro.id == libro_id).first()
        if libro:
            return libro
        return None
    except Exception as e:
        return f"Ocurrió un error: {e}"
    finally:
        db.close()

# Crea un nuevo libro
def createLibro(libro: CreateLibroDTO):
    try:
        db: Session = SessionLocal()
        nuevo_libro = Libro(
            titulo=libro.titulo,
            autor=libro.autor,
            publicado_en=libro.publicado_en,
            isbn=libro.isbn
        )
        db.add(nuevo_libro)
        db.commit()
        db.refresh(nuevo_libro)
        return nuevo_libro
    except Exception as e:
        db.rollback()
        return f"Ocurrió un error: {e}"
    finally:
        db.close()

# Actualiza los detalles de un libro existente por su ID
def updateLibro(libro_actualizado: UpdateLibroDTO, libro_id: UUID):
    try:
        db: Session = SessionLocal()
        libro = db.query(Libro).filter(Libro.id == libro_id).first()
        if libro:
            libro.titulo = libro_actualizado.titulo
            libro.autor = libro_actualizado.autor
            libro.publicado_en = libro_actualizado.publicado_en
            libro.isbn = libro_actualizado.isbn
            db.commit()
            db.refresh(libro)
            return libro
        return None
    except Exception as e:
        db.rollback()
        return f"Ocurrió un error: {e}"
    finally:
        db.close()

# Borrado lógico de un libro por su ID (marcar como eliminado)
def deleteLibro(libro_borrar: DeleteLibroDTO):
    try:
        db: Session = SessionLocal()
        libro = db.query(Libro).filter(Libro.id == libro_borrar.id).first()
        if libro:
            libro.deleted = libro_borrar.deleted
            db.commit()
            db.refresh(libro)
            return libro
        return None
    except Exception as e:
        db.rollback()
        return f"Ocurrió un error: {e}"
    finally:
        db.close()
