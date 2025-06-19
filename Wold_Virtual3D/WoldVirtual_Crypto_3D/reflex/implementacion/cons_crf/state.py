"""
Estado modular para WoldVirtual - Versión simplificada
"""
import reflex as rx
import os

class GlobalState(rx.State):
    """Estado global simplificado"""
    app_status: str = "Inicializando..."
    current_directory: str = ""
    show_networks_menu: bool = False
    selected_network: str = "Redes Blockchain"

    def on_load(self):
        self.current_directory = os.getcwd()
        if "reflex" in self.current_directory:
            self.app_status = "✅ Módulos funcionando desde /reflex"
        else:
            self.app_status = f"⚠️ Directorio: {self.current_directory}"

    def toggle_networks_menu(self):
        self.show_networks_menu = not self.show_networks_menu

    def select_network(self, network: str):
        self.selected_network = network
        self.show_networks_menu = False

# Alias para compatibilidad
NetworkState = GlobalState
SceneState = GlobalState  
WalletState = GlobalState