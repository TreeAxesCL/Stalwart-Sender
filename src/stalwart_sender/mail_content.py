"""Construcción del correo de prueba."""

from email.message import EmailMessage


def build_message(sender, recipient):
    """Construye el correo de prueba en texto y HTML."""
    message = EmailMessage()
    message["Subject"] = "◆ STALWART // ORACLE RELAY — DELIVERY REPORT"
    message["From"] = sender
    message["To"] = recipient
    message.set_content(
        "╔══════════════════════════════════════════════╗\n"
        "║       STALWART // ORACLE RELAY                ║\n"
        "║              DELIVERY REPORT                 ║\n"
        "╚══════════════════════════════════════════════╝\n\n"
        "◆ STATUS   // MESSAGE ACCEPTED\n"
        "◆ ROUTE    // STALWART → ORACLE RELAY\n\n"
        "Si recibes este mensaje, Stalwart aceptó correctamente la entrega.\n"
        "Mensaje enviado desde la VM Ubuntu mediante el relay configurado.\n\n"
        "──────────────────────────────────────────────\n"
        "AUTOMATED NOTICE // STALWART SMTP TEST"
    )
    message.add_alternative(
        """\
        <div style="margin:0;background:#0b1020;padding:32px 16px;font-family:Arial,sans-serif;color:#e5e7eb">
          <div style="max-width:560px;margin:auto;border:1px solid #3b4260;background:#11182b">
            <div style="padding:24px;border-bottom:1px solid #3b4260">
              <div style="color:#d946ef;font-size:12px;letter-spacing:2px">STALWART // ORACLE RELAY</div>
              <h1 style="margin:10px 0 0;font-size:22px;color:#67e8f9">DELIVERY REPORT</h1>
            </div>
            <div style="padding:24px">
              <div style="color:#4ade80;font-weight:bold">◆ &nbsp; MESSAGE ACCEPTED</div>
              <div style="margin-top:8px;color:#a5b4fc;font-size:13px">ROUTE // STALWART → ORACLE RELAY</div>
              <p style="margin:24px 0 8px;line-height:1.6">Si recibes este mensaje, Stalwart aceptó correctamente la entrega.</p>
              <p style="margin:0;line-height:1.6;color:#9ca3af">Mensaje enviado desde la VM Ubuntu mediante el relay configurado.</p>
            </div>
            <div style="padding:14px 24px;border-top:1px solid #3b4260;color:#6b7280;font-size:11px;letter-spacing:1px">AUTOMATED NOTICE // STALWART SMTP TEST</div>
          </div>
        </div>
        """,
        subtype="html",
    )
    return message
