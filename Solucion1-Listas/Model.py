from ALg_Ordenamiento import  merge_sort

class Jugador:
    def __init__(self, id, nombre, edad, rendimiento):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento

    def __lt__(self, other):
        if self.rendimiento == other.rendimiento:
            return self.edad > other.edad
        return self.rendimiento < other.rendimiento

    def __repr__(self):
        return f"{{id: {self.id}, nombre: {self.nombre}, edad: {self.edad}, rendimiento: {self.rendimiento}}}"

class Equipo:
    def __init__(self, deporte, sede=None):
        self.deporte = deporte
        self.sede = sede
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def rendimiento_promedio(self):
        if not self.jugadores:
            return 0
        return sum(j.rendimiento for j in self.jugadores) / len(self.jugadores)

    def ordenar_jugadores(self):
        self.jugadores = merge_sort(self.jugadores)

class Sede:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

    def agregar_equipo(self, equipo):
        equipo.sede = self
        self.equipos.append(equipo)

    def rendimiento_promedio(self):
        if not self.equipos:
            return 0
        return sum(e.rendimiento_promedio() for e in self.equipos) / len(self.equipos)

    def ordenar_equipos(self):
        self.equipos = merge_sort(self.equipos, key=lambda e: (e.rendimiento_promedio(), -len(e.jugadores)))
