import statistics
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


def medir_busqueda(catalogo, titulo, repeticiones=500):
    tiempos_secuencial = []
    tiempos_binaria = []

    for _ in range(repeticiones):
        inicio = time.perf_counter_ns()
        catalogo.buscar_secuencial(titulo)
        tiempos_secuencial.append(time.perf_counter_ns() - inicio)

        inicio = time.perf_counter_ns()
        catalogo.buscar_binaria(titulo)
        tiempos_binaria.append(time.perf_counter_ns() - inicio)

    mediana_secuencial = statistics.median(tiempos_secuencial) / 1000
    mediana_binaria = statistics.median(tiempos_binaria) / 1000

    return mediana_secuencial, mediana_binaria


def ejecutar_mediciones():
    cantidades = [100, 1000, 10000]

    print("\n==============================================================")
    print("       MEDICIONES DE BÚSQUEDA - MEDIANA EN MICROSEGUNDOS")
    print("==============================================================")
    print(f"{'Elementos':>10} | {'Secuencial':>14} | {'Binaria':>14}")
    print("-" * 46)

    for cantidad in cantidades:
        catalogo = crear_catalogo(cantidad)
        titulo = f"Videojuego {cantidad - 1}"

        tiempo_secuencial, tiempo_binaria = medir_busqueda(
            catalogo,
            titulo
        )

        print(
            f"{cantidad:>10} | "
            f"{tiempo_secuencial:>11.3f} us | "
            f"{tiempo_binaria:>11.3f} us"
        )


if __name__ == "__main__":
    ejecutar_mediciones()
