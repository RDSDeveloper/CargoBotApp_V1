# Este script genera la carpeta CargoBot Files que va a contener archivos extraidos y adjuntables.

import os
import platform
import subprocess

import tkinter.messagebox as tkmsg


def create_cargobot_files_folder():
    # Obtener la ruta de la carpeta "CargoBot Files" en la carpeta de inicio del usuario actual
    folder_path = os.path.join(os.path.expanduser("~"), "CargoBot Files")

    # Comprobar si la carpeta "CargoBot Files" existe
    if not os.path.exists(folder_path):
        # Si la carpeta no existe, crearla
        os.makedirs(folder_path)

    # Mostrar mensaje para el usuario
    tkmsg.showinfo("Importante", "Esta carpeta 'CARGOBOT FILES' es el lugar para guardar los archivos importantes.")

    # Abrir la carpeta "CargoBot Files" en el explorador de archivos
    if platform.system() == "Windows":
        # Para Windows
        subprocess.Popen('explorer "{0}"'.format(folder_path))
    elif platform.system() == "Darwin":
        # Para macOS
        subprocess.Popen(["open", folder_path])
    else:
        # Para Linux
        subprocess.Popen(["xdg-open", folder_path])