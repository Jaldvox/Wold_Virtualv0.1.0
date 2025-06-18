import reflex as rx

class State(rx.State):
    """Estado global de la aplicación."""
    
    # Estado de la escena 3D
    scene_loaded: bool = False
    current_scene: str = "main"
    
    # Estado del usuario
    is_authenticated: bool = False
    username: str = ""
    wallet_address: str = ""
    
    # Estado de la cámara
    camera_position: list[float] = [0, 0, 5]
    camera_target: list[float] = [0, 0, 0]
    
    def load_scene(self, scene_name: str):
        """Carga una escena 3D."""
        self.current_scene = scene_name
        self.scene_loaded = True
        
    def update_camera(self, position: list[float], target: list[float]):
        """Actualiza la posición y objetivo de la cámara."""
        self.camera_position = position
        self.camera_target = target
        
    def connect_wallet(self):
        """Conecta la wallet del usuario."""
        # Aquí implementaremos la conexión real con Web3
        self.is_authenticated = True
        self.wallet_address = "0x123..."  # Placeholder
        self.username = f"Usuario_{self.wallet_address[:6]}" 