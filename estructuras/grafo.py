from collections import deque

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

    
    def recorrido_bfs(self, titulo_inicio):
        """Recorre los videojuegos por niveles usando BFS."""
        inicio = self._clave(titulo_inicio)

        if inicio not in self._vertices:
            return []

        visitados = {inicio}
        cola = deque([inicio])
        recorrido = []

        while cola:
            actual = cola.popleft()
            recorrido.append(self._vertices[actual])

            for vecino in self._adyacencia[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        return recorrido

    def recorrido_dfs(self, titulo_inicio):
        """Recorre los videojuegos en profundidad usando DFS."""
        inicio = self._clave(titulo_inicio)

        if inicio not in self._vertices:
            return []

        visitados = set()
        pila = [inicio]
        recorrido = []

        while pila:
            actual = pila.pop()

            if actual not in visitados:
                visitados.add(actual)
                recorrido.append(self._vertices[actual])

                vecinos = list(self._adyacencia[actual].keys())

                for vecino in reversed(vecinos):
                    if vecino not in visitados:
                        pila.append(vecino)

        return recorrido

    def camino_mas_corto_bfs(self, titulo_inicio, titulo_destino):
        """Encuentra el camino con menos aristas entre dos videojuegos."""
        inicio = self._clave(titulo_inicio)
        destino = self._clave(titulo_destino)

        if inicio not in self._vertices or destino not in self._vertices:
            return []

        visitados = {inicio}
        cola = deque([inicio])
        anteriores = {inicio: None}

        while cola:
            actual = cola.popleft()

            if actual == destino:
                camino = []
                while actual is not None:
                    camino.append(self._vertices[actual])
                    actual = anteriores[actual]

                return camino[::-1]

            for vecino in self._adyacencia[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    anteriores[vecino] = actual
                    cola.append(vecino)

        return []


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
