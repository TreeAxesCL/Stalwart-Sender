from unittest.mock import patch

from stalwart_sender import stalwart_sender


def test_main_completes_when_message_is_accepted():
    with (
        patch.object(stalwart_sender.signal, "signal"),
        patch.object(stalwart_sender, "banner"),
        patch.object(stalwart_sender, "phase"),
        patch.object(
            stalwart_sender,
            "ask_email",
            side_effect=["sender@example.com", "recipient@example.com"],
        ),
        patch.object(stalwart_sender.getpass, "getpass", return_value="secret"),
        patch.object(stalwart_sender, "result") as result,
        patch.object(stalwart_sender, "send_message") as send_message,
    ):
        assert stalwart_sender.main() == 0

    send_message.assert_called_once()
    assert result.call_args_list[-1].args == (True, "MESSAGE ACCEPTED // QUEUED BY STALWART")


def test_main_reports_smtp_failure():
    with (
        patch.object(stalwart_sender.signal, "signal"),
        patch.object(stalwart_sender, "banner"),
        patch.object(stalwart_sender, "phase"),
        patch.object(
            stalwart_sender,
            "ask_email",
            side_effect=["sender@example.com", "recipient@example.com"],
        ),
        patch.object(stalwart_sender.getpass, "getpass", return_value="secret"),
        patch.object(stalwart_sender, "result") as result,
        patch.object(stalwart_sender, "send_message", side_effect=OSError("offline")),
    ):
        assert stalwart_sender.main() == 1

    assert result.call_args.args[0] is False
    assert "SMTP FAILURE // offline" in result.call_args.args[1]
