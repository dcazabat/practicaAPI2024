from config.cnx import sessionlocal
from libros.entity import Libro
from libros.dto import CreateLibro,DeleteLibroDTO,UpdateLibro,LibroDTO

def getLibros():
    try:
        db = sessionlocal()
        libros = db.query(Libro).filter(Libro.deleted == False).all() 
        if libros:
            return libros
        return None
    except Exception as err:
        return f'Ah ocurrido un error,{err}'
    finally:
        db.close()

def getLibrosInactive():
    try:
        db = sessionlocal()
        libros = db.query(Libro).filter(Libro.deleted == True).all() 
        if libros:
            return libros
        return None
    except Exception as err:
        return f'Ah ocurrido un error,{err}'
    finally:
        db.close()

def getLibro(id:int):
    try:
        db = sessionlocal()
        libro = db.query(Libro).filter(Libro.id == id).first() 
        if libro:
            return libro
        return None
    except Exception as err:
        return f'Ah ocurrido un error,{err}'
    finally:
        db.close()

def createLibro(libro:CreateLibro):
    try:
        db = sessionlocal()
        libroNew = Libro(
            titulo= libro.titulo,
            autor= libro.autor,
            publicado_en= libro.publicado_en,
            isbn=libro.isbn,
        )
        db.add(libroNew)
        db.commit()
        db.refresh()
        db.close()
        return libroNew
    except Exception as err:
        return f'Ah ocurrido un error,{err}'
    finally:
        db.close()

def updateLibro(libroUpdate1:UpdateLibro,id:int):
    try:
        db = sessionlocal()
        libroUpdate2 = db.query(Libro).filter(Libro.id == id).first() 
        if libroUpdate2:
            libroUpdate2.titulo = libroUpdate1.titulo
            libroUpdate2.isbn = libroUpdate1.isbn

        db.add(libroUpdate2)
        db.commit()
        db.refresh()
        db.close()
        return libroUpdate2
    except Exception as err:
        return f'Ah ocurrido un error,{err}'
    finally:
        db.close()


def deleteLibro(libroDelete1: DeleteLibroDTO):
    try:
        db = sessionlocal()
        libroDelete2 = db.query(Libro).filter(Libro.id == libroDelete1.id).first()
        if libroDelete2:
            libroDelete2.deleted = libroDelete1.deleted
            db.commit()
            db.refresh(libroDelete2)
            return libroDelete2
        return None
    except Exception as err:
        return f'Ah ocurrido un error,{err}'
    finally:
        db.close()