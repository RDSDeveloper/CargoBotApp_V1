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
asunto = f"NOTOC // OB-709 - {fecha_actual}"

cuerpo = (
    "Estimados Colegas,\n\n"
    "Adjunto se encuentra el NOTOC y AWB del Vuelo de Referencia OB709 para su revisión y consideración. Solicitamos su confirmación de recepción.\n\n"
    "Les informamos que al finalizar el vuelo, se requiere el envío del NOTOC firmado por el capitán para nuestros registros.\n\n"
    "Agradecemos su atención en este asunto y quedamos a la espera de su pronta respuesta.\n\n"
    "Atentamente,"
)

# Crear el correo electrónico
mensaje = create_email(remitente, destinatarios, asunto, cuerpo)

# Lista de tuplas con información de archivos a adjuntar
archivos_adjuntos = [
    (
        os.path.join(os.path.expanduser("~"), "CargoBot Files"),
        r"(?i)notoc\.pdf$",
    ),
]

# Adjuntar archivos al mensaje
for path, regex in archivos_adjuntos:
    attach_files(mensaje, path, regex)

# Guardar el borrador
save_draft(mensaje)
