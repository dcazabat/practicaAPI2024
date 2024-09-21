# Contiene todas las funciones que manejan la logica de Negocio (QUE ACCIONES REALIZO con la BD)
from libro.entity import Libro
from config.cnx import sessionlocal
from libro.dto import CreateLibro, DeleteLibroDTO, UpdateLibroDTO, LibroDTO

def getLibros():
    try:
        db = sessionlocal()
        libro = db.query(Libro).filter(Libro.delete == False).all()
        if libro:
            return libro 
        return None
    except Exception as ex:
        return f'Ups algo anda mal,{ex}'
    finally: 
        db.close()
    
def getLibrosInactive():
    try:
        db = sessionlocal()
        libro = db.query(Libro).filter(Libro.delete == True).all()
        if libro:
            return libro 
        return None
    except Exception as ex:
        return f'Ups algo anda mal,{ex}'
    finally: 
        db.close()

def getLibro(id:int):
    try:
        db = sessionlocal()
        libro = db.query(Libro).filter(Libro.id == id).firts()
        if libro:
            return libro 
        return None
    except Exception as ex:
        return f'Ups algo anda mal,{ex}'
    finally:
        db.close()

def createLibro(libro:CreateLibro):
    try:
        db = sessionlocal()
        libro_new = Libro(
            titulo = libro.titulo,
            autor = libro.autor,
            publicado_en = libro.publicado_en,
            isbn = libro.isbn,
        
        )
        db.add(libro_new)
        db.commit()
        db.refresh(libro_new)
        db.close()
        return libro_new
    except Exception as ex:
        db.rollback()
        return f'Ups algo anda mal, {ex}'
    finally:
        db.close()

def updateLibro(libroupdate: UpdateLibroDTO, id: int):
    try:
        db = sessionlocal()
        libro_update = db.query(Libro).filter(Libro.id == int(id)).first()
        if libro_update:
            libro_update.titulo = libroupdate.titulo
            libro_update.autor = libroupdate.autor
            libro_update.isbn = libroupdate.isbn
            return libro_update
        return None
    except Exception as ex:
            db.rollback()
            return f'Ups, algo anda mal, {ex}'
    finally:
            db.close()

def deleteLibro(librodelete: DeleteLibroDTO):
    try:
        db = sessionlocal()
        libro_delete = db.query(Libro).filter(Libro.id == librodelete.id).first()
        if libro_delete:
            libro_delete.delete = librodelete.delete
            db.commit()
            db.refresh(libro_delete)
            return libro_delete
        return None
    except Exception as ex:
        db.rollback()
        return f'Ups, algo anda mal, {ex}'
    finally:
        db.close()
    
        