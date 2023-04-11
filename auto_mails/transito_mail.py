import datetime
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from herramientas.create_email import *

# Configurar los datos del correo electrónico
remitente = "***"
destinatarios = "; ".join(["***"])

fecha_actual = datetime.datetime.now().strftime("%d%b%y").upper()
asunto = f"CARGA EN TRANSITO OB-709 - {fecha_actual}"

cuerpo = (
    "Estimados,\n\n"
    "Solicito confeccionar hojas de seguridad correspondientes para las cargas de exportación.\n\n"
    "Adjunto encontrarán el manifiesto correspondiente para su revisión.\n\n"
    "Agradeceremos su pronta respuesta.\n\n"
    "Atentamente,"
)

# Crear el correo electrónico
mensaje = create_email(remitente, destinatarios, asunto, cuerpo)

# Lista de tuplas con información de archivos a adjuntar
archivos_adjuntos = [
    (
        os.path.join(os.path.expanduser("~"), "CargoBot Files"),
        r"(?i)tto\.pdf$",
    ),
]

# Adjuntar archivos al mensaje
for path, regex in archivos_adjuntos:
    attach_files(mensaje, path, regex)

# Guardar el borrador
save_draft(mensaje)
