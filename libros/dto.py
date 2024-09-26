from pydantic import BaseModel, Field
from datetime import date

class CreateLibro(BaseModel):
    titulo: str = Field(...,description='Nombre del libro',example='La Odisea')
    autor: str = Field(...,description='Nombre del autor', example='Homero')
    publicado_en: date=Field(...,description='Fecha de publicacion',example="1-1-1906")
    isbn:str = Field(...,description='Isbn del libro', example='978-8403870154')
    
    class Config:
        schema_extra = {
            "example": {
                "titulo": 'La Odisea',
                "autor": 'Homero',
                "publicado_en": "1-1-1906",
                "isbn": '978-8403870154',
            }
        }

class LibroDTO(BaseModel):
    id:int=Field(...,description='Id del libro', example=1)
    titulo: str = Field(...,description='Nombre del libro',example='La Odisea')
    autor: str = Field(...,description='Nombre del autor', example='Homero')
    publicado_en: date=Field(...,description='Fecha de publicacion',example="1-1-1906")
    isbn:str = Field(...,description='Isbn del libro', example='978-8403870154')
    
    class Config:
        schema_extra = {
            "example": {
                "id":1,
                "titulo": 'La Odisea',
                "autor": 'Homero',
                "publicado_en": "1-1-1906",
                "isbn": '978-8403870154',
            }
        }

class UpdateLibro(BaseModel):
    titulo: str = Field(...,description='Nombre del libro',example='La Odisea')
    autor: str = Field(...,description='Nombre del autor', example='Homero')
    isbn:str = Field(...,description='Isbn del libro', example='978-8403870154')

    class Config:
        schema_extra = {
            "example": {
                "id":1,
                "titulo": 'La Odisea',
                "autor": 'Homero',
                "isbn": '978-8403870154',
            }
        }
class DeleteLibroDTO(BaseModel):
        id: int = Field(..., description="Id de Usuario", example=1)
        deleted : bool = Field(..., description="Es True o False segun quiera Eliminar o Recuperar", example="True")
    
        class Config:
            json_schema_extra = {
                "example": {
                    "id": 1,
                    "deleted": True,
                }
            }