#Son las diferentes formas de aceptar o devolver los datos
from pydantic import BaseModel, Field
from datetime  import date

class CreateLibro(BaseModel):
    titulo: str = Field(..., description="Titulo del Libro", example="Amate a ti mismo")
    autor: str = Field(..., description="Nombre del autor", example="Louise Hay")
    publicado_en: date= Field(..., description="Fecha de lanzamiento", example="2012-06-18")
    isbn: str = Field(..., description="Identificador unico", example="9780937611692")

    class Config:
        schema_extra = {
            "example": {
                "titulo": "Amate a ti mismo",
                "autor": "Louise Hay",
                "publicado_en": "2012-06-18",
                "isbn": "9780937611692",
            }
        }

    
class LibroDTO(BaseModel):
    id: int = Field(..., description="Id de Libro", example=1)
    titulo: str = Field(..., description="Titulo del libro", example="Amate a ti mismo")
    autor: str = Field(..., description="Nombre del Autor", example="Louise Hay")
    publicado_en: str = Field(..., description="Fecha de Lnazamiento", example="18-06-2012")
    isbn: str = Field(..., description="Identificador unico", example="9780937611692")
    
    class Config:
        json_schema_extra = {   
            "example": {
                "titulo": "Amate a ti mismo",
                "autor": "Louise Hay",
                "publicado_en": "18-06-2012",
                "isbn": "9780937611692",
            }
        }
            
class UpdateLibroDTO(BaseModel):
    titulo: str = Field(..., description="Titulo del libro", example="Amate a ti mismo")
    autor: str = Field(..., description="Nombre del Autor", example="Louise Hay")
    isbn: str = Field(..., description="Identificador unico", example="9780937611692")

    class Config:
        json_schema_extra = {
            "example": {
                # "id": 1,
                "titulo": "Amate a ti mismo",
                "autor": "Louise Hay",
                "isbn": "9780937611692",
            }
        }
    
class DeleteLibroDTO(BaseModel):
    id: int = Field(..., description="Id de Libro", example=1)
    deleted : bool = Field(..., description="Es True o False segun quiera Eliminar o Recuperar", example="True")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "deleted": True,
            }
        }