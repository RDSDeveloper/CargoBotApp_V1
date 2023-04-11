import pyautogui, time, ctypes

# Obtener la resolución de la pantalla
ancho, alto = pyautogui.size()

# Evitar mayusculas
def mayusculas_activas():
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL) & 0x01

if mayusculas_activas():
    pyautogui.press('capslock')
else:
    pass

# Cierre de emergencia, llevar mouse a la esquina superior izquierda
pyautogui.FAILSAFE = True

def abrir_chrome():
    pyautogui.hotkey("winleft", "s")
    time.sleep(1)
    pyautogui.write("chrome")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey('winleft', 'up') # Maximizar ventana
    time.sleep(1)

def ingresar_sistema():
    pyautogui.write("http://sms.obairlines.bo/cargaInter/Account/LogOn?ReturnUrl=%2fcargaInter%2f")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down") 
    time.sleep(1)
    pyautogui.press("enter") 
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab") 
    time.sleep(1)
    pyautogui.press("enter") 
    time.sleep(1)

def flights_ingreso():
    pyautogui.moveTo(1605, 148)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press("tab") 
    time.sleep(1)
    pyautogui.press("enter") 
    time.sleep(1)

def registrar_vuelo():
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyautogui.write('registrar vuelo')
    time.sleep(1)
    pyautogui.hotkey("shift", 'tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

def nuevo_vuelo(matricula, numero):
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(matricula)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(numero)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write("s") # Santa Cruz
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    #pyautogui.press('enter')



abrir_chrome()
ingresar_sistema()
flights_ingreso()
registrar_vuelo()
nuevo_vuelo("3151", "709")


print("Done")