from default.defaultmodel import Base
from sqlalchemy import Column, Integer, String, Boolean, Date

class Libro(Base):
    __tablename__ = 'libros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(50), nullable=False)
    autor = Column(String(50),nullable=False)
    publicado_en = Column(Date, nullable=False)
    isbn = Column(String(30),nullable=False)
    deleted = Column(Boolean,default=False)