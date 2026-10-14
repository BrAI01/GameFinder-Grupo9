
from estructuras.arbol_binario import ArbolBinarioBusqueda
from estructuras.arbol_avl import ArbolAVL
from modelos.videojuego import Videojuego


def crear_videojuego(titulo):
    return Videojuego(
        titulo,
        "Prueba",
        "Desarrollador",
        2020,
        8.0
    )


def calcular_altura(raiz):
    if raiz is None:
        return 0

    altura = 0
    nivel = [raiz]

    while nivel:
        siguiente_nivel = []

        for nodo in nivel:
            if nodo.izquierda is not None:
                siguiente_nivel.append(nodo.izquierda)

            if nodo.derecha is not None:
                siguiente_nivel.append(nodo.derecha)

        altura += 1
        nivel = siguiente_nivel

    return altura


def contar_comparaciones(raiz, titulo):
    actual = raiz
    comparaciones = 0
    titulo = titulo.strip().lower()

    while actual is not None:
        comparaciones += 1
        titulo_actual = actual.videojuego.titulo.strip().lower()

        if titulo == titulo_actual:
            return comparaciones

        if titulo < titulo_actual:
            actual = actual.izquierda
        else:
            actual = actual.derecha

    return comparaciones


def ejecutar_experimento(cantidad):
    bst = ArbolBinarioBusqueda()
    avl = ArbolAVL()

    for numero in range(1, cantidad + 1):
        titulo = f"Juego {numero:04d}"
        videojuego = crear_videojuego(titulo)

        bst.insertar(videojuego)
        avl.insertar(videojuego)

    altura_bst = calcular_altura(bst.raiz)
    altura_avl = calcular_altura(avl.raiz)

    print(f"\nCantidad de videojuegos: {cantidad}")
    print(f"BST - Altura: {altura_bst}")
    print(f"AVL - Altura: {altura_avl}")

    titulos_a_probar = [
        "Juego 0001",
        f"Juego {cantidad // 2:04d}",
        f"Juego {cantidad:04d}"
    ]

    for titulo in titulos_a_probar:
        comparaciones_bst = contar_comparaciones(
            bst.raiz, titulo
        )
        comparaciones_avl = contar_comparaciones(
            avl.raiz, titulo
        )

        assert bst.buscar(titulo) is not None
        assert avl.buscar(titulo) is not None

        print(f"\nBúsqueda de {titulo}:")
        print(f"BST - Comparaciones: {comparaciones_bst}")
        print(f"AVL - Comparaciones: {comparaciones_avl}")


def main():
    print("COMPARACIÓN ENTRE BST Y AVL")
    print("===========================")
    print("Inserción de títulos en orden alfabético")

    for cantidad in [100, 500, 1000]:
        ejecutar_experimento(cantidad)

    print("\nExperimentos finalizados correctamente.")


if __name__ == "__main__":
    main()
