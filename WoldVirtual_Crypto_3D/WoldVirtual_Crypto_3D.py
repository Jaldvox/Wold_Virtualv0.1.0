"""
Archivo principal de WoldVirtual Crypto 3D
Punto de entrada único - Botón de encendido para toda la aplicación
"""

import sys
import os
import logging
import subprocess
import threading
import time
from pathlib import Path
from typing import Optional, Dict, Any

# Agregar el directorio del proyecto al path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Importaciones del proyecto
try:
    # Importar Reflex y configuración
    import reflex as rx
    from rxconfig import config
    from state import WoldVirtualState
    from pages import MainPage, ScenePage, SettingsPage, HelpPage
    
    # Importar utilidades
    from utils.constants import *
    from utils.helpers import *
    from utils.web3_utils import Web3Manager, WalletManager, TransactionManager
    from utils.three_utils import *
    
    # Importar modelos
    from models.user import User
    from models.asset import Asset
    from models.scene import Scene
    from models.transaction import Transaction
    
    # Importar componentes
    from components.navbar import Navbar
    from components.scene3d import Scene3D
    from components.marketplace import Marketplace
    from components.profile import Profile
    from components.explore import Explore
    from components.create import Create
    from components.home import Home
    
    # Importar backend
    from backend.database import Database
    from backend.models import *
    from backend.crud import *
    from backend.utils import *
    
    # Importar assets managers
    from assets.asset_manager import AssetManager
    from assets.scene_manager import SceneManager
    from assets.texture_manager import TextureManager
    from assets.audio_manager import AudioManager
    
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    print("Please ensure all required modules are installed and the project structure is correct.")
    sys.exit(1)

