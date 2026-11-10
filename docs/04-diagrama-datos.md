# 04 - Diagrama de datos

## GameFinder

**Grupo 9**

Los datos persistentes se almacenan en `datos/videojuegos.json`.

```mermaid
erDiagram
    VIDEOJUEGO {
        string titulo
        string genero
        string desarrollador
        int anio
        float rating
    }
```

## Estructura del archivo JSON

Cada elemento representa un videojuego con la siguiente forma:

```json
{
  "titulo": "The Witcher 3",
  "genero": "RPG",
  "desarrollador": "CD Projekt Red",
  "anio": 2015,
  "rating": 9.8
}
```

## Uso de los datos

- `servicios/reader.py` lee el archivo JSON.
- `main.py` transforma cada registro en un objeto `Videojuego`.
- `Catalogo` almacena los objetos para búsquedas y filtros.
- BST y AVL organizan los videojuegos por título.
- El árbol general organiza géneros y títulos jerárquicamente.
- La heap utiliza el rating como prioridad para construir el Top-N.


## Conexión entre estructuras

```mermaid
flowchart TD
    JSON[Archivo videojuegos.json] --> LEER[reader.py]
    LEER --> OBJ[Objetos Videojuego]
    OBJ --> CAT[Catálogo: búsquedas y filtros]
    OBJ --> BST[BST por título]
    OBJ --> AVL[AVL por título]
    OBJ --> NAR[Árbol general: géneros]
    CAT --> HEAP[Heap: ranking por rating]
    CAT --> GRAFO[Grafo: género o desarrollador]
    CAT --> MENU[main.py - terminal]
    BST --> MENU
    AVL --> MENU
    NAR --> MENU
    HEAP --> MENU
    GRAFO --> MENU
```
