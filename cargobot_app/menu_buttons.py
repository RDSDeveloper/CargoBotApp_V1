# Este script genera los botones de menu principales y la funcion de volver

import tkinter as tk
from tkinter import ttk

from action_buttons import *

# crea una función para mostrar los botones y ocultar el botón "Mails"
def show_buttons(buttons):
    for button in buttons:
        button.pack()
    general_mails_main_button.pack_forget()
    mails_boa_expo_main_button.pack_forget()
    mails_boa_notoc_main_button.pack_forget()
    import_manifest_retriever_main_button.pack_forget()
    export_manifest_main_button.pack_forget()
    flight_location_main_button.pack_forget()
    return_button.pack(side=tk.BOTTOM)


# crea una función para volver a la pantalla de inicio
def back_to_home():
    for button in general_mails_action_buttons:
        button.pack_forget()
    for button in mails_boa_expo_action_buttons:
        button.pack_forget()
    for button in mails_boa_notoc_action_buttons:
        button.pack_forget()
    for button in import_manifest_retriever_action_buttons:
        button.pack_forget()
    for button in export_manifest_action_buttons:
        button.pack_forget()
    for button in flight_location_action_buttons:
        button.pack_forget()
    general_mails_main_button.pack()
    mails_boa_expo_main_button.pack()
    mails_boa_notoc_main_button.pack()
    import_manifest_retriever_main_button.pack()
    export_manifest_main_button.pack()
    flight_location_main_button.pack()
    return_button.pack_forget() # oculta el botón "Volver"

# Creamos botones generales
general_mails_main_button = ttk.Button(root, text="Mails Generales", command=lambda: show_buttons(general_mails_action_buttons))
general_mails_main_button.pack()

mails_boa_expo_main_button = ttk.Button(root, text="Mails BOA", command=lambda: show_buttons(mails_boa_expo_action_buttons))
mails_boa_expo_main_button.pack()

mails_boa_notoc_main_button = ttk.Button(root, text="NOTOC BOA", command=lambda: show_buttons(mails_boa_notoc_action_buttons))
mails_boa_notoc_main_button.pack()

import_manifest_retriever_main_button = ttk.Button(root, text="Manifiestos de Importacion", command=lambda: show_buttons(import_manifest_retriever_action_buttons))
import_manifest_retriever_main_button.pack()

export_manifest_main_button = ttk.Button(root, text="Manifiestos de Exportación", command=lambda: show_buttons(export_manifest_action_buttons))
export_manifest_main_button.pack()

flight_location_main_button = ttk.Button(root, text="Ubicacion del vuelo", command=lambda: show_buttons(flight_location_action_buttons))
flight_location_main_button.pack()

# crea un botón "Volver" para volver a la pantalla de inicio
return_button = ttk.Button(root, text="Volver", command=back_to_home)