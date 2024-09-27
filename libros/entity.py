# Declaracion del Modelo de Datos que se conecta con la BD

from default.defaultmodel import Base
from sqlalchemy import Column, Integer, String, Boolean, UUID, Date
from sqlalchemy.orm import relationship

class Libro(Base):
    __tablename__ = 'libros'
    id = Column(Integer, as_uuid=True,  primary_key=True)
    titulo = Column(String(50), unique=True, nullable=False)
    autor = Column(String(100), nullable=False)
    publicado_en = Column(Date, nullable=True)
    isbn = Column(String, nullable=True)
    deleted = Column(Boolean, default=False)