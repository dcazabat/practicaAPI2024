from fastapi import FastAPI
from default.defaultmodel import Base
from config.cnx import engine

# Ruotes
from default.routes import default
from libro.routes import libro


app = FastAPI(
    title="API Rest FastAPI",
    description="Ejemplo de API Rest con FASTAPI",
    version="0.0.1",
        contact={
        "name": "Soporte Técnico",
        "email": "soporte@miempresa.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)

app.include_router(default, prefix='', tags=['App Routes Default'])
app.include_router(libro, prefix='/libros', tags=['Libros'])


Base.metadata.create_all(bind=engine)