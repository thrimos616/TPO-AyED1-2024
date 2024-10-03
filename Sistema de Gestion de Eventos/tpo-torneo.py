from os import system, name
from typing import Tuple
from tabulate import tabulate
import json as js

def torneo()-> None:
    """
    Precondición: Nada
    Argumentos: Presenta torneo
    Postcondicion: nada
    """
    print("OLYMPUS ESPORTS")
    return None

def limpiar_pantalla() -> None:
    """
    Precondición: nada
    Argumentos: Limpia la pantalla
    Postcondición: nada
    """
    system("cls" if name == "nt" else "clear")
    torneo()
    return None

# Funciones para el menú de carga de datos.

def mostrar_juegos()-> Tuple[str]:
    """
    Precondición: None
    Argumentos: Muestra los juegos disponibles y retorna la tupla con estos mismos
    Postcondición: Retorna una tupla con los juegos disponibles
    """
    juegos = ( #Juegos permitidos
    "Counter Strike",
    "Valorant",
    "League of Legend",
    "Rainbow 6s",
    "Overwatch"
    )
    print("\nJuegos permitidos:")
    for index,juego in enumerate(juegos):
        print(f"{index + 1}. {juego}")
    return juegos

def seleccionar_juego() -> str:
    """
    Precondición: None
    Argumentos: Utiliza la funcion 'mostrar juegos' y selecciona un juego disponible en la tupla
    Postcondición: Retorna el juego seleccionado.
    """

    limpiar_pantalla()
    print("Seleccion de juego.\n")

    juegos = mostrar_juegos()
    while True:
        try:
            juego_seleccionado = int(input("\nIndica el número del juego: "))
            if juego_seleccionado <= 0 or juego_seleccionado > 5:
                print("Número inválido, intente nuevamente.")
            else:
                return juegos[juego_seleccionado- 1]
        except ValueError:
            print("\nError - Ingrese un valor válido.")


def cargar_equipo() -> None:
    """
    Precondición: El torneo debe estar registrado previamente.
    Postcondición: Se registra un equipo en el torneo y se muestra un mensaje confirmando la carga.
    """

    limpiar_pantalla()
    print("Cargar equipo\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


def cargar_integrantes() -> None:
    """
    Precondición: El equipo debe estar cargado previamente.
    Postcondición: Se registran los integrantes del equipo y se muestra un mensaje confirmando la carga.
    """

    limpiar_pantalla()
    print("Cargar datos de cada integrante\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


# Funciones para el menú de funcionamiento del programa
def elegir_enfrentamientos() -> None:
    """
    Precondición: Deben estar registrados los 8 equipos para el torneo.
    Postcondición: Se seleccionan los equipos que se enfrentarán en la próxima ronda.
    """

    limpiar_pantalla()
    print("Elegir enfrentamientos\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


def ingresar_resultado_ronda() -> str:
    """
    Precondicion: Ninguna
    Argumentos: Ingresa el ganador de cada ronda hasta que uno llegue a 5 rondas ganadas
    Postcondicion: Retorna el ganador de la ronda
    """
    equipo1 = 0
    equipo2 = 0

    print(f"1:{equipo1} o 2:{equipo2}")

    resultado_ronda = int(input("Ingrese el ganador de la ronda (1 o 2): "))

    while True:
        if resultado_ronda not in (1,2):
            print("Ingrese un número válido.")
        elif resultado_ronda == 1:
            equipo1 += 1
        else:
            equipo2 += 1
        if equipo1 == 5:
            print(f"El equipo {equipo1} es el ganador.")
            ganador = equipo1
            break
        elif equipo2 == 5:
            print(f"El equipo {equipo2} es el ganador.")
            ganador = equipo2
            break
    input("Presione Enter para volver al menú...")
    return ganador


def mostrar_estadisticas() -> None:
    """
    Precondición: Debe haber al menos un resultado registrado en el torneo.
    Postcondición: Se muestran las estadísticas actuales del torneo.
    """
    limpiar_pantalla()
    print("Mostrar estadísticas del torneo\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


def editar_datos_jugador() -> None:
    """
    Precondición: El jugador debe estar registrado en un equipo.
    Postcondición: Se modifican los datos del jugador seleccionado.
    """

    limpiar_pantalla()
    print("Editar datos del jugador\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


def generar_podio_mvp() -> None:
    """
    Precondición: El torneo debe haber finalizado.
    Postcondición: Se genera el podio de los equipos y se selecciona el MVP del torneo.
    """

    limpiar_pantalla()
    print("Generar podio y MVP\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


# Funciones de menú
def opciones_cargar_datos() -> None:
    """
    Precondición: Ninguna.
    Postcondición: Se muestran las opciones del menú para la carga de datos inicial.
    """

    print("Menú de carga de datos inicial..\n")
    print("1- Seleccionar juego.")
    print("2- Cargar equipo.")
    print("3- Cargar integrantes del equipo.")
    print("0- Volver al menú principal.")
    return None


def opciones_funcionamiento() -> None:
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
    return None


def menu_cargar_datos() -> None:
    """
    Precondición: Ninguna.
    Postcondición: Ejecuta la función seleccionada entre las opciones del menú de carga de datos inicial.
    """
    while True:
        limpiar_pantalla()
        opciones_cargar_datos()
        try:
            
            op = int(input("Ingrese una opción(0 Menú principal): "))
            if op >= 0 and op <= 3:
                if op == 0:
                    break
                if op == 1:
                    limpiar_pantalla()
                    juego = seleccionar_juego()
                    input(f"El juego seleccionado fue el {juego}.\nEnter para continuar.")
                elif op == 2:
                    pass
                elif op == 3:
                    pass
            else:
                print("Opción inválida.")
                input("Presione Enter para continuar...")
        except ValueError:
            print("Opción inválida, ingrese un número.")
            input("Presione Enter para continuar...")
    return None


def menu_funcionamiento() -> None:
    """
    Precondición: Ninguna.
    Postcondición: Ejecuta la función seleccionada entre las opciones del menú de funcionamiento del programa.
    """
    while True:
        limpiar_pantalla()
        opciones_funcionamiento()
        try:
            op = int(input("Ingrese una opción(0 Menú principal.): "))
            if op >= 0 and op <= 5:
                if op == 0:
                    break
                if op == 1:
                    limpiar_pantalla()
                elif op == 2:
                    limpiar_pantalla()
                    ganador = ingresar_resultado_ronda()
                    input(f"El ganador de la ronda es el equipo {ganador}.")
                elif op == 3:
                    limpiar_pantalla()
                elif op == 4:
                    limpiar_pantalla()
                elif op == 5:
                    limpiar_pantalla()
            else:
                print("Opción inválida.")
                input("Presione Enter para continuar...")
        except ValueError:
            print("Opción inválida, ingrese un número.")
            input("Presione Enter para continuar...")
    return None


def menu_principal() -> None:
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
    return None

if __name__ == "__main__":
    menu_principal()
