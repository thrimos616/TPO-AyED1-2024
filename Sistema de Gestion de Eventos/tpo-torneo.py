from os import system, name
from typing import Tuple
import json as js
import csv

def presentacion()-> None:
    """
    Precondición: Nada
    Argumentos: Nada
    Postcondicion: Muestra el nombre del torneo
    """
    print("OLYMPUS ESPORTS\n")
    return None

def limpiar_pantalla() -> None:
    """
    Precondición: Nada
    Argumentos: Nada
    Postcondición: Limpia la pantalla e invoca a la funcion: presentacion()
    """
    system("cls" if name == "nt" else "clear")
    presentacion()
    return None

def pausa()-> None:
    """
    Precondición: Nada
    Argumentos: Nada
    Postcondición: Para la ejecucion hasta que se presione Enter
    """
    input("Presione Enter para continuar...")

# Funciones para el menú de carga de datos.

def cargar_torneos(archivo: str) -> dict:
    """
    Precondicion: Debe recibir un archivo json existente
    Argumentos: Carga los torneos desde un archivo JSON
    Postcondicion: Retorna un diccionario con los torneos. Si tira error, retorna un diccionario vacio
    """
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return js.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}.")
        return {}
    except js.JSONDecodeError:
        print(f"Error: El archivo {archivo} no contiene un JSON válido.")
        return {}

def guardar_torneos(archivo: str, torneos: dict) -> None:
    """
    Precondición: El diccionario de torneos es válido
    Argumentos: Carga los torneos y guarda los datos en el json 
    Postcondición: nada
    """
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            js.dump(torneos, f, indent=4)
        print("Datos guardados en el archivo json.\n")
    except (OSError, js.JSONDecodeError) as e:
        print(f"Error al guardar el archivo {archivo}: {e}")

def mostrar_juegos()-> Tuple[str]:
    """
    Precondición: Nada
    Argumentos: Muestra los juegos disponibles
    Postcondición: Retorna una tupla con los juegos disponibles y muestra los juegos disponibles
    """
    juegos = (
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

def seleccionar_juego(archivo: str, torneo_nombre: str) -> str:
    """
    Precondición: El diccionario de torneos y el JSON tienen que ser válidos, tienen que haber juegos permitidos para seleccionar
    Argumentos: Carga el JSON del torneo y carga el juego que se seleccione en el mismo torneo 
    Postcondición: Retorna el juego seleccionado 
    """

    limpiar_pantalla()
    print("Seleccion de juego.\n")

    # Hace un bucle para que se pueda seleccionar un juego
    juegos = mostrar_juegos()
    while True:
        try:
            juego_seleccionado = int(input("\nIndica el número del juego: "))
        except ValueError:
            print("\nError - Ingrese un valor válido.")
        else:
            if juego_seleccionado <= 0 or juego_seleccionado > 5:
                print("Número inválido, intente nuevamente.")
            else:
                torneos = cargar_torneos(archivo)

                for torneo in torneos.get('torneos', []):
                    if torneo.get('nombre_torneo') == torneo_nombre:
                        torneo['juego'] = juegos[juego_seleccionado- 1]
                        guardar_torneos(archivo, torneos)

                return juegos[juego_seleccionado- 1]


def cargar_equipo(archivo: str, torneo_nombre: str) -> None:
    """
    Precondición: El torneo debe estar registrado previamente. El JSON y el nombre del torneo tienen que ser validos
    Argumentos: Se registran los equipos en el torneo y se muestra un mensaje confirmando la carga.
    Postcondición: nada
    """
    torneos = cargar_torneos(archivo)

    # Busca el equipo al cual se le va a cargar el nombre
    for i in range(8):
        equipo = input("Ingrese el nombre del equipo: ")

        for torneo in torneos['torneos']:
            if torneo['nombre_torneo'] == torneo_nombre:
                if 'equipos' not in torneo:
                    torneo['equipos'] = []
                if len(torneo['equipos']) > 0 and i == 0:
                    torneo['equipos'] = []
                torneo['equipos'].append(equipo)
                print(f"El equipo {equipo} ha sido registrado en el torneo {torneo_nombre}.")
                guardar_torneos(archivo, torneos)
    print("\nSe pudo cargar los 8 equipos de forma efectiva.")
    pausa()
    return None

def cargar_integrantes(archivo: str, torneo_nombre: str, equipo_nombre: str) -> None:
    """
    Precondición: El equipo debe estar cargado previamente.
    Argumentos: Recibe el nombre del archivo JSON, nombre del torneo y nombre del equipo y carga todos los datos en el archivo JSON y el CSV.
    Permite cargar 5 integrantes en un equipo y los guarda en el JSON y el CSV
    Postcondición: nada
    """
    ruta_csv = 'participantes.csv'

    # Ingresar nuevos integrantes
    integrantes = []
    for _ in range(5):
        nombre = input("\nIngrese el nombre del integrante: ")
        apellido = input("Ingrese el apellido del integrante: ")
        dni = input("Ingrese el DNI del integrante: ")

        integrante = {
            'Equipo': equipo_nombre,
            'Nombre': nombre,
            'Apellido': apellido,
            'DNI': dni
        }
        integrantes.append(integrante)

    # Abrir el archivo CSV en modo 'a' para agregar sin sobrescribir
    try:
        with open(ruta_csv, mode='a', newline='', encoding='utf-8') as archivo_csv:
            campos = ['Equipo', 'Nombre', 'Apellido', 'DNI']
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos)

            archivo_csv.seek(0, 2)  
            if archivo_csv.tell() == 0:  
                escritor.writeheader()  

            for integrante in integrantes:
                escritor.writerow(integrante)
    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except:
        print('Error en los datos')
    else:
        print('\nArchivo leído correctamente')

    # Registra los integrantes en el torneo
    torneos = cargar_torneos(archivo)
    for torneo in torneos['torneos']:
        if torneo['nombre_torneo'] == torneo_nombre:
            if 'integrantes' not in torneo:
                torneo['integrantes'] = {}
            torneo['integrantes'][equipo_nombre] = integrantes  
            guardar_torneos(archivo, torneos)  
            print(f"Integrantes cargados para el equipo {equipo_nombre}.")
            return None

    print(f"No se encontró el equipo {equipo_nombre} en el torneo {torneo_nombre}.")
    return None

