# Ejercicio 7: Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos = int(input("Introduce los minutos: "))

horas = minutos // 60
minutos_restantes = minutos % 60

print(horas, "horas y", minutos_restantes, "minutos")