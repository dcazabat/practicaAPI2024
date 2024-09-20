# Son las diferentes formas de aceptar o devolver los datos
from pydantic import BaseModel, EmailStr, Field

class CreateUser(BaseModel):
    name: str = Field(..., description="Nombre del usuario", example="Juan")
    firstname: str = Field(..., description="Primer nombre del usuario", example="Carlos")
    lastname: str = Field(..., description="Apellido del usuario", example="Pérez")
    email: EmailStr = Field(..., description="Correo electrónico del usuario", example="juan.perez@example.com")
    password: str = Field(..., description="Contraseña del usuario", example="password123")

    class Config:
        schema_extra = {
            "example": {
                "name": "Juan",
                "firstname": "Carlos",
                "lastname": "Pérez",
                "email": "juan.perez@example.com",
                "password": "password123"
            }
        }

    
class UserDTO(BaseModel):
    id: int = Field(..., description="Id de Usuario", example=1)
    name: str = Field(..., description="Nombre del usuario", example="Juan")
    firstname: str = Field(..., description="Primer nombre del usuario", example="Carlos")
    lastname: str = Field(..., description="Apellido del usuario", example="Pérez")
    email: EmailStr = Field(..., description="Correo electrónico del usuario", example="juan.perez@example.com")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Juan",
                "firstname": "Carlos",
                "lastname": "Pérez",
                "email": "juan.perez@example.com",
            }
        }
            
class UpdateUserDTO(BaseModel):
    # id: int = Field(..., description="Id de Usuario", example=1)
    firstname: str = Field(..., description="Primer nombre del usuario", example="Carlos")
    lastname: str = Field(..., description="Apellido del usuario", example="Pérez")
    email: EmailStr = Field(..., description="Correo electrónico del usuario", example="juan.perez@example.com")

    class Config:
        json_schema_extra = {
            "example": {
                # "id": 1,
                "firstname": "Carlos",
                "lastname": "Pérez",
                "email": "juan.perez@example.com",
            }
        }
    
class DeleteUserDTO(BaseModel):
    id: int = Field(..., description="Id de Usuario", example=1)
    deleted : bool = Field(..., description="Es True o False segun quiera Eliminar o Recuperar", example="True")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "deleted": True,
            }
        }
