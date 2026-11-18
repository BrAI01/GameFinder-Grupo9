# GameFinder

Trabajo Práctico Integrador de Estructuras de Datos - TP8

Grupo 9

## Integrantes

- Braian Cabral
- Lautaro Agustín Penalba
- Gabriel Alejandro Kapala

## Descripción

GameFinder es una aplicación de terminal en Python para consultar un catálogo de videojuegos e incorporar progresivamente las estructuras de datos estudiadas en la materia.

Estado actual: **TP8 - versión 6**.

## Funcionalidades actuales

- búsqueda secuencial por título;
- búsqueda binaria por título;
- listado del catálogo;
- filtro por género;
- búsqueda y recorrido con Árbol Binario de Búsqueda (BST);
- búsqueda y recorrido con árbol AVL;
- exploración de categorías mediante árbol general o n-ario;
- ranking Top 5 mediante heap binaria por rating;
- recomendación de videojuegos relacionados mediante un grafo;
- recorridos BFS y DFS sobre el grafo;
- búsqueda del camino con menor cantidad de conexiones entre dos videojuegos mediante BFS.

## Estructuras implementadas

### TP2 - Búsquedas

- secuencial: O(n);
- binaria: O(log n) sobre el catálogo ordenado.

Las mediciones se encuentran en `mediciones.py` y `docs/TP2.md`.

### TP3 - Árbol Binario de Búsqueda

El BST organiza los videojuegos por título e implementa:

- inserción;
- búsqueda;
- recorrido inorden;
- recorrido preorden;
- recorrido postorden.

La comparación contra búsqueda secuencial se encuentra en `comparacion_bst.py`.

### TP4 - Árbol AVL

El AVL mantiene el árbol balanceado mediante rotaciones y conserva búsquedas e inserciones de complejidad O(log n) cuando mantiene el equilibrio.

### TP5 - Árbol general

Ejemplo de la jerarquía original de TP5 (el catálogo actual contiene más juegos):

```text
Videojuegos
├── RPG
│   ├── The Witcher 3
│   └── Skyrim
├── Acción
│   └── God of War
├── Sandbox
│   └── Minecraft
└── Deportes
    └── FIFA 23
```

Se integra mediante la opción `9. Explorar categorías`.

### TP6 - Heap binaria

Se utiliza una max-heap donde el `rating` define la prioridad. La opción `10. Ver TOP 5 videojuegos por rating` obtiene los videojuegos de mayor prioridad.

La implementación se encuentra en `estructuras/heap_binario.py` y las pruebas en `pruebas_heap.py`.

### TP7 - Grafos

Cada videojuego es un vértice y dos videojuegos se conectan con una arista cuando comparten género o desarrollador. El grafo es no dirigido y no pesado, y se representa con una lista de adyacencia porque es disperso.

Se integra mediante la opción `11. Explorar relaciones entre videojuegos`. El submenú permite mostrar videojuegos relacionados, verificar una conexión directa y mostrar el grafo completo.

La implementación se encuentra en `estructuras/grafo.py` y las pruebas en `pruebas_grafo.py`.

### TP8 - Recorridos BFS y DFS

Se incorporan dos recorridos sobre el grafo:

- **BFS (búsqueda en anchura):** recorre los videojuegos por niveles usando una cola FIFO. También se utiliza para encontrar el camino con menor cantidad de aristas entre dos videojuegos, ya que el grafo no tiene pesos.
- **DFS (búsqueda en profundidad):** explora una rama antes de retroceder, utilizando una pila.

Ambos recorridos tienen complejidad temporal **O(V + E)** y espacial **O(V)**, donde `V` es la cantidad de vértices y `E` la cantidad de aristas. Los métodos `recorrido_bfs`, `recorrido_dfs` y `camino_mas_corto_bfs` están implementados en `estructuras/grafo.py` y se acceden desde el submenú de la opción `11`.

## Estructura del repositorio

```text
GameFinder-Grupo9/
├── main.py
├── catalogo.py
├── mediciones.py
├── comparacion_bst.py
├── experimentos_avl.py
├── pruebas_heap.py
├── pruebas_grafo.py
├── modelos/
│   ├── __init__.py
│   └── videojuego.py
├── estructuras/
│   ├── __init__.py
│   ├── nodo.py
│   ├── arbol_binario.py
│   ├── arbol_avl.py
│   ├── arbol_general.py
│   ├── heap_binario.py
│   └── grafo.py
├── datos/
│   └── videojuegos.json
├── servicios/
│   ├── __init__.py
│   └── reader.py
├── docs/
│   ├── 01-requerimientos.md
│   ├── 02-casos-de-uso.md
│   ├── 03-diagrama-clases.md
│   ├── 04-diagrama-datos.md
│   ├── 05-gestion-proyecto.md
│   ├── TP0.md
│   ├── TP1.md
│   ├── TP2.md
│   ├── TP3.md
│   ├── TP4.md
│   ├── TP5.md
│   ├── TP6.md
│   ├── TP7.md
│   └── TP8.md
├── README.md
└── .gitignore
```

## Ejecución

Para ejecutar GameFinder:

```bash
python main.py
```

En algunos equipos puede ser necesario utilizar `py main.py` o `python3 main.py`.

Para ejecutar las mediciones del TP2:

```bash
python mediciones.py
```

Para comparar búsqueda secuencial y BST:

```bash
python comparacion_bst.py
```

Para comparar BST y AVL:

```bash
python experimentos_avl.py
```

Para probar la heap:

```bash
python pruebas_heap.py
```

Para probar el grafo:

```bash
python pruebas_grafo.py
```

## Documentación

- [Requerimientos](docs/01-requerimientos.md)
- [Casos de uso](docs/02-casos-de-uso.md)
- [Diagrama de clases](docs/03-diagrama-clases.md)
- [Diagrama de datos](docs/04-diagrama-datos.md)
- [Gestión del proyecto](docs/05-gestion-proyecto.md)
- [TP0](docs/TP0.md)
- [TP1](docs/TP1.md)
- [TP2](docs/TP2.md)
- [TP3](docs/TP3.md)
- [TP4](docs/TP4.md)
- [TP5](docs/TP5.md)
- [TP6](docs/TP6.md)
- [TP7](docs/TP7.md)
- [TP8](docs/TP8.md)
