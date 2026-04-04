class Mascota():

    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        # validamos la edad antes de guardarla
        if edad < 0:
            print(f"La edad no puede ser negativa. Seteando a 0.")
            self.edad = 0
        else:
            self.edad = edad

    def saludar(self):
        print(f"¡Hola! Me llamo {self.nombre} y mi edad es {self.edad} años")


mascota = Mascota("Pluto", 3)
mascota.saludar()
otra_mascota = Mascota("Snowball", 1)
otra_mascota.saludar()