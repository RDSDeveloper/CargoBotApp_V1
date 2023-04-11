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

def buscar_aerodromo():
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    for i in range(3):
        pyautogui.press("e")                      
        time.sleep(0.5)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)


def buscar_vuelo(valor):
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyautogui.write(valor)
    time.sleep(1)
    pyautogui.hotkey("shift", 'tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')

valor = user_input.user_input()

evitar_mayusculas.mayusculas_activas()
user_input.user_input()
abrir_chrome.abrir_chrome()
ingresar_pagina_web.ingresar_pagina("http://www.tams.com.ar/organismos/Vuelos.aspx")
buscar_aerodromo()
buscar_vuelo(valor)