# Funciones para el menú de funcionamiento del programa
def elegir_enfrentamientos(archivo: str, nombre_del_torneo: str) -> None:
    """
    Precondición: Deben estar registrados los 8 equipos para el torneo.
    Argumentos: Se seleccionan los equipos que se enfrentarán en la próxima ronda.
    Postcondición: Nada
    """

    torneos = cargar_torneos(archivo)

    # Busca el torneo por el nombre
    torneo_encontrado = None
    for t in torneos['torneos']:
        if t['nombre_torneo'] == nombre_del_torneo:
            torneo_encontrado = t
            break
    
    if torneo_encontrado is None:
        print(f"Torneo '{nombre_del_torneo}' no encontrado.")
        return 
    
    equipos = torneo_encontrado.get("equipos", [])


    # Crea los enfrentamientos de cuartos de final
    enfrentamientos = []
    cargas = 0
    while cargas < 8:
        print(equipos)
        print("\nIngrese el nombre de los equipos a enfrentarse\n")
        equipo_1 = input("Equipo 'A': ")
        equipo_2 = input("Equipo 'B': ")
        if equipo_1 and equipo_2 not in equipos:
            print("\nError - Ingrese un equipo válido.\n")
            continue
        enfrentamientos.append({
            "equipo1": equipo_1,
            "equipo2": equipo_2,
            "ganador": None,
            "mvp": None
        })
        cargas += 2
    # Agregar los cuartos al torneo
    nueva_ronda = {
        "ronda": "cuartos",
        "resultados": enfrentamientos
    }

    # Crea la key "rondas" en el diccionario si no existe, y si existe la deja vacía para cambiar los enfrentamientos
    torneo_encontrado["rondas"] = []

    torneo_encontrado["rondas"].append(nueva_ronda)

    guardar_torneos(archivo, torneos)
    
    print(f"Enfrentamientos generados para el torneo '{nombre_del_torneo}':")
    for enfrentamiento in enfrentamientos:
        print(f"{enfrentamiento['equipo1']} vs {enfrentamiento['equipo2']}")
    
    return None


def ingresar_resultado_ronda(torneo_nombre: str, ronda_numero: int, archivo: str) -> str:
    """
    Precondicion: El torneo, junto a los equipos y la ronda deben existir en el JSON.
    Argumentos: Ingresa los resultados de una ronda en el torneo especificado y actualiza el json con esos resultados.
    Postcondicion: Retorna una cadena de texto mostrando el resultado de la funcion.
    """
    limpiar_pantalla()
    torneos = cargar_torneos(archivo)

    # Busca el torneo en la lista de torneos cargados
    for torneo in torneos.get('torneos', []):
        if torneo.get('nombre_torneo') == torneo_nombre:
            if ronda_numero - 1 < len(torneo.get('rondas', [])):
                ronda = torneo['rondas'][ronda_numero - 1]
                print(f"Ingresando resultados de {ronda_numero} ronda de {torneo_nombre}")

                for resultado in ronda.get('resultados', []):
                    print(f"Resultado de {resultado['equipo1']} vs {resultado['equipo2']}:")

                    while True:
                        ganador = input(f"Ingrese el ganador (debe ser {resultado['equipo1']} o {resultado['equipo2']}): ")
                        if ganador in (resultado['equipo1'], resultado['equipo2']):
                            break
                        print("Ganador inválido.  Intente nuevamente, debe ser uno de los equipos que compiten.")

                    mvp = input("Ingrese el MVP de la ronda: ")
                    resultado['ganador'] = ganador
                    resultado['mvp'] = mvp

                # Guarda los torneos actualizados en el archivo
                guardar_torneos(archivo, torneos)
                return "Resultados ingresados correctamente"

    print("Torneo no encontrado.")
    return "Error: Torneo no encontrado."


