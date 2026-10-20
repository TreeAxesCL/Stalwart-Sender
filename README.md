# Stalwart Sender

A small interactive SMTP client for testing the Stalwart submissions listener and its configured Oracle Email Delivery relay.

## Language

- 🇺🇸 English
- 🇪🇸 [Español](README.es.md)

## Flow

```text
sender account and password
            ↓
interactive Stalwart Sender
            ↓  implicit TLS / SMTP
Stalwart on localhost:465
            ↓
configured outbound relay
```

The program submits one test message. A successful SMTP response means Stalwart accepted the message for processing; check Stalwart logs and the relay for final delivery status.

## Project structure

```text
src/stalwart_sender/
├── stalwart_sender.py  # interactive flow and command entry point
├── terminal_ui.py      # Colorama styling, prompts, and status output
├── mail_content.py     # subject and plain-text / HTML message bodies
└── smtp_client.py      # SMTP over implicit TLS
tests/                  # unit tests with a mocked SMTP connection
.agents/skills/         # SMTP delivery and email template guidance
```

## Requirements and installation

Python 3.13 or later and [uv](https://docs.astral.sh/uv/) are required. From the project directory, install the application and development dependencies:

```bash
uv sync --group dev
```

## Run

Start the interactive sender:

```bash
uv run stalwart-sender
```

It asks for the Stalwart account, its password, and the recipient address. The password prompt uses `getpass`, so the password is not echoed in the terminal.

## SMTP settings

The current connection settings are defined in `src/stalwart_sender/smtp_client.py`:

| Setting | Value |
| --- | --- |
| Host | `localhost` |
| Port | `465` |
| Timeout | 20 seconds |
| Connection | SMTP over implicit TLS |

There are currently no CLI flags or environment variables for these settings.

The client currently disables certificate verification because the local Stalwart listener may use its own certificate. Use it only with a trusted endpoint. For an untrusted or production endpoint, configure certificate validation before sending credentials.

## Test message

The message has a Stalwart // Oracle Relay themed subject and includes both a plain-text fallback and a styled HTML version. The two alternatives report that the test message was accepted by Stalwart; they do not claim final delivery has completed.

## Tests and code quality

```bash
uv run --group dev pytest
uv run --group dev ruff check .
uv run --group dev ruff format --check .
```

Apply Ruff formatting with `uv run --group dev ruff format .`.

The SMTP tests use mocks and do not send real email.

## Build

Build the wheel and source distribution:

```bash
uv build
```

Artifacts are written to `dist/`.
