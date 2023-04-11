import win32com.client

from herramientas import file_finder


def create_email(sender_email, recipient_emails, subject, body):
    outlook = win32com.client.Dispatch("Outlook.Application")
    mensaje = outlook.CreateItem(0)
    mensaje.To = recipient_emails
    mensaje.Subject = subject
    mensaje.Body = body
    return mensaje


def attach_files(mensaje, attachment_path, attachment_regex):
    attachment_file = file_finder.FileFinder(
        attachment_path, attachment_regex
    ).find_files()[0]
    mensaje.Attachments.Add(attachment_file)


def save_draft(mensaje):
    mensaje.Save()
    print("Borrador creado y guardado en la carpeta de borradores")
