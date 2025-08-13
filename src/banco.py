from cuenta_bancaria import CuentaBancaria

class Banco():
    def __init__(self):
        self._cuentas = [] #lista con cuentas del banco

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
                del self._cuentas[i]
                return True
        return False

    def buscar_cuenta_por_nombre(self,nombre_cuenta):
        nombre_cuenta = nombre_cuenta.strip().lower()
        for cuenta in self._cuentas:
            if cuenta.nombre_cuenta.strip().lower() == nombre_cuenta:
                return cuenta
        return None   
