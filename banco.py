from cuenta_bancaria import CuentaBancaria

class Banco():
    def __init__(self):
        self.cuentas = [] #lista con cuentas del banco
    
    
    
    
    #Metodos
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
    
    def eliminar_cuenta(self, cuenta):
        self.cuentas.remove(cuenta)
        
    def obtener_cuentas(self):
        return self.cuentas