# TP1 - Implementación inicial

**## GameFinder - Sistema de recomendación de videojuegos**

**Grupo 9**

**## Objetivo**

Implementar la primera versión funcional de GameFinder utilizando Python, programación orientada a objetos y archivos JSON para almacenar los videojuegos.

**## Funcionalidades**

- Buscar un videojuego por título.
- Listar videojuegos.
- Filtrar videojuegos por género.
- Cargar los datos desde un archivo JSON.

**## Implementación**

Se creó la clase `Videojuego` para representar cada elemento del catálogo y la clase `Catalogo` para administrar los videojuegos.

También se incorporó un lector para cargar los datos desde `videojuegos.json`.

**## Archivos**

- `main.py`
- `catalogo.py`
- `modelos/videojuego.py`
- `servicios/reader.py`
- `datos/videojuegos.json`

**## Resultado**

Se desarrolló una aplicación de terminal funcional que permite consultar y filtrar el catálogo de videojuegos.