import reflex as rx
from reflex.state import State

class MetaverseState(State):
    """Estado base para la aplicación del metaverso."""
    pass

def index():
    """Página principal del metaverso."""
    return rx.vstack(
        rx.heading("Metaverso Crypto 3D", size="lg"),
        rx.text("Bienvenido al mundo virtual"),
        spacing="4",
        padding="4",
    )

# Configuración de la aplicación
app = rx.App(state=MetaverseState)
app.add_page(index)

if __name__ == "__main__":
    app.run() 