class Catalogo:
    def __init__(self):
        self._videojuegos = []

    def agregar(self, videojuego):
        self._videojuegos.append(videojuego)

    def listar(self):
        return self._videojuegos.copy()

    def buscar(self, titulo):
        titulo = titulo.strip().lower()

        for videojuego in self._videojuegos:
            if videojuego.titulo.lower() == titulo:
                return videojuego

        return None

    def filtrar_por_genero(self, genero):
        genero = genero.strip().lower()
        resultados = []

        for videojuego in self._videojuegos:
            if videojuego.genero.lower() == genero:
                resultados.append(videojuego)

        return resultados
