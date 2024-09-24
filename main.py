from fastapi import FastAPI
from default.defaultmodel import Base
from config.cnx import engine

from default.routes import default
from libro.routes import libro

app = FastAPI(
    title="API Rest FastAPI",
    description="Trabajo práctico FASTAPI & SQLITE",
    version="0.0.1",
        contact={
        "name": "Gaspar Clavin",
        "email": "gaspar@clavin.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)

app.include_router(default, prefix='', tags=['App Routes Default'])
app.include_router(libro, prefix='/libros', tags=['Libros Endpoints'])

Base.metadata.create_all(bind=engine)