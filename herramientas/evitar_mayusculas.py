# Evitar mayusculas

import ctypes
import pyautogui

def mayusculas_activas():
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL) & 0x01

if mayusculas_activas():
    pyautogui.press('capslock')
else:
    pass