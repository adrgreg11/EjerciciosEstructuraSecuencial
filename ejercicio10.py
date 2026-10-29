#Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.

parcial1 = float(input("Nota del primer parcial: "))
parcial2 = float(input("Nota del segundo parcial: "))
parcial3 = float(input("Nota del tercer parcial: "))
examen_final = float(input("Nota del examen final: "))
trabajo_final = float(input("Nota del trabajo final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
calificacion_final = (
    promedio_parciales * 0.55
    + examen_final * 0.30
    + trabajo_final * 0.15
)

print("La calificación final es:", calificacion_final)