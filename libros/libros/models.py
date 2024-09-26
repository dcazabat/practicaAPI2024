from sqlalchemy import Column, String, Date
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()

class Libro(Base):
    __tablename__ = "libros"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid4()), index=True)
    titulo = Column(String, index=True)
    autor = Column(String)
    publicado_en = Column(Date)
    isbn = Column(String, unique=True, index=True)
