# TP3 - Árbol Binario de Búsqueda

## GameFinder - Sistema de recomendación de videojuegos

**Grupo 9**

## Objetivo

Implementar un Árbol Binario de Búsqueda (BST) para organizar y buscar los videojuegos del catálogo, incorporar los recorridos pedidos y comparar la búsqueda en el árbol con la búsqueda secuencial del TP2.

## Árbol Binario de Búsqueda

Los videojuegos se organizan según su título:

- títulos menores: subárbol izquierdo;
- títulos mayores o iguales: subárbol derecho.

## Operaciones implementadas

- inserción de videojuegos;
- búsqueda por título;
- recorrido inorden;
- recorrido preorden;
- recorrido postorden.

Los tres recorridos se encuentran implementados en `estructuras/arbol_binario.py`.

## Recorridos

Con los videojuegos actuales del catálogo, el recorrido inorden permite obtener los títulos ordenados alfabéticamente:

`FIFA 23, God of War, Minecraft, Skyrim, The Witcher 3`

El preorden visita primero la raíz y luego los subárboles izquierdo y derecho. El postorden visita primero los subárboles y deja la raíz para el final.

## Comparación búsqueda secuencial vs. BST

El archivo `comparacion_bst.py` genera conjuntos de prueba y compara la cantidad de elementos o nodos visitados para encontrar el último título. Para evitar que el BST quede degenerado, los títulos se insertan en un orden que produce un árbol razonablemente equilibrado.

| Elementos | Búsqueda secuencial | Búsqueda BST |
| ---: | ---: | ---: |
| 100 | 100 comparaciones | 6 comparaciones |
| 1.000 | 1.000 comparaciones | 9 comparaciones |
| 10.000 | 10.000 comparaciones | 13 comparaciones |

## Análisis

La búsqueda secuencial puede necesitar recorrer todos los elementos, por lo que su complejidad es **O(n)**.

En un BST equilibrado, la búsqueda reduce el espacio de búsqueda en cada nivel y se aproxima a **O(log n)**. Sin embargo, si el árbol queda completamente desbalanceado, su peor caso también puede degradarse a **O(n)**.

## Archivos

- `estructuras/nodo.py`
- `estructuras/arbol_binario.py`
- `comparacion_bst.py`
- `main.py`
- `datos/videojuegos.json`

## Ejecución

Para ejecutar la comparación:

```bash
python comparacion_bst.py
```

## Resultado

El BST quedó integrado a GameFinder y cuenta con búsqueda, recorrido inorden, preorden y postorden. La comparación muestra la ventaja de un árbol razonablemente equilibrado frente a una búsqueda secuencial cuando aumenta la cantidad de elementos.
