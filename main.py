from cuenta_bancaria import CuentaBancaria

mi_cuenta_bancaria = CuentaBancaria() #Instancia de CuentaBancaria creada

print(f"El saldo actual de la cuenta es: {mi_cuenta_bancaria.saldo}")

mi_cuenta_bancaria.asignar_tarjeta()

print(mi_cuenta_bancaria.tiene_tarjeta)