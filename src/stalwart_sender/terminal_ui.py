"""Estilo y entrada interactiva de la consola."""

import sys
from email.utils import parseaddr

from colorama import Fore, Style
from colorama import init as init_colors

HOST_LABEL = "STALWART // ORACLE RELAY"
init_colors()


class Neon:
    RESET = Style.RESET_ALL
    CYAN = Fore.CYAN
    MAGENTA = Fore.MAGENTA
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    RED = Fore.RED
    WHITE = Fore.WHITE
    DIM = Style.DIM


def paint(color, text):
    """Aplica color ANSI y restaura el terminal al terminar."""
    return f"{color}{text}{Neon.RESET}"


def stop_on_ctrl_c(_sig, _frame):
    """Cancela la prueba sin dejar la terminal en un estado extraño."""
    print(f"\n{paint(Neon.YELLOW, '[!] SECUENCIA CANCELADA // CTRL+C')}")
    sys.exit(0)


def banner(host, port, timeout):
    """Muestra la cabecera con el estilo de consola de la referencia."""
    print(
        paint(
            Neon.RED,
            rf"""
╔══════════════════════════════════════════════════════════════╗
║                    {HOST_LABEL}                  ║
╚══════════════════════════════════════════════════════════════╝
""",
        )
    )
    print(paint(Neon.DIM, f"SESSION > MAIL DELIVERY  //  {host}:{port}  //  TIMEOUT {timeout}s"))


def phase(number, title, detail):
    """Imprime una fase numerada como en un flujo de procesamiento."""
    label = paint(Neon.MAGENTA, f"◆ PHASE {number}/4")
    print(f"\n{label}  {paint(Neon.CYAN, title.upper())} {paint(Neon.DIM, '— ' + detail)}")


def result(ok, text):
    """Imprime un resultado visual de éxito o error."""
    symbol = paint(Neon.GREEN, "◆") if ok else paint(Neon.RED, "◆")
    color = Neon.GREEN if ok else Neon.RED
    print(f"{symbol} {paint(color, text)}")


def ask_email(label):
    """Solicita y valida una dirección de correo básica."""
    while True:
        address = input(paint(Neon.WHITE, f"│ {label}: ")).strip()
        _, parsed = parseaddr(address)
        if parsed and "@" in parsed and not parsed.startswith("@") and not parsed.endswith("@"):
            return parsed
        print(paint(Neon.RED, "│ Dirección inválida // ejemplo: usuario@dominio.com"))
