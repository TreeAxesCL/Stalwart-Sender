#!/usr/bin/env python3
"""Prueba SMTP contra el listener de submissions de Stalwart."""

import getpass
import signal
import smtplib

from .mail_content import build_message
from .smtp_client import HOST, PORT, TIMEOUT, send_message
from .terminal_ui import Neon, ask_email, banner, paint, phase, result, stop_on_ctrl_c


def main():
    """Ejecuta la secuencia interactiva completa."""
    signal.signal(signal.SIGINT, stop_on_ctrl_c)
    banner(HOST, PORT, TIMEOUT)

    phase(1, "Identity manifest", "collecting Stalwart account")
    sender = ask_email("Correo en Stalwart")
    password = getpass.getpass(paint(Neon.CYAN, "│ Contraseña del correo: "))
    result(True, f"ACCOUNT READY // {sender}")

    phase(2, "Target manifest", "selecting delivery destination")
    recipient = ask_email("Correo destinatario")
    message = build_message(sender, recipient)
    result(True, f"TARGET LOCKED // {recipient}")

    phase(3, "SMTP uplink", f"opening encrypted session on {HOST}:{PORT}")
    try:
        send_message(sender, password, message)
    except (OSError, smtplib.SMTPException) as error:
        result(False, f"SMTP FAILURE // {error}")
        return 1
    result(True, "MESSAGE ACCEPTED // QUEUED BY STALWART")

    phase(4, "Relay handoff", "Oracle Email Delivery confirmation is available in the logs")
    print(paint(Neon.GREEN, "╭────────────────────────────────────────────────────────────╮"))
    print(paint(Neon.GREEN, "│   SEQUENCE COMPLETE // inspect Stalwart logs for delivery  │"))
    print(paint(Neon.GREEN, "╰────────────────────────────────────────────────────────────╯"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
