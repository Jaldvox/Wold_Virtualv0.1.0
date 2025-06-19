"""Archivo principal de WoldVirtual Crypto 3D para Reflex (refactorizado)."""
import reflex as rx
from state import WoldVirtualState
from pages import routes  # Importar el diccionario de rutas centralizado


def create_app() -> rx.App:
    """Crea y configura la aplicación principal de Reflex."""
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
    
    # Registrar rutas principales automáticamente desde el diccionario
    for route, page_func in routes.items():
        app.add_page(page_func, route=route)

    # Página 404 personalizada
    @app.add_page
    def not_found():
        """Página mostrada cuando la ruta no existe."""
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
    return app


if __name__ == "__main__":
    # Crear y compilar la app
    app = create_app()
    app.compile() 