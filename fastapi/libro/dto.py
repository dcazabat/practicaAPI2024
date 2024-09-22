# Son las diferentes formas de aceptar o devolver los datos
from pydantic import BaseModel

# Modelo base para el Libro
class LibroBase(BaseModel):
    titulo: str
    autor: str
    anio_publicacion: int
    editorial: str

# Esquema para crear un nuevo libro
class LibroCreate(LibroBase):
    pass

# Esquema para la representación del libro en las respuestas
class Libro(LibroBase):
    id: int

    class Config:
        orm_mode = True
