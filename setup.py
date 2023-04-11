# Este script configura la creacion de la app ejecutable .exe

from cx_Freeze import setup, Executable

# Reemplaza "nombre_archivo.py" con el nombre de tu archivo principal de Python
executables = [Executable("cargobot_app/cargobot_startapp.py")]

# Reemplaza "nombre_app" con el nombre que deseas darle a tu aplicación
setup(name="Cargo Bot",
        version="1.0",
        description="Descripción de tu aplicación",
        executables=executables,
        options={
            "build_exe": {
                "include_files": [
                    "auto_vuelo",
                    "auto_boa",
                ]
            }
        })