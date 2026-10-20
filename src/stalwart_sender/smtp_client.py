"""Conexión TLS y entrega SMTP."""

import smtplib
import ssl

HOST = "localhost"
PORT = 465
TIMEOUT = 20


def send_message(sender, password, message):
    """Autentica contra Stalwart y entrega el mensaje para su procesamiento."""
    # El listener local usa TLS implícito y puede tener un certificado propio.
    context = ssl._create_unverified_context()
    with smtplib.SMTP_SSL(HOST, PORT, context=context, timeout=TIMEOUT) as smtp:
        smtp.ehlo()
        smtp.login(sender, password)
        smtp.send_message(message)
