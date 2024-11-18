from os import system, name
from typing import Tuple
import json as js
import csv


def presentacion() -> None:
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


def pausa() -> None:
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
        with open(archivo, "r", encoding="utf-8") as f:
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
        with open(archivo, "w", encoding="utf-8") as f:
            js.dump(torneos, f, indent=4)
        print("Datos guardados en el archivo json.\n")
    except (OSError, js.JSONDecodeError) as e:
        print(f"Error al guardar el archivo {archivo}: {e}")


def mostrar_juegos() -> Tuple[str]:
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
        "Overwatch",
    )
    print("\nJuegos permitidos:")
    for index, juego in enumerate(juegos):
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

    while True:
        juegos = mostrar_juegos()
        try:
            juego_seleccionado = int(input("\nIndica el número del juego: "))
        except ValueError:
            print("\nError - Ingrese un valor válido.")
            pausa()
            limpiar_pantalla()
            continue
        else:
            if juego_seleccionado <= 0 or juego_seleccionado > 5:
                print("\nNúmero inválido, intente nuevamente.")
                pausa()
                limpiar_pantalla()
                continue
            else:
                torneos = cargar_torneos(archivo)

                for torneo in torneos.get("torneos", []):
                    if torneo.get("nombre_torneo") == torneo_nombre:
                        torneo["juego"] = juegos[juego_seleccionado - 1]
                        guardar_torneos(archivo, torneos)

                return juegos[juego_seleccionado - 1]


def cargar_equipo(archivo: str, torneo_nombre: str) -> None:
    """
    Precondición: El torneo debe estar registrado previamente. El JSON y el nombre del torneo tienen que ser validos
    Argumentos: Se registran los equipos en el torneo y se muestra un mensaje confirmando la carga.
    Postcondición: nada
    """
    torneos = cargar_torneos(archivo)

    for torneo in torneos["torneos"]:
        if torneo["nombre_torneo"] == torneo_nombre:
            if "equipos" not in torneo or len(torneo["equipos"]) > 0:
                torneo["equipos"] = []

            equipos_registrados = 0

            while equipos_registrados < 8:
                equipo = input("Ingrese el nombre del equipo: ")

                if equipo == "" or equipo in torneo["equipos"]:
                    print(
                        "El nombre no puede estar vacío y tampoco puede repetirse, ingrese un nombre válido."
                    )
                    continue

                torneo["equipos"].append(equipo)
                equipos_registrados += 1
                print(
                    f"\nEl equipo {equipo} ha sido registrado en el torneo {torneo_nombre}.\n"
                )

            index = 0
            print("Los equipos cargados son:")
            for equipo in torneo["equipos"]:
                print(f"{index + 1}. {equipo}")
                index += 1
            pausa()

            break

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
    limpiar_pantalla()

    ruta_csv = "participantes.csv"

    # Ingresar nuevos integrantes
    integrantes = []
    integrantes_registrados = 0
    while integrantes_registrados < 5:
        print(f"Cargando integrante del equipo {equipo_nombre}")

        nombre = input("\nIngrese el nombre del integrante: ").strip().title()
        apellido = input("Ingrese el apellido del integrante: ").strip().title()
        dni = input("Ingrese el DNI del integrante: ").strip()

        if nombre == "" or apellido == "" or dni == "":
            print("No puede haber ningun dato vacío.")
            pausa()
            limpiar_pantalla()
            continue

        if (
            not nombre.isalpha()
            or not apellido.isalpha
            or not dni.isdigit()
            or len(dni) != 8
        ):
            print(
                "\nIngrese un dato válido. \nNombre y Apellido: Solo datos alfabeticos. \nDNI: Unicamente 8 digitos"
            )
            pausa()
            limpiar_pantalla()
            continue

        integrante = {
            "Equipo": equipo_nombre,
            "Nombre": nombre,
            "Apellido": apellido,
            "DNI": dni,
        }
        integrantes.append(integrante)
        integrantes_registrados += 1

    # Abrir el archivo CSV en modo 'a' para agregar sin sobrescribir
    try:
        with open(ruta_csv, mode="at", newline="", encoding="utf-8-sig") as archivo_csv:
            campos = ["Equipo", "Nombre", "Apellido", "DNI"]
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
            archivo_csv.seek(0, 2)
            if archivo_csv.tell() == 0:
                escritor.writeheader()

            for integrante in integrantes:
                escritor.writerow(integrante)

    except FileNotFoundError as msg:
        print(f"No se encuentra el archivo: {msg}")
    except OSError as msg:
        print(f"No se puede leer el archivo: {msg}")
    except:
        print("Error en los datos")

    # Registra los integrantes en el torneo
    torneos = cargar_torneos(archivo)
    for torneo in torneos["torneos"]:
        if torneo["nombre_torneo"] == torneo_nombre:
            if "integrantes" not in torneo:
                torneo["integrantes"] = {}
            torneo["integrantes"][equipo_nombre] = integrantes
            guardar_torneos(archivo, torneos)
            print(f"Integrantes cargados para el equipo {equipo_nombre}.")
            pausa()
            return None

    print(f"No se encontró el equipo {equipo_nombre} en el torneo {torneo_nombre}.")
    pausa()
    return None


