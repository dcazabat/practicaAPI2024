# Declaracion del Modelo de Datos que se conecta con la BD

from default.defaultmodel import Base
from sqlalchemy import Column, Integer, String

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    autor = Column(String, index=True)
    anio_publicacion = Column(Integer)
    editorial = Column(String)