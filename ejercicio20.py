#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

monedas_2 = int(input("Monedas de 2 €: "))

monedas_1 = int(input("Monedas de 1 €: "))

monedas_50 = int(input("Monedas de 50 céntimos: "))

monedas_20 = int(input("Monedas de 20 céntimos: "))

monedas_10 = int(input("Monedas de 10 céntimos: "))

centimos = monedas_2 * 200 + monedas_1 * 100 + monedas_50 * 50 + monedas_20 * 20 + monedas_10 * 10

euros = centimos // 100
centimos_restantes = centimos % 100

print(euros, "euros y", centimos_restantes, "céntimos")