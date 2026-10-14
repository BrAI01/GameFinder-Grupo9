# GameFinder

Trabajo Práctico Integrador de Estructuras de Datos - TP4

Grupo 9

## Integrantes

- Braian Cabral
- Lautaro Agustín Penalba
- Gabriel Alejandro Kapala

## Descripción

GameFinder es un programa en Python para consultar un catálogo de videojuegos desde la terminal y aplicar progresivamente las estructuras de datos estudiadas en la materia.

En el estado actual permite:

- buscar un videojuego mediante búsqueda secuencial;
- buscar un videojuego mediante búsqueda binaria;
- buscar un videojuego mediante un Árbol Binario de Búsqueda (BST);
- buscar un videojuego mediante un árbol AVL;
- listar los videojuegos cargados;
- filtrar videojuegos por género;
- listar los videojuegos ordenados mediante recorrido inorden del BST;
- listar los videojuegos ordenados mediante recorrido inorden del AVL;
- comparar experimentalmente el comportamiento de BST y AVL.

Los datos se guardan en `datos/videojuegos.json` y se cargan mediante `servicios/reader.py`.

## Estructuras implementadas

### Búsqueda secuencial

En el peor caso recorre todos los elementos del catálogo.

Complejidad: **O(n)**.

### Búsqueda binaria

Trabaja sobre el catálogo ordenado y reduce aproximadamente a la mitad el espacio de búsqueda en cada paso.

Complejidad: **O(log n)**.

### Árbol Binario de Búsqueda (BST)

Organiza los videojuegos según el título. Permite inserción, búsqueda y recorrido inorden.

En un árbol razonablemente equilibrado puede ofrecer búsquedas eficientes, pero con inserciones ordenadas puede degenerarse y alcanzar complejidad **O(n)**.

### Árbol AVL

Es un árbol binario de búsqueda autoequilibrado. Después de las inserciones calcula alturas y factores de equilibrio y aplica rotaciones cuando es necesario.

Esto mantiene la altura proporcional a `log n` y permite búsquedas e inserciones de complejidad **O(log n)**.

## TP4 - Comparación BST vs. AVL

El archivo `experimentos_avl.py` inserta videojuegos en orden alfabético para producir un caso desfavorable para el BST y compara:

- altura del BST;
- altura del AVL;
- cantidad de comparaciones en distintas búsquedas.

Con 1.000 elementos insertados en orden, el BST alcanza una altura de 1.000, mientras el AVL mantiene una altura de 10.

La documentación completa del experimento y sus resultados se encuentra en [`docs/TP4.md`](docs/TP4.md).

## Estructura

```text
GameFinder-Grupo9/
├── main.py
├── catalogo.py
├── mediciones.py
├── experimentos_avl.py
├── modelos/
│   ├── __init__.py
│   └── videojuego.py
├── estructuras/
│   ├── __init__.py
│   ├── nodo.py
│   ├── arbol_binario.py
│   └── arbol_avl.py
├── datos/
│   └── videojuegos.json
├── servicios/
│   ├── __init__.py
│   └── reader.py
├── docs/
│   ├── TP0.md
│   ├── TP1.md
│   ├── TP2.md
│   ├── TP3.md
│   └── TP4.md
├── README.md
└── .gitignore
```

## Ejecución

Para ejecutar GameFinder:

```bash
python main.py
```

En algunos equipos puede ser necesario usar `py main.py` o `python3 main.py`.

Para ejecutar las mediciones del TP2:

```bash
python mediciones.py
```

Para ejecutar la comparación del TP4:

```bash
python experimentos_avl.py
```

## Documentación

- [TP0 - Propuesta inicial](docs/TP0.md)
- [TP1 - Implementación inicial](docs/TP1.md)
- [TP2 - Búsqueda y medición](docs/TP2.md)
- [TP3 - Árbol Binario de Búsqueda](docs/TP3.md)
- [TP4 - Árbol AVL y comparación con BST](docs/TP4.md)
