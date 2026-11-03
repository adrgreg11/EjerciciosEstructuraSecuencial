#Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

numero1 = float(input("Primer número: "))
numero2 = float(input("Segundo número: "))

distancia = abs(numero1 - numero2)

print("La distancia es:", distancia)