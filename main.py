from pathlib import Path

from catalogo import Catalogo
from modelos.videojuego import Videojuego
from servicios.reader import leer_videojuegos


RUTA_DATOS = Path(__file__).parent / "datos" / "videojuegos.json"


def cargar_catalogo():
    datos = leer_videojuegos(RUTA_DATOS)
    catalogo = Catalogo()

    for dato in datos:
        videojuego = Videojuego(
            dato["titulo"],
            dato["genero"],
            dato["desarrollador"],
            dato["anio"],
            dato["rating"]
        )
        catalogo.agregar(videojuego)

    return catalogo


def mostrar_lista(videojuegos):
    for videojuego in videojuegos:
        videojuego.mostrar()
        print("-----------------------")


def main():
    catalogo = cargar_catalogo()

    while True:
        print("\n================================")
        print("          GAMEFINDER")
        print("================================")
        print("1. Buscar videojuego")
        print("2. Listar videojuegos")
        print("3. Filtrar por género")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            titulo = input("\nIngrese el título: ")
            videojuego = catalogo.buscar(titulo)

            if videojuego:
                print("\nVIDEOJUEGO ENCONTRADO")
                print("----------------------")
                videojuego.mostrar()
            else:
                print("\nNo se encontró el videojuego.")

        elif opcion == "2":
            print("\nCATÁLOGO DE VIDEOJUEGOS")
            print("------------------------")
            mostrar_lista(catalogo.listar())

        elif opcion == "3":
            genero = input("\nIngrese el género: ")
            resultados = catalogo.filtrar_por_genero(genero)

            if resultados:
                print("\nVIDEOJUEGOS ENCONTRADOS")
                print("-----------------------")
                mostrar_lista(resultados)
            else:
                print("\nNo se encontraron videojuegos.")

        elif opcion == "0":
            print("\nGracias por usar GameFinder.")
            break

        else:
            print("\nOpción inválida.")


if __name__ == "__main__":
    main()