def mostrar_estadisticas() -> None:
    """
    Precondición: Debe haber al menos un resultado registrado en el torneo.
    Argumentos: Nada
    Postcondición: Se muestran las estadísticas actuales del torneo.
    """
    limpiar_pantalla()
    print("Mostrar estadísticas del torneo\n")
    # Función en construcción, vuelva prontos.
    input("Presione Enter para volver al menú...")

def generar_podio_mvp() -> None:
    """
    Precondición: El torneo debe haber finalizado.
    Argumentos: Nada
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
    Argumentos: Se muestran las opciones del menú para la carga de datos inicial.
    Postcondición: Nada
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
    Argumentos: Se muestran las opciones del menú de funcionamiento del programa.
    Postcondición: Nada
    """
    print("Menú de funcionamiento del programa.\n")
    print("1- Elegir enfrentamientos")
    print("2- Ingresar resultado de la ronda")
    print("3- Mostrar estadísticas del torneo")
    print("4- Generar podio y MVP")
    print("0- Volver al menú principal")
    return None


def menu_cargar_datos() -> None:
    """
    Precondición: Ninguna.
    Argumentos: Ejecuta la función seleccionada entre las opciones del menú de carga de datos inicial.
    Postcondición: Nada
    """
    while True:
        limpiar_pantalla()
        opciones_cargar_datos()
        try:
            op = int(input("Ingrese una opción(0 Menú principal): "))
        except ValueError:
            print("Opción inválida, ingrese un número.")
            pausa()
        else:
            if op >= 0 and op <= 3:
                if op == 0:
                    break
                if op == 1:
                    limpiar_pantalla()
                    juego = seleccionar_juego(archivo_json, nombre_torneo)
                    input(f"El juego seleccionado fue el {juego}.\nEnter para continuar.")
                elif op == 2:
                    limpiar_pantalla()
                    cargar_equipo(archivo_json, nombre_torneo)
                elif op == 3:
                    torneos = cargar_torneos('resultados_torneos.json')
                    while True:
                        for torneo in torneos['torneos']:
                            print(torneo['equipos'])
                        nombre_equipo = input("\nIngrese el nombre del equipo para agregar el integrante(0 para salir): ")
                        if nombre_equipo == "0":
                            print("saliendo.")
                            pausa()
                            break
                        cargar_integrantes(archivo_json, nombre_torneo, nombre_equipo)
            else:
                print("Opción inválida.")
                pausa()
    return None

def menu_funcionamiento() -> None:
    """
    Precondición: Ninguna.
    Argumentos: Ejecuta la función seleccionada entre las opciones del menú de funcionamiento del programa.
    Postcondición: Nada
    """
    while True:
        limpiar_pantalla()
        opciones_funcionamiento()
        try:
            op = int(input("Ingrese una opción(0 Menú principal.): "))
        except ValueError:
            print("Opción inválida, ingrese un número.")
            pausa()
        else:
            if op >= 0 and op <= 5:
                if op == 0:
                    break
                if op == 1:
                    limpiar_pantalla()
                elif op == 2:
                    limpiar_pantalla()
                    print("Rondas \n1. Octavos \n2. Cuartos \n3. Semi-Final \n4. Final")
                    ronda_a_actualizar = int(input("Ingrese el número de la ronda que desea actualizar: "))
                    resultado = ingresar_resultado_ronda(nombre_torneo, ronda_a_actualizar, archivo_json)
                    print(resultado)
                    pausa()
                elif op == 3:
                    limpiar_pantalla()
                elif op == 4:
                    limpiar_pantalla()
            else:
                print("Opción inválida.")
                pausa()
    return None


def menu_principal() -> None:
    """
    Precondición: Ninguna.
    Argumentos: Ejecuta el submenú seleccionado o cierra el programa.
    Postcondición: Nada
    """
    while True:
        limpiar_pantalla()
        print("Bienvenido al menú principal.\n")
        print("1- Carga de datos inicial")
        print("2- Funcionamiento del programa")
        print("0- Salir")

        try:
            op = int(input("Ingrese una opción: "))
        except ValueError:
            print("Opción inválida, ingrese un número.")
            pausa()
        else:
            if op == 0:
                print("Saliendo del programa...")
                break
            elif op == 1:
                menu_cargar_datos()
            elif op == 2:
                menu_funcionamiento()
            else:
                print("Opción inválida.")
                pausa()
    return None


archivo_json = "resultados_torneos.json"  
nombre_torneo = "Olympus Esports"  

if __name__ == "__main__":
    menu_principal()
