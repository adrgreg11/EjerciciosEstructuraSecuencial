# Ejercicio 9: aplicar un descuento del 15% a una compra

total_compra = float(input("Introduce el total de la compra: "))

descuento = total_compra * 0.15
total_a_pagar = total_compra - descuento

print("Descuento aplicado:", descuento)
print("Total a pagar:", total_a_pagar)