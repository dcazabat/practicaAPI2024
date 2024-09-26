from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, func
from sqlalchemy import create_engine


Base = declarative_base()

class Libro(Base):
    __tablename__ = 'libros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    autor = Column(String)
    publicado_en = Column(Date)
    isbn = Column(String)


engine = create_engine('sqlite:///./libros.db')
Base.metadata.create_all(bind=engine)