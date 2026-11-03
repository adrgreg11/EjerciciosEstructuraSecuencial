#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.

correctas = int(input("Respuestas correctas: "))
incorrectas = int(input("Respuestas incorrectas: "))
blancas = int(input("Respuestas en blanco: "))

nota = correctas * 5 - incorrectas

print("Nota final:", nota)