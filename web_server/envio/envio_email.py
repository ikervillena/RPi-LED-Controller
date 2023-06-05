import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(subject, mensaje, destinatario):

    # Cuenta y contraseña
    remitente = "deustotickets@outlook.es"
    contraseña = "VentaDeEntradas"

    # Configuración del servidor SMTP
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587
    
    # Crear objeto MIMEMultipart para el correo
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = subject

    # Agregar el cuerpo del mensaje al objeto MIMEMultipart
    msg.attach(MIMEText(mensaje, 'plain'))

    # Crear conexión segura con el servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Iniciar sesión en la cuenta de correo
    server.login(remitente, contraseña)

    # Enviar el correo electrónico
    server.sendmail(remitente, destinatario, msg.as_string())

    # Cerrar la conexión con el servidor SMTP
    server.quit()
