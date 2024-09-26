from sqlalchemy import Column, String, Date, UUID, Boolean
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Libro(Base):
    __tablename__ = "libros"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    publicado_en = Column(Date, nullable=False)
    isbn = Column(String, nullable=False, unique=True)
    deleted = Column(Boolean, default= False)