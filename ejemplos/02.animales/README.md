# Informe de Actividad: Pilares de POO
** Alumna: ** Valeria Igarzabal
---
## 1. Seleccion de Pilares
He seleccionado los conceptos de
**Herencia** y **Polimorfismo** para explicar el código del proyecto.

## 2. Explicación de Herencia:
La **Herencia** permite que las clases hijas (Perro, Gato, Raton) reutilcen el código de la clase padre.
* **Implementación:** En mi ejemplo, el método __init__ se define una sola vez en la clase padre para gestionar el nombre.
* **Ventaja:** Las subclases lo utilizan automáticamente sin necesidad de repetirlo. Incluso apliqué **Herencia múltiple** en los casos quecorrespondía.

## 3. Explicación de Polimorfismo
El **Polimorfismo** permite que diferentes objetos respondan al mismo mensaje de distintas maneras.

* **Aplicación:** Creé un método hablar() en todas las clases.
* **Resultado:** Aunque el bucle for llamo al método de la misma forma para todos los elementos, cada animal emite su propio sonido (*"Guau"*, *"Miau"*, *"Squeak"*) dependiendo de su clase.
