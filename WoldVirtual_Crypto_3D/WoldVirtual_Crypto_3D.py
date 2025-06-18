"""
Archivo principal de WoldVirtual Crypto 3D
"""

import sys
import os
import logging
from pathlib import Path

# Agregar el directorio del proyecto al path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Importaciones del proyecto (ahora usando imports absolutos)
try:
    from core.engine import Engine3D
    from core.security_manager import SecurityManager
    from components.scene import Scene3D
    from components.ui import UI
    from config.settings import Settings
    from database.secure_database_manager import SecureDatabaseManager
    from utils.logger import setup_logging
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Please ensure all required modules are installed and the project structure is correct.")
    sys.exit(1)

class WoldVirtualCrypto3D:
    """Clase principal de la aplicación"""
    
    def __init__(self):
        self.logger = setup_logging(__name__)
        self.settings = Settings()
        self.security_manager = None
        self.database_manager = None
        self.engine_3d = None
        self.scene = None
        self.ui = None
        
        self.logger.info("Initializing WoldVirtual Crypto 3D...")
        
    def initialize(self):
        """Inicializar todos los componentes"""
        try:
            # Inicializar seguridad
            self.security_manager = SecurityManager()
            self.logger.info("Security manager initialized")
            
            # Inicializar base de datos
            from database.database_factory import DatabaseFactory
            self.database_manager = DatabaseFactory.create_database_manager(
                environment=self.settings.get('environment', 'development')
            )
            self.logger.info("Database manager initialized")
            
            # Inicializar motor 3D
            self.engine_3d = Engine3D(
                width=self.settings.get('graphics.resolution.width', 1920),
                height=self.settings.get('graphics.resolution.height', 1080),
                quality=self.settings.get('graphics.quality', 'high')
            )
            self.logger.info("3D Engine initialized")
            
            # Inicializar escena 3D
            self.scene = Scene3D(self.engine_3d)
            self.logger.info("3D Scene initialized")
            
            # Inicializar UI
            self.ui = UI(self.scene, self.security_manager)
            self.logger.info("UI initialized")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Initialization failed: {str(e)}")
            return False
    
    def run(self):
        """Ejecutar la aplicación"""
        if not self.initialize():
            self.logger.error("Application initialization failed")
            return False
        
        try:
            self.logger.info("Starting WoldVirtual Crypto 3D...")
            
            # Configurar la escena inicial
            self.scene.setup_crypto_visualization()
            
            # Iniciar loop principal
            self.engine_3d.run()
            
        except KeyboardInterrupt:
            self.logger.info("Application interrupted by user")
        except Exception as e:
            self.logger.error(f"Runtime error: {str(e)}")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Limpieza al cerrar la aplicación"""
        self.logger.info("Cleaning up resources...")
        
        if self.engine_3d:
            self.engine_3d.cleanup()
        
        if self.database_manager:
            # Cerrar conexiones de base de datos
            pass
        
        self.logger.info("Cleanup completed")

def main():
    """Función principal"""
    print("=" * 60)
    print("  WoldVirtual Crypto 3D - Advanced Cryptocurrency Visualization")
    print("  Version: 0.0.9")
    print("=" * 60)
    
    # Verificar dependencias
    try:
        import OpenGL
        import numpy
        import pygame
        print("✅ Core dependencies verified")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install required packages: pip install -r requirements.txt")
        return
    
    # Crear y ejecutar aplicación
    app = WoldVirtualCrypto3D()
    app.run()

if __name__ == "__main__":
    main()