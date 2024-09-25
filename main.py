from fastapi import FastAPI
from default.defaultmodel import Base
from config.cnx import engine


from default.routes import default
from Libro.routes import Libro

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
app.include_router(Libro, prefix='/libros', tags=['Libros'])

Base.metadata.create_all(bind=engine)