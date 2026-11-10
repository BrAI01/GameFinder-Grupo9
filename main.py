from pathlib import Path

from catalogo import Catalogo
from modelos.videojuego import Videojuego
from servicios.reader import leer_videojuegos
from estructuras.arbol_binario import ArbolBinarioBusqueda
from estructuras.arbol_avl import ArbolAVL
from estructuras.arbol_general import ArbolGeneral
from estructuras.heap_binario import HeapBinario
from estructuras.grafo import construir_grafo


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

    grafo = construir_grafo(catalogo.listar())

    return catalogo, arbol, arbol_avl, arbol_categorias, grafo



def mostrar_lista(videojuegos):
    if not videojuegos:
        print("No se encontraron videojuegos.")
        return

    for videojuego in videojuegos:
        videojuego.mostrar()


def mostrar_top_videojuegos(catalogo, cantidad=5):
    heap = HeapBinario()

    for videojuego in catalogo.listar():
        heap.insertar(videojuego)

    ranking = heap.obtener_top_n(cantidad)

    print(f"\nTOP {len(ranking)} VIDEOJUEGOS POR RATING")
    print("-----------------------------------")

    if not ranking:
        print("No hay videojuegos en el catálogo.")
        return

    for posicion, videojuego in enumerate(ranking, start=1):
        print(f"{posicion}. {videojuego.titulo} - Rating: {videojuego.rating}")



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


def explorar_relaciones(grafo):
    while True:
        print("\n================================")
        print("   RELACIONES ENTRE VIDEOJUEGOS")
        print("================================")
        print("1. Ver videojuegos relacionados")
        print("2. Verificar si dos videojuegos están relacionados")
        print("3. Ver grafo completo (lista de adyacencia)")
        print("0. Volver")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            titulo = input("\nIngrese el título: ")
            videojuego = grafo.obtener_vertice(titulo)

            if videojuego is None:
                print("\nNo se encontró el videojuego.")
                continue

            vecinos = grafo.obtener_vecinos(titulo)
            print(f"\nSi te gustó {videojuego.titulo}, quizás te interesen:")
            print("------------------------------------------")

            if not vecinos:
                print("No hay videojuegos relacionados.")

            for vecino in vecinos:
                print(
                    f"- {vecino.titulo} ({vecino.genero}, "
                    f"{vecino.desarrollador}) - Rating: {vecino.rating}"
                )

        elif opcion == "2":
            titulo_a = input("\nPrimer videojuego: ")
            titulo_b = input("Segundo videojuego: ")

            if grafo.obtener_vertice(titulo_a) is None or grafo.obtener_vertice(titulo_b) is None:
                print("\nAlguno de los videojuegos no existe en el catálogo.")
            elif grafo.estan_conectados(titulo_a, titulo_b):
                print("\nSí, están relacionados (comparten género o desarrollador).")
            else:
                print("\nNo están relacionados directamente.")

        elif opcion == "3":
            print("\nGRAFO DE VIDEOJUEGOS")
            print("--------------------")
            print(f"Vértices: {grafo.cantidad_vertices()} - Aristas: {grafo.cantidad_aristas()}\n")

            for titulo, vecinos in grafo.lista_adyacencia():
                print(f"{titulo} -> {', '.join(vecinos) if vecinos else '(sin relaciones)'}")

        elif opcion == "0":
            break

        else:
            print("\nOpción inválida.")


def main():
    catalogo, arbol, arbol_avl, arbol_categorias, grafo = cargar_catalogo()

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
        print("10. Ver TOP 5 videojuegos por rating")
        print("11. Explorar relaciones entre videojuegos")
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

        elif opcion == "10":
            mostrar_top_videojuegos(catalogo)

        elif opcion == "11":
            explorar_relaciones(grafo)

        elif opcion == "0":
            print("\nGracias por usar GameFinder.")
            break

        else:
            print("\nOpción inválida.")


if __name__ == "__main__":
    main()
