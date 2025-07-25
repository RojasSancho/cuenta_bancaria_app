from cuenta_bancaria import CuentaBancaria
from errores import SaldoInsuficienteError

def mostrar_menu_principal():
    print("\n------------------------------\nCUENTA BANCARIA")
    print("1. Crear nueva cuenta bancaria")
    print("2. Consultar saldo")
    print("3. Consultar titular")
    print("4. Depositar dinero")
    print("5. Retirar dinero")
    print("6. Salir")
    
def main():
    while True:
        mostrar_menu_principal()
        opcion = input("\nDigite el numero para seleccionar: ")
        
        if opcion=="1":
            try:
                cuenta_bancaria = CuentaBancaria(input("Digite el nombre del titular de la cuenta: "))
            except ValueError as error:
                print(error)
        
        elif opcion=="2":
            try:
                print(f"El saldo actual de la cuenta es de: {cuenta_bancaria.saldo}")
            except UnboundLocalError:
                print("\nLa cuenta bancaria aun no sido creada.")
                input("Presiona ENTER para continuar.")
                
        elif opcion=="3":  
            try:
                print(f"El titular de la cuenta es: {cuenta_bancaria.titular}")
            except UnboundLocalError:
                print("\nLa cuenta bancaria aun no sido creada.")   
                input("Presiona ENTER para continuar.") 
        elif opcion=="4":      
            try:
                monto_deposito = float(input("Digite la cantidad que desea depositar: "))
            except ValueError as error:
                print("El monto debe digitarse en numeros.")
            else:    
                try:    
                    cuenta_bancaria.depositar_dinero(monto_deposito)
                    print("El monto se ha depositado exitosamente!")
                except TypeError as error:
                    print(error)
                except ValueError as error:
                    print(error)
                    
        elif opcion=="5":
            try:
                monto_retiro = float(input("Digite el monto a retirar: "))
            except ValueError as error:
                print("El monto debe digitarse en numeros.")
            else:
                try: 
                    cuenta_bancaria.retirar_dinero(monto_retiro)
                    print("El monto se ha retirado exitosamente!")
                except TypeError as error: 
                    print(error)
                except ValueError as error:
                    print(error)
                except SaldoInsuficienteError as error:
                    print(error)
                    
        elif opcion=="6":
            print("Cerrando programa...")
            break
        
        else:
            print("La opcion elegida no es correcta, vuelva a intentarlo.")
            input("Presiona ENTER para continuar.")

if __name__ == "__main__":
    main()