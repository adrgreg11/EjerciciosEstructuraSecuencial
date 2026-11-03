#Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:  55% del promedio de sus tres calificaciones parciales.  30% de la calificación del examen final.  15% de la calificación de un trabajo final.

parcial1 = float(input("Nota del primer parcial: "))
parcial2 = float(input("Nota del segundo parcial: "))
parcial3 = float(input("Nota del tercer parcial: "))
examen = float(input("Nota del examen final: "))
trabajo = float(input("Nota del trabajo final: "))

nota_final = ((parcial1 + parcial2 + parcial3) / 3) * 0.55 + examen * 0.30 + trabajo * 0.15

print("Calificación final:", nota_final)