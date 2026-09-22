class Catalogo:

    def __init__(self):
        self._videojuegos = []

    # Agrega un videojuego al catálogo
    def agregar(self, videojuego):
        self._videojuegos.append(videojuego)

    # Devuelve la lista de videojuegos
    def listar(self):
        return self._videojuegos.copy()

    # Ordena los videojuegos por título
    def ordenar_por_titulo(self):
        self._videojuegos.sort(
            key=lambda videojuego: videojuego.titulo.strip().lower()
        )

    # Búsqueda secuencial - O(n)
    def buscar_secuencial(self, titulo):
        titulo = titulo.strip().lower()

        for videojuego in self._videojuegos:
            if videojuego.titulo.lower() == titulo:
                return videojuego

        return None

    # Búsqueda binaria - O(log n)
    def buscar_binaria(self, titulo):
        titulo = titulo.strip().lower()

        inicio = 0
        fin = len(self._videojuegos) - 1

        while inicio <= fin:

            medio = (inicio + fin) // 2

            videojuego = self._videojuegos[medio]
            titulo_actual = videojuego.titulo.strip().lower()

            if titulo_actual == titulo:
                return videojuego

            elif titulo_actual < titulo:
                inicio = medio + 1

            else:
                fin = medio - 1

        return None

    # Filtra los videojuegos por género
    def filtrar_por_genero(self, genero):
        genero = genero.strip().lower()
        resultados = []

        for videojuego in self._videojuegos:
            if videojuego.genero.lower() == genero:
                resultados.append(videojuego)

        return resultados