from modelos.videojuego import Videojuego
from catalogo import Catalogo
from estructuras.arbol_binario import ArbolBinarioBusqueda


def crear_videojuego(titulo):
    return Videojuego(titulo, "Prueba", "Desarrollador", 2020, 8.0)


def orden_balanceado(titulos):
    if not titulos:
        return []

    medio = len(titulos) // 2
    return (
        [titulos[medio]]
        + orden_balanceado(titulos[:medio])
        + orden_balanceado(titulos[medio + 1:])
    )


def comparaciones_secuencial(catalogo, titulo):
    objetivo = titulo.strip().lower()
    comparaciones = 0

    for videojuego in catalogo.listar():
        comparaciones += 1
        if videojuego.titulo.strip().lower() == objetivo:
            break

    return comparaciones


def comparaciones_bst(arbol, titulo):
    objetivo = titulo.strip().lower()
    actual = arbol.raiz
    comparaciones = 0

    while actual is not None:
        comparaciones += 1
        titulo_actual = actual.videojuego.titulo.strip().lower()

        if objetivo == titulo_actual:
            break

        if objetivo < titulo_actual:
            actual = actual.izquierda
        else:
            actual = actual.derecha

    return comparaciones


def ejecutar_comparacion(cantidad):
    titulos = [f"Juego {i:05d}" for i in range(1, cantidad + 1)]
    catalogo = Catalogo()
    arbol = ArbolBinarioBusqueda()

    for titulo in titulos:
        catalogo.agregar(crear_videojuego(titulo))

    for titulo in orden_balanceado(titulos):
        arbol.insertar(crear_videojuego(titulo))

    objetivo = titulos[-1]

    secuencial = comparaciones_secuencial(catalogo, objetivo)
    bst = comparaciones_bst(arbol, objetivo)

    print(
        f"{cantidad:>6} elementos | "
        f"Secuencial: {secuencial:>6} comparaciones | "
        f"BST: {bst:>3} comparaciones"
    )


if __name__ == "__main__":
    print("COMPARACIÓN BÚSQUEDA SECUENCIAL VS BST")
    print("=======================================")

    for cantidad in [100, 1000, 10000]:
        ejecutar_comparacion(cantidad)
