# GameFinder

Trabajo Práctico Integrador de Estructuras de Datos - TP3

Grupo 9

## Integrantes

* Braian Cabral
* Lautaro Agustín Penalba
* Gabriel Alejandro Kapala

## Descripción

GameFinder es un programa en Python para consultar un catálogo de videojuegos desde la terminal.

En esta entrega permite:

* buscar un videojuego mediante búsqueda secuencial;
* buscar un videojuego mediante búsqueda binaria;
* buscar un videojuego mediante un Árbol Binario de Búsqueda (BST);
* listar los videojuegos cargados;
* filtrar videojuegos por género;
* listar los videojuegos ordenados mediante el árbol BST.

Los datos se guardan en `datos/videojuegos.json` y se cargan mediante `servicios/reader.py`.

## Búsquedas

La búsqueda secuencial tiene una complejidad O(n).

La búsqueda binaria tiene una complejidad O(log n) y requiere que los videojuegos estén ordenados por título.

El Árbol Binario de Búsqueda organiza los videojuegos según su título y permite realizar búsquedas recorriendo el árbol.

También se implementó un recorrido inorden para obtener los videojuegos ordenados alfabéticamente.

## Estructura

```text
GameFinder-Grupo9/

├── main.py
├── catalogo.py
├── mediciones.py
├── modelos/
│   ├── __init__.py
│   └── videojuego.py
├── estructuras/
│   ├── __init__.py
│   ├── nodo.py
│   └── arbol_binario.py
├── datos/
│   └── videojuegos.json
├── servicios/
│   ├── __init__.py
│   └── reader.py
├── docs/
│   ├── TP0.md
│   ├── TP1.md
│   ├── TP2.md
│   └── TP3.md
├── README.md
└── .gitignore
```

## Ejecución

Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
python main.py
```

Desde el menú se pueden realizar las búsquedas y utilizar el Árbol Binario de Búsqueda.

Para realizar las mediciones:

```bash
python mediciones.py
```
