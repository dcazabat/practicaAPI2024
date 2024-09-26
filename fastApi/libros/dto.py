from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class CreateLibro(BaseModel):
    titulo : str = Field(..., description="Nombre del Libro", example="Pinocho")
    autor : str = Field(..., description="Nombre del autor del libro", example="Carlo Collodi")
    publicado_en : date = Field(..., description="Lanzamiento", example="Febrero 1883")
    isbn : str = Field(..., description="Codigo de identificacion unico", example="9780688022679")
    
    class Config:
        schema_extra = {
            "example": {
                "titulo" : "Pinocho",
                "autor" : "Carlo Collodi",
                "publicado_en" : "Febrero 1883",
                "isbn" : "9780688022679"
            }
        }
    
class LibroDTO(BaseModel):
    id: int = Field(..., description="Id de libro", example="1")
    titulo : str = Field(..., description="Nombre del Libro", example="Pinocho")
    autor : str = Field(..., description="Nombre del autor del libro", example="Carlo Collodi")
    publicado_en : date = Field(..., description="Lanzamiento", example="Febrero 1883")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id" : "1",
                "titulo" : "Pinocho",
                "autor" : "Carlo Collodi",
                "publicado_en" : "Febrero 1883"
            }
        }
    
class UpdateLibroDTO(BaseModel):
    titulo : str = Field(..., description="Nombre del Libro", example="Pinocho")
    autor : str = Field(..., description="Nombre del autor del libro", example="Carlo Collodi")
    
    class Config:
        json_schema_extra = {
            "example": {
                "titulo" : "Pinocho",
                "autor" : "Carlo Collodi"
            }
        }
    
class DeleteLibroDTO(BaseModel):
    id: int = Field(..., description="Id de libro", example="1")
    deleted : bool = Field(..., description="Es True o False segun quiera Eliminar o Recuperar", example="True")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id" : "1",
                "deleted" : "True"
            }
        }