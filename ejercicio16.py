#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

distancia = float(input("Distancia entre los vehículos (km): "))
velocidad_rapido = float(input("Velocidad del vehículo de atrás (km/h): "))
velocidad_lento = float(input("Velocidad del vehículo de delante (km/h): "))

tiempo_horas = distancia / (velocidad_rapido - velocidad_lento)
tiempo_minutos = tiempo_horas * 60

print("Lo alcanzará en", tiempo_minutos, "minutos")