class Animal:
# Edad es un argumento opcional
    def __init__(self, nombre, edad = -1):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        texto_hablar = "algo"
        print(f'Soy {self.nombre}y digo {self.texto_hablar}')
        

class Perro(Animal):
    texto_hablar = 'Guau!'

    def hablar(self):
        print(f"Soy {self.nombre} y digo {self.texto_hablar}")   
        

class Gato(Animal):
    texto_hablar = "Miau!"
    def hablar(self):
        print(f"soy {self.nombre} y digo {self.texto_hablar}")

class Raton(Animal):
    texto_hablar = "¡Squeak!"

    def hablar(self):
          print(f"soy {self.nombre} y digo {self.texto_hablar}")


class Gatito(Gato):
 pass

for elem in Perro('Spike'), Gato('Tom'), Raton('Jerry', 3), Gatito("Mininito"): 
    elem.hablar()
   

