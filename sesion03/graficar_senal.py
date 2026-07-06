import sys
import numpy as np
import matplotlib.pyplot as plt

tiempo = np.linspace(0, 2, 500)

frecuencia = 0.5
senal = np.sin(2 * np.pi * frecuencia * tiempo)

ruido = np.random.normal(0, 0.1, len(tiempo))
senal_con_ruido = senal + ruido

plt.plot(tiempo, senal_con_ruido, color='red', linewidth=1, label='Señal con Ruido')
plt.plot(tiempo, senal, color='blue', linewidth=2, label='Señal Senoidal')

#plt.title('Procesamiento de Señales con NumPy y Matplotlib')
#plt.xlabel('Tiempo (s)')
#plt.ylabel('Amplitud')
#plt.grid(True)
#plt.legend()



#for i in sys.path:
#    print(i)

# =========================================
# APLICANDO EL FILTRO DE MEIDA MÓVIL
# =========================================

tamano_ventana = 80
ventana = np.ones(tamano_ventana) / tamano_ventana

senal_filtrada = np.convolve(senal_con_ruido, ventana, mode='same')

plt.plot(tiempo, senal_filtrada, color='green', linewidth=2, label='Señal con Ruido')
plt.legend()

plt.show()