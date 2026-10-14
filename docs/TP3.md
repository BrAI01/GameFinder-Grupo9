# TP3 - Árbol Binario de Búsqueda

## GameFinder - Sistema de recomendación de videojuegos

**Grupo 9**

## Objetivo

Implementar un Árbol Binario de Búsqueda (BST) para organizar y buscar los videojuegos del catálogo.

## Árbol Binario de Búsqueda

Se creó un árbol donde los videojuegos se organizan según su título.

* Títulos menores: subárbol izquierdo.
* Títulos mayores o iguales: subárbol derecho.

La búsqueda permite encontrar un videojuego recorriendo el árbol según el orden de los títulos.

## Operaciones

* Inserción de videojuegos.
* Búsqueda por título.
* Recorrido inorden para listar los videojuegos ordenados alfabéticamente.

## Archivos

* `estructuras/nodo.py`
* `estructuras/arbol_binario.py`
* `main.py`
* `datos/videojuegos.json`

## Resultado

El árbol fue integrado al sistema y probado con los videojuegos del archivo `videojuegos.json`. Se comprobó la búsqueda de **God of War** y **Minecraft**, y el recorrido inorden mostró correctamente: **FIFA 23, God of War, Minecraft, Skyrim y The Witcher 3**.
