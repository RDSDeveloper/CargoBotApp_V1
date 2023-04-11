# Este script genera el menu principal y sus botones conectados a los scripts de la app

import os
import subprocess

from tkinter import ttk
from ttkthemes import ThemedTk
# crea una ventana principal
root = ThemedTk(theme="itft1")

# define la función para el botón
def button_clicked(path):
    subprocess.run(["python", path])


#Creamos botones de accion

mails_boa_expo_action_buttons = [
    ttk.Button(root, text="Manifiesto Provisorio", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_mails", "manifiesto_provisorio_mail.py"))),
    ttk.Button(root, text="Manifiesto Final", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_mails", "manifiesto_final_mail.py"))),
    ttk.Button(root, text="Datos de Exportación", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_mails", "datos_exportacion_mail.py"))),
    ttk.Button(root, text="Novedades Sin Correo", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_mails", "novedades_sin_correo_mail.py"))),
    ttk.Button(root, text="Novedades Con Correo", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_mails", "novedades_con_correo_mail.py"))),
    ttk.Button(root, text="Solicitar Transmisión", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_mails", "solicitud_transmision_mail.py")))
]

general_mails_action_buttons = [
    ttk.Button(root, text="Pedido de equipos", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_mails", "pedido_equipos_mail.py"))),
    ttk.Button(root, text="Carga en tránsito", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_mails", "transito_mail.py")))
]

mails_boa_notoc_action_buttons = [
    ttk.Button(root, text="Notoc Briefing", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_mails", "notoc_briefing_mail.py"))),
    ttk.Button(root, text="Notoc Firmado", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_mails", "notoc_firmado_mail.py"))),
    ttk.Button(root, text="CheckList", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_mails", "checklist_mail.py")))
]

import_manifest_retriever_action_buttons = [
    ttk.Button(root, text="OB-700 Manifest", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_mails", "700_file_retriever.py"))),
    ttk.Button(root, text="OB-708 Manifest", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_mails", "708_file_retriever.py")))
]

export_manifest_action_buttons = [
    ttk.Button(root, text="Fusionar manifiestos", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_manifest", "auto_merge.py"))),
]

flight_location_action_buttons = [
    ttk.Button(root, text="Flight Radar Position", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_vuelo", "flight_radar.py"))),
    ttk.Button(root, text="Tams Position", command=lambda: button_clicked(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "auto_vuelo", "tams.py"))),
]