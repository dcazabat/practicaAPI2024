from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from libros.config.cnx import get_db
from .crud import crear_libro, obtener_libros, obtener_libro, actualizar_libro, eliminar_libro

router = APIRouter()

@router.post("/libros/")
def crear_libro_endpoint(titulo: str, autor: str, publicado_en, isbn: str, db: Session = Depends(get_db)):
    return crear_libro(db, titulo=titulo, autor=autor, publicado_en=publicado_en, isbn=isbn)

@router.get("/libros/")
def obtener_libros_endpoint(db: Session = Depends(get_db)):
    return obtener_libros(db)

@router.get("/libros/{libro_id}")
def obtener_libro_endpoint(libro_id: str, db: Session = Depends(get_db)):
    libro = obtener_libro(db, libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro

@router.put("/libros/{libro_id}")
def actualizar_libro_endpoint(libro_id: str, titulo: str = None, autor: str = None, publicado_en = None, isbn: str = None, db: Session = Depends(get_db)):
    return actualizar_libro(db, libro_id, titulo=titulo, autor=autor, publicado_en=publicado_en, isbn=isbn)

@router.delete("/libros/{libro_id}")
def eliminar_libro_endpoint(libro_id: str, db: Session = Depends(get_db)):
    libro = eliminar_libro(db, libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"detalle": "Libro eliminado exitosamente"}
