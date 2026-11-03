#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Nombre: ")
apellido1 = input("Primer apellido: ")
apellido2 = input("Segundo apellido: ")

print("Iniciales:", nombre[0].upper() + apellido1[0].upper() + apellido2[0].upper())