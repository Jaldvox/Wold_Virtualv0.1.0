"""Configuración de Reflex."""
import reflex as rx

config = rx.Config(
    app_name="WoldVirtual_Crypto_3D",
    db_url="sqlite:///woldvirtual.db",
    env=rx.Env.DEV,
    frontend_port=3000,
    backend_port=8000,
    api_url="http://localhost:8000",
    deploy_url="http://localhost:3000",
    tailwind=None,
    plugins=[],
    debug=True,
    cors_allowed_origins=["http://localhost:3000"],
    cache_control="no-cache",
) 