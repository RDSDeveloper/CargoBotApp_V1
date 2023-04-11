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
    pyautogui.write("***")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.write("***")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter") 
    time.sleep(3)

def aprobador_acceso():
    for i in range(3):
        pyautogui.press("tab")
        time.sleep(1)
    time.sleep(1)
    pyautogui.press("enter")                    
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(10)

def seleccion_vuelo(vuelo):
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyautogui.write(vuelo)      
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey("shift", 'tab')
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)


def aprobar_vuelo():
    for i in range(2):
        pyautogui.press("tab")                      
        time.sleep(0.2)   
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    #pyautogui.press('enter')
    #time.sleep(1)

valor = user_input.user_input()

evitar_mayusculas.mayusculas_activas()
user_input.user_input()
abrir_chrome.abrir_chrome()
ingresar_pagina_web.ingresar_pagina("http://seguridad.tca.aero/seguridad/tca-seguridad/login.jsp")
ingresar_sistema()
aprobador_acceso()
seleccion_vuelo(valor)
aprobar_vuelo()


print("Done")