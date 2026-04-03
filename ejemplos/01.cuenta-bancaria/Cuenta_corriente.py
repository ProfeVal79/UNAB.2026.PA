from cuentaBancaria import CuentaBancaria
#Creamos la cuenta corriente hija
class CuentaCorriente(CuentaBancaria):
    def __init__(self, saldo_inicial, nombre, apellido, moneda="$", descubierto=0):
      super().__init__(saldo_inicial, nombre, apellido, moneda="$")
      self.descubierto = descubierto   #permiso de deuda temporal, aplica a Cuentas corrientes

    def extraer(self, monto):
        if monto <= (self.saldo + self.descubierto):
            self.saldo -= monto
            self.movimientos.append(f"Extracción CC.: {self.moneda}{monto}")
            return f"Extracción exitosa. Saldo actual: {self.moneda}{self.saldo}"
        else:
            return f"Rechazado. El monto supera tu saldo y tu descubierto de {self.moneda}{self.descubierto}"