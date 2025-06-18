class Asset:
    """Modelo que representa un activo en la base de datos."""

    def __init__(self, asset_id, name, description, asset_type, owner_id):
        self.asset_id = asset_id  # Identificador único del activo
        self.name = name  # Nombre del activo
        self.description = description  # Descripción del activo
        self.asset_type = asset_type  # Tipo de activo (ej. 'modelo', 'textura', etc.)
        self.owner_id = owner_id  # Identificador del propietario del activo

    def to_dict(self):
        """Convierte el modelo a un diccionario para facilitar la serialización."""
        return {
            "asset_id": self.asset_id,
            "name": self.name,
            "description": self.description,
            "asset_type": self.asset_type,
            "owner_id": self.owner_id,
        }