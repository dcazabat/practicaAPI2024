from fastapi import APIRouter
from typing import Union

default = APIRouter()

@default.get("/")
def read_root():
    saludo={"Hola":'Buenas, Bienvenido',
            'Pasele':'http://localhost:8000/libro',
            'Si quiere ir a ver el docs vaya a':'http://localhost:8000/docs'}
    
    return saludo

@default.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}