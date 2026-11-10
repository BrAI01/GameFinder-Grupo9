from pathlib import Path

from servicios.reader import leer_videojuegos
from modelos.videojuego import Videojuego
from estructuras.grafo import GrafoVideojuegos, construir_grafo


def cargar_videojuegos():
    ruta = Path(__file__).parent / "datos" / "videojuegos.json"
    datos = leer_videojuegos(ruta)

    return [
        Videojuego(
            juego["titulo"],
            juego["genero"],
            juego["desarrollador"],
            juego["anio"],
            juego["rating"],
        )
        for juego in datos
    ]


def probar_grafo_vacio():
    grafo = GrafoVideojuegos()

    assert grafo.cantidad_vertices() == 0
    assert grafo.cantidad_aristas() == 0
    assert grafo.obtener_vecinos("Minecraft") is None
    assert not grafo.estan_conectados("Minecraft", "Terraria")


def probar_operaciones_basicas():
    grafo = GrafoVideojuegos()
    minecraft = Videojuego("Minecraft", "Sandbox", "Mojang", 2011, 9.0)
    terraria = Videojuego("Terraria", "Sandbox", "Re-Logic", 2011, 8.9)

    assert grafo.agregar_vertice(minecraft)
    assert grafo.agregar_vertice(terraria)
    # No se duplican vértices.
    assert not grafo.agregar_vertice(minecraft)

    assert grafo.agregar_arista("Minecraft", "Terraria")
    # No se duplican aristas ni se permiten lazos.
    assert not grafo.agregar_arista("Terraria", "Minecraft")
    assert not grafo.agregar_arista("Minecraft", "Minecraft")
    # No se conectan vértices inexistentes.
    assert not grafo.agregar_arista("Minecraft", "Juego inexistente")

    # Grafo no dirigido: la relación vale en ambos sentidos.
    assert grafo.estan_conectados("Minecraft", "Terraria")
    assert grafo.estan_conectados("terraria", "  MINECRAFT ")
    assert grafo.cantidad_aristas() == 1

    vecinos = grafo.obtener_vecinos("Minecraft")
    vecinos.clear()
    assert grafo.estan_conectados("Minecraft", "Terraria")


def probar_grafo_con_catalogo():
    videojuegos = cargar_videojuegos()
    grafo = construir_grafo(videojuegos)

    assert grafo.cantidad_vertices() == len(videojuegos)
    assert grafo.cantidad_aristas() == 21

    # Mismo género (RPG).
    assert grafo.estan_conectados("The Witcher 3", "Skyrim")
    # Mismo desarrollador aunque distinto género (FromSoftware: RPG y Acción).
    assert grafo.estan_conectados("Elden Ring", "Dark Souls III")
    # Ni mismo género ni mismo desarrollador.
    assert not grafo.estan_conectados("Minecraft", "FIFA 23")

    # Simetría: si A está en los vecinos de B, B está en los vecinos de A.
    for videojuego in videojuegos:
        for vecino in grafo.obtener_vecinos(videojuego.titulo):
            assert grafo.estan_conectados(vecino.titulo, videojuego.titulo)

    print("GRAFO DE VIDEOJUEGOS")
    print("--------------------")
    print(
        f"Vértices: {grafo.cantidad_vertices()} - "
        f"Aristas: {grafo.cantidad_aristas()}\n"
    )

    for titulo, vecinos in grafo.lista_adyacencia():
        print(f"{titulo} -> {', '.join(vecinos)}")


if __name__ == "__main__":
    probar_grafo_vacio()
    probar_operaciones_basicas()
    probar_grafo_con_catalogo()
    print("\nTodas las pruebas del grafo pasaron correctamente.")
