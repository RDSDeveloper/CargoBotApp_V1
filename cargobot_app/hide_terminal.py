# Este script elimina la ventana de la terminal cuando el usuario inicie la app
# ALERTA: Solo activar en deploy, no en desarrollo o cierra el VSCODE

import sys

def hide_terminal():
    if sys.platform == "win32":
        import win32gui
        import win32con
        win = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(win, win32con.SW_HIDE)