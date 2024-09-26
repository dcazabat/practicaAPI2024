from fastapi import FastAPI
from typing import Union
from default.defaultmodel import Base
from config.cnx import engine

# Ruotes
from default.routes import default
from book.routes import book

app = FastAPI(
    title="API Rest FastAPI",
    description="Ejemplo de API Rest con FASTAPI",
    version="0.0.1",
)

# Ruotes Apps
app.include_router(default, prefix='', tags=['App Routes Default'])
app.include_router(book, prefix='/books', tags=['Books Endpoints'])


Base.metadata.create_all(bind=engine)