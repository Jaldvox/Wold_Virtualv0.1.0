"""Modelo de activos digitales para el metaverso."""
from typing import Optional, List, Dict
from datetime import datetime
import reflex as rx

class Asset(rx.Model):
    """Modelo de activo digital (NFT)."""
    
    # Información básica
    name: str
    description: str
    asset_type: str  # "model", "texture", "scene", etc.
    creator_id: str  # ID del usuario creador
    
    # Metadatos
    metadata: Dict = {}  # Metadatos adicionales
    tags: List[str] = []  # Etiquetas para búsqueda
    
    # Blockchain
    token_id: Optional[str] = None
    contract_address: Optional[str] = None
    blockchain: str = "ethereum"
    
    # Archivos
    file_url: str  # URL al archivo en IPFS
    thumbnail_url: Optional[str] = None
    preview_url: Optional[str] = None
    
    # Estadísticas
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    views: int = 0
    downloads: int = 0
    
    # Precios y mercado
    price: float = 0.0
    currency: str = "ETH"
    is_for_sale: bool = False
    
    class Config:
        """Configuración del modelo."""
        table = "assets"
        
    def update_metadata(self, new_metadata: Dict):
        """Actualiza los metadatos del activo."""
        self.metadata.update(new_metadata)
        self.updated_at = datetime.now()
        
    def add_tag(self, tag: str):
        """Añade una etiqueta al activo."""
        if tag not in self.tags:
            self.tags.append(tag)
            
    def remove_tag(self, tag: str):
        """Elimina una etiqueta del activo."""
        if tag in self.tags:
            self.tags.remove(tag)
            
    def increment_views(self):
        """Incrementa el contador de vistas."""
        self.views += 1
        
    def increment_downloads(self):
        """Incrementa el contador de descargas."""
        self.downloads += 1
        
    def set_price(self, price: float, currency: str = "ETH"):
        """Establece el precio del activo."""
        self.price = price
        self.currency = currency
        self.is_for_sale = True
        
    def remove_from_sale(self):
        """Retira el activo de la venta."""
        self.is_for_sale = False
        self.price = 0.0 