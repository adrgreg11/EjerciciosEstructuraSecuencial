#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

horas = int(input("Hora de salida: "))

minutos = int(input("Minutos de salida: "))

segundos = int(input("Segundos de salida: "))

viaje = int(input("Duración del viaje en segundos: "))

total = horas * 3600 + minutos * 60 + segundos + viaje
total = total % (24 * 3600)  # La hora vuelve a 00:00:00 después de medianoche

hora_llegada = total // 3600
minuto_llegada = (total % 3600) // 60
segundo_llegada = total % 60

print("Hora de llegada:", hora_llegada, ":", minuto_llegada, ":", segundo_llegada)