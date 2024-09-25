from book.entity import Book
from config.cnx import sessionlocal
from book.dto import CreateBook, DeleteBookDTO, UpdateBookDTO, BookDTO

# Devuelve todos los libros
def getBooks():
    try:
        db = sessionlocal()
        books = db.query(Book).filter(Book.deleted == False).all()
        if books:
            return books
        return None
    except Exception as e:
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Devuelve los datos del libro
def getBook(id: int):
    try:
        db = sessionlocal()
        book = db.query(Book).filter(Book.id == id).first()
        if book:
            return book
        return None
    except Exception as e:
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Crea un libro dentro de la Base de Datos (POST)
def createBook(book: CreateBook):
    try:
        db = sessionlocal()
        book_new = Book(
            titulo = book.titulo,
            autor = book.autor,
            publicado_en = book.publicado_en,
            isnb = book.isnb
        )
        db.add(book_new)
        db.commit()
        db.refresh(book_new)
        db.close()
        return book_new
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Actualizacion de datos del libro       
def updateBook(bookupdate: UpdateBookDTO):
    try:
        db = sessionlocal()
        book_update = db.query(Book).filter(Book.id == int(bookupdate.id)).first()
        if book_update:
            book_update.titulo = bookupdate.titulo
            book_update.autor = bookupdate.autor
            book_update.publicado_en = bookupdate.publicado_en
            book_update.isnb = bookupdate.isnb
            db.commit()
            db.refresh(book_update)
            return book_update
        return None
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Borrado LOGICO de datos de libro
def deleteBook(bookdelete: DeleteBookDTO):
    try:
        db = sessionlocal()
        book_delete = db.query(Book).filter(Book.id == bookdelete.id).first()
        if book_delete:
            book_delete.deleted = bookdelete.deleted
            db.commit()
            db.refresh(book_delete)
            return book_delete
        return None
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()




