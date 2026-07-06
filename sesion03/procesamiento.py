import numpy as np

tiempos_lista3_modificados = []

tiempos_lista = np.linspace(0, 9, 10)
#print("Tiempos:", tiempos_lista)

tiempos_lista2 = np.arange(0, 10, 1)
#print("Tiempos 2:", tiempos_lista2)

tiempos_lista3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Tiempos 3:", tiempos_lista3)
tiempos_lista4 = np.array(tiempos_lista3)
print("Tiempos como array:", tiempos_lista4)

for i in range(len(tiempos_lista3)):
    nuevo_valor = (tiempos_lista3[i] + 0.5) * 2
    tiempos_lista3_modificados.append(nuevo_valor)

print("Tiempos modificados con lista:", tiempos_lista3_modificados)


tiempo_lista4_modificados = (tiempos_lista4 + 0.5) * 2
print("Tiempos modificados con numpy:", tiempo_lista4_modificados)