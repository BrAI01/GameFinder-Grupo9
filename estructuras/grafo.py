class GrafoVideojuegos:
    """Grafo no dirigido de videojuegos, representado por adyacencias."""

    def __init__(self):
        self._vertices = {}
        self._adyacencia = {}

    @staticmethod
    def _clave(titulo):
        return str(titulo).strip().lower()

    def agregar_vertice(self, videojuego):
        clave = self._clave(videojuego.titulo)
        if clave in self._vertices:
            return False
        self._vertices[clave] = videojuego
        self._adyacencia[clave] = {}
        return True

    def agregar_arista(self, titulo_a, titulo_b):
        a = self._clave(titulo_a)
        b = self._clave(titulo_b)
        if a == b or a not in self._vertices or b not in self._vertices:
            return False
        if b in self._adyacencia[a]:
            return False
        self._adyacencia[a][b] = self._vertices[b]
        self._adyacencia[b][a] = self._vertices[a]
        return True

    def obtener_vertice(self, titulo):
        return self._vertices.get(self._clave(titulo))

    def obtener_vecinos(self, titulo):
        clave = self._clave(titulo)
        if clave not in self._adyacencia:
            return None
        return list(self._adyacencia[clave].values())

    def estan_conectados(self, titulo_a, titulo_b):
        a = self._clave(titulo_a)
        b = self._clave(titulo_b)
        return a in self._adyacencia and b in self._adyacencia[a]

    def cantidad_vertices(self):
        return len(self._vertices)

    def cantidad_aristas(self):
        return sum(len(vecinos) for vecinos in self._adyacencia.values()) // 2

    def lista_adyacencia(self):
        return [
            (self._vertices[clave].titulo, [vecino.titulo for vecino in vecinos.values()])
            for clave, vecinos in self._adyacencia.items()
        ]


def son_similares(a, b):
    return (
        a.genero.strip().lower() == b.genero.strip().lower()
        or a.desarrollador.strip().lower() == b.desarrollador.strip().lower()
    )


def construir_grafo(videojuegos, criterio=son_similares):
    grafo = GrafoVideojuegos()
    for juego in videojuegos:
        grafo.agregar_vertice(juego)

    for i, juego in enumerate(videojuegos):
        for otro in videojuegos[i + 1:]:
            if criterio(juego, otro):
                grafo.agregar_arista(juego.titulo, otro.titulo)
    return grafo
