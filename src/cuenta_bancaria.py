# Importa la excepción personalizada para manejar retiros con saldo insuficiente
from errores import SaldoInsuficienteError

# Función utilitaria para verificar que el texto no esté vacío y sea tipo string
def verificar_texto(texto):
    if not isinstance(texto, str) or not texto.strip():
        raise ValueError("El nombre debe ser un texto no vacío.")
def verificar_tipo(texto):
    for char in texto:
        if not (char.isalpha() or char.isspace()):  # Verifica que solo haya letras de a-z y espacios
            raise ValueError("El nombre solo puede contener letras o espacios.")

# Clase que representa una cuenta bancaria
class CuentaBancaria():
    def __init__(self, titular, nombre_cuenta, saldo=0, tiene_tarjeta=False):
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

    # Propiedad para obtener el titular
    @property
    def titular(self):
        return self._titular

    # Setter para actualizar el titular con validaciones
    @titular.setter
    def titular(self, nombre):
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

    # Propiedad para obtener el nombre de la cuenta
    @property
    def nombre_cuenta(self):
        return self._nombre_cuenta

    # Propiedad para obtener el saldo
    @property
    def saldo(self):
        return self._saldo

    # Propiedad para saber si tiene tarjeta
    @property
    def tiene_tarjeta(self):
        return self._tiene_tarjeta

    # -------------------- MÉTODOS --------------------

    # Vaciar saldo y devolver el monto retirado
    def vaciar_saldo(self):
        retirado = self._saldo
        self._saldo = 0
        return retirado

    # Depositar dinero en la cuenta
    def depositar_dinero(self, monto):
        # Validar tipo del monto
        if not isinstance(monto,(int,float)):
            raise TypeError("El monto debe tener formato de numero.")
        if monto<=0:
            raise ValueError("El monto a depositar debe ser mayor a cero.")
        self._saldo += monto

    # Retirar dinero de la cuenta
    def retirar_dinero(self, monto):
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

    # Asignar una tarjeta a la cuenta
    def asignar_tarjeta(self):
        if self._tiene_tarjeta:
            raise ValueError("La cuenta bancaria ya tiene una tarjeta vinculada.")
        self._tiene_tarjeta = True

    # Desvincular la tarjeta de la cuenta
    def desvincular_tarjeta(self):
        if not self._tiene_tarjeta:
            raise ValueError("La cuenta bancaria no tiene tarjeta para ser desvinculada.")
        self._tiene_tarjeta = False
