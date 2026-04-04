# Analisis de Arquitectura: Sistema de Geometría
## En este proyecto se implementaron los cuatro pilares de la Programación Orientada a Objetos (POO) para evaluar la estructura de figuras geométricas:
* ### 1- Abstracción: Se crearon las clases base Figura y PoligonoRegular. Estas clases abstraen la idea general de que todas las figuras tienen un área y un perímetro, sin importar su forma específica.
* ### 2- Encapsulamiento: Cada clase (como Circulo, Triangulo o Cuadrado) encapsula sus propios datos (radio, base, apotema) y sus métodos de cálculo. Los datos están protegidos dentro de cada objeto mediante self.
* ### 3- Herencia: Se utilizo una jerarquía de 3 niveles (Taxonomía):
     * Nivel 1 (Base): "Figura"
     * Nivel 2 (Intermedio): PoligonoRegular (Hereda de figura).
     * Nivel 3 (Específico): Pentagono, Hexagono, etc. (Heredan de PoligonoRegular).
    Esto permitió reutilizar la fórmula del área y perímetro para todos los polígonos n lados.
* ### 4- Polimorfismo: Se implementó un bucle for que recorre una lista de objetos distintos (mis_figuras). A pesar de ser objetos diferentes, todos responden al mismo llamado de .area() y .perimetro(). Adaptando su comportamiento según su tipo. 
