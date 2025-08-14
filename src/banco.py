"""
Módulo que define la clase Banco para administrar múltiples cuentas bancarias.
"""

# Importan la clase CuentaBancaria y la excepción personalizada
from cuenta_bancaria import CuentaBancaria
from errores import SaldoInsuficienteError

class Banco():
    """
    Clase que representa un banco que administra múltiples cuentas bancarias.

    Attributes:
        _cuentas (list): Lista que almacena las cuentas bancarias del banco.
    """
    def __init__(self):
        """
        Constructor
        Inicializa un nuevo banco con una lista vacía de cuentas.
        """
        self._cuentas = [] 

    # -------------------- PROPIEDADES --------------------

    @property
    def cantidad_cuentas(self):
        """
        Obtiene la cantidad total de cuentas en el banco.

        Returns:
            int: Número de cuentas en el banco.
        """
        return len(self._cuentas)

    # -------------------- MÉTODOS --------------------

    def agregar_cuenta(self, cuenta):
        """
        Agrega una nueva cuenta al banco.

        Args:
            cuenta (CuentaBancaria): Instancia de la cuenta a agregar.
        """
        self._cuentas.append(cuenta)

    def eliminar_cuenta(self, cuenta):
        """
        Elimina una cuenta específica del banco.

        Args:
            cuenta (CuentaBancaria): Instancia de la cuenta a eliminar.
        """
        self._cuentas.remove(cuenta)

    def obtener_cuentas(self):
        """
        Obtiene la lista completa de cuentas del banco.

        Returns:
            list: Lista de instancias de cuentas bancarias.
        """

        return self._cuentas

    def eliminar_cuenta_por_nombre(self, nombre_cuenta):
        """
        Elimina una cuenta por su nombre.

        Si la cuenta tiene saldo, lo vacía antes de eliminarla.

        Args:
            nombre_cuenta (str): Nombre de la cuenta a eliminar.

        Returns:
            tuple: (exito (bool), monto_retirado (float))
                exito: True si la cuenta fue eliminada, False si no se encontró.
                monto_retirado: Saldo que se retiró antes de eliminar la cuenta.
        """
        nombre_cuenta = nombre_cuenta.strip().lower()
        # Buscar la cuenta por nombre
        for i, cuenta in enumerate(self._cuentas):
            if cuenta.nombre_cuenta.strip().lower() == nombre_cuenta:
                # Si la cuenta tiene saldo, vaciarlo antes de eliminarla
                if cuenta.saldo>0:
                    retirado = cuenta.vaciar_saldo()
                else:
                    retirado = 0
                # Eliminar la cuenta de la lista
                del self._cuentas[i]
                return True, retirado
        # Si no se encontró, devolver False y 0
        return False, 0

    def buscar_cuenta_por_nombre(self,nombre_cuenta):
        """
        Busca una cuenta por su nombre.

        Args:
            nombre_cuenta (str): Nombre de la cuenta a buscar.

        Returns:
            CuentaBancaria | None: Instancia de la cuenta si se encuentra, None si no existe.
        """
        nombre_cuenta = nombre_cuenta.strip().lower()
        for cuenta in self._cuentas:
            if cuenta.nombre_cuenta.strip().lower() == nombre_cuenta:
                return cuenta
        return None  

    def depositar_dinero_en_cuenta(self, nombre_cuenta, monto):
        """
        Deposita dinero en una cuenta específica del banco.

        Args:
            nombre_cuenta (str): Nombre de la cuenta en la que se depositará.
            monto (float): Cantidad a depositar.

        Returns:
            tuple: (exito (bool), mensaje (str))
                exito: True si el depósito fue exitoso, False si hubo error.
                mensaje: Mensaje informativo del resultado.
        """
        cuenta = self.buscar_cuenta_por_nombre(nombre_cuenta)
        if cuenta:
            try:
                cuenta.depositar_dinero(monto)
                return True, f"\nDeposito exitoso! Nuevo total: {cuenta.saldo:,}"
            except (ValueError, TypeError) as error:
                return False, str(error)

        return False, "\nLa cuenta digitada no existe."

    def retirar_dinero_en_cuenta(self, nombre_cuenta, monto):
        """
        Retira dinero de una cuenta específica del banco.

        Args:
            nombre_cuenta (str): Nombre de la cuenta de la que se retirará.
            monto (float): Cantidad a retirar.

        Returns:
            tuple: (exito (bool), mensaje (str))
                exito: True si el retiro fue exitoso, False si hubo error.
                mensaje: Mensaje informativo del resultado.
        """
        cuenta = self.buscar_cuenta_por_nombre(nombre_cuenta)
        if cuenta:
            try:
                cuenta.retirar_dinero(monto)
                return True, f"\nRetiro realizado! Nuevo total: {cuenta.saldo:,}"
            except(ValueError, TypeError, SaldoInsuficienteError) as error:
                return False, str(error)

        return False, "\nLa cuenta digitada no existe."
