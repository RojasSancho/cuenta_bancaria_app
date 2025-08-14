from errores import SaldoInsuficienteError

def verificar_texto(texto):
    if not isinstance(texto, str) or not texto.strip():
        raise ValueError("El nombre debe ser un texto no vacío.")
def verificar_tipo(texto):
    for char in texto:
        if not (char.isalpha() or char.isspace()):  # Verifica que solo haya letras de a-z y espacios
            raise ValueError("El nombre solo puede contener letras o espacios.")

class CuentaBancaria():
    def __init__(self, titular, nombre_cuenta, saldo=0, tiene_tarjeta=False):
        verificar_texto(titular)
        verificar_tipo(titular)
        verificar_texto(nombre_cuenta)
        verificar_tipo(nombre_cuenta)
        self._titular = titular.strip().title()
        self._nombre_cuenta = nombre_cuenta.strip().title()
        self._saldo = saldo
        self._tiene_tarjeta = tiene_tarjeta

    # Propiedad Titular
    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, nombre):
        if not isinstance(nombre, str): #Validar que sea tipo string
            raise TypeError("El nombre del titular debe ser una cadena de texto que solo contenga letras.")
        if not nombre.strip(): #Validar que no este vacio
            raise ValueError("El nombre del titular no puede estar vacio.")

        # Validar que solo tenga letras y espacios manualmente (recorriendo los caracteres)
        for char in nombre:
            if not (char.isalpha() or char.isspace()): #Verifica que solo haya letras de a-z y espacios
                raise ValueError("El nombre solo puede contener letras o espacios.")

        self._titular = nombre.strip() #Da nombre al titular eliminando espacios al inicio y al final

    # Propiedad NombreCuenta
    @property
    def nombre_cuenta(self):
        return self._nombre_cuenta

    # Propiedad Saldo
    @property
    def saldo(self):
        return self._saldo

    # Propiedad TieneTarjeta
    @property
    def tiene_tarjeta(self):
        return self._tiene_tarjeta

    # Metodos
    def vaciar_saldo(self):
        retirado = self._saldo
        self._saldo = 0
        return retirado
    
    def depositar_dinero(self, monto):
        if not isinstance(monto,(int,float)):
            raise TypeError("El monto debe tener formato de numero.")
        if monto<=0:
            raise ValueError("El monto a depositar debe ser mayor a cero.")
        self._saldo += monto

    def retirar_dinero(self, monto):
        if not isinstance(monto,(int,float)):
            raise TypeError("El monto debe tener formato de numero.")
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a cero.")
        if self.saldo < monto:
            raise SaldoInsuficienteError("Saldo insuficiente para el retiro.")

        self._saldo -= monto

    def asignar_tarjeta(self):
        if self._tiene_tarjeta:
            raise ValueError("La cuenta bancaria ya tiene una tarjeta vinculada.")
        self._tiene_tarjeta = True

    def desvincular_tarjeta(self):
        if not self._tiene_tarjeta:
            raise ValueError("La cuenta bancaria no tiene tarjeta para ser desvinculada.")
        self._tiene_tarjeta = False
    
    
