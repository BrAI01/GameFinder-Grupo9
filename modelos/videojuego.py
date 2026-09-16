class Videojuego:
    def __init__(self, titulo, genero, desarrollador, anio, rating):
        self._titulo = titulo
        self._genero = genero
        self._desarrollador = desarrollador
        self._anio = anio
        self._rating = rating

    @property
    def titulo(self):
        return self._titulo

    @property
    def genero(self):
        return self._genero

    @property
    def desarrollador(self):
        return self._desarrollador

    @property
    def anio(self):
        return self._anio

    @property
    def rating(self):
        return self._rating

    def mostrar(self):
        print(f"Título: {self._titulo}")
        print(f"Género: {self._genero}")
        print(f"Desarrollador: {self._desarrollador}")
        print(f"Año: {self._anio}")
        print(f"Rating: {self._rating}")
