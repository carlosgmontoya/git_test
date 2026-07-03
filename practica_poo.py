class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El auto {self.marca} {self.modelo} está encendido.")
        else:
            print(f"El auto {self.marca} {self.modelo} ya está encendido.")

    def tocar_bocina(self):
        print(f"El auto {self.marca} {self.modelo} está tocando la bocina: ¡BEEP BEEP!")


class Camion(Auto):
    def bombear_agua(self):
        print(f"El camión {self.marca} {self.modelo} está lanzando agua.")

class Motocicleta(Auto):
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
    def hacer_caballito(self):
        print(f"La motocicleta {self.marca} {self.modelo} está haciendo un caballito.")

toyota = Auto("Toyota", "Corolla", "Rojo")
nissan = Auto("Nissan", "Altima", "Azul")
hyundai = Auto("Hyundai", "Elantra", "Negro")
bombero = Camion("Bombero", "B-200", "Rojo")
yamaha = Motocicleta("Yamaha", "YZF-R3", "Azul", 321)

toyota.encender()
nissan.tocar_bocina()
bombero.bombear_agua()
yamaha.hacer_caballito()


