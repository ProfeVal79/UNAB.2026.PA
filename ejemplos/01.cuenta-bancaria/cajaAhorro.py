#clase hija de cuentaBancaria
class CajaAhorro(CuentaBancaria):
    def __init__(self, saldo_inicial, nombre, apellido, beneficio=0, moneda = '$'):
        super().__init__(saldo_inicial, nombre, apellido, moneda)
        self.beneficio = beneficio

    def pagar_con_beneficio(self, monto, rubro="", dia_hoy=""):
#reglas segun el día de la semana
        dia_carniceria = "Sabado"
        dia_super =["lunes", "martes", "miercoles", "jueves", "viernes"]

#Definimos las reglas segun su rubro
        if rubro.lower() == "carniceria" and dia_hoy.lower() == dia_carniceria:
          porcentaje = 0.40  #40 %
        elif rubro.lower() == "almacen" or rubro.lower() == "supermercado" and dia_hoy.lower() in dia_super:
         porcentaje = 0.20
        else:
            porcentaje = 0


        