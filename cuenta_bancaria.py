from errores import SaldoInsuficienteError

class CuentaBancaria():
    titular=""
    saldo=0
    tiene_tarjeta=False
    numero_tarjeta=None
    
    #Metodos
    def depositar_dinero(self, monto):
        if monto<=0:
            raise ValueError("El monto a depositar debe ser mayor a cero.")
        self.saldo += monto
    
    def retirar_dinero(self, monto):
        if self.saldo < monto:
            raise SaldoInsuficienteError("Saldo insuficiente para el retiro.")
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a cero.")
        self.saldo -= monto
    
    def asignar_titular(self, nombre):
        try:
            self.titular = nombre
        except:
            print("Nombre del titular invalido.")
    
    def asignar_tarjeta(self):
        self.tiene_tarjeta = True
    
    def desvincular_tarjeta(self):
        self.tiene_tarjeta = False
        
    def cambiar_numero_tarjeta(self, numero):
        if str(numero).len != 16:
            print("El numero de tarjeta debe tener")
    

