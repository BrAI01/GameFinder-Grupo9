# GameFinder

Trabajo Práctico Integrador de Estructuras de Datos - TP5

Grupo 9

## Integrantes

- Braian Cabral
- Lautaro Agustín Penalba
- Gabriel Alejandro Kapala

## Descripción

GameFinder es un programa en Python para consultar un catálogo de videojuegos desde la terminal y aplicar progresivamente las estructuras de datos estudiadas en la materia.

Estado actual: **TP5 - versión 3**.

En esta versión se mantienen las funcionalidades de las entregas anteriores y se incorpora un árbol general para organizar los videojuegos por categorías.

## TP5 - Árbol general

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

El árbol general permite:

- buscar categorías o videojuegos;
- recorrer la jerarquía en preorden;
- recorrerla por niveles;
- explorar las categorías desde la terminal.

La opción `9. Explorar categorías` integra esta estructura al programa.

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
│   ├── arbol_avl.py
│   └── arbol_general.py
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
│   ├── TP4.md
│   └── TP5.md
├── README.md
└── .gitignore
```

## Ejecución

```bash
python main.py
```

En algunos equipos puede ser necesario usar `py main.py` o `python3 main.py`.

## Documentación

- [TP0 - Propuesta inicial](docs/TP0.md)
- [TP1 - Implementación inicial](docs/TP1.md)
- [TP2 - Búsqueda y medición](docs/TP2.md)
- [TP3 - Árbol Binario de Búsqueda](docs/TP3.md)
- [TP4 - Árbol AVL y comparación con BST](docs/TP4.md)
- [TP5 - Árboles generales](docs/TP5.md)
