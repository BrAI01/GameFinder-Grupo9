
from pathlib import Path

from catalogo import Catalogo
from modelos.videojuego import Videojuego
from servicios.reader import leer_videojuegos
from estructuras.arbol_binario import ArbolBinarioBusqueda
from estructuras.arbol_avl import ArbolAVL


RUTA_DATOS = Path(__file__).parent / "datos" / "videojuegos.json"


# Carga los videojuegos desde el archivo JSON
def cargar_catalogo():
    datos = leer_videojuegos(RUTA_DATOS)
    catalogo = Catalogo()
    arbol = ArbolBinarioBusqueda()
    arbol_avl = ArbolAVL()

    for dato in datos:
        videojuego = Videojuego(
            dato["titulo"],
            dato["genero"],
            dato["desarrollador"],
            dato["anio"],
            dato["rating"]
        )

        catalogo.agregar(videojuego)
        arbol.insertar(videojuego)
        arbol_avl.insertar(videojuego)

    return catalogo, arbol, arbol_avl


# Muestra una lista de videojuegos
def mostrar_lista(videojuegos):
    for videojuego in videojuegos:
        videojuego.mostrar()
        print("-----------------------")


def main():
    catalogo, arbol, arbol_avl = cargar_catalogo()

    # Ordenamos el catálogo para la búsqueda binaria
    catalogo.ordenar_por_titulo()

    while True:
        print("\n================================")
        print("          GAMEFINDER")
        print("================================")
        print("1. Buscar videojuego")
        print("2. Buscar videojuego con búsqueda binaria")
        print("3. Listar videojuegos")
        print("4. Filtrar por género")
        print("5. Buscar videojuego con árbol BST")
        print("6. Listar videojuegos ordenados con árbol BST")
        print("7. Buscar videojuego con árbol AVL")
        print("8. Listar videojuegos ordenados con árbol AVL")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        # Búsqueda secuencial
        if opcion == "1":
            titulo = input("\nIngrese el título: ")
            videojuego = catalogo.buscar_secuencial(titulo)

            if videojuego:
                print("\nVIDEOJUEGO ENCONTRADO")
                print("----------------------")
                videojuego.mostrar()
            else:
                print("\nNo se encontró el videojuego.")

        # Búsqueda binaria
        elif opcion == "2":
            titulo = input("\nIngrese el título: ")
            videojuego = catalogo.buscar_binaria(titulo)

            if videojuego:
                print("\nVIDEOJUEGO ENCONTRADO")
                print("----------------------")
                videojuego.mostrar()
            else:
                print("\nNo se encontró el videojuego.")

        # Listar videojuegos
        elif opcion == "3":
            print("\nCATÁLOGO DE VIDEOJUEGOS")
            print("------------------------")
            mostrar_lista(catalogo.listar())

        # Filtrar por género
        elif opcion == "4":
            genero = input("\nIngrese el género: ")
            resultados = catalogo.filtrar_por_genero(genero)

            if resultados:
                print("\nVIDEOJUEGOS ENCONTRADOS")
                print("-----------------------")
                mostrar_lista(resultados)
            else:
                print("\nNo se encontraron videojuegos.")

        # Búsqueda con árbol BST
        elif opcion == "5":
            titulo = input("\nIngrese el título: ")
            videojuego = arbol.buscar(titulo)

            if videojuego:
                print("\nVIDEOJUEGO ENCONTRADO CON ÁRBOL BST")
                print("-----------------------------------")
                videojuego.mostrar()
            else:
                print("\nNo se encontró el videojuego.")

        # Listar con árbol BST
        elif opcion == "6":
            print("\nVIDEOJUEGOS ORDENADOS CON ÁRBOL BST")
            print("------------------------------------")
            mostrar_lista(arbol.listar_ordenado())

        # Búsqueda con árbol AVL
        elif opcion == "7":
            titulo = input("\nIngrese el título: ")
            videojuego = arbol_avl.buscar(titulo)

            if videojuego:
                print("\nVIDEOJUEGO ENCONTRADO CON ÁRBOL AVL")
                print("-----------------------------------")
                videojuego.mostrar()
            else:
                print("\nNo se encontró el videojuego.")

        # Listar con árbol AVL
        elif opcion == "8":
            print("\nVIDEOJUEGOS ORDENADOS CON ÁRBOL AVL")
            print("------------------------------------")
            mostrar_lista(arbol_avl.listar_ordenado())

        # Salir
        elif opcion == "0":
            print("\nGracias por usar GameFinder.")
            break

        else:
            print("\nOpción inválida.")


if __name__ == "__main__":
    main()














