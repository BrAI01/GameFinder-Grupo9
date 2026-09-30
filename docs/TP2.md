# TP2 - Búsqueda y medición

**## GameFinder - Sistema de recomendación de videojuegos**

**Grupo 9**

**## Objetivo**

Implementar y comparar dos métodos de búsqueda para los videojuegos: búsqueda secuencial y búsqueda binaria.

**## Búsqueda**

- Búsqueda secuencial: recorre los elementos uno por uno. Complejidad **O(n)**.
- Búsqueda binaria: busca sobre un catálogo ordenado dividiendo el espacio de búsqueda. Complejidad **O(log n)**.

**## Mediciones**

Se creó `mediciones.py` para comparar ambos métodos utilizando catálogos de:

- 100 videojuegos.
- 1.000 videojuegos.
- 10.000 videojuegos.

Las mediciones se realizan utilizando `perf_counter()` de Python.

**## Archivos**

- `catalogo.py`
- `main.py`
- `mediciones.py`

**## Resultado**

Las mediciones permiten observar cómo cambia el tiempo de búsqueda a medida que aumenta la cantidad de videojuegos y comparar experimentalmente ambos algoritmos.