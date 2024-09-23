
from sqlalchemy import Column, String, Date
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Libro(Base):
    __tablename__ = 'libros'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    publicado_en = Column(Date, nullable=False)
    isbn = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Libro(titulo='{self.titulo}', autor='{self.autor}', publicado_en='{self.publicado_en}', isbn='{self.isbn}')>"
