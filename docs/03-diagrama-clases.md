# 03 - Diagrama de clases

## GameFinder

**Grupo 9**

```mermaid
classDiagram
    class Videojuego {
        -titulo
        -genero
        -desarrollador
        -anio
        -rating
        +mostrar()
    }

    class Catalogo {
        -videojuegos
        +agregar(videojuego)
        +listar()
        +ordenar_por_titulo()
        +buscar_secuencial(titulo)
        +buscar_binaria(titulo)
        +filtrar_por_genero(genero)
    }

    class Nodo {
        +videojuego
        +izquierda
        +derecha
    }

    class ArbolBinarioBusqueda {
        +raiz
        +insertar(videojuego)
        +buscar(titulo)
        +listar_ordenado()
        +listar_preorden()
        +listar_postorden()
    }

    class ArbolAVL {
        +raiz
        +insertar(videojuego)
        +buscar(titulo)
        +listar_ordenado()
    }

    class NodoGeneral {
        +valor
        +hijos
        +agregar_hijo(nodo)
    }

    class ArbolGeneral {
        +raiz
        +buscar(valor)
        +agregar_hijo(padre, hijo)
        +recorrer_preorden()
        +recorrer_por_niveles()
    }

    class HeapBinario {
        -elementos
        +esta_vacio()
        +insertar(videojuego)
        +extraer_maximo()
        +obtener_top_n(cantidad)
    }

    Catalogo "1" o-- "*" Videojuego
    ArbolBinarioBusqueda o-- Nodo
    Nodo --> Videojuego
    ArbolAVL --> Videojuego
    ArbolGeneral o-- NodoGeneral
    HeapBinario --> Videojuego
```

## Descripción

`Videojuego` representa la entidad principal. `Catalogo` administra la colección base. Las estructuras BST, AVL, árbol general y heap utilizan esos datos para resolver los distintos requerimientos de cada etapa del trabajo práctico.
