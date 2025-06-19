"""
WoldVirtual Crypto 3D - Versión completamente auto-contenida
"""
import reflex as rx
import os
from pathlib import Path

# Asegurar directorio
REFLEX_DIR = Path(__file__).parent.absolute()
os.chdir(str(REFLEX_DIR))

class AppState(rx.State):
    """Estado unificado de la aplicación"""
    app_status: str = "Funcionando desde /reflex ✅"
    current_directory: str = os.getcwd()
    show_networks_menu: bool = False
    selected_network: str = "Redes Blockchain"
    
    networks: list = [
        "Binance Smart Chain",
        "Ethereum", 
        "Polygon",
        "Avalanche",
        "Arbitrum",
        "Solana"
    ]

    def on_load(self):
        self.current_directory = os.getcwd()
        if "reflex" in self.current_directory:
            self.app_status = "✅ Auto-contenido funcionando desde /reflex"

    def toggle_networks_menu(self):
        self.show_networks_menu = not self.show_networks_menu

    def select_network(self, network: str):
        self.selected_network = network
        self.show_networks_menu = False

def create_header() -> rx.Component:
    """Header unificado"""
    return rx.hstack(
        rx.text("World Virtual", font_size="1.2em", color="black", font_weight="bold"),
        rx.spacer(),
        rx.text("Mapa del proyecto.", margin_left="0.5em", color="black", font_size="0.8em"),
        rx.text("Libro blanco", margin_left="0.5em", color="black", font_size="0.8em"),
        rx.text("Código abierto", margin_left="0.5em", color="black", font_size="0.8em"),
        create_network_selector(),
        width="100%",
        height="50px",
        background_color="#FFD700",
        align_items="center",
        padding_x="4",
        z_index="100",
        position="relative",
    )

def create_network_selector() -> rx.Component:
    """Selector de redes"""
    return rx.box(
        rx.button(
            AppState.selected_network,
            on_click=AppState.toggle_networks_menu,
            bg="#343a40",
            color="white",
            margin_left="0.5em",
            font_size="0.65em",
            padding="0.3em 0.6em",
            cursor="pointer",
            border_radius="4px",
        ),
        rx.cond(
            AppState.show_networks_menu,
            rx.vstack(
                *[
                    rx.button(
                        network,
                        on_click=lambda net=network: AppState.select_network(net),
                        width="100%",
                        font_size="0.7em",
                        padding="0.3em"
                    ) for network in AppState.networks
                ],
                position="absolute",
                top="100%",
                right="0",
                background_color="white",
                border="1px solid #ddd",
                border_radius="4px",
                box_shadow="0 2px 8px rgba(0,0,0,0.1)",
                z_index="1000",
                width="160px",
                align_items="stretch",
                spacing="1",
            )
        ),
        position="relative"
    )

def create_main_content() -> rx.Component:
    """Contenido principal unificado"""
    return rx.box(
        rx.box(
            rx.vstack(
                rx.text("WoldVirtual Crypto 3D", 
                       font_size="1.5em", 
                       font_weight="bold", 
                       color="#333"),
                rx.text("Versión auto-contenida en /reflex", 
                       font_size="1em", 
                       color="#666",
                       text_align="center"),
                
                # Status panel
                rx.box(
                    rx.vstack(
                        rx.heading("Estado del Sistema", size="md"),
                        rx.text(f"Directorio: {AppState.current_directory}"),
                        rx.text(f"Estado: {AppState.app_status}"),
                        rx.text(f"Red seleccionada: {AppState.selected_network}"),
                        spacing="2",
                    ),
                    padding="1rem",
                    bg="gray.100",
                    border_radius="md",
                    width="100%"
                ),
                
                # Controls
                rx.hstack(
                    rx.button("🌍 Mundo Principal", color_scheme="blue"),
                    rx.button("🛒 Marketplace", color_scheme="purple"),
                    rx.button("👤 Perfil", color_scheme="green"),
                    spacing="3",
                    justify="center"
                ),
                
                spacing="4",
                align_items="center",
                justify_content="center",
                height="100%",
            ),
            background_color="white",
            border="2px solid #4A90E2",
            border_radius="30px",
            box_shadow="0 4px 20px rgba(0,0,0,0.1)",
            width="90%",
            height="85%",
            padding="2rem",
            margin="auto",
            display="flex",
            align_items="center",
            justify_content="center",
        ),
        width="100%",
        height="100%",
        background_color="#228B22",
        display="flex",
        align_items="center",
        justify_content="center",
        padding="2",
    )

def index() -> rx.Component:
    """Página principal"""
    return rx.box(
        rx.vstack(
            create_header(),
            create_main_content(),
            width="90vw",
            height="90vh",
            border="2px solid #4A90E2",
            border_radius="15px",
            spacing="1",
            overflow="hidden",
        ),
        width="100vw",
        height="100vh",
        display="flex",
        align_items="center",
        justify_content="center",
        background="linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        margin="0",
        padding="0",
    )

app = rx.App()
app.add_page(index, route="/", on_load=AppState.on_load)