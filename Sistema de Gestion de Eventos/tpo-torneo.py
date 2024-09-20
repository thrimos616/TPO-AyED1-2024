from os import system, name
from tabulate import tabulate
import random as rn 
import json as js

def limpiar_pantalla()-> None:
    # La pantalla del terminal se limpia según el sistema operativo
    system("cls" if name == "nt" else "clear")

# Funciones para el menú de carga de datos.
def registrar_torneo()-> None:
    """
    Precondición: El sistema está listo para registrar un torneo
    Postcondición: Se registra un nuevo torneo en el sistema y se muestra un mensaje confirmando el registro.
    """ 
    limpiar_pantalla()
    print("Registrar Torneo\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


def cargar_equipo()-> None:
    """
    Precondición: El torneo debe estar registrado previamente.
    Postcondición: Se registra un equipo en el torneo y se muestra un mensaje confirmando la carga.
    """

    limpiar_pantalla()
    print("Cargar equipo\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


def cargar_integrantes()-> None:
    """
    Precondición: El equipo debe estar cargado previamente.
    Postcondición: Se registran los integrantes del equipo y se muestra un mensaje confirmando la carga.
    """
    
    limpiar_pantalla()
    print("Cargar datos de cada integrante\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


# Funciones para el menú de funcionamiento del programa
def elegir_enfrentamientos()->None:
    """
    Precondición: Deben estar registrados los 8 equipos para el torneo.
    Postcondición: Se seleccionan los equipos que se enfrentarán en la próxima ronda.
    """

    limpiar_pantalla()
    print("Elegir enfrentamientos\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


def ingresar_resultado_ronda()-> None:
    """
    Precondición: Deben estar los enfrentamientos ya definidos.
    Postcondición: Se registra el resultado de la ronda y se actualizan las estadísticas del torneo.
    """

    limpiar_pantalla()
    print("Ingresar resultado de la ronda\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


def mostrar_estadisticas()-> None:
    """
    Precondición: Debe haber al menos un resultado registrado en el torneo.
    Postcondición: Se muestran las estadísticas actuales del torneo.
    """
    limpiar_pantalla()
    print("Mostrar estadísticas del torneo\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


def editar_datos_jugador()-> None:
    """
    Precondición: El jugador debe estar registrado en un equipo.
    Postcondición: Se modifican los datos del jugador seleccionado.
    """

    limpiar_pantalla()
    print("Editar datos del jugador\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


def generar_podio_mvp()-> None:
    """
    Precondición: El torneo debe haber finalizado.
    Postcondición: Se genera el podio de los equipos y se selecciona el MVP del torneo.
    """

    limpiar_pantalla()
    print("Generar podio y MVP\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


# Funciones de menú
def opciones_cargar_datos()-> None:
    """
    Precondición: Ninguna.
    Postcondición: Se muestran las opciones del menú para la carga de datos inicial.
    """

    print("Menú de carga de datos inicial..\n")
    print("1- Registrar torneo.")
    print("2- Cargar equipo.")
    print("3- Cargar integrantes del equipo.")
    print("0- Volver al menú principal.")


def opciones_funcionamiento()-> None:
    """
    Precondición: Ninguna.
    Postcondición: Se muestran las opciones del menú de funcionamiento del programa.
    """
    print("Menú de funcionamiento del programa.\n")
    print("1- Elegir enfrentamientos")
    print("2- Ingresar resultado de la ronda")
    print("3- Mostrar estadísticas del torneo")
    print("4- Editar datos del jugador")
    print("5- Generar podio y MVP")
    print("0- Volver al menú principal")


# Listas de funciones para cada menú

funciones_cargar_datos = [
    registrar_torneo,  # op 1
    cargar_equipo,  # op 2
    cargar_integrantes,# op 3
] 

funciones_funcionamiento = [
    elegir_enfrentamientos,  # op 1
    ingresar_resultado_ronda,  # op 2
    mostrar_estadisticas,  # op 3
    editar_datos_jugador,  # op 4
    generar_podio_mvp,  # op 5
]


def menu_cargar_datos()-> None:
    """
    Precondición: Ninguna.
    Postcondición: Ejecuta la función seleccionada entre las opciones del menú de carga de datos inicial.
    """
    while True:
        limpiar_pantalla()
        opciones_cargar_datos()
        try:
            op = int(input("Ingrese una opción: "))
            if op >= 0 and op <= 3:
                if op == 0:
                    break
                elif op >= 1 and op <= 3:
                    funciones_cargar_datos[op - 1]()
            else:
                print("Opción inválida.")
                input("Presione Enter para continuar...")
        except ValueError:
            print("Opción inválida, ingrese un número.")
            input("Presione Enter para continuar...")


def menu_funcionamiento()-> None:
    """
    Precondición: Ninguna.
    Postcondición: Ejecuta la función seleccionada entre las opciones del menú de funcionamiento del programa.
    """
    while True:
        limpiar_pantalla()
        opciones_funcionamiento()
        try:
            op = int(input("Ingrese una opción: "))
            if op >= 0 and op <= 5:
                if op == 0:
                    break
                elif op >= 1 and op <= 5:
                    funciones_funcionamiento[op - 1]()
            else:
                print("Opción inválida.")
                input("Presione Enter para continuar...")
        except ValueError:
            print("Opción inválida, ingrese un número.")
            input("Presione Enter para continuar...")


def menu_principal()-> None:
    """
    Precondición: Ninguna.
    Postcondición: Ejecuta el submenú seleccionado o cierra el programa.
    """
    while True:
        limpiar_pantalla()
        print("Bienvenido al menú principal.\n")
        print("1- Carga de datos inicial")
        print("2- Funcionamiento del programa")
        print("0- Salir")

        try:
            op = int(input("Ingrese una opción: "))
            if op == 1:
                menu_cargar_datos()
            elif op == 2:
                menu_funcionamiento()
            elif op == 0:
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida.")
                input("Presione Enter para continuar...")
        except ValueError:
            print("Opción inválida, ingrese un número.")
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    menu_principal()
