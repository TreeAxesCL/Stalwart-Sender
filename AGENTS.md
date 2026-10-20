# Stalwart Sender

Instrucciones para cambios en este proyecto. Respeta las indicaciones específicas del usuario.

## Mapa del proyecto

- `src/stalwart_sender/stalwart_sender.py`: flujo interactivo y punto de entrada.
- `src/stalwart_sender/terminal_ui.py`: colores, fases, mensajes y validación básica del correo.
- `src/stalwart_sender/mail_content.py`: asunto y alternativas de texto y HTML.
- `src/stalwart_sender/smtp_client.py`: conexión SMTP sobre TLS implícito.
- `tests/`: pruebas unitarias sin conexión al servidor real.
- `.agents/skills/`: guías de trabajo para entrega SMTP y plantilla del correo.

## Reglas

- Conserva la separación entre interfaz, construcción del mensaje y transporte SMTP.
- Mantén una alternativa de texto junto con HTML para que el correo siga siendo legible sin formato.
- No envíes correos reales durante pruebas automatizadas; simula SMTP con mocks.
- Solicita autorización antes de cambiar el servidor, puerto, autenticación o política de certificados.
- Añade o ajusta pruebas cuando cambie el comportamiento observable.

## Comandos

Ejecuta desde la raíz del repositorio:

```bash
uv run --group dev ruff check .
uv run --group dev ruff format --check .
uv run --group dev pytest
uv build
```

Para corregir estilo usa `uv run --group dev ruff check . --fix` y `uv run --group dev ruff format .`.
El comando instalado del programa es `uv run stalwart-sender`.

## Skills del proyecto

- `.agents/skills/smtp-delivery/SKILL.md`: cambios a conexión y flujo de entrega.
- `.agents/skills/email-template/SKILL.md`: cambios al asunto o al contenido MIME.
