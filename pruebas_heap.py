from pathlib import Path

from servicios.reader import leer_videojuegos
from modelos.videojuego import Videojuego
from estructuras.heap_binario import HeapBinario


def probar_heap_con_catalogo():
    ruta = Path(__file__).parent / "datos" / "videojuegos.json"
    datos = leer_videojuegos(ruta)

    videojuegos = [
        Videojuego(
            juego["titulo"],
            juego["genero"],
            juego["desarrollador"],
            juego["anio"],
            juego["rating"],
        )
        for juego in datos
    ]

    heap = HeapBinario()

    # Pruebas con el heap vacío.
    assert heap.esta_vacio()
    assert heap.extraer_maximo() is None
    assert heap.obtener_top_n(5) == []

    # Cargar los videojuegos del JSON.
    for videojuego in videojuegos:
        heap.insertar(videojuego)

    # Extraer todos en orden descendente.
    ranking = []
    while not heap.esta_vacio():
        ranking.append(heap.extraer_maximo())

    ratings = [j.rating for j in ranking]
    assert ratings == sorted(ratings, reverse=True)
    assert len(ranking) == len(videojuegos)

    print("TOP DE VIDEOJUEGOS POR RATING")
    print("-----------------------------")

    for posicion, videojuego in enumerate(ranking, start=1):
        print(
            f"{posicion}. {videojuego.titulo} "
            f"- Rating: {videojuego.rating}"
        )

    print("\nTodas las pruebas del heap pasaron correctamente.")


if __name__ == "__main__":
    probar_heap_con_catalogo()
