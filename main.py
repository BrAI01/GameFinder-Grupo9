from pathlib import Path

from catalogo import Catalogo
from modelos.videojuego import Videojuego
from servicios.reader import leer_videojuegos
from estructuras.arbol_binario import ArbolBinarioBusqueda
from estructuras.arbol_avl import ArbolAVL
from estructuras.arbol_general import ArbolGeneral


RUTA_DATOS = Path(__file__).parent / "datos" / "videojuegos.json"


def cargar_catalogo():
    datos = leer_videojuegos(RUTA_DATOS)
    catalogo = Catalogo()
    arbol = ArbolBinarioBusqueda()
    arbol_avl = ArbolAVL()
    arbol_categorias = ArbolGeneral("Videojuegos")

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

        genero = dato["genero"]

        if arbol_categorias.buscar(genero) is None:
            arbol_categorias.agregar_hijo("Videojuegos", genero)

        arbol_categorias.agregar_hijo(genero, dato["titulo"])

    return catalogo, arbol, arbol_avl, arbol_categorias


def mostrar_lista(videojuegos):
    for videojuego in videojuegos:
        videojuego.mostrar()
        print("-----------------------")


def explorar_categorias(arbol_categorias):
    while True:
        print("\n================================")
        print("       EXPLORAR CATEGORÍAS")
        print("================================")
        print("1. Ver jerarquía")
        print("2. Buscar categoría o videojuego")
        print("3. Ver recorrido por niveles")
        print("0. Volver")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            print("\nJERARQUÍA DE VIDEOJUEGOS")
            print("------------------------")

            for valor, nivel in arbol_categorias.recorrer_preorden():
                print(f"{'  ' * nivel}- {valor}")

        elif opcion == "2":
            valor = input("\nIngrese una categoría o videojuego: ")
            nodo = arbol_categorias.buscar(valor)

            if nodo:
                print(f"\nEncontrado: {nodo.valor}")

                if nodo.hijos:
                    print("Contiene:")
                    for hijo in nodo.hijos:
                        print(f"- {hijo.valor}")
            else:
                print("\nNo se encontró la categoría o videojuego.")

        elif opcion == "3":
            recorrido = arbol_categorias.recorrer_por_niveles()
            print("\nRECORRIDO POR NIVELES")
            print("----------------------")
            print(" -> ".join(recorrido))

        elif opcion == "0":
            break

        else:
            print("\nOpción inválida.")


def main():
    catalogo, arbol, arbol_avl, arbol_categorias = cargar_catalogo()

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
        print("9. Explorar categorías")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            titulo = input("\nIngrese el título: ")
            videojuego = catalogo.buscar_secuencial(titulo)

            if videojuego:
                print("\nVIDEOJUEGO ENCONTRADO")
                print("----------------------")
                videojuego.mostrar()
            else:
                print("\nNo se encontró el videojuego.")

        elif opcion == "2":
            titulo = input("\nIngrese el título: ")
            videojuego = catalogo.buscar_binaria(titulo)

            if videojuego:
                print("\nVIDEOJUEGO ENCONTRADO")
                print("----------------------")
                videojuego.mostrar()
            else:
                print("\nNo se encontró el videojuego.")

        elif opcion == "3":
            print("\nCATÁLOGO DE VIDEOJUEGOS")
            print("------------------------")
            mostrar_lista(catalogo.listar())

        elif opcion == "4":
            genero = input("\nIngrese el género: ")
            resultados = catalogo.filtrar_por_genero(genero)

            if resultados:
                print("\nVIDEOJUEGOS ENCONTRADOS")
                print("-----------------------")
                mostrar_lista(resultados)
            else:
                print("\nNo se encontraron videojuegos.")

        elif opcion == "5":
            titulo = input("\nIngrese el título: ")
            videojuego = arbol.buscar(titulo)

            if videojuego:
                print("\nVIDEOJUEGO ENCONTRADO CON ÁRBOL BST")
                print("-----------------------------------")
                videojuego.mostrar()
            else:
                print("\nNo se encontró el videojuego.")

        elif opcion == "6":
            print("\nVIDEOJUEGOS ORDENADOS CON ÁRBOL BST")
            print("------------------------------------")
            mostrar_lista(arbol.listar_ordenado())

        elif opcion == "7":
            titulo = input("\nIngrese el título: ")
            videojuego = arbol_avl.buscar(titulo)

            if videojuego:
                print("\nVIDEOJUEGO ENCONTRADO CON ÁRBOL AVL")
                print("-----------------------------------")
                videojuego.mostrar()
            else:
                print("\nNo se encontró el videojuego.")

        elif opcion == "8":
            print("\nVIDEOJUEGOS ORDENADOS CON ÁRBOL AVL")
            print("------------------------------------")
            mostrar_lista(arbol_avl.listar_ordenado())

        elif opcion == "9":
            explorar_categorias(arbol_categorias)

        elif opcion == "0":
            print("\nGracias por usar GameFinder.")
            break

        else:
            print("\nOpción inválida.")


if __name__ == "__main__":
    main()
