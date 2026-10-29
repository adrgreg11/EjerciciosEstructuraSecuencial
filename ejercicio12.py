#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.

x1 = float(input("x del primer punto: "))
y1 = float(input("y del primer punto: "))
x2 = float(input("x del segundo punto: "))
y2 = float(input("y del segundo punto: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("Distancia:", distancia)