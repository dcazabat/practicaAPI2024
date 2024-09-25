from pydantic import BaseModel
from datetime import date
from typing import Optional

class CreateLibro(BaseModel):
    titulo : str
    autor : str
    publicado_en : date
    isbn : str
    
class LibroDTO(BaseModel):
    id: int
    titulo : str
    autor : str
    publicado_en : date
    user_id : int
    
class UpdateLibroDTO(BaseModel):
    titulo : str
    autor : str
    
class DeleteLibroDTO(BaseModel):
    id: int
    deleted : bool