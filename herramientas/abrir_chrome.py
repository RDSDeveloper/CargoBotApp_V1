# Este script able google chrome con pyautogui

import pyautogui
import time


def abrir_chrome():
    pyautogui.hotkey("winleft", "s")
    time.sleep(1)
    pyautogui.write("chrome")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey('winleft', 'up') # Maximizar ventana
    time.sleep(1)