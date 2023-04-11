import datetime
import email
import imaplib
import os
import smtplib
import win32api
import win32print

class EmailRetriever:
    def __init__(self, email_address, email_password):
        self.email_address = email_address
        self.email_password = email_password

    def session_started(self, smtp_server, smtp_port):
        # Establecer una conexión SMTP y autenticarse
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.starttls()
        smtp.login(self.email_address, self.email_password)

        # Devolver las credenciales de inicio de sesión
        return smtp

    def imap_auth(self, imap_server, imap_port):
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        mail.login(self.email_address, self.email_password)
        mail.select("inbox")

        today = datetime.date.today()
        two_days_ago = today - datetime.timedelta(days=3)
        today_str = today.strftime("%d-%b-%Y")
        two_days_ago_str = two_days_ago.strftime("%d-%b-%Y")
        search_str = (
            f'(SINCE "{two_days_ago_str}" BEFORE "{today_str}" SUBJECT "OB-708")'
        )

        result, data = mail.search(None, search_str)

        email_ids = data[0].split()

        for email_id in email_ids:
            result, data = mail.fetch(email_id, "(RFC822)")

            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)

            for part in email_message.walk():
                if part.get_content_maintype() == "multipart":
                    continue

                filename = part.get_filename()
                if not filename:
                    continue

                file_extension = os.path.splitext(filename)[1]
                if file_extension not in [".xls", ".xlsx", ".pdf"]:
                    continue

                file_content = part.get_payload(decode=True)
                file_name = f'OB708-{today.strftime("%d%b")}{file_extension}'
                # Obtener la ruta de la carpeta "CargoBot Files" en la carpeta de inicio del usuario actual
                folder_path = os.path.join(os.path.expanduser("~"), "CargoBot Files")

                file_path = os.path.join(folder_path, file_name)

                with open(file_path, "wb") as f:
                    f.write(file_content)

                print(f"Archivo extraído y guardado en {file_path}.")

                # Imprimir el archivo físicamente
                win32api.ShellExecute(
                    0, "print", file_path, f'/d:"Nombre de la impresora"', ".", 0
                )

        mail.close()
        mail.logout()


if __name__ == "__main__":
    email_address = "***"
    email_password = "***"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    imap_server = "imap.gmail.com"
    imap_port = 993

email_retriever = EmailRetriever(email_address, email_password)
smtp = email_retriever.session_started(smtp_server, smtp_port)
email_retriever.imap_auth(imap_server, imap_port)
smtp.quit()
