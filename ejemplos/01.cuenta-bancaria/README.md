# Sistema de Gestión Bancaria (POO)
**Materia:** **Programación Avanzada - UNAB 2026**
**Alumno:** **Valeria Igarzabal**
---
## Estructura del Proyecto
El código está organizado en módulos para separar la lógica de las clases de la ejecución de pruebas:

* **cuentaBancaria.py**: Contiene la **clase padre** CuentaBancaria.
* Define los atributos base: saldo inicial, nombre, apellido y moneda (por defecto en pesos).
* **CajaAhorro.py**: Clase hija que hereda de la base.
* **Cuenta_corriente.py**: Clase hija que hereda de la base y añade lógica específica.
* **test.py**: El archivo principal de ejecución. Aquí se instancian los objetos y se verifican los métodos (depositos, extracciones, etc.).

## Pilares de POO Implementados

1. **Herencia**: Las clases CajaAhorro y CuentaCorriente reutilizan el código de CuentaBancaria, evitando repetir la lógica de inicialización.
2. **Modularización**: Cada clase reside en su propio archivo .py, facilitando el mantenimiento y la lectura.
3. **Abstracción**: La clase padre define el comportamiento general, mientras que las hijas se encargan de los detalles específicos de cada tipo de cuenta.

4. ## Como ejecutar las pruebas
5. Para ver el sistema en funcionamiento, simplemente ejecuta el archivo test:
   ```bash
   python test.py
