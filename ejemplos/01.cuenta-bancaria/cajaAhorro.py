#clase hija de cuentaBancaria
from cuentaBancaria import CuentaBancaria
class CajaAhorro(CuentaBancaria):
    def __init__(self, saldo_inicial, nombre, apellido, beneficio=0, moneda = '$'):
        super().__init__(saldo_inicial, nombre, apellido, moneda)
        self.beneficio = beneficio

    def pagar_con_beneficio(self, monto, rubro="", dia_hoy=""):
#reglas segun el día de la semana
        dia_carniceria = "sabado"
        dia_super =["lunes", "martes", "miercoles", "jueves", "viernes"]

#Definimos las reglas segun su rubro
        if rubro.lower() == "carniceria" and dia_hoy.lower() == dia_carniceria:
          porcentaje = 0.40  #40 %
        elif (rubro.lower() == "almacen" or rubro.lower() == "supermercado") and dia_hoy.lower() in dia_super:
         porcentaje = 0.20
        else:
            porcentaje = 0
        monto_con_descuento = monto * (1 - porcentaje)
        if self.saldo >= monto_con_descuento:
            self.saldo -= monto_con_descuento
            self.movimientos.append(f"Compra {self.moneda}{monto_con_descuento}")
            return f"Compra exitosa. Pago {self.moneda}{monto_con_descuento} (descuento del {porcentaje * 100}% aplicado)"
        else:
            return "Saldo insuficiente para realizar la compra con beneficio"

#suponiendo que el banco da un 2% de interés mensual sobre el saldo. 
    def aplicar_interes_mensual(self):
        tasa_interes = 0.02
        interes_ganado = self.saldo * tasa_interes
        self.saldo += interes_ganado
        self.movimientos.append(f"beneficio:{self.moneda}{interes_ganado}")
        return f"Se aplico el interes mensual {self.moneda}{interes_ganado}. Nuevo saldo:{self.moneda}{self.saldo}"
        