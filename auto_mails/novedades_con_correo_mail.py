import datetime
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from herramientas.create_email import *

# Configurar los datos del correo electrónico
remitente = "***"
destinatarios = "; ".join(
    [
        "***",
    ]
)

fecha_actual = datetime.datetime.now().strftime("%d%b%y").upper()
asunto = f"NOVEDADES OB709 EZEVVI - {fecha_actual}"

cuerpo = (
    "Buenas tardes Estimados\n\n"
    "Adjunto encontrarán el Manifiesto y las copias de los AWB's correspondientes al vuelo en referencia.\n\n"
    "Hubo correo argentino.\n\n"
    "Guìas no voladas:\n"
    "   930-00000000:\n\n"
    "Guìas voladas con irregularidades:\n"
    "   930-00000000:\n\n"
    "Saludos cordiales"
)

# Crear el correo electrónico
mensaje = create_email(remitente, destinatarios, asunto, cuerpo)

# Lista de tuplas con información de archivos a adjuntar
archivos_adjuntos = [
    (
        os.path.join(os.path.expanduser("~"), "CargoBot Files"),
        r"(?i).*final.*\.pdf$",
        os.path.join(os.path.expanduser("~"), "CargoBot Files"),
        r"(?i).*awb.*\.pdf$",
        os.path.join(os.path.expanduser("~"), "CargoBot Files"),
        r"(?i).*cn.*\.pdf$",
        os.path.join(os.path.expanduser("~"), "CargoBot Files"),
        r"(?i).*correo.*\.xls$",
    ),
]

# Adjuntar archivos al mensaje
for path, regex in archivos_adjuntos:
    attach_files(mensaje, path, regex)

# Guardar el borrador
save_draft(mensaje)
