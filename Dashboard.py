import os
import subprocess

# ==========================================
# Función: mostrar_codigo
# Descripción: Muestra en consola el contenido de un script Python
# Parámetro: ruta_script (str) → ruta del archivo .py a mostrar
# Retorna: el contenido del archivo en texto o None si ocurre un error
# ==========================================
def mostrar_codigo(ruta_script):
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

# ==========================================
# Función: ejecutar_codigo
# Descripción: Ejecuta un script Python en una nueva terminal
# Parámetro: ruta_script (str) → ruta del archivo .py a ejecutar
# Retorna: None
# ==========================================
def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

# ==========================================
# Función: mostrar_menu
# Descripción: Muestra el menú principal del dashboard
# Permite seleccionar la unidad a explorar
# ==========================================
def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    # Diccionario de unidades: (Nombre del menú, nombre real de carpeta)
    unidades = {
        '1': ('Unidad 1 - Fundamentos de POO', 'Unidad 1'),
        '2': ('Unidad 2 - Clases y Objetos', 'Unidad 2')
    }

    while True:
        print("\nBienvenida al Dashboard de Programación Orientada a Objetos")
        print("Estudiante: Bélgica Jomayra Licto Timbila")  # <- Bienvenida personalizada

        print("\nMenu Principal - Dashboard POO")
        for key in unidades:
            print(f"{key} - {unidades[key][0]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad][1]))
        else:
            print("Opción no válida. Intenta de nuevo.")

# ==========================================
# Función: mostrar_sub_menu
# Descripción: Muestra subcarpetas dentro de una unidad
# Permite seleccionar subcarpetas para ver scripts
# ==========================================
def mostrar_sub_menu(ruta_unidad):
    if not os.path.exists(ruta_unidad):
        print(f"La ruta {ruta_unidad} no existe.")
        return

    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        try:
            indice = int(eleccion_carpeta) - 1
            if 0 <= indice < len(sub_carpetas):
                mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[indice]))
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Opción no válida. Intenta de nuevo.")

# ==========================================
# Función: mostrar_scripts
# Descripción: Muestra scripts Python en una subcarpeta
# Permite ver el código y ejecutar scripts
# ==========================================
def mostrar_scripts(ruta_sub_carpeta):
    if not os.path.exists(ruta_sub_carpeta):
        print(f"La ruta {ruta_sub_carpeta} no existe.")
        return

    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return
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
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Intenta de nuevo.")

# ==========================================
# Ejecutar el dashboard
# ==========================================
if __name__ == "__main__":
    mostrar_menu()

