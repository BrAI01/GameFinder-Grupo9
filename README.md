# GameFinder

Trabajo Práctico Integrador de Estructuras de Datos - TP4

Grupo 9

## Integrantes

- Braian Cabral
- Lautaro Agustín Penalba
- Gabriel Alejandro Kapala

## Descripción

GameFinder es un programa en Python para consultar un catálogo de videojuegos desde la terminal.

En esta entrega permite:

- buscar un videojuego mediante búsqueda secuencial;
- buscar un videojuego mediante búsqueda binaria;
- buscar un videojuego mediante un Árbol Binario de Búsqueda (BST);
- listar los videojuegos cargados;
- filtrar videojuegos por género;
- listar los videojuegos ordenados mediante el árbol BST;
- buscar un videojuego mediante un árbol AVL;
- listar los videojuegos ordenados mediante el árbol AVL.

Los datos se guardan en `datos/videojuegos.json` y se cargan mediante `servicios/reader.py`.

## Búsquedas

La búsqueda secuencial tiene una complejidad O(n).

La búsqueda binaria tiene una complejidad O(log n) y requiere que los videojuegos estén ordenados por título.

El Árbol Binario de Búsqueda organiza los videojuegos según su título y permite realizar búsquedas recorriendo el árbol.

El árbol AVL mantiene el equilibrio mediante rotaciones, lo que permite realizar búsquedas e inserciones con una complejidad O(log n).

Los recorridos inorden permiten obtener los videojuegos ordenados alfabéticamente.

## Experimentos

Se realizaron pruebas comparando el BST y el AVL con títulos insertados en orden alfabético.

| Videojuegos | Altura BST | Altura AVL |
|---:|---:|---:|
| 100 | 100 | 7 |
| 500 | 500 | 9 |
| 1000 | 1000 | 10 |

Los resultados muestran que el BST puede quedar desbalanceado cuando se insertan títulos ordenados, mientras que el AVL mantiene una altura reducida.

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

Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
python main.py
```

Desde el menú se pueden realizar las búsquedas y utilizar los árboles BST y AVL.

Para realizar las mediciones de búsqueda secuencial y binaria:

```bash
python mediciones.py
```

Para comparar el BST y el AVL:

```bash
python experimentos_avl.py
```

