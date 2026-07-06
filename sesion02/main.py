#import estadisticas
#from estadisticas import media, mediana, moda

import sys
import estadisticas as es
#from estadisticas import promedius, maximus, minimus
import random

#from sesion02 import estadisticas

for ruta in sys.path:
    print(ruta)

#print(estadisticas.__file__)
print(random.__file__)

señal = [1200, 1210, 1198, 1220]

#print(estadisticas.promedius(señal))
#print(estadisticas.maximus(señal))
#print(estadisticas.minimus(señal))

#print(promedius(señal))
#print(maximus(señal))
#print(minimus(señal))

print(es.promedius(señal))
print(es.maximus(señal))
print(es.minimus(señal))