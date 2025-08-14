"""
Módulo que define la clase CuentaBancaria y funciones auxiliares
para validar nombres de titulares y nombres de cuentas.
"""

# Importa la excepción personalizada para manejar retiros con saldo insuficiente
from errores import SaldoInsuficienteError

def verificar_texto(texto):
    """
    Verifica que el texto sea un string no vacío.

    Args:
        texto (str): Texto a validar.

    Raises:
        ValueError: Si el texto no es un string o está vacío.
    """
    if not isinstance(texto, str) or not texto.strip():
        raise ValueError("El nombre debe ser un texto no vacío.")

def verificar_tipo(texto):
    """
    Verifica que el texto contenga solo letras y espacios.

    Args:
        texto (str): Texto a validar.

    Raises:
        ValueError: Si el texto contiene caracteres distintos a letras o espacios.
    """
    for char in texto:
        if not (char.isalpha() or char.isspace()):  # Verifica que solo haya letras de a-z y espacios
            raise ValueError("El nombre solo puede contener letras o espacios.")

class CuentaBancaria():
    """
    Clase que representa una cuenta bancaria.

    Attributes:
        _titular (str): Nombre del titular de la cuenta.
        _nombre_cuenta (str): Nombre de la cuenta.
        _saldo (float): Saldo actual de la cuenta.
        _tiene_tarjeta (bool): Indica si la cuenta tiene tarjeta vinculada.
    """
    def __init__(self, titular, nombre_cuenta, saldo=0, tiene_tarjeta=False):
        """
        Constructor
        Inicializa una nueva cuenta bancaria.

        Args:
            titular (str): Nombre del titular.
            nombre_cuenta (str): Nombre de la cuenta.
            saldo (float, optional): Saldo inicial. Por defecto 0.
            tiene_tarjeta (bool, optional): Indica si la cuenta tiene tarjeta. Por defecto False.
        """
        # Validaciones de datos de entrada
        verificar_texto(titular)  # Nombre del titular, capitalizado
        verificar_tipo(titular)  # Nombre de la cuenta, capitalizado
        verificar_texto(nombre_cuenta) # Saldo inicial (por defecto 0)
        verificar_tipo(nombre_cuenta) # Indica si tiene tarjeta vinculada

        # Atributos encapsulados
        self._titular = titular.strip().title()
        self._nombre_cuenta = nombre_cuenta.strip().title()
        self._saldo = saldo
        self._tiene_tarjeta = tiene_tarjeta

    # -------------------- PROPIEDADES --------------------

    @property
    def titular(self):
        """Obtiene el nombre del titular de la cuenta."""
        return self._titular

    @titular.setter
    def titular(self, nombre):
        """
        Actualiza el nombre del titular con validaciones.

        Args:
            nombre (str): Nuevo nombre del titular.

        Raises:
            TypeError: Si el nombre no es un string.
            ValueError: Si el nombre está vacío o contiene caracteres no permitidos.
        """
        # Validar que el nuevo nombre sea string
        if not isinstance(nombre, str): #Validar que sea tipo string
            raise TypeError("El nombre del titular debe ser una cadena de texto que solo contenga letras.")
        # Validar que no esté vacío
        if not nombre.strip(): 
            raise ValueError("El nombre del titular no puede estar vacio.")
        # Validar que solo tenga letras y espacios manualmente (recorriendo los caracteres)
        for char in nombre:
            if not (char.isalpha() or char.isspace()): #Verifica que solo haya letras de a-z y espacios
                raise ValueError("El nombre solo puede contener letras o espacios.")

        # Da nombre al titular eliminando espacios al inicio y al final
        self._titular = nombre.strip() #Da nombre al titular eliminando espacios al inicio y al final

    @property
    def nombre_cuenta(self):
        """Obtiene el nombre de la cuenta."""
        return self._nombre_cuenta

    @property
    def saldo(self):
        """Obtiene el saldo actual de la cuenta."""
        return self._saldo

    @property
    def tiene_tarjeta(self):
        """Indica si la cuenta tiene tarjeta vinculada."""
        return self._tiene_tarjeta

    # -------------------- MÉTODOS --------------------

    def vaciar_saldo(self):
        """
        Vacía el saldo de la cuenta y devuelve el monto retirado.

        Returns:
            float: Monto retirado.
        """
        retirado = self._saldo
        self._saldo = 0
        return retirado

    def depositar_dinero(self, monto):
        """
        Deposita dinero en la cuenta.

        Args:
            monto (float): Cantidad a depositar.

        Raises:
            TypeError: Si el monto no es un número.
            ValueError: Si el monto es menor o igual a cero.
        """
        # Validar tipo del monto
        if not isinstance(monto,(int,float)):
            raise TypeError("El monto debe tener formato de numero.")
        # Validar que no sea negativo
        if monto<=0:
            raise ValueError("El monto a depositar debe ser mayor a cero.")
        self._saldo += monto

    def retirar_dinero(self, monto):
        """
        Retira dinero de la cuenta.

        Args:
            monto (float): Cantidad a retirar.

        Raises:
            TypeError: Si el monto no es un número.
            ValueError: Si el monto es menor o igual a cero.
            SaldoInsuficienteError: Si el saldo es insuficiente para el retiro.
        """
        # Validar tipo del monto
        if not isinstance(monto,(int,float)):
            raise TypeError("El monto debe tener formato de numero.")
        # Validar que no sea negativo
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a cero.")
        # Verificar que haya saldo suficiente
        if self.saldo < monto:
            raise SaldoInsuficienteError("Saldo insuficiente para el retiro.")

        # Disminuir el saldo
        self._saldo -= monto

    def asignar_tarjeta(self):
        """
        Vincula una tarjeta a la cuenta.

        Raises:
            ValueError: Si la cuenta ya tiene tarjeta vinculada.
        """
        if self._tiene_tarjeta:
            raise ValueError("La cuenta bancaria ya tiene una tarjeta vinculada.")
        self._tiene_tarjeta = True

    def desvincular_tarjeta(self):
        """
        Desvincula la tarjeta de la cuenta.

        Raises:
            ValueError: Si la cuenta no tiene tarjeta para desvincular.
        """
        if not self._tiene_tarjeta:
            raise ValueError("La cuenta bancaria no tiene tarjeta para ser desvinculada.")
        self._tiene_tarjeta = False
