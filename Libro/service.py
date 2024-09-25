from sqlalchemy.orm import Session
from entity import Libro
from dto import LibroCreate

class LibroService:
    def __init__(self, session: Session):
        self.session = session

    def crear_libro(self, libro_create: LibroCreate):
        libro = Libro(**libro_create.dict())
        self.session.add(libro)
        self.session.commit()
        self.session.refresh(libro)
        return libro
    
    def obtener_libros(self):
        return self.session.query(Libro).all()

    def obtener_libro_por_id(self, libro_id: str):
        return self.session.query(Libro).filter_by(id=libro_id).first()
    
    def actualizar_libro(self, libro_id: str, libro_update: LibroCreate):
        libro = self.obtener_libro_por_id(libro_id)
        if libro:
            for key, value in libro_update.dict().items():
                setattr(libro, key, value)
            self.session.commit()
            return libro
        return None



