from fastapi import FastAPI
from typing import Union
from default.model import Base
from config.cnx import engine

from default.routes import default
from libros.routes import libros 


app = FastAPI(
    title="API Rest FastAPI",
    description="Ejemplo de API Rest con FASTAPI",
    version="0.0.0",
        contact={
        "name": "Dario Coronel",
        "email": "dario.coronel@miempresa.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)

app.include_router(default, prefix='', tags=['App Routes Default'])
app.include_router(libros, prefix='/libros', tags=['Libros'])

Base.metadata.create_all(bind=engine)

