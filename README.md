# GameFinder

Trabajo Práctico Integrador de Estructuras de Datos - TP1  
Grupo 9

## Integrantes

- Braian Cabral
- Lautaro Agustín Penalba
- Gabriel Alejandro Kapala

## Descripción

GameFinder es un programa en Python para consultar un catálogo de videojuegos desde la terminal.

En esta entrega permite:

- buscar un videojuego por título;
- listar los videojuegos cargados;
- filtrar videojuegos por género.

Los datos se guardan en `datos/videojuegos.json` y se cargan mediante `servicios/reader.py`.

## Estructura

```text
GameFinder-Grupo9/
├── main.py
├── catalogo.py
├── modelos/
│   └── videojuego.py
├── datos/
│   └── videojuegos.json
├── servicios/
│   └── reader.py
├── docs/
│   └── TP0 GameFinder Grupo9.pdf
├── README.md
└── .gitignore
```

## Ejecución

Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
python main.py
```

En algunos equipos puede ser necesario usar `py main.py` o `python3 main.py`.
