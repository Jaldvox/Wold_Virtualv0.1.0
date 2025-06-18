import reflex as rx
from rxconfig import config
from state import State

# Importar componentes
from components.scene import Scene3D
from components.ui import UI

def index():
    """Página principal del metaverso."""
    return rx.vstack(
        Scene3D(),
        UI(),
        width="100vw",
        height="100vh",
        position="relative",
    )

# Crear la aplicación
app = rx.App(
    theme=rx.theme(
        appearance="dark",
        accent_color="violet",
        gray_color="slate",
    ),
)

# Añadir la página principal
app.add_page(index, route="/")