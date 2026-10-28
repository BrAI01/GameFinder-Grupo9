
class HeapBinario:
    def __init__(self):
        self._elementos = []

    def esta_vacio(self):
        return len(self._elementos) == 0

    def insertar(self, videojuego):
        self._elementos.append(videojuego)
        self._subir(len(self._elementos) - 1)

    def _subir(self, indice):
        while indice > 0:
            padre = (indice - 1) // 2

            if self._elementos[indice].rating <= self._elementos[padre].rating:
                break

            self._elementos[indice], self._elementos[padre] = (
                self._elementos[padre],
                self._elementos[indice],
            )

            indice = padre

    def extraer_maximo(self):
        if self.esta_vacio():
            return None

        if len(self._elementos) == 1:
            return self._elementos.pop()

        maximo = self._elementos[0]
        self._elementos[0] = self._elementos.pop()
        self._bajar(0)

        return maximo

    def _bajar(self, indice):
        cantidad = len(self._elementos)

        while True:
            izquierdo = 2 * indice + 1
            derecho = 2 * indice + 2
            mayor = indice

            if (
                izquierdo < cantidad
                and self._elementos[izquierdo].rating
                > self._elementos[mayor].rating
            ):
                mayor = izquierdo

            if (
                derecho < cantidad
                and self._elementos[derecho].rating
                > self._elementos[mayor].rating
            ):
                mayor = derecho

            if mayor == indice:
                break

            self._elementos[indice], self._elementos[mayor] = (
                self._elementos[mayor],
                self._elementos[indice],
            )

            indice = mayor

    def obtener_top_n(self, cantidad):
        if cantidad <= 0:
            return []

        resultado = []
        limite = min(cantidad, len(self._elementos))

        for _ in range(limite):
            resultado.append(self.extraer_maximo())

        return resultado
