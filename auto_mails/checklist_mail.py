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
asunto = f"CheckList // OB-709 - {fecha_actual}"

cuerpo = (
    "Buenos días colegas,\n\n"
    "Adjunto encontrarán el CheckList firmado del vuelo de referencia.\n\n"
    "Por favor, confirmar la recepción del presente correo.\n\n"
    "Muchas gracias y saludos cordiales."
)

# Crear el correo electrónico
mensaje = create_email(remitente, destinatarios, asunto, cuerpo)

attachment_path = os.path.join(os.path.expanduser("~"), "CargoBot Files")
attachment_regex = r"(?i)cl\.pdf$"

attach_files(mensaje, attachment_path, attachment_regex)

# Guardar el borrador
save_draft(mensaje)
