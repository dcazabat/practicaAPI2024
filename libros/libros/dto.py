#Son las diferentes formas de aceptar o devolver los datos
from pydantic import BaseModel, Field
from datetime  import date

class CreateLibro(BaseModel):
    titulo: str 
    autor: str 
    publicado_en: date
    isbn: str 
    
class LibroDTO(BaseModel):
    id: int 
    titulo: str 
    autor: str 
    publicado_en: str 
    isbn: str 
            
class UpdateLibroDTO(BaseModel):
    titulo: str 
    autor: str
    isbn: str

class DeleteLibroDTO(BaseModel):
    id: int 
    deleted : bool
    
