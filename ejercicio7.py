# Ejercicio 7: convertir minutos en horas y minutos

minutos_totales = int(input("Introduce la cantidad de minutos: "))

horas = minutos_totales // 60
minutos = minutos_totales % 60

print(minutos_totales, "minutos son", horas, "horas y", minutos, "minutos.")