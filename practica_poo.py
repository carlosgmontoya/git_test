class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
        self.__kilometraje = 0  # Atributo privado

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El auto {self.marca} {self.modelo} está encendido.")
        else:
            print(f"El auto {self.marca} {self.modelo} ya está encendido.")

    def tocar_bocina(self):
        print(f"El auto {self.marca} {self.modelo} está tocando la bocina: ¡BEEP BEEP!")

    def obtener_kilometraje(self):
        return self.__kilometraje
    
    def conducir(self, distancia):
        if self.encendido:
            self.__kilometraje += distancia
            print(f"El auto {self.marca} {self.modelo} ha recorrido {distancia} km.")
        else:
            print(f"El auto {self.marca} {self.modelo} no puede conducir porque está apagado.")


class Camion(Auto):
    def bombear_agua(self):
        print(f"El camión {self.marca} {self.modelo} está lanzando agua.")
    
    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El camión {self.marca} {self.modelo} está encendido y listo para apagar incendios.")


class Motocicleta(Auto):
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada
    def hacer_caballito(self):
        print(f"La motocicleta {self.marca} {self.modelo} está haciendo un caballito.")

toyota = Auto("Toyota", "Corolla", "Rojo")
nissan = Auto("Nissan", "Altima", "Azul")
hyundai = Auto("Hyundai", "Elantra", "Negro")
bombero = Camion("Bombero", "B-200", "Rojo")
yamaha = Motocicleta("Yamaha", "YZF-R3", "Azul", 321)

#toyota.encender()
#nissan.tocar_bocina()
#bombero.bombear_agua()
#bombero.encender()
#yamaha.hacer_caballito()

toyota.encender()
toyota.conducir(50)
toyota.__kilometraje = 100
toyota.conducir(50)
print(f"Kilometraje del Toyota: {toyota.obtener_kilometraje()} km")  # Debería mostrar 50 km, no 100 km



