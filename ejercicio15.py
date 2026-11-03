#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuánto valen al final las dos variables.
a = input("Valor de A: ")
b = input("Valor de B: ")

a, b = b, a

print("A vale:", a)
print("B vale:", b)