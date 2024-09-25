from sqlalchemy.orm import Session
from uuid import UUID
from libro.entity import Libro
from libro.dto import CreateLibro, UpdateLibroDTO, LibroDTO, DeleteLibroDTO
from config.cnx import sessionlocal

def get_all_libros():
    try:
        db: Session = sessionlocal()
        libros = db.query(Libro).filter(Libro.deleted == False).all() 
        return libros if libros else []
    except Exception as e:
        return f"Ocurrió un error al obtener los libros: {e}"
    finally:
        db.close()

def get_libro_by_id(libro_id: UUID):
    try:
        db: Session = sessionlocal()
        libro = db.query(Libro).filter(Libro.id == libro_id, Libro.deleted == False).first()  
        return libro if libro else None
    except Exception as e:
        return f"Ocurrió un error al obtener el libro: {e}"
    finally:
        db.close()

def create_libro(libro: CreateLibro):
    try:
        db: Session = sessionlocal()
        new_libro = Libro(
            titulo=libro.titulo,
            autor=libro.autor,
            publicado_en=libro.publicado_en,
            isbn=libro.isbn
        )
        db.add(new_libro)
        db.commit()
        db.refresh(new_libro)
        return new_libro
    except Exception as e:
        db.rollback()
        return f"Ocurrió un error al crear el libro: {e}"
    finally:
        db.close()

def update_libro(libro_id: UUID, libro_data: UpdateLibroDTO):
    try:
        db: Session = sessionlocal()
        libro_to_update = db.query(Libro).filter(Libro.id == libro_id, Libro.deleted == False).first()
        if libro_to_update:
            libro_to_update.titulo = libro_data.titulo
            libro_to_update.autor = libro_data.autor
            libro_to_update.publicado_en = libro_data.publicado_en
            libro_to_update.isbn = libro_data.isbn

            db.commit()
            db.refresh(libro_to_update)
            return libro_to_update
        return None 
    except Exception as e:
        db.rollback()
        return f"Ocurrió un error al actualizar el libro: {e}"
    finally:
        db.close()

def delete_libro(libro_id: UUID):
    try:
        db: Session = sessionlocal()
        libro_to_delete = db.query(Libro).filter(Libro.id == libro_id, Libro.deleted == False).first()
        if libro_to_delete:
            libro_to_delete.deleted = True  
            db.commit()
            return {"message": "Libro eliminado correctamente."}
        return None  
    except Exception as e:
        db.rollback()
        return f"Ocurrió un error al eliminar el libro: {e}"
    finally:
        db.close()
