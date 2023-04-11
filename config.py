# Este script establece a la carpeta herramientas como ruta accesible e importa los scripts de la misma para su reutilizacion. 

import os
import sys

# Agregar la ruta relativa de la carpeta herramientas al sys.path
ruta_local = os.path.dirname(os.path.abspath(__file__))
ruta_herramientas = os.path.join(ruta_local, 'herramientas')
sys.path.append(ruta_herramientas)

# Agrega aquí todas las importaciones de los scripts que se encuentran en la carpeta herramientas

from herramientas import abrir_chrome, evitar_mayusculas, user_input, ingresar_pagina_web


