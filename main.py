from cuenta_bancaria import CuentaBancaria
from errores import SaldoInsuficienteError

import os
import platform

def limpiar_consola():
    if platform.system().lower().startswith('win'):
        os.system('cls')
    else:
        os.system('clear')
        
def crear_cuenta():
    try:
        cuenta_bancaria = CuentaBancaria(input("Digite el nombre del titular de la cuenta: "))
        print("Cuenta creada correctamente!")
        input("Presiona ENTER para continuar.") 
        limpiar_consola()
        return cuenta_bancaria
    except ValueError as error:
        print(error)
        input("Presiona ENTER para continuar.") 
        limpiar_consola()

def mostrar_menu_principal():
    print("\n--------------------------------\nCUENTA BANCARIA")
    print("1. Crear nueva cuenta bancaria")
    print("2. Consultar saldo")
    print("3. Consultar titular")
    print("4. Depositar dinero")
    print("5. Retirar dinero")
    print("6. Salir\n--------------------------------\n")
    
def main():
    cuenta_bancaria = None
    print("\n--------------------------------\nBienvenido(a) a la aplicacion!\n")
    input("Presiona ENTER para continuar...\n--------------------------------\n")
    while True:
        limpiar_consola()  
        mostrar_menu_principal()
        opcion = input("\nDigite un numero para seleccionar: ")
        
        if opcion=="1":
            cuenta_bancaria = crear_cuenta()
            
        elif opcion=="2":
            if cuenta_bancaria == None:
                print("\nLa cuenta bancaria aun no sido creada.")
                input("Presiona ENTER para continuar...")
            else:
                print(f"El saldo actual de la cuenta es de: {cuenta_bancaria.saldo}")
                input("Presiona ENTER para continuar...") 
        elif opcion=="3":  
            if cuenta_bancaria == None:
                print("\nLa cuenta bancaria aun no sido creada.")   
                input("Presiona ENTER para continuar...") 
            else:
                print(f"El titular de la cuenta es: {cuenta_bancaria.titular}")
                input("Presiona ENTER para continuar...") 
                
        elif opcion=="4":  
            if cuenta_bancaria == None:
                print("\nLa cuenta bancaria aun no sido creada.")   
                input("Presiona ENTER para continuar...")    
            else:
                try:
                    monto_deposito = float(input("Digite la cantidad que desea depositar: "))
                except ValueError as error:
                    print("El monto debe digitarse en numeros.")
                    input("Presiona ENTER para continuar...")  
                else:    
                    try:    
                        cuenta_bancaria.depositar_dinero(monto_deposito)
                        print("El monto se ha depositado exitosamente!")
                        input("Presiona ENTER para continuar...") 
                    except (TypeError, ValueError) as error:
                        print(error)
                        input("Presiona ENTER para continuar...") 
        elif opcion=="5":
            if cuenta_bancaria == None:
                print("\nLa cuenta bancaria aun no sido creada.")   
                input("Presiona ENTER para continuar...") 
            else:
                try:
                    monto_retiro = float(input("Digite el monto a retirar: "))
                except ValueError as error:
                    print("El monto debe digitarse en numeros.")
                    input("Presiona ENTER para continuar...") 
                else:
                    try: 
                        cuenta_bancaria.retirar_dinero(monto_retiro)
                        print("El monto se ha retirado exitosamente!")
                        input("Presiona ENTER para continuar...") 
                    except (TypeError, ValueError, SaldoInsuficienteError) as error: 
                        print(error)
                        input("Presiona ENTER para continuar...") 

        elif opcion=="6":
            print("Gracias por utilizar esta aplicacion!\nCerrando...")
            break
        else:
            print("La opcion elegida no es correcta, vuelva a intentarlo.")
            input("Presiona ENTER para continuar...")

if __name__ == "__main__":
    main()