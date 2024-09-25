from config.cnx import sessionlocal
from libros.entity import Libro
from libros.dto import CreateLibro, UpdateLibroDTO, DeleteLibroDTO, LibroDTO

# Devuelve todos los libros
def getLibros():
    try:
        db = sessionlocal()
        libritos = db.query(Libro).filter(Libro.deleted == False).all()
        if libritos:
            return libritos
        return None
    except Exception as e:
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Devuelve todos los Usuarios Inactivos
def getLibrosInactive():
    try:
        db = sessionlocal()
        libritos = db.query(Libro).filter(Libro.deleted == True).all()
        if libritos:
            return libritos
        return None
    except Exception as e:
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Devuelve los datos por id
def getLibro(id: int):
    try:
        db = sessionlocal()
        libro = db.query(Libro).filter(Libro.id == id).first()
        if libro:
            return libro
        return None
    except Exception as e:
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Crea un Libro dentro de la Base de Datos (POST)
def createLibro(libro: CreateLibro):
    try:
        db = sessionlocal()
        libro_new = Libro(
            titulo = libro.titulo,
            autor = libro.autor, 
            publicado_en = libro.publicado_en, 
            isbn = libro.isbn
            
        )
        db.add(libro_new)
        db.commit()
        db.refresh(libro_new)
        db.close()
        return libro_new
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Actualizacion de Datos del libro       
def updateLibro(libroupdate: UpdateLibroDTO):
    try:
        db = sessionlocal()
        libro_update = db.query(Libro).filter(Libro.id == int(libroupdate.id)).first()
        if libro_update:
            libro_update.titulo = libroupdate.titulo
            libro_update.autor = libroupdate.autor
            
            db.commit()
            db.refresh(libro_update)
            return libro_update
        return None
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Borrado LOGICO de libro
def deleteLibro(librodelete: DeleteLibroDTO):
    try:
        db = sessionlocal()
        libro_delete = db.query(Libro).filter(Libro.id == librodelete.id).first()
        if libro_delete:
            libro_delete.deleted = librodelete.deleted
            db.commit()
            db.refresh(libro_delete)
            return libro_delete
        return None
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()
