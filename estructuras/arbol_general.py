from collections import deque


class NodoGeneral:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)


class ArbolGeneral:
    def __init__(self, valor_raiz):
        self.raiz = NodoGeneral(valor_raiz)

    def buscar(self, valor):
        objetivo = str(valor).strip().lower()
        cola = deque([self.raiz])

        while cola:
            nodo = cola.popleft()

            if str(nodo.valor).strip().lower() == objetivo:
                return nodo

            cola.extend(nodo.hijos)

        return None

    def agregar_hijo(self, valor_padre, valor_hijo):
        padre = self.buscar(valor_padre)

        if padre is None:
            return False

        padre.agregar_hijo(NodoGeneral(valor_hijo))
        return True

    def recorrer_preorden(self):
        resultado = []
        self._preorden(self.raiz, 0, resultado)
        return resultado

    def _preorden(self, nodo, nivel, resultado):
        resultado.append((nodo.valor, nivel))

        for hijo in nodo.hijos:
            self._preorden(hijo, nivel + 1, resultado)

    def recorrer_por_niveles(self):
        resultado = []
        cola = deque([self.raiz])

        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)
            cola.extend(nodo.hijos)

        return resultado
