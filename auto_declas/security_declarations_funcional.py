import time
import pyautogui
import sys
import os

ruta_local = os.path.dirname(os.path.abspath(__file__))
ruta_config = os.path.join(ruta_local, '..')
sys.path.append(ruta_config)

from config import abrir_chrome, evitar_mayusculas, user_input, ingresar_pagina_web

# Cierre de emergencia, llevar mouse a la esquina superior izquierda
pyautogui.FAILSAFE = True

def ingresar_sistema():
    time.sleep(1)
    pyautogui.write("***")
    pyautogui.press("tab")
    pyautogui.write("***")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter") 
    time.sleep(2)

def acceder_busqueda_declaraciones():
    for i in range(3):
        pyautogui.press("tab")
        time.sleep(1)
    pyautogui.press("enter")                    
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)

def ingresar_declaracion(guia):
    pyautogui.write(guia)      
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("right")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)

def buscar_consultar():
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyautogui.write('Consultar')
    time.sleep(1)
    pyautogui.hotkey("shift", 'tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

def acceder_detalle_declaracion():
    for i in range(3):
        pyautogui.press("tab")                      
        time.sleep(0.2)       
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)

def descargar_declaracion(guia):
    for i in range(8):                      
        pyautogui.press("tab")
        time.sleep(0.2)         
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write(guia)
    time.sleep(1) 
    pyautogui.press("enter")          
    time.sleep(1) 

def imprimir_declaracion():
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")        

def retroceder_paginas():
    for i in range(2):                      
        pyautogui.hotkey("altleft", "left")
        time.sleep(0.5) 
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'f')

def entrar_nueva_consulta():
    pyautogui.write('Otra consulta')
    time.sleep(1)
    pyautogui.hotkey("shift", 'tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)



# Añadir guias:
#guias = ["93000987722", "93001037934"]

guias_totales = ["93000987722", "93001037934"]

# while True:
#     try:
#         contador = int(user_input.user_input())
#         if contador > 0:
#             print("Numero correcto")
#             break
#         else:
#             print("Debe ingresar un número positivo.")
#     except ValueError:
#         print("Debe ingresar un número válido.")


# while len(guias_totales) < contador:
#     guia = user_input.user_input()
#     guias_totales.append(guia)

evitar_mayusculas.mayusculas_activas()
abrir_chrome.abrir_chrome()
ingresar_pagina_web.ingresar_pagina("http://seguridad.tca.aero/seguridad/tca-seguridad/login.jsp")
ingresar_sistema()


for guia in guias_totales:
    ingresar_declaracion(guia)
    buscar_consultar()
    acceder_detalle_declaracion()
    descargar_declaracion(guia)
    imprimir_declaracion()
    retroceder_paginas()
    entrar_nueva_consulta()

print("Done")