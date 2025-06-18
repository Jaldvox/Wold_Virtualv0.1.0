import reflex as rx
import os

# Configuración de la aplicación
config = rx.Config(
    app_name="metaverso_crypto_3d",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    frontend_port=3000,
    backend_port=8000,
    api_url="http://localhost:8000",
    deploy_url="http://localhost:3000",
    tailwind=True,  # Activamos Tailwind para mejor estilizado
    plugins=[
        "reflex.plugins.tailwind",
    ],
    # Configuración adicional para desarrollo
    debug=True,
    # Configuración de seguridad
    cors_allowed_origins=["http://localhost:3000"],
    # Configuración de caché
    cache_control="no-cache",
) 