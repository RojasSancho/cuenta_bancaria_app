from cuenta_bancaria import CuentaBancaria
from banco import Banco
from errores import SaldoInsuficienteError

import os
import platform

def verificar_solo_letras(texto):
    for char in texto:
        if not (char.isalpha() or char.isspace()):  # Verifica que solo haya letras de a-z y espacios
            return False
    return True

def limpiar_consola():
    if platform.system().lower().startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def crear_cuenta(titular):
    while True:
        nombre_cuenta = input("Ingrese un nombre para la nueva cuenta bancaria: ")
        try: 
            cuenta_bancaria = CuentaBancaria(titular, nombre_cuenta)
        except ValueError as error:
            print(error)    
            input("Presione ENTER para continuar.") 
            limpiar_consola()
        else:
            print("Cuenta creada correctamente!")
            input("Presione ENTER para continuar.")
            limpiar_consola()
            return cuenta_bancaria

def eliminar_cuenta(banco):
    if banco.obtener_cuentas() == []:
        print("No hay cuentas existentes.")
        input("Presione ENTER para continuar...")
        return
    
    cuenta_a_borrar = input("Digite el nombre de la cuenta que desea eliminar: ").strip().lower()
    
    if not verificar_solo_letras(cuenta_a_borrar):
        print("\nLa entrada debe tener formato de texto.")
        input("Presione ENTER para continuar...")
        return
    
    if banco.eliminar_cuenta_por_nombre(cuenta_a_borrar):
        print("\nCuenta bancaria eliminada!")
    else:
        print("\nLa cuenta digitada no existe.")

    input("Presione ENTER para continuar...")

# def consultar_saldo(cuenta_bancaria):
#     if cuenta_bancaria is None:
#         print("\nLa cuenta bancaria aun no sido creada.")
#         input("Presione ENTER para continuar...")
#     else:
#         print(f"El saldo actual de la cuenta es de: {cuenta_bancaria.saldo}")
#         input("Presione ENTER para continuar...")

def consultar_titular(banco):
    cuentas = banco.obtener_cuentas()
    if cuentas == []:
        print("No hay cuentas existentes.")
        input("Presione ENTER para continuar...")
        return

    opcion_cuenta = input("Digite el nombre de la cuenta a consultar: ").strip().lower()
    print()
    if not verificar_solo_letras(opcion_cuenta):
        print("La entrada debe tener formato de texto.")
        input("Presione ENTER para continuar...")
        return

    cuenta = banco.buscar_cuenta_por_nombre(opcion_cuenta)
    if cuenta is None:
        print("La cuenta digitada no existe.")
        input("Presione ENTER para continuar...")
    else:
        print(f"El titular de la cuenta bancaria es: {cuenta.titular}")
        input("Presione ENTER para continuar...")

def depositar_dinero(cuenta_bancaria):
    if cuenta_bancaria is None:
        print("\nLa cuenta bancaria aun no sido creada.")   
        input("Presione ENTER para continuar...")    
    else:
        try:
            monto_deposito = float(input("Digite la cantidad que desea depositar: "))
        except ValueError as error:
            print("El monto debe digitarse en numeros.")
            input("Presione ENTER para continuar...")  
        else:    
            try:    
                cuenta_bancaria.depositar_dinero(monto_deposito)
                print("El monto se ha depositado exitosamente!")
                input("Presione ENTER para continuar...") 
            except (TypeError, ValueError) as error:
                print(error)
                input("Presione ENTER para continuar...") 

def retirar_dinero(cuenta_bancaria):
    if cuenta_bancaria is None:
        print("\nLa cuenta bancaria aun no sido creada.")   
        input("Presione ENTER para continuar...") 
    elif cuenta_bancaria.saldo == 0:
        print("\nSaldo insuficiente para el retiro.")
        input("Presione ENTER para continuar...")
    else:
        try:
            monto_retiro = float(input("Digite el monto a retirar: "))
        except ValueError as error:
            print("El monto debe digitarse en numeros.")
            input("Presione ENTER para continuar...") 
        else:
            try: 
                cuenta_bancaria.retirar_dinero(monto_retiro)
                print("El monto se ha retirado exitosamente!")
                input("Presione ENTER para continuar...") 
            except (TypeError, ValueError, SaldoInsuficienteError) as error: 
                print(error)
                input("Presione ENTER para continuar...") 

def mostrar_menu_principal():
    print("\n------------------------------------")
    print("|         CUENTA BANCARIA          |")
    print("------------------------------------")
    print("| 1. Crear nueva cuenta bancaria   |")
    print("| 2. Eliminar cuenta bancaria      |")
    print("| 3. Consultar titular             |")
    print("| 4. Depositar dinero              |")
    print("| 5. Retirar dinero                |")
    print("|                                  |")
    print("| 6. Salir                         |")
    print("------------------------------------\n")


# Ejecucion del programa
def main():
    banco = Banco()
    cuenta_bancaria = None
    print("\n-------------------------------------")
    print("| Bienvenido(a) a la aplicacion!    |")
    print("|                                   |")
    input("| Presione ENTER para continuar...  |\n-------------------------------------\n")
    limpiar_consola()
    titular = input("Digite el nombre del titular de las cuentas bancarias: ").strip()
    while not titular.strip() or not verificar_solo_letras(titular):
        limpiar_consola()
        titular = input("El nombre debe ser un texto no vacío. \nDigite el nombre del titular de las cuentas bancarias: ")

    while True:
        try:
            limpiar_consola()  
            mostrar_menu_principal()
            cuentas = banco.obtener_cuentas()
            if cuentas != []:
                print("Cuentas actuales:")
                for cuenta in cuentas:
                    print(f"{cuenta.nombre_cuenta} || Saldo: {cuenta.saldo}")
            opcion = input("\nDigite un numero para seleccionar: ").strip()
            print("")

            if opcion == "1":  # 1.Crear nueva cuenta bancaria
                cuenta_bancaria = crear_cuenta(titular)
                if cuenta_bancaria:
                    banco.agregar_cuenta(cuenta_bancaria)

            elif opcion == "2":  # 2.Eliminar cuenta bancaria
                eliminar_cuenta(banco)

            elif opcion =="3": # 3. Consultar titular
                consultar_titular(banco)

            elif opcion == "4":  # 4. Depositar dinero
                depositar_dinero(cuenta_bancaria)

            elif opcion == "5":  # 5. Retirar dinero
                retirar_dinero(cuenta_bancaria)

            elif opcion == "6":  # 6. Salir
                print("Gracias por utilizar esta aplicacion!\nCerrando...")
                break
            else:
                # Indica que no se eligio una opcion correcta
                print("La opcion elegida no es correcta, vuelva a intentarlo.")
                input("Presione ENTER para continuar...")
        except Exception as error:
            print(f"Ocurrio un error en la ejecucion de la aplicacion: {error}")
            input("Presione ENTER para continuar...")


if __name__ == "__main__":
    main()
