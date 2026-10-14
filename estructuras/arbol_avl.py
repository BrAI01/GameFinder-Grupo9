
class NodoAVL:
    def __init__(self, videojuego):
        self.videojuego = videojuego
        self.izquierda = None
        self.derecha = None
        self.altura = 1


class ArbolAVL:

    def __init__(self):
        self.raiz = None

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def _actualizar_altura(self, nodo):
        nodo.altura = 1 + max(
            self._altura(nodo.izquierda),
            self._altura(nodo.derecha)
        )

    def _factor_equilibrio(self, nodo):
        if nodo is None:
            return 0

        return (
            self._altura(nodo.izquierda)
            - self._altura(nodo.derecha)
        )

    def _rotar_derecha(self, y):
        x = y.izquierda
        subarbol = x.derecha

        x.derecha = y
        y.izquierda = subarbol

        self._actualizar_altura(y)
        self._actualizar_altura(x)

        return x

    def _rotar_izquierda(self, x):
        y = x.derecha
        subarbol = y.izquierda

        y.izquierda = x
        x.derecha = subarbol

        self._actualizar_altura(x)
        self._actualizar_altura(y)

        return y

    def insertar(self, videojuego):
        self.raiz = self._insertar(self.raiz, videojuego)

    def _insertar(self, nodo, videojuego):
        if nodo is None:
            return NodoAVL(videojuego)

        titulo_nuevo = videojuego.titulo.strip().lower()
        titulo_actual = nodo.videojuego.titulo.strip().lower()

        if titulo_nuevo < titulo_actual:
            nodo.izquierda = self._insertar(
                nodo.izquierda, videojuego
            )
        else:
            nodo.derecha = self._insertar(
                nodo.derecha, videojuego
            )

        self._actualizar_altura(nodo)

        equilibrio = self._factor_equilibrio(nodo)

        # Caso izquierda-izquierda
        if equilibrio > 1 and titulo_nuevo < nodo.izquierda.videojuego.titulo.strip().lower():
            return self._rotar_derecha(nodo)

        # Caso derecha-derecha
        if equilibrio < -1 and titulo_nuevo >= nodo.derecha.videojuego.titulo.strip().lower():
            return self._rotar_izquierda(nodo)

        # Caso izquierda-derecha
        if equilibrio > 1 and titulo_nuevo >= nodo.izquierda.videojuego.titulo.strip().lower():
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)

        # Caso derecha-izquierda
        if equilibrio < -1 and titulo_nuevo < nodo.derecha.videojuego.titulo.strip().lower():
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    def buscar(self, titulo):
        titulo = titulo.strip().lower()
        actual = self.raiz

        while actual is not None:
            titulo_actual = actual.videojuego.titulo.strip().lower()

            if titulo == titulo_actual:
                return actual.videojuego

            if titulo < titulo_actual:
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
