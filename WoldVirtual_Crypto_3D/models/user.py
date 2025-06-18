"""Modelo de usuario para el metaverso."""
from typing import Optional, List
from datetime import datetime
import reflex as rx

class User(rx.Model):
    """Modelo de usuario del metaverso."""
    
    # Información básica
    username: str
    email: str
    wallet_address: str
    created_at: datetime = datetime.now()
    
    # Estado
    is_active: bool = True
    is_verified: bool = False
    
    # Preferencias
    avatar_url: Optional[str] = None
    theme: str = "dark"
    language: str = "es"
    
    # Inventario
    owned_assets: List[str] = []  # Lista de IDs de NFTs
    created_scenes: List[str] = []  # Lista de IDs de escenas
    
    # Estadísticas
    total_transactions: int = 0
    reputation_score: float = 0.0
    
    class Config:
        """Configuración del modelo."""
        table = "users"
        
    def verify_wallet(self, signature: str) -> bool:
        """Verifica la firma de la wallet del usuario."""
        # TODO: Implementar verificación de firma
        return True
        
    def add_asset(self, asset_id: str):
        """Añade un activo al inventario del usuario."""
        if asset_id not in self.owned_assets:
            self.owned_assets.append(asset_id)
            
    def remove_asset(self, asset_id: str):
        """Elimina un activo del inventario del usuario."""
        if asset_id in self.owned_assets:
            self.owned_assets.remove(asset_id)
            
    def create_scene(self, scene_id: str):
        """Registra una nueva escena creada por el usuario."""
        if scene_id not in self.created_scenes:
            self.created_scenes.append(scene_id)
            
    def update_reputation(self, score: float):
        """Actualiza la puntuación de reputación del usuario."""
        self.reputation_score = (self.reputation_score + score) / 2 