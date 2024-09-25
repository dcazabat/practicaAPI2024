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
URL: http://127.0.0.1:8000/libro/{id}