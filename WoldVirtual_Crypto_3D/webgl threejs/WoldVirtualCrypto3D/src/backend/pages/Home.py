from reflex import rx

class Home(rx.Page):
    """Página principal de la aplicación."""

    def __init__(self):
        super().__init__()

    def render(self):
        return rx.vstack(
            rx.heading("Bienvenido al Metaverso Cripto 3D", size="2xl"),
            rx.text("Explora, interactúa y crea en un mundo virtual."),
            rx.button("Comenzar", on_click=self.start_exploration, color_scheme="teal"),
            spacing="1rem",
            align="center",
            padding="2rem"
        )

    def start_exploration(self):
        """Inicia la exploración del metaverso."""
        # Lógica para iniciar la exploración del metaverso
        pass