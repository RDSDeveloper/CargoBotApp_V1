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
asunto = f"DATOS //  OB-708  VVI - EZE // - {fecha_actual}"

cuerpo = (
    "Estimados,\n\n"
    "A la fecha aún no hemos recibido la transmisión del vuelo en referencia.\n\n"
    "Solicitamos con urgencia la realización de la misma y el envío de los manifiestos correspondientes en tiempo y forma, tal como lo exige nuestra aduana.\n\n"
    "Quedamos a la espera de su pronta respuesta.\n\n"
    "Atentamente,"
)

# Crear el correo electrónico
mensaje = create_email(remitente, destinatarios, asunto, cuerpo)

# Guardar el borrador
save_draft(mensaje)
