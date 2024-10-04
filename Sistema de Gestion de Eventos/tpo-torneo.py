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

def crear_torneo(): 
    torneo = {
        "nombre_torneo": nombre_torneo,
        "juego": juego,
        "equipos": [],
        "rondas": [],
        "podio": [],
        "mvp_torneo": ""
    }
    
    # lo guarda en un json
    try:
        with open('torneos.json', 'a') as file:
            json.dump({"torneos": [torneo]}, file, indent=4)
    except Exception as e:
        print(f"Error al guardar el torneo: {e}")

    print(f"Torneo '{nombre_torneo}' registrado con éxito para el juego '{juego}'.")
    input("Presione Enter para volver al menú...")

def cargar_equipo():
    limpiar_pantalla()
    print("Cargar equipo\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


def cargar_integrantes():
    limpiar_pantalla()
    print("Cargar datos de cada integrante\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


# Funciones para el menú de funcionamiento del programa
def elegir_enfrentamientos():
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
    resultados = []
    equipo1 = 0
    equipo2 = 0

    print(f"1:{equipo1} o 2:{equipo2}") 

    resultado_ronda = int(input("Ingrese el ganador de la ronda (1 o 2): "))

    while True:

        resultado = {
            "equipo1": equipo1,
            "equipo2": equipo2,
            "ganador_ronda": f"Equipo {resultado_ronda}"
        }
        resultados.append(resultado)

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

    with open('resultados_partida.json', 'w') as archivo_json:
        js.dump(resultados, archivo_json, indent=4)

    return ganador


#TAB
def mostrar_estadisticas_partidas():
    limpiar_pantalla()
    # (matriz con todas las estadisticas de cada partida en particular) = [[]]
    # print(tabulate(matriz, headers=["Nombre", "Kills", "Veces que murió"]))
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


def editar_datos_jugador():
    limpiar_pantalla()
    print("Editar datos del jugador\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")

#TAB
def generar_podio_mvp():
    limpiar_pantalla()
    # print(tabulate(matriz, headers=["Puesto", "Equipo"]))
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")


# Funciones de menú
def opciones_cargar_datos():
    print("Menú de carga de datos inicial...\n")
    print("1- Registrar torneo.")
    print("2- Cargar equipo.")
    print("3- Cargar integrantes del equipo.")
    print("0- Volver al menú principal.")


def opciones_funcionamiento():
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
    cargar_integrantes,
]  # op 3

funciones_funcionamiento = [
    elegir_enfrentamientos,  # op 1
    ingresar_resultado_ronda,  # op 2
    mostrar_estadisticas,  # op 3
    editar_datos_jugador,  # op 4
    generar_podio_mvp,  # op 5
]


def menu_cargar_datos():
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


def menu_funcionamiento():
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


def menu_principal():
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