# Funciones para el menú de funcionamiento del programa
def elegir_enfrentamientos(archivo: str, torneo_nombre: str) -> None:
    """
    Precondición: Deben estar registrados los 8 equipos para el torneo.
    Argumentos: Se seleccionan los equipos que se enfrentarán en la próxima ronda.
    Postcondición: Nada
    """

    torneos = cargar_torneos(archivo)

    # Busca el torneo por el nombre
    torneo_encontrado = None
    for torneo in torneos["torneos"]:
        if torneo["nombre_torneo"] == torneo_nombre:
            torneo_encontrado = torneo
            break

    if torneo_encontrado is None:
        print(f"Torneo '{torneo_nombre}' no encontrado.")
        return

    equipos = torneo_encontrado.get("equipos", [])

    # Crea los enfrentamientos de cuartos de final
    enfrentamientos = []
    cargas = 0
    ya_cargados = []
    while cargas < 8:
        limpiar_pantalla()
        print(equipos)
        print("\nIngrese el nombre de los equipos a enfrentarse\n")
        equipo_1 = input("Equipo 'A': ")
        equipo_2 = input("Equipo 'B': ")

        if equipo_1 not in equipos or equipo_2 not in equipos:
            print("\nError - Ingrese un equipo válido.\n")
            pausa()
            continue

        if equipo_1 == equipo_2:
            print("Error - No podes elegir los mismos equipos.")
            pausa()
            continue

        if equipo_1 in ya_cargados or equipo_2 in ya_cargados:
            print("Error - Ya fue cargado al menos un equipo.")
            pausa()
            continue

        ya_cargados.append(equipo_1)
        ya_cargados.append(equipo_2)

        enfrentamientos.append(
            {
                "equipo1": equipo_1,
                "equipo2": equipo_2,
                "ganador": "No determinado",
                "mvp": "No determinado",
            }
        )
        cargas += 2
    # Agregar los cuartos al torneo
    nueva_ronda = {"ronda": "cuartos", "resultados": enfrentamientos}

    # Crea la key "rondas" en el diccionario si no existe, y si existe la deja vacía para cambiar los enfrentamientos
    torneo_encontrado["rondas"] = []

    torneo_encontrado["rondas"].append(nueva_ronda)

    guardar_torneos(archivo, torneos)

    print(f"Enfrentamientos generados para el torneo '{torneo_nombre}':\n")
    for enfrentamiento in enfrentamientos:
        print(f"{enfrentamiento['equipo1']} vs {enfrentamiento['equipo2']}")
    print()

    return None


