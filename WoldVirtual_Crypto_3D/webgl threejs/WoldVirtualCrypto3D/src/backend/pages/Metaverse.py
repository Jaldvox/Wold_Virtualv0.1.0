from reflex import rx
from src.backend.state.MetaverseState import MetaverseState

class Metaverse(rx.Page):
    """Página del Metaverso que integra la escena 3D y la lógica de negocio."""

    def __init__(self):
        super().__init__()
        self.state = MetaverseState()

    def render(self):
        return rx.vstack(
            rx.heading("Metaverso Cripto 3D", size="2xl"),
            rx.box(
                id="three-container",
                width="100%",
                height="500px",
                border_radius="12px",
                overflow="hidden"
            ),
            rx.text("Estado del Metaverso: " + str(self.state.scene_data)),
            width="100%",
            padding="2rem"
        )

app = rx.App(state=MetaverseState)
app.add_page(Metaverse)