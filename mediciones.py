import time

from catalogo import Catalogo
from modelos.videojuego import Videojuego


def crear_catalogo(cantidad):
    catalogo = Catalogo()

    for i in range(cantidad):
        videojuego = Videojuego(
            f"Videojuego {i}",
            "Acción",
            "Desarrollador",
            2020,
            8.0
        )

        catalogo.agregar(videojuego)

    catalogo.ordenar_por_titulo()

    return catalogo


def medir_busqueda(catalogo, titulo):

    inicio = time.perf_counter()
    catalogo.buscar_secuencial(titulo)
    fin = time.perf_counter()

    tiempo_secuencial = fin - inicio

    inicio = time.perf_counter()
    catalogo.buscar_binaria(titulo)
    fin = time.perf_counter()

    tiempo_binaria = fin - inicio

    return tiempo_secuencial, tiempo_binaria


def ejecutar_mediciones():

    cantidades = [100, 1000, 10000]

    print("\n========================================")
    print("       MEDICIONES DE BÚSQUEDA")
    print("========================================")

    for cantidad in cantidades:

        catalogo = crear_catalogo(cantidad)

        titulo = f"Videojuego {cantidad - 1}"

        tiempo_secuencial, tiempo_binaria = medir_busqueda(
            catalogo,
            titulo
        )

        print(f"\nCantidad de elementos: {cantidad}")
        print(f"Búsqueda secuencial: {tiempo_secuencial:.10f} segundos")
        print(f"Búsqueda binaria:    {tiempo_binaria:.10f} segundos")


if __name__ == "__main__":
    ejecutar_mediciones()