def ingresar_resultado_ronda(
    torneo_nombre: str, ronda_numero: int, archivo: str
) -> None:
    """
    Precondición: El torneo, junto a los equipos y la ronda deben existir en el JSON.
    Argumentos: Ingresa los resultados de una ronda en el torneo especificado y actualiza el JSON con esos resultados.
    Postcondición: Retorna una cadena de texto mostrando el resultado de la función.
    """
    limpiar_pantalla()
    torneos = cargar_torneos(archivo)
    nombre_ronda = ["cuartos", "semi-final", "final", "tercer-lugar"]

    # Busca el torneo en la lista de torneos cargados
    for torneo in torneos.get("torneos", []):
        if torneo.get("nombre_torneo") == torneo_nombre:
            # Verifica si la clave 'rondas', si no existe la crea..
            if "rondas" not in torneo:
                torneo["rondas"] = []

            # Verifica si la ronda existe, si no existe creala ronda
            if ronda_numero - 1 < len(torneo["rondas"]):
                ronda = torneo["rondas"][ronda_numero - 1]
            else:
                # Si la ronda no existe, crea la estructura de la ronda
                ronda = {"ronda": nombre_ronda[ronda_numero - 1], "resultados": []}
                torneo["rondas"].append(ronda)

            print(
                f"Ingresando resultados de la ronda {nombre_ronda[ronda_numero - 1]} de {torneo_nombre}"
            )

            # Si no existen enfrentamientos en la ronda, se crean
            if not ronda.get("resultados"):
                equipos = torneo.get("equipos", [])
                if ronda_numero == 1:  # cuartos de final
                    # Empareja los equipos para cuartos
                    for i in range(0, len(equipos), 2):
                        equipo1 = equipos[i]
                        equipo2 = equipos[i + 1] if i + 1 < len(equipos) else None
                        if equipo2:
                            ronda["resultados"].append(
                                {
                                    "equipo1": equipo1,
                                    "equipo2": equipo2,
                                    "ganador": "No determinado",
                                    "mvp": "No determinado",
                                }
                            )
                elif ronda_numero == 2:  # semi-final
                    # Los ganadores de los cuartos están en esta ronda
                    try:
                        ganadores_cuartos = [
                            resultado["ganador"]
                            for resultado in torneo["rondas"][0]["resultados"]
                        ]
                        for i in range(0, len(ganadores_cuartos), 2):
                            equipo1 = ganadores_cuartos[i]
                            equipo2 = (
                                ganadores_cuartos[i + 1]
                                if i + 1 < len(ganadores_cuartos)
                                else None
                            )
                            if equipo2:
                                ronda["resultados"].append(
                                    {
                                        "equipo1": equipo1,
                                        "equipo2": equipo2,
                                        "ganador": "No determinado",
                                        "mvp": "No determinado",
                                    }
                                )
                    except IndexError:
                        print(
                            "Error: No se han registrado los resultados en la ronda de cuartos."
                        )
                        pausa()
                        return
                elif ronda_numero == 3:  # final
                    try:
                        # Los ganadores de la semi-final están en esta ronda
                        ganadores_semi = [
                            resultado["ganador"]
                            for resultado in torneo["rondas"][1]["resultados"]
                        ]
                        ronda["resultados"].append(
                            {
                                "equipo1": ganadores_semi[0],
                                "equipo2": ganadores_semi[1],
                                "ganador": "No determinado",
                                "mvp": "No determinado",
                            }
                        )
                    except IndexError:
                        print(
                            "Error: No se han registrado los resultados en la ronda de semi-final."
                        )
                        pausa()
                        return
                elif ronda_numero == 4:  # tercer-lugar
                    try:
                        # Los perdedores de la semi-final están en esta ronda
                        perdedores_semi = [
                            (
                                resultado["equipo1"]
                                if resultado["ganador"] == resultado["equipo2"]
                                else resultado["equipo2"]
                            )
                            for resultado in torneo["rondas"][1]["resultados"]
                        ]
                        ronda["resultados"].append(
                            {
                                "equipo1": perdedores_semi[0],
                                "equipo2": perdedores_semi[1],
                                "ganador": "No determinado",
                                "mvp": "No determinado",
                            }
                        )
                    except IndexError:
                        print(
                            "Error: No se han registrado los resultados en la ronda de semi-final para los perdedores."
                        )
                        pausa()
                        return

            # Ingresa los resultados de la ronda
            for resultado in ronda.get("resultados", []):
                print(f"Resultado de {resultado['equipo1']} vs {resultado['equipo2']}:")
                while True:
                    ganador = input(
                        f"Ingrese el ganador (debe ser {resultado['equipo1']} o {resultado['equipo2']}): "
                    )
                    if ganador in (resultado["equipo1"], resultado["equipo2"]):
                        break
                    print(
                        "Ganador inválido. Intente nuevamente, debe ser uno de los equipos que se enfrentan."
                    )
                print()

                while True:
                    # Bucle para ingresar el MVP de la ronda y verificar que sea válido.
                    for integrante in torneo["integrantes"][ganador]:
                        print(f"{integrante['Nombre']} {integrante['Apellido']}")

                    mvp = input(
                        "Ingrese el MVP de la ronda (separar el nombre del apellido únicamente con una (,): "
                    )

                    if "," not in mvp:
                        print(
                            "Error - Debe separar el nombre del apellido solamente con una (,). Intente nuevamente."
                        )
                        pausa()
                        limpiar_pantalla()
                        continue

                    nombre_mvp, apellido_mvp = mvp.split(",")
                    nombre_mvp = nombre_mvp.strip()
                    apellido_mvp = apellido_mvp.strip()

                    mvp_es_valido = False
                    for integrante in torneo["integrantes"][ganador]:
                        if (
                            integrante["Nombre"] == nombre_mvp
                            and integrante["Apellido"] == apellido_mvp
                        ):
                            mvp_es_valido = True
                            break

                    if not mvp_es_valido:
                        print(
                            f"Error - {nombre_mvp} {apellido_mvp} no es un integrante de {ganador}. Intente nuevamente."
                        )
                        pausa()
                        limpiar_pantalla()
                    else:
                        print(
                            f"El MVP {nombre_mvp} {apellido_mvp} se ingresó correctamente."
                        )
                        pausa()
                        limpiar_pantalla()
                        break
                resultado["ganador"] = ganador
                resultado["mvp"] = mvp

            guardar_torneos(archivo, torneos)
            print("Resultados ingresados correctamente")
            return None

    print("Error: Torneo no encontrado.")
    return None

