# Alumnos de 2do año ISFDyT
# Trabajo Práctico: Implementación de una API con FastAPI y SQLite

## Objetivo
Implementar una API RESTful utilizando FastAPI, conectada a una base de datos SQLite mediante SQLAlchemy, permitiendo realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una entidad específica.

## Descripción
Se te solicita crear una API que gestione una base de datos para almacenar información sobre **Libros**. La API debe ser capaz de realizar las siguientes operaciones:
- Crear un nuevo libro.
- Obtener la lista de todos los libros.
- Obtener los detalles de un libro específico por su ID.
- Actualizar la información de un libro.
- Eliminar un libro.

## Requisitos
### 1. Entidad `Libro`:
La base de datos debe almacenar la siguiente información sobre los libros:
- `id` (UUID): Identificador único del libro.
- `titulo` (String): Título del libro.
- `autor` (String): Autor del libro.
- `publicado_en` (Date): Fecha de publicación del libro.
- `isbn` (String): Código ISBN del libro.

### 2. Base de datos:
- Usa **SQLite** como base de datos.
- Usa **SQLAlchemy** para definir el modelo y realizar las operaciones CRUD.

### 3. Endpoints:
1. **POST /libros/**: Crea un nuevo libro.
    - Recibe un objeto JSON con los datos del libro.
    - Devuelve el libro creado con su ID asignado.
    
2. **GET /libros/**: Devuelve la lista de todos los libros almacenados en la base de datos.

3. **GET /libros/{id}**: Devuelve la información de un libro específico según su ID.
    
4. **PUT /libros/{id}**: Actualiza los datos de un libro específico.
    - Recibe un objeto JSON con los datos actualizados del libro.
    - Devuelve el libro actualizado.

5. **DELETE /libros/{id}**: Elimina un libro según su ID.
    - Devuelve un mensaje confirmando la eliminación.

## Entregables:
- Código fuente de la API. en una rama de este repositorio creda a partir de "main" con su apellido y nombre
- Se debera realizar "commit" paso a paso, como minimo 10, por ejemplo (Creacion de Entidad, DTO, Rutas, Servicios)
- Instrucciones para ejecutar la API y la base de datos.
- Ejemplo de uso de cada uno de los endpoints con **Postman**

---
