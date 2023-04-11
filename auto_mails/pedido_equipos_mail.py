import datetime
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from herramientas.create_email import create_email, save_draft

# Configurar los datos del correo electrónico
remitente = "***"
destinatarios = "; ".join(
    [
        "***",
    ]
)

fecha_actual = datetime.datetime.now().strftime("%d%b%y").upper()
asunto = f"PEDIDO DE EQUIPOS PARA BOA - OB709 - {fecha_actual}"

cuerpo = (
    "Buenos días,\n\n"
    "Por favor enviar lo antes posible los siguientes EQUIPOS para el armado del vuelo de BOA del día de hoy:\n\n"
    "- Bodega Seca: \n"
    "- Bodega Perecedero: \n\n"
    "Muchas gracias.\n\n"
    "Saludos."
)

# Crear el correo electrónico
mensaje = create_email(remitente, destinatarios, asunto, cuerpo)

# Guardar el borrador
save_draft(mensaje)
