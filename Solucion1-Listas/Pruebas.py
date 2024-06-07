from Model import Jugador, Sede, Equipo
from ALg_Ordenamiento import merge_sort


# Datos de ejemplo
jugadores = [
    Jugador(1, "Sofia Garcia", 21, 66),
    Jugador(2, "Alejandro Torres", 27, 24),
    Jugador(3, "Valentina Rodriguez", 19, 15),
    Jugador(4, "Juan Lopez", 22, 78),
    Jugador(5, "Martina Martinez", 30, 55),
    Jugador(6, "Sebastian Perez", 25, 42),
    Jugador(7, "Camila Fernandez", 24, 36),
    Jugador(8, "Mateo Gonzalez", 29, 89),
    Jugador(9, "Isabella Diaz", 21, 92),
    Jugador(10, "Daniel Ruiz", 17, 57),
    Jugador(11, "Luciana Sanchez", 18, 89),
    Jugador(12, "Lucas Vasquez", 26, 82),
]

sede_cali = Sede("Cali")
sede_medellin = Sede("Medellin")

equipo_futbol_cali = Equipo("Futbol")
equipo_futbol_cali.agregar_jugador(jugadores[9])
equipo_futbol_cali.agregar_jugador(jugadores[1])
sede_cali.agregar_equipo(equipo_futbol_cali)

equipo_volleyball_cali = Equipo("Volleyball")
equipo_volleyball_cali.agregar_jugador(jugadores[0])
equipo_volleyball_cali.agregar_jugador(jugadores[8])
equipo_volleyball_cali.agregar_jugador(jugadores[11])
equipo_volleyball_cali.agregar_jugador(jugadores[5])
sede_cali.agregar_equipo(equipo_volleyball_cali)

equipo_futbol_medellin = Equipo("Futbol")
equipo_futbol_medellin.agregar_jugador(jugadores[10])
equipo_futbol_medellin.agregar_jugador(jugadores[7])
equipo_futbol_medellin.agregar_jugador(jugadores[6])
sede_medellin.agregar_equipo(equipo_futbol_medellin)

equipo_volleyball_medellin = Equipo("Volleyball")
equipo_volleyball_medellin.agregar_jugador(jugadores[2])
equipo_volleyball_medellin.agregar_jugador(jugadores[3])
equipo_volleyball_medellin.agregar_jugador(jugadores[4])
sede_medellin.agregar_equipo(equipo_volleyball_medellin)

# Ordenar jugadores dentro de los equipos
for sede in [sede_cali, sede_medellin]:
    for equipo in sede.equipos:
        equipo.ordenar_jugadores()

# Ordenar equipos dentro de las sedes
for sede in [sede_cali, sede_medellin]:
    sede.ordenar_equipos()

# Ordenar sedes
sedes = [sede_cali, sede_medellin]
sedes = merge_sort(sedes, key=lambda s: (s.rendimiento_promedio(), -sum(len(e.jugadores) for e in s.equipos)))

# Imprimir resultados
for sede in sedes:
    print(f"Sede {sede.nombre}:")
    for equipo in sede.equipos:
        print(f"  {equipo.deporte}: {[jugador.id for jugador in equipo.jugadores]}")

# Ranking de jugadores
todos_jugadores = [jugador for sede in sedes for equipo in sede.equipos for jugador in equipo.jugadores]
ranking_jugadores = merge_sort(todos_jugadores)
print("Ranking Jugadores:", [jugador.id for jugador in ranking_jugadores])

# Datos adicionales

# Equipo con mayor rendimiento
equipo_mayor_rendimiento = max([equipo for sede in sedes for equipo in sede.equipos], key=lambda e: e.rendimiento_promedio())
print("Equipo con mayor rendimiento:", f"{equipo_mayor_rendimiento.deporte} sede {equipo_mayor_rendimiento.sede.nombre}")

# Equipo con menor rendimiento
equipo_menor_rendimiento = min([equipo for sede in sedes for equipo in sede.equipos], key=lambda e: e.rendimiento_promedio())
print("Equipo con menor rendimiento:", f"{equipo_menor_rendimiento.deporte} sede {equipo_menor_rendimiento.sede.nombre}")

# Jugador con mayor rendimiento
jugador_mayor_rendimiento = max(todos_jugadores, key=lambda j: j.rendimiento)
print("Jugador con mayor rendimiento:", jugador_mayor_rendimiento)

# Jugador con menor rendimiento
jugador_menor_rendimiento = min(todos_jugadores, key=lambda j: j.rendimiento)
print("Jugador con menor rendimiento:", jugador_menor_rendimiento)

# Jugador más joven
jugador_mas_joven = min(todos_jugadores, key=lambda j: j.edad)
print("Jugador mas joven:", jugador_mas_joven)

# Jugador más veterano
jugador_mas_veterano = max(todos_jugadores, key=lambda j: j.edad)
print("Jugador mas veterano:", jugador_mas_veterano)

# Promedio de edad de los jugadores
promedio_edad = sum(jugador.edad for jugador in todos_jugadores) / len(todos_jugadores)
print("Promedio de edad de los jugadores:", promedio_edad)

# Promedio del rendimiento de los jugadores
promedio_rendimiento = sum(jugador.rendimiento for jugador in todos_jugadores) / len(todos_jugadores)
print("Promedio del rendimiento de los jugadores:", promedio_rendimiento)