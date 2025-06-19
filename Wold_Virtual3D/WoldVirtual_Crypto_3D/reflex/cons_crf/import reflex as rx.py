import reflex as rx
import os
import sys
from pathlib import Path

# Obtener directorio de la aplicación (WoldVirtual_Crypto_3D)
CONFIG_DIR = Path(__file__).parent.absolute()
APP_DIR = CONFIG_DIR.parent / "WoldVirtual_Crypto_3D"

# Asegurar que estamos en el directorio correcto de la aplicación
os.chdir(str(APP_DIR))

# Agregar directorio de config al path para imports
sys.path.insert(0, str(CONFIG_DIR))

config = rx.Config(
    app_name="WoldVirtual_Crypto_3D",
    frontend_port=3000,
    backend_port=8000,
    # Especificar rutas relativas desde el directorio de la app
    app_dir=str(APP_DIR),
)