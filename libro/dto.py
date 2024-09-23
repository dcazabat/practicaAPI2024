from pydantic import BaseModel, Field

class CreateLibro(BaseModel):
    nombre : str = Field(..., description="Nombre de la rana", example="Rana Verde")
    nombreCientifico : str
    caracteristicas : str
    habitat : str
    alimentacion : str
    
class LibroDTO(BaseModel):
    id: int
    nombre : str
    nombreCientifico : str
    caracteristicas : str
    habitat : str
    alimentacion : str
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "nombre": "Rana Verde",
                "nombreCientifico": "Agalychnis callidryas",
                "caracteristicas":"Color verde intenso, venenosa",
                "habitat": "Jungla",
                "alimentacion": "Insectos"
            }
        }
            
class UpdateLibroDTO(BaseModel):
    id: int
    nombre : str
    nombreCientifico : str
    caracteristicas : str
    habitat : str
    alimentacion : str
    
class DeleteLibroDTO(BaseModel):
    id: int
    deleted : bool