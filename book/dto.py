from pydantic import BaseModel
from datetime import date

class CreateBook(BaseModel):
    titulo : str
    autor : str
    publicado_en : date
    isnb : str
    
class BookDTO(BaseModel):
    id: int
    titulo : str
    autor : str
    publicado_en : date
    isnb : str
    
class UpdateBookDTO(BaseModel):
    id: int
    titulo : str
    autor : str
    
class DeleteBookDTO(BaseModel):
    id: int
    deleted : bool