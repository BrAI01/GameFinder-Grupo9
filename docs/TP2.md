# TP2 - Búsqueda y medición

## GameFinder - Sistema de recomendación de videojuegos

**Grupo 9**

## Objetivo

Implementar y comparar dos métodos de búsqueda para los videojuegos: búsqueda secuencial y búsqueda binaria.

## Estrategias

- **Búsqueda secuencial:** recorre los elementos uno por uno. Complejidad **O(n)**.
- **Búsqueda binaria:** trabaja sobre el catálogo ordenado y reduce el espacio de búsqueda en cada paso. Complejidad **O(log n)**.

## Metodología

El archivo `mediciones.py` genera catálogos de 100, 1.000 y 10.000 videojuegos y busca un título ubicado hacia el final del conjunto.

Para reducir el ruido propio de mediciones muy pequeñas, cada búsqueda se ejecuta 500 veces con `perf_counter_ns()` y se informa la mediana en microsegundos.

## Resultados de referencia

Los tiempos pueden variar según el equipo, pero una ejecución de referencia produjo:

| Elementos | Búsqueda secuencial | Búsqueda binaria |
| ---: | ---: | ---: |
| 100 | 5,3 us | 1,1 us |
| 1.000 | 51,4 us | 1,8 us |
| 10.000 | 559,5 us | 3,3 us |

## Análisis

Al aumentar la cantidad de elementos, el tiempo de la búsqueda secuencial crece de forma marcada porque puede tener que revisar el catálogo completo.

La búsqueda binaria aumenta mucho más lentamente porque en cada comparación descarta aproximadamente la mitad de los elementos restantes. Para poder utilizarla, el catálogo debe estar previamente ordenado por título.

## Conclusión técnica

Para búsquedas repetidas por título sobre un catálogo ordenado, la búsqueda binaria es la estrategia más conveniente de las dos analizadas, especialmente cuando aumenta el tamaño del conjunto.

La búsqueda secuencial sigue siendo útil cuando el conjunto es pequeño o no está ordenado, pero su costo en el peor caso es lineal.

## Archivos

- `catalogo.py`
- `main.py`
- `mediciones.py`

## Ejecución

```bash
python mediciones.py
```
