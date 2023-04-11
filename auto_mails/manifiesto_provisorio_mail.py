import datetime
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from herramientas.create_email import create_email, save_draft

# Configurar los datos del correo electrónico
remitente = "***"

destinatario = "; ".join(
    [
        "***",
    ]
)

fecha_actual = datetime.datetime.now().strftime("%d%b%y").upper()
asunto = f"** MANIFIESTO PROVISORIO **  OB-709 - {fecha_actual}"

cuerpo = (
    "Estimados,\n\n"
    "En este mail encontrarán la planificación del Vuelo OB-709 correspondiente a la fecha indicada. Por favor, no duden en contactarnos por esta vía si tienen alguna consulta al respecto.\n\n"
    "Agradeceremos que confirmen la recepción de este correo.\n\n"
    "Equipos:\n"
    "Kilos:\n\n"
    "Saludos cordiales,"
)

# Crear el correo electrónico
mensaje = create_email(remitente, destinatario, asunto, cuerpo)

# Guardar el borrador
save_draft(mensaje)
