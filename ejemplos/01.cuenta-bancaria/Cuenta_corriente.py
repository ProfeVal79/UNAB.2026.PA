from cuentaBancaria import CuentaBancaria
#Creamos la cuenta corriente hija
class CuentaCorriente(CuentaBancaria):
    def __init__(self, saldo_inicial, nombre, apellido, moneda="$", descubierto=0):
      super().__init__(saldo_inicial, nombre, apellido, moneda="$")
      self.descubierto = descubierto   #permiso de deuda temporal, aplica a Cuentas corrientes

    def extraer(self, monto):
        if monto <= (self.saldo + self.descubierto):
            self.saldo -= monto
            self.movimientos.append(f"Extracción CC.: - {self.moneda}{monto}")
            return f"Extracción exitosa. Saldo actual: {self.moneda}{self.saldo}"
        else:
            return f"Rechazado. El monto supera tu saldo y tu descubierto de {self.moneda}{self.descubierto}"

    def emitir_cheque(self, monto, beneficiario):
        impuesto = monto * 0.06
        total_a_descontar = monto + impuesto
        if total_a_descontar <= (self.saldo + self.descubierto):
            self.saldo -= total_a_descontar
            self.movimientos.append(f"Cheque a {beneficiario} por - {self.moneda}{total_a_descontar}")
            return f"se emitio cheque a {beneficiario}: {self.moneda}{monto} (Impuesto: {self.moneda}{impuesto})"
        else:
            return f"Cheque rechazado: saldo insuficiente para cubrir monto e impuestos"

    def cobrar_mantenimiento(self, monto_mantenimiento):
        self.saldo -= monto_mantenimiento
        self.movimientos.append(f"Mantenimiento: - {self.moneda}{monto_mantenimiento}")
        return f"Mantenimiento: - {self.moneda}{monto_mantenimiento}"

    def depositar(self, monto):
        self.saldo += monto
        self.movimientos.append(f"Depósito: {self.moneda}{monto}")
        return f"Deposito exitoso. Saldo actual: {self.moneda}{self.saldo}"

    def recibir_transferencia(self, monto, emisor):
        self.saldo += monto
        self.movimientos.append(f"Transferencia de {emisor}: {self.moneda}{monto}")
        return f"Recibiste {self.moneda}{monto} de {emisor}. Saldo actual: {self.saldo}"
