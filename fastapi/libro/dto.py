from pydantic import BaseModel
from datetime import date
from uuid import UUID
from typing import Optional

# DTO para la creación de un nuevo libro
class CreateLibroDTO(BaseModel):
    titulo: str
    autor: str
    publicado_en: date
    isbn: str

# DTO para actualizar los datos de un libro existente
class UpdateLibroDTO(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    publicado_en: Optional[date] = None
    isbn: Optional[str] = None

# DTO para el borrado lógico de un libro
class DeleteLibroDTO(BaseModel):
    id: UUID
    deleted: bool

# DTO para devolver la información completa de un libro
class LibroDTO(BaseModel):
    id: UUID
    titulo: str
    autor: str
    publicado_en: date
    isbn: str
    deleted: bool

    class Config:
        orm_mode = True
