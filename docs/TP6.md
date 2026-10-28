# TP6 - Heap binario y ranking Top-N

## GameFinder - Sistema de recomendación de videojuegos

**Grupo 9**

## Objetivo

Implementar manualmente una heap binaria para priorizar videojuegos y obtener un ranking Top-N integrado a GameFinder.

## Prioridad elegida

La prioridad se define por el `rating` del videojuego:

- mayor rating = mayor prioridad;
- se utiliza una **max-heap**;
- el videojuego con mayor rating queda en la raíz.

## Implementación

El archivo `estructuras/heap_binario.py` implementa la estructura sin utilizar `heapq` ni otra heap de la biblioteca estándar.

Operaciones principales:

- `insertar(videojuego)`;
- `_subir(indice)` para restaurar la propiedad de la heap después de una inserción;
- `extraer_maximo()`;
- `_bajar(indice)` para restaurar la propiedad de la heap después de una extracción;
- `obtener_top_n(cantidad)`.

## Complejidad

- inserción: **O(log n)**;
- extracción del máximo: **O(log n)**;
- consultar si está vacía: **O(1)**;
- obtener Top-N luego de cargar la heap: **O(k log n)** para extraer `k` elementos.

En esta implementación la heap se construye insertando los elementos uno por uno, por lo que cargar `n` videojuegos tiene un costo de **O(n log n)**.

## ¿Por qué usar una heap en lugar de ordenar todo?

El objetivo del TP6 es trabajar con prioridades y obtener los elementos de mayor prioridad. Una heap permite mantener esa prioridad mientras se agregan elementos y extraer el máximo en O(log n), sin necesitar reordenar toda la colección cada vez que se incorpora un videojuego.

Para GameFinder esto resulta adecuado para un ranking dinámico: si se agregan nuevos videojuegos, pueden incorporarse a la heap en O(log n) y luego extraerse los mejores según el rating.

Ordenar toda la lista también puede resolver un ranking estático, pero obliga a producir un orden total de todos los elementos. La heap está orientada directamente al problema de prioridad y Top-N.

## Integración en GameFinder

En `main.py` se agregó la opción:

```text
10. Ver TOP 5 videojuegos por rating
```

Al seleccionar esa opción se construye una max-heap con los videojuegos del catálogo y se extraen hasta cinco elementos en orden descendente de rating.

Con el catálogo actual, el ranking esperado comienza con los videojuegos de mayor rating y finaliza con los de menor rating dentro del Top 5.

## Pruebas

El archivo `pruebas_heap.py` verifica:

- comportamiento de una heap vacía;
- inserción de todos los videojuegos del JSON;
- extracción de elementos;
- orden descendente de los ratings;
- que se extraiga la misma cantidad de videojuegos que se cargó.

## Archivos del TP6

- `estructuras/heap_binario.py`
- `pruebas_heap.py`
- `main.py`
- `datos/videojuegos.json`
- `docs/TP6.md`

## Ejecución

Para ejecutar GameFinder:

```bash
python main.py
```

Para ejecutar las pruebas de la heap:

```bash
python pruebas_heap.py
```

El TP6 corresponde a la versión 4 de GameFinder.
