import tkinter as tk

def user_input():
    # Obtener valor ingresado en el widget de entrada de texto
    valor = entrada.get()
    # Devolver el valor ingresado
    return valor

# Crear ventana
ventana = tk.Tk()
ventana.title("Ingrese el numero de vuelo:")

# Crear widget de entrada de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Crear botón de aceptar
boton_aceptar = tk.Button(ventana, text="Aceptar", command=ventana.quit)
boton_aceptar.pack()

# Ejecutar la ventana y esperar a que el usuario ingrese la entrada
ventana.mainloop()

# Obtener el valor ingresado por el usuario
valor = user_input()
