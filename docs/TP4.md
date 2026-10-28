# TP4 - Árbol AVL

## GameFinder - Sistema de recomendación de videojuegos

**Grupo 9**

## Objetivo

Implementar un árbol AVL para organizar y buscar los videojuegos del catálogo, manteniendo el equilibrio del árbol después de las inserciones.

## Árbol AVL

Se creó un árbol donde los videojuegos se organizan según su título.

- Títulos menores: subárbol izquierdo.
- Títulos mayores o iguales: subárbol derecho.

El árbol actualiza las alturas y calcula el factor de equilibrio de cada nodo. Cuando detecta un desequilibrio, realiza las rotaciones correspondientes para mantener el árbol balanceado.

## Rotaciones

Se implementaron los cuatro casos de rotación:

- Izquierda-izquierda.
- Derecha-derecha.
- Izquierda-derecha.
- Derecha-izquierda.

## Operaciones

- Inserción de videojuegos.
- Búsqueda por título.
- Recorrido inorden para listar los videojuegos ordenados alfabéticamente.
- Actualización de alturas.
- Cálculo del factor de equilibrio.
- Rotaciones para mantener el balance del árbol.

## Archivos

- `estructuras/arbol_avl.py`
- `main.py`
- `experimentos_avl.py`
- `datos/videojuegos.json`

## Experimentos

Se creó el archivo `experimentos_avl.py` para comparar la altura y las búsquedas de un BST y un AVL.

Los títulos se insertaron en orden alfabético y se realizaron pruebas con 100, 500 y 1000 videojuegos.

| Videojuegos | Altura BST | Altura AVL |
|---:|---:|---:|
| 100 | 100 | 7 |
| 500 | 500 | 9 |
| 1000 | 1000 | 10 |

También se compararon las búsquedas de distintos títulos para medir la cantidad de nodos visitados.

## Resultado

El árbol AVL fue integrado al sistema mediante las opciones 7 y 8 del menú principal. Se comprobó la búsqueda de **God of War** ingresando el título en minúsculas, y se verificó que el árbol encontrara correctamente el videojuego.

Los experimentos mostraron que el BST puede quedar desbalanceado al insertar títulos ordenados, mientras que el AVL mantiene una altura reducida mediante rotaciones.
