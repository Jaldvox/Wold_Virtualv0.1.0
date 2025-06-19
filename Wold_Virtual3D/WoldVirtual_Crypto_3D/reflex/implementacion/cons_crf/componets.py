"""
Componentes UI modulares para WoldVirtual
"""
import reflex as rx
from state import GlobalState, NetworkState, WalletState

def header() -> rx.Component:
    """Componente de header modular"""
    return rx.hstack(
        rx.text("World Virtual", font_size="1.2em", color="black", font_weight="bold"),
        rx.spacer(),
        
        # Navegación
        navigation_menu(),
        
        # Selector de redes
        network_selector(),
        
        # Estado de wallet
        wallet_status(),
        
        width="100%",
        height="50px",
        background_color="#FFD700",
        align_items="center",
        padding_x="4",
        z_index="100",
        position="relative",
    )

def navigation_menu() -> rx.Component:
    """Menú de navegación"""
    return rx.hstack(
        rx.text("Mapa del proyecto.", margin_left="0.5em", color="black", font_size="0.8em"),
        rx.text("Libro blanco", margin_left="0.5em", color="black", font_size="0.8em"),
        rx.text("Código abierto", margin_left="0.5em", color="black", font_size="0.8em"),
        spacing="2"
    )

def network_selector() -> rx.Component:
    """Selector de redes blockchain"""
    return rx.box(
        rx.button(
            GlobalState.selected_network,
            on_click=NetworkState.toggle_networks_menu,
            bg="#343a40",
            color="white",
            margin_left="0.5em",
            font_size="0.65em",
            padding="0.3em 0.6em",
            cursor="pointer",
            border_radius="4px",
        ),
        rx.cond(
            GlobalState.show_networks_menu,
            rx.vstack(
                *[
                    rx.button(
                        network, 
                        on_click=lambda net=network: NetworkState.select_network(net),
                        width="100%", 
                        font_size="0.7em", 
                        padding="0.3em"
                    ) for network in NetworkState.networks
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
            ),
            None,
        ),
        position="relative"
    )

def wallet_status() -> rx.Component:
    """Estado del wallet"""
    return rx.cond(
        GlobalState.wallet_connected,
        rx.hstack(
            rx.text(f"🟢 {GlobalState.wallet_address}", font_size="0.7em", color="green"),
            rx.button("Desconectar", on_click=WalletState.disconnect_wallet, size="sm"),
            spacing="2"
        ),
        rx.button(
            "Conectar Wallet",
            on_click=WalletState.connect_wallet,
            color_scheme="green",
            size="sm"
        )
    )

def status_panel() -> rx.Component:
    """Panel de estado del sistema"""
    return rx.box(
        rx.vstack(
            rx.heading("Estado del Sistema", size="md"),
            rx.text(f"Directorio: {GlobalState.current_directory}"),
            rx.text(f"Estado: {GlobalState.app_status}"),
            rx.text(f"Escena actual: {GlobalState.current_scene}"),
            rx.text(f"Red: {GlobalState.current_network}"),
            spacing="2",
        ),
        padding="1rem",
        bg="gray.100",
        border_radius="md",
        width="100%"
    )

def main_content_area() -> rx.Component:
    """Área de contenido principal modular"""
    return rx.box(
        rx.box(
            rx.vstack(
                rx.text("WoldVirtual Crypto 3D", 
                       font_size="1.5em", 
                       font_weight="bold", 
                       color="#333"),
                rx.text("Arquitectura modular en /reflex", 
                       font_size="1em", 
                       color="#666",
                       text_align="center"),
                
                # Panel de estado
                status_panel(),
                
                # Controles de escena
                scene_controls(),
                
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

def scene_controls() -> rx.Component:
    """Controles de escena 3D"""
    from state import SceneState
    
    return rx.hstack(
        rx.button(
            "🌍 Mundo Principal",
            on_click=lambda: SceneState.change_scene("main"),
            color_scheme="blue"
        ),
        rx.button(
            "🛒 Marketplace",
            on_click=lambda: SceneState.change_scene("marketplace"),
            color_scheme="purple"
        ),
        rx.button(
            "👤 Perfil",
            on_click=lambda: SceneState.change_scene("profile"),
            color_scheme="green"
        ),
        spacing="3",
        justify="center"
    )