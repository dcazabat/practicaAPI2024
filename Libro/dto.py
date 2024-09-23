from pydantic import BaseModel
from datetime import date

class LibroBase(BaseModel):
    titulo: str
    autor: str
    publicado_en: date
    isbn: str

class LibroCreate(LibroBase):
    pass

class Libro(LibroBase):
    id: str

    class Config:
        orm_mode = True