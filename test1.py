bpm = 72
spo2 = 98
temperatura = 36.5
señal = [1200, 1210, 1198, 1220]
frecuencias = [72, 75, 74, 73, 76]


def promedio(datos):
    prom = sum(datos) / len(datos)
    return prom

def maximus(datos):
    maxi = max(datos)
    return maxi

def minimus(datos):
    mini = min(datos)
    return mini

prom =promedio(frecuencias)
maxim = max(frecuencias)
minim = min(frecuencias)

print("Promedio de frecuencias:", prom)
print("Máximo de frecuencias:", maxim)
print("Mínimo de frecuencias:", minim)
