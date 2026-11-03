#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

numero = int(input("Introduce un número de dos cifras: "))

decenas = numero // 10
unidades = numero % 10

invertido = unidades * 10 + decenas

print("Número invertido:", invertido)