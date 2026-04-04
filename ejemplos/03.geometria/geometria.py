PI = 3.1416
class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado 

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado**2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base 
        self.altura = altura 

    def perimetro(self):
        return 2*(self.base + self.altura)

    def area(self):
        return self.base * self.altura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def perimetro(self):
        return 2 * PI * self.radio
    def area(self):
        return PI * (self.radio ** 2)

class Triangulo(Figura):
    def __init__(self, base, altura, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        return self.base + self.lado2 + self.lado3

    def area(self):
        return (self.base * self.altura)/2

class PoligonoRegular(Figura):
    def __init__(self, lado, longitud, apotema):  #apotema es la distancia del centro al lado
        self.lado = lado
        self.longitud = longitud
        self.apotema = apotema

    def perimetro(self):
        return self.lado * self.longitud

    def area(self):
    #Esta fórmula sirve para cualquier poligono regular
       return (self.perimetro() * self.apotema) / 2

class Pentagono(PoligonoRegular):
    def __init__(self, longitud, apotema):
            super().__init__(5, longitud, apotema)

class Hexagono(PoligonoRegular):
    def __init__(self, longitud, apotema):
            super().__init__(6, longitud, apotema)

class Heptagono(PoligonoRegular):
    def __init__(self, longitud, apotema):
            super().__init__(7, longitud, apotema)

class Octogono(PoligonoRegular):
    def __init__(self, longitud, apotema):
            super().__init__(8, longitud, apotema)


    

# TODO: Pensar en otra posible herencia (taxonomía)
#Taxonomía aplicada: Se creó la clase intermedia "PoligonoRegular" que hereda de "Figura". De esta forma, Pentagono,
#Hexágono, etc..., son hijos de "PoligonoRegular" (y nietos de "Figura")
#Permitiendo reutilizar la fórmula del área y el perimetro para cualquier polígono de n lados. 


# Pruebas
c1 = Cuadrado(6)
r1 = Rectangulo(3,4)
t1 = Triangulo(6,4,3,2)
cir = Circulo(7)
p1 = Pentagono(10, 6.88)
h1 = Hexagono(10, 8.66)
hept = Heptagono(10, 10.38)
oct = Octogono(10, 11.33)
mis_figuras = [c1, r1, t1, cir, p1, h1, hept, oct ]
print(f"RESULTADOS DE GEOMETRIA")

for f in mis_figuras:
    print({type(f).__name__})
    print(f"Perimetro: {f.perimetro()}")
    print(f"Area: {f.area()}")