def mostrar_resultados(archivo: str, torneo_nombre: str) -> None:
    """
    Precondición: Debe haber al menos un resultado ya registrado en el torneo, recibe como parametro el nombre del archivo y el nombre del torneo (str)
    Argumentos: Muestra los participantes y los resultados de cada ronda que hay en el JSON.
    Postcondición: Se muestran las estadísticas actuales del torneo.
    """
    limpiar_pantalla()
    torneos = cargar_torneos(archivo)

    # Buscar el torneo en la lista de torneos cargados
    for torneo in torneos.get('torneos', []):
        if torneo.get('nombre_torneo') == torneo_nombre:
            print(f"Estadísticas del torneo: {torneo_nombre}\n")

            # Mostrar equipos participantes
            print("Equipos participantes:")
            for equipo in torneo.get('equipos', []):
                print(f" - {equipo}")

            # Mostrar rondas y resultados
            for ronda in torneo.get('rondas', []):
                print(f"\nRonda: {ronda['ronda']}")
                for resultado in ronda.get('resultados', []):
                    print(f"{resultado['equipo1']} vs {resultado['equipo2']}:")
                    print(f"  Ganador: {resultado.get('ganador', 'No determinado')}")
                    print(f"  MVP: {resultado.get('mvp', 'No determinado')}")

            return None

    print(f"No se encontró el torneo {torneo_nombre}.")
    return None

