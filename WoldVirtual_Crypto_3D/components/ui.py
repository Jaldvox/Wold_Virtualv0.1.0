import reflex as rx
from state import State
from ..styles import UI_STYLE, BUTTON_STYLE

def UI():
    """Componente para la interfaz de usuario."""
    return rx.vstack(
        rx.hstack(
            rx.heading("WoldVirtual Crypto 3D", size="lg"),
            rx.spacer(),
            rx.cond(
                State.is_authenticated,
                rx.text(f"Conectado: {State.username}"),
                rx.button(
                    "Conectar Wallet",
                    on_click=State.connect_wallet,
                    style=BUTTON_STYLE,
                ),
            ),
            width="100%",
            padding="4",
            background="rgba(0, 0, 0, 0.8)",
            style=UI_STYLE,
        ),
        rx.vstack(
            rx.text("Bienvenido al Metaverso"),
            rx.text("Usa WASD para moverte y el mouse para mirar"),
            padding="4",
            position="absolute",
            bottom=0,
            left=0,
            background="rgba(0, 0, 0, 0.8)",
            border_radius="md",
            style=UI_STYLE,
        ),
    ) 