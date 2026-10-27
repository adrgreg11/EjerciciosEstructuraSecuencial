# Ejercicio 8: calcular comisiones y sueldo total del mes

sueldo_base = float(input("Introduce el sueldo base: "))
venta1 = float(input("Introduce el importe de la primera venta: "))
venta2 = float(input("Introduce el importe de la segunda venta: "))
venta3 = float(input("Introduce el importe de la tercera venta: "))

comisiones = (venta1 + venta2 + venta3) * 0.10

total_mes = sueldo_base + comisiones

print("Comisiones del mes:", comisiones)
print("Total que recibirá este mes:", total_mes)