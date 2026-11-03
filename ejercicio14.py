#Vamos a crear un programa para trabajar con una pila. Una pila es una estructura de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el último elemento que se añade al conjunto es el primero que se puede sacar

pila = []

pila.append(input("Añade un elemento: "))
pila.append(input("Añade otro elemento: "))

print("Pila:", pila)
print("Sale primero:", pila.pop())
print("Quedan:", len(pila))