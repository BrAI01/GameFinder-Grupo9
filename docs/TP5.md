# TP5 - Árboles generales

## GameFinder - Sistema de recomendación de videojuegos

**Grupo 9**

## Objetivo

Representar una jerarquía natural del dominio de videojuegos mediante un árbol general o n-ario, agregar búsqueda y recorridos e integrarlo a la interfaz de terminal.

## Jerarquía utilizada

La jerarquía se genera con los datos existentes de `datos/videojuegos.json`:

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

La raíz representa el dominio completo. Cada género es hijo de la raíz y cada videojuego es hijo de su género.

## Implementación

El archivo `estructuras/arbol_general.py` contiene:

- `NodoGeneral`, que almacena un valor y una lista de hijos;
- `ArbolGeneral`, que administra la raíz y las operaciones del árbol;
- búsqueda por valor;
- recorrido preorden;
- recorrido por niveles.

El árbol se construye en `main.py` al cargar el catálogo, utilizando los géneros y títulos del archivo JSON.

## Recorridos

### Preorden

```text
Videojuegos
RPG
The Witcher 3
Skyrim
Acción
God of War
Sandbox
Minecraft
Deportes
FIFA 23
```

### Por niveles

```text
Videojuegos
RPG
Acción
Sandbox
Deportes
The Witcher 3
Skyrim
God of War
Minecraft
FIFA 23
```

## Integración en terminal

Se agregó la opción:

```text
9. Explorar categorías
```

Desde esa opción se puede:

- visualizar la jerarquía;
- buscar una categoría o un videojuego dentro del árbol;
- ejecutar el recorrido por niveles.

## Archivos del TP5

- `estructuras/arbol_general.py`
- `main.py`
- `datos/videojuegos.json`
- `docs/TP5.md`

## Ejecución

```bash
python main.py
```

El TP5 corresponde a la versión 3 de GameFinder.
