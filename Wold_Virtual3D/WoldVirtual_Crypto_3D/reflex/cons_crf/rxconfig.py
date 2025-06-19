import reflex as rx
import os
from pathlib import Path

# Obtener directorio reflex (donde está este archivo)
REFLEX_DIR = Path(__file__).parent.absolute()

# Asegurar que estamos en el directorio reflex
os.chdir(str(REFLEX_DIR))

config = rx.Config(
    app_name="WoldVirtual_Crypto_3D",
    frontend_port=3000,
    backend_port=8000,
    
    # 🎯 CONFIGURACIÓN PARA MANTENER TODO EN /reflex
    app_dir=str(REFLEX_DIR),                    # Directorio base
    web_dir=str(REFLEX_DIR / ".web"),          # .web aquí
    assets_dir=str(REFLEX_DIR / "assets"),     # assets aquí
    db_url=f"sqlite:///{REFLEX_DIR}/app.db",   # DB aquí
    
    # Configuraciones adicionales
    compile=True,
    dev_mode=True,
    telemetry_enabled=False,
)

print(f"🎯 Reflex ejecutándose desde: {REFLEX_DIR}")
print(f"📁 Directorio actual: {os.getcwd()}")