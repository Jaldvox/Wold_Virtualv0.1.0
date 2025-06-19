"""
Gestor externo de WoldVirtual - Script para manejar la aplicación desde fuera
"""
import sys
import time
from pathlib import Path

class ExternalWoldVirtualManager:
    """Gestor externo de WoldVirtual"""
    
    def __init__(self):
        self._setup_imports()
    
    def _setup_imports(self):
        """Configurar imports y verificar disponibilidad"""
        try:
            # Agregar ruta de reflex al path si es necesario
            current_dir = Path(__file__).parent
            reflex_path = current_dir / "reflex"
            
            if reflex_path.exists() and str(reflex_path) not in sys.path:
                sys.path.insert(0, str(reflex_path))
            
            from woldvirtual_control import start_woldvirtual, stop_woldvirtual, get_woldvirtual_status
            
            self.start_woldvirtual = start_woldvirtual
            self.stop_woldvirtual = stop_woldvirtual
            self.get_woldvirtual_status = get_woldvirtual_status
            self.is_available = True
            
        except ImportError as e:
            print(f"⚠️ Módulo de control no disponible: {e}")
            self.is_available = False
    
    def launch_application(self):
        """Lanzar aplicación con manejo completo"""
        if not self.is_available:
            print("❌ Sistema de control no disponible")
            return False
        
        print("🚀 Lanzando WoldVirtual desde gestor externo...")
        
        try:
            # Verificar estado actual
            status = self.get_woldvirtual_status()
            print(f"Estado actual: {status.get('status', 'unknown')}")
            
            # Iniciar si no está corriendo
            if not status.get('is_running', False):
                result = self.start_woldvirtual()
                if result.get('success'):
                    print("✅ WoldVirtual iniciado exitosamente")
                    return True
                else:
                    print(f"❌ Error iniciando: {result.get('message')}")
                    return False
            else:
                print("ℹ️ WoldVirtual ya está corriendo")
                return True
                
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            return False
    
    def shutdown_application(self):
        """Cerrar aplicación"""
        if not self.is_available:
            print("❌ Sistema de control no disponible")
            return False
        
        print("🛑 Cerrando WoldVirtual...")
        
        try:
            result = self.stop_woldvirtual()
            
            if result.get('success'):
                print("✅ WoldVirtual cerrado")
                return True
            else:
                print(f"❌ Error cerrando: {result.get('message')}")
                return False
                
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            return False
    
    def get_status(self):
        """Obtener estado actual"""
        if not self.is_available:
            return {"available": False, "status": "Control no disponible"}
        
        try:
            return self.get_woldvirtual_status()
        except Exception as e:
            return {"available": False, "error": str(e)}
    
    def monitor_application(self):
        """Monitorear aplicación en bucle"""
        if not self.is_available:
            print("❌ Sistema de control no disponible")
            return
        
        print("📊 Monitoreando WoldVirtual (Ctrl+C para parar)...")
        
        try:
            while True:
                status = self.get_woldvirtual_status()
                print(f"Estado: {status.get('status')} | Corriendo: {status.get('is_running')}")
                time.sleep(5)
        except KeyboardInterrupt:
            print("\n👋 Monitoreo detenido")
        except Exception as e:
            print(f"❌ Error en monitoreo: {e}")

def main():
    """Función principal del gestor externo"""
    manager = ExternalWoldVirtualManager()
    
    print("🎛️ Gestor Externo de WoldVirtual")
    print("=" * 40)
    
    if not manager.is_available:
        print("❌ Sistema no disponible. Verifica la instalación.")
        return
    
    while True:
        print("\nOpciones disponibles:")
        print("1. Lanzar aplicación")
        print("2. Cerrar aplicación") 
        print("3. Ver estado")
        print("4. Monitorear aplicación")
        print("5. Salir")
        
        try:
            choice = input("\nSelecciona opción (1-5): ").strip()
            
            if choice == '1':
                manager.launch_application()
            elif choice == '2':
                manager.shutdown_application()
            elif choice == '3':
                status = manager.get_status()
                print(f"📊 Estado: {status}")
            elif choice == '4':
                manager.monitor_application()
            elif choice == '5':
                print("👋 Saliendo...")
                break
            else:
                print("❌ Opción inválida")
                
        except KeyboardInterrupt:
            print("\n👋 Saliendo...")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()