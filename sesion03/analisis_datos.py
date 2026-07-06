import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tiempo = np.linspace(0, 5, 100)
voltaje_sensor = np.sin (2 *np.pi * 1.2 * tiempo) + np.random.normal(0,0.1, 100)

datos_simulados = pd.DataFrame({'Tiempo': tiempo, 'Voltaje': voltaje_sensor})
datos_simulados.to_csv('datos_simulados.csv', index=False)
print("¡Archivo creado con éxito!")

df = pd.read_csv('datos_simulados.csv')
print(df.head())

#plt.plot(tiempo, voltaje_sensor, color='blue', linewidth=1, label='Voltaje Sensor')
#plt.show()