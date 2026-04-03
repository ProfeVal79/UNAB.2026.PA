from cuentaBancaria import CuentaBancaria
print("MI CUENTA BANCARIA")
print()
#Creamos una cuenta y luego imprimimos los datos y el saldo
cuenta = CuentaBancaria(500, "Valeria", "Igarzabal")
print(cuenta.datos_titular())
print(cuenta.datos_saldo())

#Probamos depositando
print("Depositando $1000")
print(cuenta.depositar(1000))
print(cuenta.depositar(-500))

#probamos extracción
print("extracción de $300")
print(cuenta.extraer(300))
print(cuenta.extraer(2000))
print(f"Movimientos de la cuenta: ", cuenta.datos_movimientos())
print("_"* 20)

from cajaAhorro import CajaAhorro
print()
print(f"MI CAJA DE AHORRO")
print()
mi_ahorro = CajaAhorro(1000, "Valeria", "Igarzabal")
print(mi_ahorro.datos_titular())
print(mi_ahorro.pagar_con_beneficio(500, "almacen", "sabado"))
print(mi_ahorro.pagar_con_beneficio(300, "supermercado", "miercoles"))
print(mi_ahorro.depositar(10000))
print(mi_ahorro.datos_saldo())
print(mi_ahorro.pagar_con_beneficio(600, "carniceria", "sabado"))
print(mi_ahorro.datos_saldo())
print(mi_ahorro.datos_movimientos())
print(mi_ahorro.aplicar_interes_mensual())
print(mi_ahorro.datos_movimientos())
print("_" * 20)
#prueba de cuenta corriente
from Cuenta_corriente import CuentaCorriente
print()
print(f" MI CUENTA CORRIENTE")
print()
mi_CC = CuentaCorriente(33000,"Valeria", "Igarzabal", 5000)
print(mi_CC.datos_titular())
print(mi_CC.extraer(10000))
print(mi_CC.datos_movimientos())
print(mi_CC.emitir_cheque(5000, "Pedro"))
print(mi_CC.datos_movimientos())
print(mi_CC.cobrar_mantenimiento(8000))
print(mi_CC.depositar(80000))
print(mi_CC.recibir_transferencia(90000, "Lucas"))
print(mi_CC.datos_movimientos())