import datetime
import os
import re
import PyPDF2
import win32api

# Definimos la ruta de la carpeta donde se encuentran los archivos PDF
ruta_archivos = os.path.join(os.path.expanduser("~"), "CargoBot Files")

# Definimos la ruta de destino del archivo PDF fusionado
ruta_destino = os.path.join("C:", os.sep, "Users", "Cross01", "Desktop", "Archivos del dia", "MANIFIESTO EXPO - {} - OB709.pdf")

# Buscamos todos los archivos que cumplan con la condición especificada
regex = r"(?i).*manifest.*\.pdf$"
pdf_files = [os.path.join(ruta_archivos, f) for f in os.listdir(ruta_archivos) if re.match(regex, f)]

# Iniciamos el objeto PdfFileMerger y agregamos los archivos PDF
pdf_merger = PyPDF2.PdfMerger()
for pdf_file in pdf_files:
    with open(pdf_file, 'rb') as f:
        pdf_merger.append(f)

# Obtenemos la fecha actual y la formateamos
fecha = datetime.datetime.now().strftime("%d%b%y").upper()

# Escribimos el archivo fusionado en la ubicación de destino especificada
with open(ruta_destino.format(fecha), 'wb') as f:
    pdf_merger.write(f)

# Imprimimos el archivo físicamente
#win32api.ShellExecute(
#    0, "print", ruta_destino.format(fecha), f'/d:"Nombre de la impresora"', ".", 0
#)
