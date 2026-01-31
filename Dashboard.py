import os
import subprocess

# ==============================================
# Dashboard POO - Universidad Estatal Amazónica
# Autora: Bélgica Jomayra Licto Timbila
# Descripción: Dashboard personalizado para organizar
# scripts y actividades de la asignatura Programación
# Orientada a Objetos. Contiene menú principal, submenús,
# visualización y ejecución de scripts de Python.
# ==============================================

# Función para mostrar el código de un script
# Parámetro: ruta del script (string con la ruta al archivo .py)
# Retorna: el contenido del archivo como texto e imprime en pantalla
def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un archivo .py en la consola.
    Parámetros:
        ruta_script (str): Ruta del archivo Python.
    Retorna:
        codigo (str) si se pudo leer, None en caso contrario.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

# Función para ejecutar un script de Python
def ejecutar_codigo(ruta_script):
    """
    Ejecuta un archivo Python en una terminal separada.
    Funciona en Windows y sistemas Unix-based.
    """
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix/Linux/Mac
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

# Función del menú principal
def mostrar_menu():
    """
    Muestra el menú principal del dashboard y permite
    seleccionar unidades de la asignatura.
    """
    ruta_base = os.path.dirname(__file__)  # Carpeta del dashboard

    unidades = {
        '1': 'Unidad 1 - Fundamentos de POO',
        '2': 'Unidad 2 - Clases y Objetos'
    }

    while True:
        print("\nBienvenida al Dashboard de Programación Orientada a Objetos")
        # Personalización: nombre del estudiante
        print("Estudiante: Bélgica Jomayra Licto Timbila")
        print("\nMenu Principal - Dashboard POO")

        # Mostrar las unidades disponibles
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")

        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("Opción no válida. Intenta de nuevo.")

# Función para mostrar submenú con subcarpetas de cada unidad
def mostrar_sub_menu(ruta_unidad):
    """
    Lista las subcarpetas dentro de una unidad y permite
    seleccionar scripts para ver o ejecutar.
    """
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")

        if eleccion_carpeta == '0':
            break
        else:
            try:
                indice = int(eleccion_carpeta) - 1
                if 0 <= indice < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[indice]))
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

# Función para mostrar scripts dentro de una subcarpeta
def mostrar_scripts(ruta_sub_carpeta):
    """
    Lista los scripts Python dentro de la subcarpeta,
    permite ver su código y ejecutarlos.
    """
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts disponibles:")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")

        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return  # Volver al menú principal
        else:
            try:
                indice = int(eleccion_script) - 1
                if 0 <= indice < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida.")
                        input("\nPresiona Enter para volver al menú de scripts...")
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

# Ejecutar el dashboard si se llama directamente
if __name__ == "__main__":
    mostrar_menu()
