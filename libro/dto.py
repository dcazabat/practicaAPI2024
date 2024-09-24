from pydantic import BaseModel, Field
from datetime import date
from uuid import UUID

class CreateLibro(BaseModel):
    titulo: str = Field(..., description="Título del libro", example="Don Quijote de la Mancha")
    autor: str = Field(..., description="Autor del libro", example="Miguel de Cervantes")
    publicado_en: date = Field(..., description="Fecha de publicación", example="1605-01-16")
    isbn: str = Field(..., description="Código ISBN del libro", example="978-3-16-148410-0")

class LibroDTO(BaseModel):
    id: UUID = Field(..., description="Identificador único del libro")
    titulo: str
    autor: str
    publicado_en: date
    isbn: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "titulo": "Don Quijote de la Mancha",
                "autor": "Miguel de Cervantes",
                "publicado_en": "1605-01-16",
                "isbn": "978-3-16-148410-0"
            }
        }

class UpdateLibroDTO(BaseModel):
    titulo: str = Field(..., description="Título del libro")
    autor: str = Field(..., description="Autor del libro")
    publicado_en: date = Field(..., description="Fecha de publicación")
    isbn: str = Field(..., description="Código ISBN del libro")

class DeleteLibroDTO(BaseModel):
    id: UUID = Field(..., description="Identificador único del libro")
    deleted: bool = Field(..., description="Estado de eliminación del libro", example=True)
