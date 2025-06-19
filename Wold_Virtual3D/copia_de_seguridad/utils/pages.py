"""Páginas principales de WoldVirtual Crypto 3D."""
import reflex as rx
from typing import Dict, Any

def home_page() -> rx.Component:
    """Página principal del metaverso."""
    return rx.box(
        rx.vstack(
            rx.heading(
                "🌍 WoldVirtual Crypto 3D",
                size="2xl",
                color="primary.600",
                font_weight="bold",
                text_align="center",
                mb=4,
            ),
            rx.text(
                "Metaverso descentralizado con capacidades de criptomonedas",
                color="gray.600",
                text_align="center",
                mb=8,
            ),
            rx.hstack(
                rx.button(
                    "🚀 Iniciar Metaverso",
                    color_scheme="primary",
                    size="lg",
                    px=8,
                    py=4,
                    font_weight="semibold",
                    _hover={"transform": "translateY(-2px)", "box_shadow": "lg"},
                    transition="all 0.2s",
                ),
                rx.button(
                    "💼 Conectar Wallet",
                    color_scheme="secondary",
                    size="lg",
                    px=8,
                    py=4,
                    font_weight="semibold",
                    _hover={"transform": "translateY(-2px)", "box_shadow": "lg"},
                    transition="all 0.2s",
                ),
                spacing=6,
                justify="center",
                mb=8,
            ),
            rx.simple_grid(
                rx.box(
                    rx.icon("cube", size=8, color="primary.500", mb=4),
                    rx.heading("Crear", size="md", mb=2),
                    rx.text("Construye tu mundo virtual con herramientas 3D avanzadas"),
                    p=6,
                    bg="white",
                    border_radius="lg",
                    box_shadow="md",
                    _hover={"transform": "translateY(-4px)", "box_shadow": "xl"},
                    transition="all 0.3s",
                ),
                rx.box(
                    rx.icon("globe", size=8, color="secondary.500", mb=4),
                    rx.heading("Explorar", size="md", mb=2),
                    rx.text("Descubre mundos creados por la comunidad"),
                    p=6,
                    bg="white",
                    border_radius="lg",
                    box_shadow="md",
                    _hover={"transform": "translateY(-4px)", "box_shadow": "xl"},
                    transition="all 0.3s",
                ),
                rx.box(
                    rx.icon("store", size=8, color="accent.500", mb=4),
                    rx.heading("Marketplace", size="md", mb=2),
                    rx.text("Compra y vende assets digitales con criptomonedas"),
                    p=6,
                    bg="white",
                    border_radius="lg",
                    box_shadow="md",
                    _hover={"transform": "translateY(-4px)", "box_shadow": "xl"},
                    transition="all 0.3s",
                ),
                columns=[1, 2, 3],
                spacing=6,
                mb=8,
            ),
            rx.divider(mb=8),
            rx.hstack(
                rx.text("© 2024 WoldVirtual Crypto 3D", color="gray.500"),
                rx.spacer(),
                rx.hstack(
                    rx.link("Documentación", href="#", color="primary.500"),
                    rx.link("GitHub", href="#", color="primary.500"),
                    rx.link("Discord", href="#", color="primary.500"),
                    spacing=4,
                ),
                width="100%",
            ),
            spacing=0,
            align="center",
            justify="center",
            min_height="100vh",
            bg="gray.50",
            px=4,
        ),
        width="100%",
    )

def create_page() -> rx.Component:
    """Página de creación de contenido."""
    return rx.box(
        rx.vstack(
            rx.heading("🎨 Crear Contenido", size="xl", mb=6),
            rx.text("Herramientas para crear tu mundo virtual", mb=8),
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

def explore_page() -> rx.Component:
    """Página de exploración."""
    return rx.box(
        rx.vstack(
            rx.heading("🌍 Explorar Mundos", size="xl", mb=6),
            rx.text("Descubre mundos creados por la comunidad", mb=8),
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

def marketplace_page() -> rx.Component:
    """Página del marketplace."""
    return rx.box(
        rx.vstack(
            rx.heading("💼 Marketplace", size="xl", mb=6),
            rx.text("Compra y vende assets digitales", mb=8),
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

def profile_page() -> rx.Component:
    """Página de perfil de usuario."""
    return rx.box(
        rx.vstack(
            rx.heading("👤 Perfil de Usuario", size="xl", mb=6),
            rx.text("Gestiona tu cuenta y configuración", mb=8),
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

# Configuración de rutas
routes = {
    "/": home_page,
    "/create": create_page,
    "/explore": explore_page,
    "/marketplace": marketplace_page,
    "/profile": profile_page,
} 