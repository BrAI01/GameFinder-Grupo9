# GameFinder

Trabajo Práctico Integrador de Estructuras de Datos - TP6

Grupo 9

## Integrantes

- Braian Cabral
- Lautaro Agustín Penalba
- Gabriel Alejandro Kapala

## Descripción

GameFinder es una aplicación de terminal en Python para consultar un catálogo de videojuegos e incorporar progresivamente las estructuras de datos estudiadas en la materia.

Estado actual: **TP6 - versión 4**.

## Funcionalidades actuales

- búsqueda secuencial por título;
- búsqueda binaria por título;
- listado del catálogo;
- filtro por género;
- búsqueda y recorrido con Árbol Binario de Búsqueda (BST);
- búsqueda y recorrido con árbol AVL;
- exploración de categorías mediante árbol general o n-ario;
- ranking Top 5 mediante heap binaria por rating.

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

La jerarquía utilizada es:

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

## Estructura del repositorio

```text
GameFinder-Grupo9/
├── main.py
├── catalogo.py
├── mediciones.py
├── comparacion_bst.py
├── experimentos_avl.py
├── pruebas_heap.py
├── modelos/
│   ├── __init__.py
│   └── videojuego.py
├── estructuras/
│   ├── __init__.py
│   ├── nodo.py
│   ├── arbol_binario.py
│   ├── arbol_avl.py
│   ├── arbol_general.py
│   └── heap_binario.py
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
│   └── TP6.md
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
