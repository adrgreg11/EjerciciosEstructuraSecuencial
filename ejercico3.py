# Ejercicio 3: calcular la hipotenusa de un triángulo rectángulo

cateto1 = float(input("Introduce el primer cateto: "))
cateto2 = float(input("Introduce el segundo cateto: "))

hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5

print("La hipotenusa mide:", hipotenusa)