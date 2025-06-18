"""Modelo de escenas 3D para el metaverso."""
from typing import Optional, List, Dict
from datetime import datetime
import reflex as rx

class Scene(rx.Model):
    """Modelo de escena 3D."""
    
    # Información básica
    name: str
    description: str
    creator_id: str  # ID del usuario creador
    
    # Configuración de la escena
    width: int = 1000  # Ancho en unidades del mundo
    height: int = 1000  # Alto en unidades del mundo
    depth: int = 1000  # Profundidad en unidades del mundo
    
    # Contenido
    assets: List[str] = []  # IDs de los activos en la escena
    objects: List[Dict] = []  # Objetos y sus transformaciones
    environment: Dict = {}  # Configuración del entorno
    
    # Metadatos
    metadata: Dict = {}  # Metadatos adicionales
    tags: List[str] = []  # Etiquetas para búsqueda
    
    # Blockchain
    token_id: Optional[str] = None
    contract_address: Optional[str] = None
    blockchain: str = "ethereum"
    
    # Archivos
    scene_file_url: str  # URL al archivo de la escena en IPFS
    thumbnail_url: Optional[str] = None
    preview_url: Optional[str] = None
    
    # Estadísticas
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    views: int = 0
    visits: int = 0
    
    # Precios y mercado
    price: float = 0.0
    currency: str = "ETH"
    is_for_sale: bool = False
    
    class Config:
        """Configuración del modelo."""
        table = "scenes"
        
    def add_asset(self, asset_id: str, transform: Dict):
        """Añade un activo a la escena."""
        if asset_id not in self.assets:
            self.assets.append(asset_id)
            self.objects.append({
                "asset_id": asset_id,
                "transform": transform
            })
            self.updated_at = datetime.now()
            
    def remove_asset(self, asset_id: str):
        """Elimina un activo de la escena."""
        if asset_id in self.assets:
            self.assets.remove(asset_id)
            self.objects = [obj for obj in self.objects if obj["asset_id"] != asset_id]
            self.updated_at = datetime.now()
            
    def update_environment(self, new_environment: Dict):
        """Actualiza la configuración del entorno."""
        self.environment.update(new_environment)
        self.updated_at = datetime.now()
        
    def add_tag(self, tag: str):
        """Añade una etiqueta a la escena."""
        if tag not in self.tags:
            self.tags.append(tag)
            
    def remove_tag(self, tag: str):
        """Elimina una etiqueta de la escena."""
        if tag in self.tags:
            self.tags.remove(tag)
            
    def increment_views(self):
        """Incrementa el contador de vistas."""
        self.views += 1
        
    def increment_visits(self):
        """Incrementa el contador de visitas."""
        self.visits += 1
        
    def set_price(self, price: float, currency: str = "ETH"):
        """Establece el precio de la escena."""
        self.price = price
        self.currency = currency
        self.is_for_sale = True
        
    def remove_from_sale(self):
        """Retira la escena de la venta."""
        self.is_for_sale = False
        self.price = 0.0 