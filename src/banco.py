from cuenta_bancaria import CuentaBancaria
from errores import SaldoInsuficienteError

class Banco():
    def __init__(self):
        self._cuentas = [] #lista con cuentas del banco

    @property
    def cantidad_cuentas(self):
        return len(self._cuentas)

    # Metodos
    def agregar_cuenta(self, cuenta):
        self._cuentas.append(cuenta)

    def eliminar_cuenta(self, cuenta):
        self._cuentas.remove(cuenta)

    def obtener_cuentas(self):
        return self._cuentas

    def eliminar_cuenta_por_nombre(self, nombre_cuenta):
        nombre_cuenta = nombre_cuenta.strip().lower()
        for i, cuenta in enumerate(self._cuentas):
            if cuenta.nombre_cuenta.strip().lower() == nombre_cuenta:
                if cuenta.saldo>0:
                    retirado = cuenta.vaciar_saldo()
                else:
                    retirado = 0
                del self._cuentas[i]
                return True, retirado
        return False, 0

    def buscar_cuenta_por_nombre(self,nombre_cuenta):
        nombre_cuenta = nombre_cuenta.strip().lower()
        for cuenta in self._cuentas:
            if cuenta.nombre_cuenta.strip().lower() == nombre_cuenta:
                return cuenta
        return None  

    def depositar_dinero_en_cuenta(self, nombre_cuenta, monto):
        cuenta = self.buscar_cuenta_por_nombre(nombre_cuenta)
        if cuenta:
            try:
                cuenta.depositar_dinero(monto)
                return True, f"\nDeposito exitoso! Nuevo total: {cuenta.saldo}"
            except (ValueError, TypeError) as error:
                return False, str(error)

        return False, "\nLa cuenta digitada no existe."

    def retirar_dinero_en_cuenta(self, nombre_cuenta, monto):
        cuenta = self.buscar_cuenta_por_nombre(nombre_cuenta)
        if cuenta:
            try:
                cuenta.retirar_dinero(monto)
                return True, f"\nRetiro realizado! Nuevo total: {cuenta.saldo}"
            except(ValueError, TypeError, SaldoInsuficienteError) as error:
                return False, str(error)

        return False, "\nLa cuenta digitada no existe."