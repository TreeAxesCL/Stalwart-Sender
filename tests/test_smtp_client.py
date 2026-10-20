from unittest.mock import MagicMock, patch

from stalwart_sender import smtp_client


def test_send_message_authenticates_and_sends_over_implicit_tls():
    message = object()
    smtp = MagicMock()
    client = MagicMock()
    client.__enter__.return_value = smtp

    with (
        patch.object(smtp_client.ssl, "_create_unverified_context", return_value="tls-context"),
        patch.object(smtp_client.smtplib, "SMTP_SSL", return_value=client) as smtp_ssl,
    ):
        smtp_client.send_message("sender@example.com", "secret", message)

    smtp_ssl.assert_called_once_with(
        smtp_client.HOST,
        smtp_client.PORT,
        context="tls-context",
        timeout=smtp_client.TIMEOUT,
    )
    smtp.ehlo.assert_called_once_with()
    smtp.login.assert_called_once_with("sender@example.com", "secret")
    smtp.send_message.assert_called_once_with(message)
