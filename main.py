from cuenta_bancaria import CuentaBancaria
from errores import SaldoInsuficienteError

mi_cuenta_bancaria = CuentaBancaria("Hermes Rojas Sancho") #Instancia de CuentaBancaria creada

def mostrar_menu_principal():
    print("CUENTA BANCARIA")
    print("1. Crear nueva cuenta bancaria")
    print("2. Consultar saldo")
    print("3. Depositar dinero")
    print("4. Retirar dinero")
    print("5. Salir")
    
def main():
    while True:
        mostrar_menu_principal()
        opcion = input("\nDigite el numero para seleccionar:")
        
        if opcion=="1":
            try:
                cuenta_bancaria = CuentaBancaria(input("Digite el nombre del titular de la cuenta: "))
            except ValueError as error:
                print(error)
        
        elif opcion=="5":
            print("Cerrando programa...")
            break

if __name__ == "__main__":
    main()