# Stalwart Sender

Un pequeño cliente SMTP interactivo para probar el listener de submissions de Stalwart y el relay de Oracle Email Delivery configurado.

## Idioma

- 🇪🇸 Español
- 🇺🇸 [English](README.md)

## Flujo

```text
cuenta y contraseña del remitente
                 ↓
        Stalwart Sender interactivo
                 ↓  TLS implícito / SMTP
       Stalwart en localhost:465
                 ↓
          relay de salida configurado
```

El programa envía un mensaje de prueba. Una respuesta SMTP exitosa significa que Stalwart aceptó el mensaje para procesarlo; revisa los logs de Stalwart y el relay para confirmar la entrega final.

## Estructura del proyecto

```text
src/stalwart_sender/
├── stalwart_sender.py  # flujo interactivo y punto de entrada
├── terminal_ui.py      # estilos Colorama, prompts y estados
├── mail_content.py     # asunto y cuerpos de texto plano / HTML
└── smtp_client.py      # SMTP sobre TLS implícito
tests/                  # pruebas unitarias con SMTP simulado
.agents/skills/         # guías de entrega SMTP y plantilla del correo
```

## Requisitos e instalación

Se requiere Python 3.13 o posterior y [uv](https://docs.astral.sh/uv/). Desde la carpeta del proyecto, instala la aplicación y las dependencias de desarrollo:

```bash
uv sync --group dev
```

## Ejecutar

Inicia el remitente interactivo:

```bash
uv run stalwart-sender
```

Solicita la cuenta de Stalwart, su contraseña y la dirección destinataria. El prompt usa `getpass`, por lo que la contraseña no aparece en la terminal mientras se escribe.

## Configuración SMTP

Los valores actuales de conexión están definidos en `src/stalwart_sender/smtp_client.py`:

| Opción | Valor |
| --- | --- |
| Host | `localhost` |
| Puerto | `465` |
| Timeout | 20 segundos |
| Conexión | SMTP sobre TLS implícito |

Actualmente no hay argumentos CLI ni variables de entorno para estos valores.

El cliente desactiva la verificación del certificado porque el listener local de Stalwart puede usar un certificado propio. Úsalo solo con un endpoint de confianza. Antes de enviar credenciales a un endpoint de producción o que no sea de confianza, configura la validación del certificado.

## Mensaje de prueba

El mensaje tiene un asunto con la estética Stalwart // Oracle Relay e incluye una alternativa de texto plano y otra HTML con estilos. Ambas indican que Stalwart aceptó el mensaje de prueba; no afirman que la entrega final haya terminado.

## Tests y calidad

```bash
uv run --group dev pytest
uv run --group dev ruff check .
uv run --group dev ruff format --check .
```

Aplica el formato de Ruff con `uv run --group dev ruff format .`.

Las pruebas SMTP usan mocks y no envían correos reales.

## Build

Genera el wheel y la distribución de código fuente:

```bash
uv build
```

Los artefactos se guardan en `dist/`.
