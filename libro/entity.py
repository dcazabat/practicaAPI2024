from default.defaultmodel import Base
import uuid
from sqlalchemy import Column, String, Date, Boolean
from sqlalchemy.dialects.sqlite import UUID

class Libro(Base):
    __tablename__ = "libros"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    publicado_en = Column(Date, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    deleted = Column(Boolean, default=False)
    