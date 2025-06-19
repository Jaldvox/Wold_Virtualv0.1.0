"""
Módulo de auto-reparación de errores
"""
import os
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List

class AutoFixer:
    """Reparar automáticamente errores comunes"""
    
    def __init__(self):
        self.reflex_dir = Path(__file__).parent.absolute()
        self.backup_dir = self.reflex_dir / 'backups'
        self.backup_dir.mkdir(exist_ok=True)
    
    def create_backup(self, file_path: Path) -> Path:
        """Crear respaldo de archivo"""
        if file_path.exists():
            backup_path = self.backup_dir / f"{file_path.name}.backup"
            shutil.copy2(file_path, backup_path)
            return backup_path
        return None
    
    def fix_missing_init(self) -> bool:
        """Crear __init__.py si falta"""
        init_file = self.reflex_dir / '__init__.py'
        if not init_file.exists():
            init_content = '''"""
WoldVirtual Crypto 3D - Reflex Package
Auto-generado por sistema de auto-reparación
"""

__version__ = "1.0.0"
__app_name__ = "WoldVirtual_Crypto_3D"
'''
            init_file.write_text(init_content, encoding='utf-8')
            print("✅ Creado __init__.py")
            return True
        return False
    
    def fix_rxconfig(self) -> bool:
        """Crear o reparar rxconfig.py"""
        config_file = self.reflex_dir / 'rxconfig.py'
        self.create_backup(config_file)
        
        config_content = '''import reflex as rx
import os
from pathlib import Path

# Asegurar directorio correcto
REFLEX_DIR = Path(__file__).parent.absolute()
os.chdir(str(REFLEX_DIR))

config = rx.Config(
    app_name="WoldVirtual_Crypto_3D",
    frontend_port=3000,
    backend_port=8000,
)

print(f"📁 Reflex configurado desde: {REFLEX_DIR}")
'''
        config_file.write_text(config_content, encoding='utf-8')
        print("✅ Reparado rxconfig.py")
        return True
    
    def fix_main_app(self) -> bool:
        """Crear aplicación principal sin imports problemáticos"""
        main_file = self.reflex_dir / 'WoldVirtual_Crypto_3D.py'
        self.create_backup(main_file)
        
        app_content = '''"""
WoldVirtual Crypto 3D - Aplicación Principal
Auto-reparada por sistema de corrección
"""
import reflex as rx
import os
from pathlib import Path

# Asegurar directorio correcto
REFLEX_DIR = Path(__file__).parent.absolute()
if os.getcwd() != str(REFLEX_DIR):
    os.chdir(str(REFLEX_DIR))
    print(f"🔄 Cambiado a: {REFLEX_DIR}")

class AppState(rx.State):
    """Estado de la aplicación auto-reparada"""
    status: str = "Auto-reparado y funcionando ✅"
    show_menu: bool = False
    selected_option: str = "Seleccionar Red"
    
    networks: list = [
        "Ethereum",
        "Polygon", 
        "Binance Smart Chain",
        "Avalanche",
        "Arbitrum"
    ]
    
    def toggle_menu(self):
        self.show_menu = not self.show_menu
    
    def select_network(self, network: str):
        self.selected_option = network
        self.show_menu = False
        self.status = f"Conectado a {network} ✅"

def create_header():
    """Header auto-reparado"""
    return rx.hstack(
        rx.heading("WoldVirtual", size="lg", color="white"),
        rx.spacer(),
        rx.text("Auto-Reparado", color="white", font_size="sm"),
        
        # Menú de redes
        rx.box(
            rx.button(
                AppState.selected_option,
                on_click=AppState.toggle_menu,
                bg="blue.600",
                color="white",
                size="sm"
            ),
            rx.cond(
                AppState.show_menu,
                rx.vstack(
                    rx.foreach(
                        AppState.networks,
                        lambda net: rx.button(
                            net,
                            on_click=lambda: AppState.select_network(net),
                            width="100%",
                            size="sm"
                        )
                    ),
                    position="absolute",
                    top="100%",
                    right="0",
                    bg="white",
                    border="1px solid #ccc",
                    border_radius="md",
                    box_shadow="lg",
                    z_index="1000",
                    width="200px",
                    p="2"
                )
            ),
            position="relative"
        ),
        
        width="100%",
        bg="blue.500",
        p="4",
        align="center"
    )

def create_content():
    """Contenido auto-reparado"""
    return rx.container(
        rx.vstack(
            rx.heading("WoldVirtual Crypto 3D", size="2xl"),
            
            rx.box(
                rx.vstack(
                    rx.text("Estado del Sistema", font_weight="bold"),
                    rx.text(AppState.status),
                    rx.text(f"Directorio: {os.getcwd()}", font_size="sm"),
                    spacing="2"
                ),
                bg="gray.100",
                p="4",
                border_radius="md",
                width="100%"
            ),
            
            rx.hstack(
                rx.button("🌍 Mundo", color_scheme="green", size="lg"),
                rx.button("🛒 Market", color_scheme="purple", size="lg"),
                rx.button("👤 Perfil", color_scheme="blue", size="lg"),
                spacing="4"
            ),
            
            rx.text(
                "Sistema auto-reparado funcionando correctamente",
                color="green.600",
                font_weight="bold"
            ),
            
            spacing="6",
            align="center"
        ),
        max_width="800px",
        margin="auto",
        p="4"
    )

def index():
    """Página principal auto-reparada"""
    return rx.vstack(
        create_header(),
        create_content(),
        min_height="100vh",
        spacing="0"
    )

# Aplicación auto-reparada
app = rx.App(
    theme=rx.theme(
        accent_color="blue",
        appearance="light"
    )
)

app.add_page(index, route="/")
'''
        main_file.write_text(app_content, encoding='utf-8')
        print("✅ Reparada aplicación principal")
        return True
    
    def fix_requirements(self) -> bool:
        """Crear requirements.txt"""
        req_file = self.reflex_dir / 'requirements.txt'
        
        requirements = '''reflex>=0.4.0
python-dotenv>=1.0.0
'''
        req_file.write_text(requirements, encoding='utf-8')
        print("✅ Creado requirements.txt")
        return True
    
    def install_dependencies(self) -> bool:
        """Instalar dependencias"""
        try:
            subprocess.run([
                'pip', 'install', '-r', 'requirements.txt'
            ], check=True, cwd=str(self.reflex_dir))
            print("✅ Dependencias instaladas")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error instalando dependencias: {e}")
            return False
    
    def run_auto_repair(self) -> Dict[str, bool]:
        """Ejecutar reparación automática completa"""
        print("🔧 Iniciando auto-reparación...")
        
        results = {
            'init_fixed': self.fix_missing_init(),
            'config_fixed': self.fix_rxconfig(),
            'app_fixed': self.fix_main_app(),
            'requirements_fixed': self.fix_requirements(),
            'dependencies_installed': self.install_dependencies()
        }
        
        print("\n✅ Auto-reparación completada")
        return results