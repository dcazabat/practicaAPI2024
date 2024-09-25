from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from service import LibroService
from dto import LibroCreate, Libro
from entity import Base

DATABASE_URL = "sqlite:///./libros.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()
libro_service = LibroService(session=SessionLocal())

@app.post("/libros/", response_model=Libro)
def crear_libro(libro: LibroCreate):
    return libro_service.crear_libro(libro)

@app.get("/libros/", response_model=list[Libro])
def obtener_libros():
    return libro_service.obtener_libros()

@app.get("/libros/{libro_id}", response_model=Libro)
def obtener_libro(libro_id: str):
    libro = libro_service.obtener_libro_por_id(libro_id)
    if libro:
        return libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")

@app.put("/libros/{libro_id}", response_model=Libro)
def actualizar_libro(libro_id: str, libro: LibroCreate):
    updated_libro = libro_service.actualizar_libro(libro_id, libro)
    if updated_libro:
        return updated_libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")

@app.delete("/libros/{libro_id}")
def eliminar_libro(libro_id: str):
    if libro_service.eliminar_libro(libro_id):
        return {"mensaje": "Libro eliminado"}
    raise HTTPException(status_code=404, detail="Libro no encontrado")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
