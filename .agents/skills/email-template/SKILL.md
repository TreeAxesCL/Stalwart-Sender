---
name: email-template
description: Change or review the subject, plain-text body, HTML body, or MIME structure of Stalwart Sender emails.
---

# Plantilla del correo

Usa esta guía para cambios en `src/stalwart_sender/mail_content.py`.

- Mantén el contenido en `multipart/alternative`: texto plano primero y HTML después.
- Sigue la estética de consola Stalwart // Oracle Relay y usa estilos CSS en línea para compatibilidad con clientes de correo.
- Mantén las dos versiones con el mismo estado y la misma información.
- No agregues direcciones u otros datos del usuario al cuerpo si no son necesarios.
- Actualiza `tests/test_mail_content.py` cuando cambien encabezados, formato MIME o contenido visible.
- Ejecuta los comandos de Ruff y pytest documentados en `AGENTS.md`.
