from stalwart_sender.mail_content import build_message


def test_build_message_includes_plain_text_and_styled_html():
    message = build_message("sender@example.com", "recipient@example.com")

    assert message["From"] == "sender@example.com"
    assert message["To"] == "recipient@example.com"
    assert "STALWART // ORACLE RELAY" in message["Subject"]
    assert message.get_content_type() == "multipart/alternative"
    plain, html = message.get_payload()
    assert "MESSAGE ACCEPTED" in plain.get_content()
    assert "#0b1020" in html.get_content()
