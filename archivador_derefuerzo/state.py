"""Estado global de la aplicación WoldVirtual Crypto 3D."""
import reflex as rx
from typing import Dict, List, Any, Optional
import os
import json
from datetime import datetime

class WoldVirtualState(rx.State):
    """Estado principal de la aplicación."""
    
    # Configuración de la aplicación
    app_name: str = "WoldVirtual Crypto 3D"
    app_version: str = "0.0.9"
    environment: str = "development"
    
    # Estado del usuario
    user_id: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    is_authenticated: bool = False
    is_wallet_connected: bool = False
    wallet_address: Optional[str] = None
    wallet_balance: float = 0.0
    
    # Estado de la interfaz
    current_page: str = "/"
    sidebar_open: bool = False
    theme_mode: str = "light"
    language: str = "es"
    
    # Estado de carga
    is_loading: bool = False
    loading_message: str = ""
    
    # Estado de notificaciones
    notifications: List[Dict[str, Any]] = []
    
    # Estado del metaverso
    current_scene: Optional[str] = None
    available_scenes: List[Dict[str, Any]] = []
    user_assets: List[Dict[str, Any]] = []
    
    # Estado del marketplace
    marketplace_items: List[Dict[str, Any]] = []
    user_inventory: List[Dict[str, Any]] = []
    
    # Estado de Web3
    web3_connected: bool = False
    web3_provider: Optional[str] = None
    chain_id: Optional[int] = None
    gas_price: Optional[int] = None
    
    # Estado de errores
    error_message: Optional[str] = None
    error_type: Optional[str] = None
    
    def __init__(self):
        """Inicializar el estado."""
        super().__init__()
        self.load_initial_data()
    
    def load_initial_data(self):
        """Cargar datos iniciales."""
        try:
            # Cargar configuración desde archivo si existe
            config_file = "config.json"
            if os.path.exists(config_file):
                with open(config_file, "r", encoding="utf-8") as f:
                    config = json.load(f)
                    self.app_name = config.get("app_name", self.app_name)
                    self.app_version = config.get("app_version", self.app_version)
                    self.environment = config.get("environment", self.environment)
            
            # Cargar datos de usuario si existe
            user_file = "user_data.json"
            if os.path.exists(user_file):
                with open(user_file, "r", encoding="utf-8") as f:
                    user_data = json.load(f)
                    self.user_id = user_data.get("user_id")
                    self.username = user_data.get("username")
                    self.email = user_data.get("email")
                    self.is_authenticated = user_data.get("is_authenticated", False)
                    self.wallet_address = user_data.get("wallet_address")
                    self.is_wallet_connected = user_data.get("is_wallet_connected", False)
            
            # Cargar escenas disponibles
            self.load_available_scenes()
            
            # Cargar items del marketplace
            self.load_marketplace_items()
            
        except Exception as e:
            self.set_error(f"Error al cargar datos iniciales: {str(e)}", "load_error")
    
    def load_available_scenes(self):
        """Cargar escenas disponibles."""
        try:
            # Escenas de ejemplo
            self.available_scenes = [
                {
                    "id": "scene_1",
                    "name": "Plaza Central",
                    "description": "Plaza principal del metaverso",
                    "thumbnail": "/assets/scenes/plaza_central.jpg",
                    "creator": "WoldVirtual Team",
                    "created_at": "2024-01-01",
                    "visitors": 1250,
                    "rating": 4.8
                },
                {
                    "id": "scene_2",
                    "name": "Bosque Mágico",
                    "description": "Bosque encantado con criaturas mágicas",
                    "thumbnail": "/assets/scenes/bosque_magico.jpg",
                    "creator": "NatureCreator",
                    "created_at": "2024-01-15",
                    "visitors": 890,
                    "rating": 4.6
                },
                {
                    "id": "scene_3",
                    "name": "Ciudad Futurista",
                    "description": "Metrópolis del futuro con tecnología avanzada",
                    "thumbnail": "/assets/scenes/ciudad_futurista.jpg",
                    "creator": "FutureBuilder",
                    "created_at": "2024-02-01",
                    "visitors": 2100,
                    "rating": 4.9
                }
            ]
        except Exception as e:
            self.set_error(f"Error al cargar escenas: {str(e)}", "scene_error")
    
    def load_marketplace_items(self):
        """Cargar items del marketplace."""
        try:
            # Items de ejemplo
            self.marketplace_items = [
                {
                    "id": "item_1",
                    "name": "Espada Mágica",
                    "description": "Espada legendaria con poderes mágicos",
                    "price": 100.0,
                    "currency": "WOLD",
                    "seller": "MagicSmith",
                    "thumbnail": "/assets/items/espada_magica.jpg",
                    "category": "weapons",
                    "rarity": "legendary"
                },
                {
                    "id": "item_2",
                    "name": "Casa Flotante",
                    "description": "Residencia flotante con vista panorámica",
                    "price": 500.0,
                    "currency": "WOLD",
                    "seller": "ArchitectPro",
                    "thumbnail": "/assets/items/casa_flotante.jpg",
                    "category": "properties",
                    "rarity": "epic"
                },
                {
                    "id": "item_3",
                    "name": "Mascota Dragón",
                    "description": "Compañero dragón leal y poderoso",
                    "price": 250.0,
                    "currency": "WOLD",
                    "seller": "DragonBreeder",
                    "thumbnail": "/assets/items/mascota_dragon.jpg",
                    "category": "pets",
                    "rarity": "rare"
                }
            ]
        except Exception as e:
            self.set_error(f"Error al cargar marketplace: {str(e)}", "marketplace_error")
    
    def set_loading(self, loading: bool, message: str = ""):
        """Establecer estado de carga."""
        self.is_loading = loading
        self.loading_message = message
    
    def set_error(self, message: str, error_type: str = "general"):
        """Establecer mensaje de error."""
        self.error_message = message
        self.error_type = error_type
        self.add_notification(message, "error")
    
    def clear_error(self):
        """Limpiar mensaje de error."""
        self.error_message = None
        self.error_type = None
    
    def add_notification(self, message: str, notification_type: str = "info"):
        """Agregar notificación."""
        notification = {
            "id": f"notif_{len(self.notifications)}_{datetime.now().timestamp()}",
            "message": message,
            "type": notification_type,
            "timestamp": datetime.now().isoformat(),
            "read": False
        }
        self.notifications.append(notification)
    
    def mark_notification_read(self, notification_id: str):
        """Marcar notificación como leída."""
        for notification in self.notifications:
            if notification["id"] == notification_id:
                notification["read"] = True
                break
    
    def clear_notifications(self):
        """Limpiar todas las notificaciones."""
        self.notifications = []
    
    def toggle_sidebar(self):
        """Alternar estado del sidebar."""
        self.sidebar_open = not self.sidebar_open
    
    def set_current_page(self, page: str):
        """Establecer página actual."""
        self.current_page = page
    
    def toggle_theme(self):
        """Alternar modo de tema."""
        self.theme_mode = "dark" if self.theme_mode == "light" else "light"
    
    def set_language(self, language: str):
        """Establecer idioma."""
        self.language = language
    
    def connect_wallet(self, address: str):
        """Conectar wallet."""
        try:
            self.set_loading(True, "Conectando wallet...")
            # Simular conexión de wallet
            self.wallet_address = address
            self.is_wallet_connected = True
            self.add_notification("Wallet conectada exitosamente", "success")
        except Exception as e:
            self.set_error(f"Error al conectar wallet: {str(e)}", "wallet_error")
        finally:
            self.set_loading(False)
    
    def disconnect_wallet(self):
        """Desconectar wallet."""
        self.wallet_address = None
        self.is_wallet_connected = False
        self.add_notification("Wallet desconectada", "info")
    
    def enter_scene(self, scene_id: str):
        """Entrar a una escena."""
        try:
            self.set_loading(True, "Cargando escena...")
            self.current_scene = scene_id
            self.add_notification(f"Entrando a la escena: {scene_id}", "info")
        except Exception as e:
            self.set_error(f"Error al entrar a la escena: {str(e)}", "scene_error")
        finally:
            self.set_loading(False)
    
    def exit_scene(self):
        """Salir de la escena actual."""
        self.current_scene = None
        self.add_notification("Saliendo de la escena", "info")
    
    def save_user_data(self):
        """Guardar datos del usuario."""
        try:
            user_data = {
                "user_id": self.user_id,
                "username": self.username,
                "email": self.email,
                "is_authenticated": self.is_authenticated,
                "wallet_address": self.wallet_address,
                "is_wallet_connected": self.is_wallet_connected,
                "theme_mode": self.theme_mode,
                "language": self.language,
                "last_updated": datetime.now().isoformat()
            }
            
            with open("user_data.json", "w", encoding="utf-8") as f:
                json.dump(user_data, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.set_error(f"Error al guardar datos del usuario: {str(e)}", "save_error")
    
    def get_user_stats(self) -> Dict[str, Any]:
        """Obtener estadísticas del usuario."""
        return {
            "total_assets": len(self.user_assets),
            "total_scenes_visited": len(set([scene["id"] for scene in self.available_scenes])),
            "wallet_balance": self.wallet_balance,
            "join_date": "2024-01-01",  # Fecha de ejemplo
            "last_login": datetime.now().isoformat()
        } 