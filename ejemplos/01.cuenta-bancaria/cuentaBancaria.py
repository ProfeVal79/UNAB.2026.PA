class CuentaBancaria():
    ''' Clase que nos permite la gestión de una Cuenta Bancaria genérica!
    '''
    
    def __init__(self, saldo_inicial, nombre, apellido, moneda = '$'):
        # TODO: Ver la forma de soportar cajas de ahorro y/o cuentas corrientes
        self.movimientos = []
        self.saldo = saldo_inicial
        self.nombre = nombre
        self.apellido = apellido
        self.moneda = moneda

    def depositar(self, monto):
        '''Método que nos permite realizar un depósito bancario'''
        #validación de monto(si es cero o negativo no lo realiza) y devuelve error!!!
        if monto <= 0:
            return f"ERROR!!! El monto debe ser positivo. Saldo Actual:{self.moneda}{self.saldo}"
        else:
          self.movimientos.append(f"DEPOSITO:{self.moneda}{monto}")
          self.saldo += monto
          return f"Deposito exitoso. Nuevo saldo: {self.moneda}{self.saldo}"


    def extraer(self, monto):
        '''Método que nos permite realizar una extracción de un cuenta bancaria'''
        if self.saldo - monto >= 0:
            self.movimientos.append(f"EXTRACCION:{self.moneda}{monto}")
            self.saldo -= monto
            return f"saldo:{self.moneda}{self.saldo}"
        else:
           self.movimientos.append(f"SALDO INSUFICIENTE:{self.moneda}{monto}") 
           return f"Saldo insuficiente. Saldo Actual: {self.moneda}{self.saldo}"
        

    def datos_titular(self):
        '''Método que nos permite mostrar los datos del titular y su saldo'''
        return f"{self.apellido}, {self.nombre}\n Saldo:{self.moneda}{self.saldo}"
    
    def datos_saldo(self):
        return f"{self.moneda} {self.saldo}"

    def _reset_saldo(self):
        self.saldo = 0 

    def datos_movimientos(self):
        return list(self.movimientos)  