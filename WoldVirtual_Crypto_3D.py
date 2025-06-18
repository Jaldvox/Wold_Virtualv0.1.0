"""Archivo principal de WoldVirtual Crypto 3D para Reflex."""
import reflex as rx
from state import WoldVirtualState
from pages import home_page, create_page, explore_page, marketplace_page, profile_page

# Definir la aplicación principal
app = rx.App(
    state=WoldVirtualState,
    title="WoldVirtual Crypto 3D",
    description="Metaverso descentralizado con capacidades de criptomonedas",
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="medium",
        accent_color="blue",
        gray_color="slate",
        panel_background="solid",
    ),
)

# Rutas principales
app.add_page(home_page, route="/")
app.add_page(create_page, route="/create")
app.add_page(explore_page, route="/explore")
app.add_page(marketplace_page, route="/marketplace")
app.add_page(profile_page, route="/profile")

# Página 404
@app.add_page
def not_found():
    return rx.box(
        rx.vstack(
            rx.heading("404 - Página no encontrada", size="xl", mb=4),
            rx.text("La página que buscas no existe.", mb=6),
            rx.button("Volver al Inicio", href="/", color_scheme="primary"),
            spacing=4,
            align="center",
            justify="center",
            min_height="100vh",
            bg="gray.50",
            px=4,
        ),
        width="100%",
    )

if __name__ == "__main__":
    app.compile() 