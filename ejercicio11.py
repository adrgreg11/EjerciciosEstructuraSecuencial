#Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

distancia = abs(numero1 - numero2)

print("La distancia entre los números es:", distancia)