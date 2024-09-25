Ejemplos de uso de cada uno de los métodos con POSTMAN.

1- Obtener todos los libros (GET)
URL: http://127.0.0.1:8000/libros/
Ejemplo de Respuesta: [
  {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "titulo": "Don Quijote de la Mancha",
    "autor": "Miguel de Cervantes",
    "publicado_en": "1605-01-16",
    "isbn": "978-3-16-148410-0"
  },
  {
    "id": "987e6543-a21b-43d7-a654-426614174111",
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "publicado_en": "1967-05-30",
    "isbn": "978-0-14-310647-0"
  }
]

2- Obtener un libro por UUID (GET)
URL: http://127.0.0.1:8000/libros/{id}
Ejemplo de respuesta: {
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "titulo": "Don Quijote de la Mancha",
  "autor": "Miguel de Cervantes",
  "publicado_en": "1605-01-16",
  "isbn": "978-3-16-148410-0"
}

3- Crear un nuevo libro (POST)
URL: http://127.0.0.1:8000/libros/
Body: Selecciona raw y JSON en Postman.
Ejemplo de solicitud: {
  "titulo": "1984",
  "autor": "George Orwell",
  "publicado_en": "1949-06-08",
  "isbn": "978-0-452-28423-4"
}

4- Actualizar un libro (PUT)
URL: http://127.0.0.1:8000/libros/{id}
Body: Selecciona raw y JSON en Postman.
Ejemplo de solicitud: {
  "titulo": "Animal Farm",
  "autor": "George Orwell",
  "publicado_en": "1945-08-17",
  "isbn": "978-0-452-28423-4"
}
Ejemplo de respuesta: {
  "id": "98ae12cd-8f4b-4a9f-b88d-6d89dfad4b3a",
  "titulo": "Animal Farm",
  "autor": "George Orwell",
  "publicado_en": "1945-08-17",
  "isbn": "978-0-452-28423-4"
}

5- Eliminar un libro (DELETE)
URL: http://127.0.0.1:8000/libros/{id}
Ejemplo de Respuesta: {
  "message": "Libro eliminado correctamente."
}
