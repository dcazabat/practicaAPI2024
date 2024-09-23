from default.defaultmodel import Base
from sqlalchemy import Column, String, Boolean, UUID, Integer, Date
from sqlalchemy.orm import relationship

class Libro(Base):
    __tablename__ = 'libros'
    id = Column(UUID, primary_key=True)
    titulo = Column(String(50), nullable=False)
    autor = Column(String(100), nullable=False)
    publicado_en = Column(Date(100), nullable=False)
    isbn = Column(Integer(100))
    deleted = Column(Boolean, default=False)
    