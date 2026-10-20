---
name: smtp-delivery
description: Change or review Stalwart Sender authentication, TLS connection, SMTP delivery, or its interactive send flow.
---

# Entrega SMTP

Usa esta guía para cambios en `smtp_client.py` o en la secuencia de envío de `stalwart_sender.py`.

- `smtp_client.py` posee el host, puerto, timeout y la sesión SMTP_SSL.
- El flujo pide la contraseña con `getpass` y la entrega al cliente SMTP; no la imprimas ni la guardes.
- Las pruebas deben simular `SMTP_SSL`; nunca dependas de credenciales o de un servidor activo.
- Conserva el manejo visible de errores SMTP en el punto de entrada.
- Antes de cambiar TLS, validación de certificados, autenticación o destino, confirma el requisito con el usuario.
- Ejecuta los comandos de Ruff y pytest documentados en `AGENTS.md`.
