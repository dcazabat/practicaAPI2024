from fastapi import FastAPI, HTTPException, Depends
from uuid import UUID
from sqlalchemy.orm import Session
from libro.dto import CreateLibroDTO, UpdateLibroDTO, DeleteLibroDTO, LibroDTO
from libro.service import (
    getLibros, 
    getLibro, 
    createLibro, 
    updateLibro, 
    deleteLibro
)
from config.cnx import get_db

app = FastAPI()

# Ruta para obtener todos los libros activos
@app.get("/libros/", response_model=list[LibroDTO])
def leer_libros(db: Session = Depends(get_db)):
    libros = getLibros()
    if not libros:
        raise HTTPException(status_code=404, detail="No se encontraron libros.")
    return libros

# Ruta para obtener un libro específico por su ID
@app.get("/libros/{libro_id}", response_model=LibroDTO)
def leer_libro(libro_id: UUID, db: Session = Depends(get_db)):
    libro = getLibro(libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado.")
    return libro

# Ruta para crear un nuevo libro
@app.post("/libros/", response_model=LibroDTO)
def crear_libro(libro: CreateLibroDTO, db: Session = Depends(get_db)):
    nuevo_libro = createLibro(libro)
    if not nuevo_libro:
        raise HTTPException(status_code=400, detail="Error al crear el libro.")
    return nuevo_libro

# Ruta para actualizar un libro existente por su ID
@app.put("/libros/{libro_id}", response_model=LibroDTO)
def actualizar_libro(libro_id: UUID, libro_actualizado: UpdateLibroDTO, db: Session = Depends(get_db)):
    libro = updateLibro(libro_actualizado, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado o no se pudo actualizar.")
    return libro

# Ruta para eliminar un libro (borrado lógico) por su ID
@app.delete("/libros/{libro_id}", response_model=LibroDTO)
def eliminar_libro(libro_id: UUID, db: Session = Depends(get_db)):
    libro_borrar = DeleteLibroDTO(id=libro_id, deleted=True)
    libro_eliminado = deleteLibro(libro_borrar)
    if not libro_eliminado:
        raise HTTPException(status_code=404, detail="Libro no encontrado o no se pudo eliminar.")
    return libro_eliminado