class WoldVirtualCrypto3D:
    """Clase principal de la aplicación - Botón de encendido"""
    
    def __init__(self):
        self.logger = self._setup_logging()
        self.app = None
        self.web3_manager = None
        self.wallet_manager = None
        self.transaction_manager = None
        self.asset_manager = None
        self.scene_manager = None
        self.database = None
        self.is_initialized = False
        
        self.logger.info("🚀 WoldVirtual Crypto 3D - Botón de encendido inicializado")
        
    def _setup_logging(self) -> logging.Logger:
        """Configurar logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/woldvirtual.log'),
                logging.StreamHandler()
            ]
        )
        return logging.getLogger(__name__)
    
    def _check_dependencies(self) -> bool:
        """Verificar que todas las dependencias estén instaladas"""
        self.logger.info("🔍 Verificando dependencias...")
        
        required_packages = [
            'reflex', 'web3', 'numpy', 'pillow', 'fastapi', 
            'sqlalchemy', 'pydantic', 'uvicorn'
        ]
        
        missing_packages = []
        for package in required_packages:
            try:
                __import__(package)
                self.logger.info(f"✅ {package}")
            except ImportError:
                missing_packages.append(package)
                self.logger.error(f"❌ {package} - FALTANTE")
        
        if missing_packages:
            self.logger.error(f"Dependencias faltantes: {missing_packages}")
            self.logger.info("Ejecuta: pip install -r requirements.txt")
            return False
        
        self.logger.info("✅ Todas las dependencias verificadas")
        return True
    
    def _initialize_database(self) -> bool:
        """Inicializar base de datos"""
        try:
            self.logger.info("🗄️ Inicializando base de datos...")
            self.database = Database()
            self.database.create_tables()
            self.logger.info("✅ Base de datos inicializada")
            return True
        except Exception as e:
            self.logger.error(f"❌ Error inicializando base de datos: {e}")
            return False
    
    def _initialize_web3(self) -> bool:
        """Inicializar componentes Web3"""
        try:
            self.logger.info("🔗 Inicializando Web3...")
            
            # Inicializar Web3 Manager
            self.web3_manager = Web3Manager(
                provider_url=config.env_vars.get("WEB3_PROVIDER_URL", "http://localhost:8545"),
                chain_id=int(config.env_vars.get("WEB3_CHAIN_ID", "1"))
            )
            
            # Inicializar Wallet Manager
            self.wallet_manager = WalletManager(self.web3_manager)
            
            # Inicializar Transaction Manager
            self.transaction_manager = TransactionManager(self.web3_manager)
            
            self.logger.info("✅ Web3 inicializado")
            return True
        except Exception as e:
            self.logger.error(f"❌ Error inicializando Web3: {e}")
            return False
    
    def _initialize_assets(self) -> bool:
        """Inicializar gestores de assets"""
        try:
            self.logger.info("🎨 Inicializando gestores de assets...")
            
            # Inicializar Asset Manager
            self.asset_manager = AssetManager()
            
            # Inicializar Scene Manager
            self.scene_manager = SceneManager()
            
            # Inicializar Texture Manager
            self.texture_manager = TextureManager()
            
            # Inicializar Audio Manager
            self.audio_manager = AudioManager()
            
            self.logger.info("✅ Gestores de assets inicializados")
            return True
        except Exception as e:
            self.logger.error(f"❌ Error inicializando assets: {e}")
            return False
    
    def _create_reflex_app(self) -> bool:
        """Crear y configurar la aplicación Reflex"""
        try:
            self.logger.info("🌐 Creando aplicación Reflex...")
            
            # Crear aplicación Reflex
            self.app = rx.App(
                state=WoldVirtualState,
                theme=rx.theme(
                    appearance="light",
                    has_background=True,
                    radius="medium",
                    accent_color="violet",
                    gray_color="slate",
                    styles={
                        "*": {
                            "margin": "0",
                            "padding": "0",
                            "boxSizing": "border-box",
                        },
                        "html, body": {
                            "height": "100%",
                            "width": "100%",
                            "overflow": "hidden",
                            "fontFamily": "system-ui, -apple-system, sans-serif",
                        },
                        "body": {
                            "&::-webkit-scrollbar": {
                                "display": "none",
                            },
                            "scrollbarWidth": "none",
                            "msOverflowStyle": "none",
                        },
                    },
                ),
            )
            
            # Agregar páginas
            self.app.add_page(
                MainPage,
                route="/",
                title="WoldVirtual Crypto 3D",
                description="Metaverso descentralizado 3D con capacidades de criptomonedas",
            )
            
            self.app.add_page(
                ScenePage,
                route="/scene",
                title="Escena 3D - WoldVirtual",
            )
            
            self.app.add_page(
                SettingsPage,
                route="/settings",
                title="Configuración - WoldVirtual",
            )
            
            self.app.add_page(
                HelpPage,
                route="/help",
                title="Ayuda - WoldVirtual",
            )
            
            self.logger.info("✅ Aplicación Reflex creada")
            return True
        except Exception as e:
            self.logger.error(f"❌ Error creando aplicación Reflex: {e}")
            return False
    
    def _initialize_all_modules(self) -> bool:
        """Inicializar todos los módulos del sistema"""
        self.logger.info("🔧 Inicializando todos los módulos...")
        
        # Verificar dependencias
        if not self._check_dependencies():
            return False
        
        # Inicializar base de datos
        if not self._initialize_database():
            return False
        
        # Inicializar Web3
        if not self._initialize_web3():
            return False
        
        # Inicializar assets
        if not self._initialize_assets():
            return False
        
        # Crear aplicación Reflex
        if not self._create_reflex_app():
            return False
        
        self.is_initialized = True
        self.logger.info("✅ Todos los módulos inicializados correctamente")
        return True
    
    def _start_reflex_server(self):
        """Iniciar servidor Reflex en un hilo separado"""
        try:
            self.logger.info("🚀 Iniciando servidor Reflex...")
            
            # Configurar variables de entorno para Reflex
            os.environ["REFLEX_FRONTEND_PORT"] = str(config.frontend_port)
            os.environ["REFLEX_BACKEND_PORT"] = str(config.backend_port)
            os.environ["REFLEX_API_URL"] = config.api_url
            os.environ["REFLEX_DEPLOY_URL"] = config.deploy_url
            
            # Compilar la aplicación
            self.app.compile()
            
            # Iniciar servidor
            self.app.run(
                host="0.0.0.0",
                port=config.frontend_port,
                log_level="info"
            )
            
        except Exception as e:
            self.logger.error(f"❌ Error iniciando servidor Reflex: {e}")
    
    def _show_startup_banner(self):
        """Mostrar banner de inicio"""
        banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║  ██╗    ██╗ ██████╗ ██╗     ██╗     ██╗   ██╗██╗   ██╗██████╗ ██╗   ██╗    ║
║  ██║    ██║██╔═══██╗██║     ██║     ██║   ██║██║   ██║██╔══██╗██║   ██║    ║
║  ██║ █╗ ██║██║   ██║██║     ██║     ██║   ██║██║   ██║██████╔╝██║   ██║    ║
║  ██║███╗██║██║   ██║██║     ██║     ██║   ██║██║   ██║██╔══██╗██║   ██║    ║
║  ╚███╔███╔╝╚██████╔╝███████╗███████╗╚██████╔╝╚██████╔╝██║  ██║╚██████╔╝    ║
║   ╚══╝╚══╝  ╚═════╝ ╚══════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝     ║
║                                                                              ║
║                    🚀 CRYPTO METAVERSE 3D 🚀                                ║
║                                                                              ║
║  Version: 0.0.9                    Status: Initializing...                  ║
║  Environment: Development          Framework: Reflex + Three.js             ║
║  Blockchain: Multi-chain          Database: SQLite/PostgreSQL              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def _show_system_status(self):
        """Mostrar estado del sistema"""
        status = {
            "Database": "✅ Connected" if self.database else "❌ Disconnected",
            "Web3": "✅ Connected" if self.web3_manager else "❌ Disconnected",
            "Assets": "✅ Loaded" if self.asset_manager else "❌ Not Loaded",
            "Reflex": "✅ Ready" if self.app else "❌ Not Ready",
            "Network": self.web3_manager.network_name if self.web3_manager else "Unknown",
            "Port": f"{config.frontend_port}",
            "Environment": config.env.value
        }
        
        print("\n📊 SYSTEM STATUS:")
        print("=" * 50)
        for key, value in status.items():
            print(f"  {key:<12}: {value}")
        print("=" * 50)
    
    def _show_access_info(self):
        """Mostrar información de acceso"""
        print("\n🌐 ACCESS INFORMATION:")
        print("=" * 50)
        print(f"  Frontend: http://localhost:{config.frontend_port}")
        print(f"  Backend:  http://localhost:{config.backend_port}")
        print(f"  API:      {config.api_url}")
        print("=" * 50)
        print("\n🎮 Ready to explore the metaverse!")
        print("   Press Ctrl+C to stop the server")
        print("=" * 50)
    
    def start(self):
        """Iniciar la aplicación completa"""
        try:
            # Mostrar banner
            self._show_startup_banner()
            
            # Inicializar todos los módulos
            if not self._initialize_all_modules():
                self.logger.error("❌ Failed to initialize modules")
                return False
            
            # Mostrar estado del sistema
            self._show_system_status()
            
            # Mostrar información de acceso
            self._show_access_info()
            
            # Iniciar servidor Reflex
            self._start_reflex_server()
            
        except KeyboardInterrupt:
            self.logger.info("🛑 Application stopped by user")
        except Exception as e:
            self.logger.error(f"❌ Runtime error: {e}")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Limpieza al cerrar la aplicación"""
        self.logger.info("🧹 Cleaning up resources...")
        
        try:
            # Cerrar conexiones de base de datos
            if self.database:
                self.database.close()
            
            # Cerrar conexiones Web3
            if self.web3_manager:
                self.web3_manager.w3.provider.disconnect()
            
            # Limpiar assets
            if self.asset_manager:
                self.asset_manager.cleanup()
            
            self.logger.info("✅ Cleanup completed")
            
        except Exception as e:
            self.logger.error(f"❌ Error during cleanup: {e}")

def main():
    """Función principal - Botón de encendido"""
    print("🔌 Starting WoldVirtual Crypto 3D - Power Button...")
    
    # Crear y ejecutar aplicación
    app = WoldVirtualCrypto3D()
    app.start()

if __name__ == "__main__":
    main()