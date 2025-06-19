"""
Utilidades compartidas para WoldVirtual
"""
import os
import json
from pathlib import Path
from typing import Dict, Any, Optional

class FileManager:
    """Gestor de archivos"""
    
    @staticmethod
    def get_project_root() -> Path:
        """Obtener directorio raíz del proyecto"""
        return Path(__file__).parent.absolute()
    
    @staticmethod
    def load_json(file_path: str) -> Optional[Dict[str, Any]]:
        """Cargar archivo JSON"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error cargando {file_path}: {e}")
            return None
    
    @staticmethod
    def save_json(data: Dict[str, Any], file_path: str) -> bool:
        """Guardar archivo JSON"""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error guardando {file_path}: {e}")
            return False

class Logger:
    """Sistema de logging simple"""
    
    @staticmethod
    def info(message: str):
        """Log de información"""
        print(f"ℹ️ INFO: {message}")
    
    @staticmethod
    def warning(message: str):
        """Log de advertencia"""
        print(f"⚠️ WARNING: {message}")
    
    @staticmethod
    def error(message: str):
        """Log de error"""
        print(f"❌ ERROR: {message}")
    
    @staticmethod
    def success(message: str):
        """Log de éxito"""
        print(f"✅ SUCCESS: {message}")

class ConfigManager:
    """Gestor de configuración"""
    
    def __init__(self):
        self.config_file = FileManager.get_project_root() / "config.json"
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """Cargar configuración"""
        default_config = {
            "app": {
                "name": "WoldVirtual_Crypto_3D",
                "version": "1.0.0",
                "debug": True
            },
            "blockchain": {
                "default_network": "Polygon",
                "supported_networks": ["Ethereum", "Polygon", "BSC"]
            },
            "ui": {
                "theme": "violet",
                "default_scene": "main"
            }
        }
        
        if self.config_file.exists():
            loaded_config = FileManager.load_json(str(self.config_file))
            if loaded_config:
                return loaded_config
        
        # Crear archivo de configuración por defecto
        FileManager.save_json(default_config, str(self.config_file))
        return default_config
    
    def get(self, key: str, default=None):
        """Obtener valor de configuración"""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value
    
    def set(self, key: str, value: Any):
        """Establecer valor de configuración"""
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
        FileManager.save_json(self.config, str(self.config_file))

# Instancias globales
file_manager = FileManager()
logger = Logger()
config_manager = ConfigManager()