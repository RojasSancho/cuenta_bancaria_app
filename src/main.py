# ==============================
# Archivo: main.py
# Autor: Hermes Rojas Sancho
# Descripción: Aplicación simple para gestionar cuentas bancarias.
# Permite crear bancos, cuentas y realizar operaciones básicas.
# Utiliza una interfaz en terminal.
# ==============================

from cuenta_bancaria import CuentaBancaria
from banco import Banco
from errores import SaldoInsuficienteError
from tabulate import tabulate

import os
import platform

def verificar_solo_letras(texto):
    """
    Verifica si una cadena contiene únicamente letras y espacios.

    Args:
        texto (str): Cadena a validar.

    Returns:
        bool: True si el texto contiene solo letras y espacios, False en caso contrario.
    """
    for char in texto:
        if not (char.isalpha() or char.isspace()):  # Verifica que solo haya letras de a-z y espacios
            return False
    return True

def limpiar_consola():
    """
    Limpia la consola dependiendo del sistema operativo (Windows o Unix).
    """
    if platform.system().lower().startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def crear_cuenta(titular):
    """
    Crea una nueva cuenta bancaria para el titular especificado.

    Args:
        titular (str): Nombre del titular de la cuenta.

    Returns:
        CuentaBancaria: Instancia de la cuenta creada.
    """
    while True:
        nombre_cuenta = input("\nIngrese un nombre para la nueva cuenta bancaria: ")
        try: 
            cuenta_bancaria = CuentaBancaria(titular, nombre_cuenta)
        except ValueError as error:
            print(error)     
        else:
            print("Cuenta creada correctamente!")
            input("Presione ENTER para continuar.")
            limpiar_consola()
            return cuenta_bancaria

def eliminar_cuenta(banco):
    """
    Elimina una cuenta bancaria del banco si existe.

    Args:
        banco (Banco): Instancia del banco que contiene las cuentas.
    """
    if banco.obtener_cuentas() == []:
        print("No hay cuentas existentes.")
        input("Presione ENTER para continuar...")
        return

    cuenta_a_borrar = input("Digite el nombre de la cuenta que desea eliminar: ").strip().lower()

    if not verificar_solo_letras(cuenta_a_borrar):
        print("\nLa entrada debe tener formato de texto.")
        input("Presione ENTER para continuar...")
        return

    eliminado, monto_retirado = banco.eliminar_cuenta_por_nombre(cuenta_a_borrar)

    if eliminado:
        print(f"\nCuenta bancaria eliminada! Monto retirado automaticamente: {monto_retirado}")
    else:
        print("\nLa cuenta digitada no existe.")

    input("Presione ENTER para continuar...")

def consultar_titular(banco):
    """
    Muestra el titular de una cuenta bancaria específica.

    Args:
        banco (Banco): Instancia del banco que contiene las cuentas.
    """
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

def depositar_dinero(banco):
    """
    Permite depositar dinero en una cuenta bancaria.

    Args:
        banco (Banco): Instancia del banco que contiene las cuentas.
    """

    cuentas = banco.obtener_cuentas()
    if not cuentas:
        print("No hay cuentas existentes.")
        input("Presione ENTER para continuar...")
        return

    nombre_cuenta = input("Digite el nombre de la cuenta en la que desea depositar: ").strip().lower()
    existencia_cuenta = banco.buscar_cuenta_por_nombre(nombre_cuenta)
    if existencia_cuenta is None:
        print("\nLa cuenta digitada no existe.")
        input("Presione ENTER para continuar...")
        return
    print()
    try:
        monto = float(input("Digite el monto a depositar: ").strip())
    except ValueError:
        print("\nDebe ingresar un numero valido.")
        input("Presione ENTER para continuar...")
    else:
        estado, mensaje = banco.depositar_dinero_en_cuenta(nombre_cuenta, monto)
        print(mensaje)
        input("Presione ENTER para continuar...")

def retirar_dinero(banco):
    """
    Permite retirar dinero de una cuenta bancaria.

    Args:
        banco (Banco): Instancia del banco que contiene las cuentas.
    """

    cuentas = banco.obtener_cuentas()
    if not cuentas:
        print("No hay cuentas existentes.")
        input("Presione ENTER para continuar...")
        return

    nombre_cuenta = (input("Digite el nombre de la cuenta de la que desea retirar: ").strip().lower())
    existencia_cuenta = banco.buscar_cuenta_por_nombre(nombre_cuenta)
    if existencia_cuenta is None:
        print("\nLa cuenta digitada no existe.")
        input("Presione ENTER para continuar...")
        return
    print()
    try:
        monto = float(input("Digite el monto a retirar: ").strip())
    except ValueError:
        print("\nDebe ingresar un numero valido.")
        input("Presione ENTER para continuar...")
    else:
        estado, mensaje = banco.retirar_dinero_en_cuenta(nombre_cuenta, monto)
        print(mensaje)
        input("Presione ENTER para continuar...")

def mostrar_cuentas(banco):
    """
    Muestra todas las cuentas del banco en formato de tabla.

    Args:
        banco (Banco): Instancia del banco que contiene las cuentas.
    """
    cuentas = banco.obtener_cuentas()
    if cuentas != []:
        lista_cuentas = []
        for cuenta in cuentas:
            lista_para_cuenta = [cuenta.nombre_cuenta, f"{cuenta.saldo:,}"]
            lista_cuentas.append(lista_para_cuenta)

        print(tabulate(lista_cuentas, headers=["    NOMBRE DE CUENTA  ", "   SALDO   "], tablefmt="fancy_grid"))

def mostrar_menu_principal():
    """
    Muestra el menú principal con las opciones disponibles en la aplicación.
    """
    print("\n------------------------------------")
    print("|            APP BANCO             |")
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
    """
    Función principal de la aplicación.

    Flujo:
    - Solicita el nombre del titular.
    - Muestra un menú interactivo.
    - Permite realizar las operaciones bancarias disponibles.
    """
    
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
            mostrar_cuentas(banco)
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
                depositar_dinero(banco)

            elif opcion == "5":  # 5. Retirar dinero
                retirar_dinero(banco)

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