def generar_mvp(archivo: str, torneo_nombre: str) -> None:
    """
    Precondición:Debe existir el torneo y el JSON con los datos y estructura adecuada para la función,
    -------------Recibe como parametros el archivo (str), el nombre del torneo (str)


    Argumentos:Muesta en pantalla el MVP del torneo y la cantidad de veces que fue seleccionado, si no se completaron suficientes rondas
    ----------Si no se registraron rondas o si el torneo no existe en el archivo, se muestra un mensaje de error.

    Postcondición: La funcion no retorna nada.
    """
    limpiar_pantalla()
    print("Generar MVP\n")

    torneos = cargar_torneos(archivo)

    try:
        for torneo in torneos["torneos"]:
            if torneo["nombre_torneo"] == torneo_nombre:
                rondas = torneo["rondas"]
                if len(rondas) == 0:
                    print("Error: No se han registrado rondas para este torneo.")
                    pausa()
                    return

                contador_mvp = {}
                for ronda in rondas:
                    for resultado in ronda["resultados"]:
                        mvp = resultado["mvp"]
                        if mvp != "No determinado":
                            if mvp not in contador_mvp:
                                contador_mvp[mvp] = 0
                            contador_mvp[mvp] += 1

                mvp_torneo = ""
                max_mvp = 0
                for jugador in contador_mvp:
                    if contador_mvp[jugador] > max_mvp:
                        max_mvp = contador_mvp[jugador]
                        mvp_torneo = jugador

                print(
                    f"MVP del torneo '{torneo_nombre}': {mvp_torneo} (Total MVPs: {max_mvp})"
                )
                pausa()
                return

    except KeyError:
        print("Error: No se cargaron datos suficientes para generar el MVP.")
        pausa()
        return

    print(f"Error: Torneo '{torneo_nombre}' no encontrado.")
    pausa()
    return


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
    print("3- Mostrar resultados del torneo")
    print("4-Generar MVP")
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
                    input(
                        f"El juego seleccionado fue el {juego}.\nEnter para continuar."
                    )
                elif op == 2:
                    limpiar_pantalla()
                    cargar_equipo(archivo_json, nombre_torneo)
                elif op == 3:
                    torneos = cargar_torneos("resultados_torneos.json")
                    equipos_finalizados = 0
                    equipos_completos = []
                    while equipos_finalizados < 8:
                        limpiar_pantalla()
                        for torneo in torneos["torneos"]:
                            print(torneo["equipos"])
                        nombre_equipo = input(
                            "\nIngrese el nombre del equipo para agregar el integrante(0 para salir): "
                        )
                        if nombre_equipo == "0":
                            print("saliendo.")
                            pausa()
                            break

                        if nombre_equipo not in torneo["equipos"]:
                            print(
                                "\nError - Equipo no encontrado. Ingrese el nombre de un equipo registrado.\n"
                            )
                            pausa()
                            continue

                        if nombre_equipo in equipos_completos:
                            print(
                                "\nYa se registraron los integrantes de este equipo, intente con otro."
                            )
                            pausa()
                            continue

                        cargar_integrantes(archivo_json, nombre_torneo, nombre_equipo)
                        equipos_completos.append(nombre_equipo)
                        equipos_finalizados += 1
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
            print("Dato inválido, ingrese un número.")
            pausa()
        else:
            if op >= 0 and op <= 5:
                if op == 0:
                    break
                if op == 1:
                    limpiar_pantalla()
                    elegir_enfrentamientos(archivo_json, nombre_torneo)
                    pausa()

                elif op == 2:
                    while True:
                        limpiar_pantalla()
                        print(
                            "Rondas \n1. Cuartos \n2. Semi-Final \n3. Final \n4. Tercer-Lugar"
                        )
                        try:
                            ronda_a_actualizar = int(
                                input(
                                    "Ingrese el número de la ronda que desea actualizar (-1 salir): "
                                )
                            )
                        except ValueError:
                            print("Dato inválido, ingrese un número.")
                            pausa()
                        else:
                            if ronda_a_actualizar == -1:
                                break

                            if ronda_a_actualizar in (1, 2, 3, 4):
                                ingresar_resultado_ronda(
                                    nombre_torneo, ronda_a_actualizar, archivo_json
                                )
                                pausa()
                            else:
                                print("Ingrese un número que corresponda a una ronda.")
                                pausa()

                elif op == 3:
                    limpiar_pantalla()
                    mostrar_resultados(archivo_json, nombre_torneo)
                    pausa()

                elif op == 4:
                    limpiar_pantalla()
                    generar_mvp(archivo_json, nombre_torneo)
                    pausa()

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
            print("Dato inválido, ingrese un número.")
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
