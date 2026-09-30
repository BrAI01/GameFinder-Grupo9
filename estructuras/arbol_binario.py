from estructuras.nodo import Nodo


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, videojuego):
        nuevo_nodo = Nodo(videojuego)

        if self.raiz is None:
            self.raiz = nuevo_nodo
            return

        actual = self.raiz

        while True:
            if videojuego.titulo.lower() < actual.videojuego.titulo.lower():

                if actual.izquierda is None:
                    actual.izquierda = nuevo_nodo
                    return

                actual = actual.izquierda

            else:

                if actual.derecha is None:
                    actual.derecha = nuevo_nodo
                    return

                actual = actual.derecha

    def buscar(self, titulo):
        actual = self.raiz

        while actual is not None:

            if titulo.lower() == actual.videojuego.titulo.lower():
                return actual.videojuego

            if titulo.lower() < actual.videojuego.titulo.lower():
                actual = actual.izquierda
            else:
                actual = actual.derecha

        return None

    def listar_ordenado(self):
        videojuegos = []
        self._inorden(self.raiz, videojuegos)
        return videojuegos

    def _inorden(self, nodo, videojuegos):

        if nodo is not None:
            self._inorden(nodo.izquierda, videojuegos)
            videojuegos.append(nodo.videojuego)
            self._inorden(nodo.derecha, videojuegos)