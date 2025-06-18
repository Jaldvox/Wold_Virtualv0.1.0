"""Modelo de transacciones para el metaverso."""
from typing import Optional, Dict
from datetime import datetime
import reflex as rx

class Transaction(rx.Model):
    """Modelo de transacción blockchain."""
    
    # Información básica
    transaction_type: str  # "purchase", "sale", "transfer", etc.
    sender_id: str  # ID del usuario remitente
    receiver_id: str  # ID del usuario destinatario
    
    # Detalles de la transacción
    asset_id: Optional[str] = None  # ID del activo involucrado
    scene_id: Optional[str] = None  # ID de la escena involucrada
    amount: float = 0.0  # Cantidad de la transacción
    currency: str = "ETH"  # Moneda de la transacción
    
    # Blockchain
    transaction_hash: str  # Hash de la transacción
    block_number: Optional[int] = None  # Número del bloque
    block_timestamp: Optional[datetime] = None  # Timestamp del bloque
    
    # Estado
    status: str = "pending"  # "pending", "confirmed", "failed"
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    
    # Metadatos
    metadata: Dict = {}  # Metadatos adicionales
    
    class Config:
        """Configuración del modelo."""
        table = "transactions"
        
    def update_status(self, new_status: str):
        """Actualiza el estado de la transacción."""
        self.status = new_status
        self.updated_at = datetime.now()
        
    def add_metadata(self, new_metadata: Dict):
        """Añade metadatos a la transacción."""
        self.metadata.update(new_metadata)
        self.updated_at = datetime.now()
        
    def confirm_transaction(self, block_number: int, block_timestamp: datetime):
        """Confirma la transacción con información del bloque."""
        self.block_number = block_number
        self.block_timestamp = block_timestamp
        self.status = "confirmed"
        self.updated_at = datetime.now()
        
    def fail_transaction(self):
        """Marca la transacción como fallida."""
        self.status = "failed"
        self.updated_at = datetime.now() 