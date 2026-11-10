class GrafoVideojuegos:
    """Grafo no dirigido y no pesado de videojuegos.

    - Vértice: un videojuego (se guarda una referencia al mismo objeto
      Videojuego que usan las demás estructuras).
    - Arista: dos videojuegos están conectados si son similares, es decir,
      si comparten género o desarrollador.
    - Representación: lista de adyacencia mediante un diccionario donde la
      clave es el título normalizado y el valor es la lista de vecinos.
    """

    def __init__(self):
        # titulo normalizado -> objeto Videojuego
        self._vertices = {}
        # titulo normalizado -> lista de objetos Videojuego vecinos
        self._adyacencia = {}

    @staticmethod
    def _clave(titulo):
        return str(titulo).strip().lower()

    # Agrega un vértice - O(1)
    def agregar_vertice(self, videojuego):
        clave = self._clave(videojuego.titulo)

        if clave in self._vertices:
            return False

        self._vertices[clave] = videojuego
        self._adyacencia[clave] = []
        return True

    # Agrega una arista no dirigida entre dos videojuegos - O(grado)
    def agregar_arista(self, titulo_a, titulo_b):
        clave_a = self._clave(titulo_a)
        clave_b = self._clave(titulo_b)

        if clave_a == clave_b:
            return False

        if clave_a not in self._vertices or clave_b not in self._vertices:
            return False

        if self.estan_conectados(clave_a, clave_b):
            return False

        # Como el grafo es no dirigido, la arista se guarda en ambos sentidos.
        self._adyacencia[clave_a].append(self._vertices[clave_b])
        self._adyacencia[clave_b].append(self._vertices[clave_a])
        return True

    # Devuelve el videojuego asociado a un título - O(1)
    def obtener_vertice(self, titulo):
        return self._vertices.get(self._clave(titulo))

    # Devuelve los videojuegos relacionados (vecinos) - O(1) acceso, O(grado) copia
    def obtener_vecinos(self, titulo):
        clave = self._clave(titulo)

        if clave not in self._adyacencia:
            return None

        return self._adyacencia[clave].copy()

    # Verifica si dos videojuegos están conectados - O(grado)
    def estan_conectados(self, titulo_a, titulo_b):
        clave_a = self._clave(titulo_a)
        clave_b = self._clave(titulo_b)

        if clave_a not in self._adyacencia:
            return False

        for vecino in self._adyacencia[clave_a]:
            if self._clave(vecino.titulo) == clave_b:
                return True

        return False

    def cantidad_vertices(self):
        return len(self._vertices)

    def cantidad_aristas(self):
        # Cada arista aparece dos veces en la lista de adyacencia.
        return sum(len(vecinos) for vecinos in self._adyacencia.values()) // 2

    # Devuelve la lista de adyacencia completa - O(V + E)
    def lista_adyacencia(self):
        resultado = []

        for clave, vecinos in self._adyacencia.items():
            titulo = self._vertices[clave].titulo
            resultado.append((titulo, [vecino.titulo for vecino in vecinos]))

        return resultado


def son_similares(videojuego_a, videojuego_b):
    """Criterio de arista: mismo género o mismo desarrollador."""
    mismo_genero = (
        videojuego_a.genero.strip().lower() == videojuego_b.genero.strip().lower()
    )
    mismo_desarrollador = (
        videojuego_a.desarrollador.strip().lower()
        == videojuego_b.desarrollador.strip().lower()
    )
    return mismo_genero or mismo_desarrollador


def construir_grafo(videojuegos, criterio=son_similares):
    """Construye el grafo comparando cada par de videojuegos - O(n^2).

    El criterio se recibe como parámetro para poder cambiar la definición
    de "similar" sin modificar la estructura del grafo.
    """
    grafo = GrafoVideojuegos()

    for videojuego in videojuegos:
        grafo.agregar_vertice(videojuego)

    for i in range(len(videojuegos)):
        for j in range(i + 1, len(videojuegos)):
            if criterio(videojuegos[i], videojuegos[j]):
                grafo.agregar_arista(videojuegos[i].titulo, videojuegos[j].titulo)

    return grafo
