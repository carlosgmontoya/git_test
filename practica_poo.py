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


toyota = Auto("Toyota", "Corolla", "Rojo")
nissan = Auto("Nissan", "Altima", "Azul")
hyundai = Auto("Hyundai", "Elantra", "Negro")

toyota.encender()
toyota.tocar_bocina()

