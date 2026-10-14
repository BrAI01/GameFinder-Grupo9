# TP4 - Árbol AVL y comparación con BST

## GameFinder - Sistema de recomendación de videojuegos

**Grupo 9**

## Objetivo

Implementar un árbol AVL para mantener el catálogo balanceado automáticamente y comparar su comportamiento con el Árbol Binario de Búsqueda (BST) implementado en el TP3.

## Problema del BST desbalanceado

Un BST puede funcionar bien cuando las inserciones quedan distribuidas entre los subárboles izquierdo y derecho. Sin embargo, si los elementos se insertan ya ordenados, el árbol puede degenerarse y comportarse de forma similar a una lista enlazada.

En ese peor caso, la altura del BST puede crecer hasta `n` y las operaciones de búsqueda e inserción pueden degradarse a **O(n)**.

## Árbol AVL

El AVL mantiene el árbol balanceado después de cada inserción. Para hacerlo, cada nodo conserva su altura y se calcula el factor de equilibrio:

`altura(subárbol izquierdo) - altura(subárbol derecho)`

Cuando el factor queda fuera del rango `[-1, 1]`, se realizan rotaciones para recuperar el equilibrio.

Se implementaron los cuatro casos clásicos:

- izquierda-izquierda: rotación simple a la derecha;
- derecha-derecha: rotación simple a la izquierda;
- izquierda-derecha: rotación izquierda y luego derecha;
- derecha-izquierda: rotación derecha y luego izquierda.

Gracias al balance, la altura del AVL se mantiene proporcional a `log n`, por lo que la búsqueda y la inserción tienen complejidad **O(log n)**.

## Integración en GameFinder

El archivo `estructuras/arbol_avl.py` implementa el árbol AVL.

El AVL se carga junto con el catálogo y el BST desde `main.py`. Desde el menú se puede:

- buscar un videojuego mediante el árbol AVL;
- listar los videojuegos ordenados mediante recorrido inorden del AVL.

## Experimento BST vs. AVL

El archivo `experimentos_avl.py` genera títulos en orden ascendente. Esto produce un caso desfavorable para el BST porque cada nuevo elemento queda a la derecha del anterior.

Se probaron árboles con 100, 500 y 1.000 videojuegos. Para cada tamaño se comparó:

- altura del BST;
- altura del AVL;
- cantidad de comparaciones necesarias para encontrar el primer elemento;
- cantidad de comparaciones necesarias para encontrar un elemento intermedio;
- cantidad de comparaciones necesarias para encontrar el último elemento.

## Resultados

| Elementos | Altura BST | Altura AVL | Búsqueda | Comparaciones BST | Comparaciones AVL |
| ---: | ---: | ---: | --- | ---: | ---: |
| 100 | 100 | 7 | Juego 0001 | 1 | 7 |
| 100 | 100 | 7 | Juego 0050 | 50 | 6 |
| 100 | 100 | 7 | Juego 0100 | 100 | 7 |
| 500 | 500 | 9 | Juego 0001 | 1 | 9 |
| 500 | 500 | 9 | Juego 0250 | 250 | 8 |
| 500 | 500 | 9 | Juego 0500 | 500 | 9 |
| 1000 | 1000 | 10 | Juego 0001 | 1 | 10 |
| 1000 | 1000 | 10 | Juego 0500 | 500 | 8 |
| 1000 | 1000 | 10 | Juego 1000 | 1000 | 10 |

## Análisis

La diferencia se observa claramente en la altura de los árboles. Con inserciones ordenadas, el BST alcanza una altura igual a la cantidad de elementos: 100, 500 y 1.000 niveles respectivamente.

El AVL, en cambio, mantiene alturas de 7, 9 y 10 niveles para esos mismos tamaños. Esto reduce de forma muy importante la cantidad máxima de comparaciones necesarias para encontrar un elemento.

El primer elemento es un caso particular favorable al BST porque quedó como raíz. Sin embargo, a medida que se buscan elementos más alejados de la raíz, el costo del BST crece linealmente. En el AVL, las búsquedas se mantienen cercanas a la altura logarítmica del árbol.

## Complejidad

### BST desbalanceado

- búsqueda: O(n);
- inserción: O(n).

### AVL

- búsqueda: O(log n);
- inserción: O(log n).

El recorrido completo de cualquiera de los dos árboles sigue siendo O(n), porque para listar todos los elementos es necesario visitar todos los nodos.

## Conclusión

El experimento muestra por qué el balanceo es importante. Un BST sin mecanismo de balance puede perder su ventaja cuando recibe datos ordenados y degradarse hasta un comportamiento lineal.

El AVL agrega el costo de mantener alturas y realizar rotaciones, pero a cambio conserva una altura cercana a `log n`. Para GameFinder, esto permite que las búsquedas sigan siendo eficientes incluso cuando el orden de inserción de los videojuegos es desfavorable.

## Archivos utilizados

- `estructuras/arbol_avl.py`
- `estructuras/arbol_binario.py`
- `experimentos_avl.py`
- `main.py`

## Ejecución

Para ejecutar GameFinder:

```bash
python main.py
```

Para reproducir la comparación entre BST y AVL:

```bash
python experimentos_avl.py
```
