nombre_jugador = input("Nombre del jugador: ")
puntaje_base = float(input("Puntaje base: "))
bonificacion = float(input("Bonificacion: "))
penalizacion = float(input("Penalizacion: "))

puntaje_final = puntaje_base + bonificacion - penalizacion
alcanzo_meta = puntaje_final >= 100

print(f"\nJugador: {nombre_jugador}")
print(f"Puntaje final: {puntaje_final}")
print("Alcanzo la meta de 100 puntos:", alcanzo_meta)
