from sqlalchemy.orm import Session
from entity import Libro
from dto import LibroCreate

class LibroService:
    def __init__(self, session: Session):
        self.session = session

