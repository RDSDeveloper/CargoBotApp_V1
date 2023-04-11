import pyautogui
import time

def ingresar_pagina(pagina):
    pyautogui.write(pagina)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)