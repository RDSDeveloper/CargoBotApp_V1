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

asunto = f"DATOS // OB-709 - {fecha_actual}"
cuerpo = (
    "Buenas tardes Estimados\n\n"
    "Adjunto encontrarán el Manifiesto y las copias de los AWB's correspondientes al vuelo en referencia.\n\n"
    "Por favor, confirmen la recepción de este correo.\n\n"
    "Saludos cordiales,"
)


# Crear el correo electrónico
mensaje = create_email(remitente, destinatarios, asunto, cuerpo)

# Lista de tuplas con información de archivos a adjuntar
archivos_adjuntos = [
    (
        os.path.join(os.path.expanduser("~"), "CargoBot Files"),
        r"(?i).*MANIFIESTO EXPO.*\.pdf$",
    ),
    (os.path.join(os.path.expanduser("~"), "CargoBot Files"), r"(?i).*awb.*\.pdf$"),
]

# Adjuntar archivos al mensaje
for path, regex in archivos_adjuntos:
    attach_files(mensaje, path, regex)

# Guardar el borrador
save_draft(mensaje)
