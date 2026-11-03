# Ejercicio 8: Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo = float(input("Sueldo base: "))

venta1 = float(input("Importe de la primera venta: "))
venta2 = float(input("Importe de la segunda venta: "))
venta3 = float(input("Importe de la tercera venta: "))

comisiones = (venta1 + venta2 + venta3) * 0.10
total = sueldo + comisiones

print("Comisiones:", comisiones)
print("Total a recibir:", total)