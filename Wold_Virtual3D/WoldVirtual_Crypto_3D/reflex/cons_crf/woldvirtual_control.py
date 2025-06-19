"""
Script para controlar WoldVirtual desde otros módulos o línea de comandos
"""
import sys
import json
import argparse
from pathlib import Path

# Agregar directorio reflex al path
reflex_dir = Path(__file__).parent.absolute()
sys.path.insert(0, str(reflex_dir))

try:
    from control_api import api
    API_AVAILABLE = True
except ImportError:
    API_AVAILABLE = False
    print("⚠️ API de control no disponible")

class WoldVirtualControl:
    """Controlador externo para WoldVirtual"""
    
    def __init__(self):
        self.api = api if API_AVAILABLE else None
    
    def execute_command(self, command: str, **kwargs) -> Dict[str, Any]:
        """Ejecutar comando"""
        if not self.api:
            return {'error': 'API no disponible'}
        
        commands = {
            'start': self.api.start,
            'stop': self.api.stop,
            'restart': self.api.restart,
            'status': self.api.status,
            'health': self.api.health,
            'diagnostics': self.api.diagnostics,
            'fix': self.api.fix,
            'logs': lambda: self.api.logs(kwargs.get('count', 20))
        }
        
        if command in commands:
            try:
                return commands[command]()
            except Exception as e:
                return {'error': str(e)}
        else:
            return {'error': f'Comando desconocido: {command}'}
    
    def start_interactive(self):
        """Modo interactivo"""
        print("🎛️ WoldVirtual Control - Modo Interactivo")
        print("Comandos: start, stop, restart, status, health, diagnostics, fix, logs, quit")
        
        while True:
            try:
                command = input("\n> ").strip().lower()
                
                if command == 'quit':
                    break
                elif command == 'help':
                    self.show_help()
                elif command:
                    result = self.execute_command(command)
                    print(json.dumps(result, indent=2))
                    
            except KeyboardInterrupt:
                print("\n👋 Saliendo...")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def show_help(self):
        """Mostrar ayuda"""
        help_text = """
🎛️ COMANDOS DISPONIBLES:

start      - Iniciar WoldVirtual
stop       - Detener WoldVirtual
restart    - Reiniciar WoldVirtual
status     - Mostrar estado actual
health     - Verificar salud de la aplicación
diagnostics- Ejecutar diagnósticos
fix        - Aplicar correcciones automáticas
logs       - Mostrar logs recientes
quit       - Salir del control
help       - Mostrar esta ayuda
"""
        print(help_text)

def main():
    """Función principal para línea de comandos"""
    parser = argparse.ArgumentParser(description='Control de WoldVirtual')
    parser.add_argument('command', nargs='?', 
                       choices=['start', 'stop', 'restart', 'status', 'health', 'diagnostics', 'fix', 'logs', 'interactive'],
                       help='Comando a ejecutar')
    parser.add_argument('--count', type=int, default=20, help='Número de logs a mostrar')
    
    args = parser.parse_args()
    
    control = WoldVirtualControl()
    
    if not args.command or args.command == 'interactive':
        control.start_interactive()
    else:
        result = control.execute_command(args.command, count=args.count)
        print(json.dumps(result, indent=2))

# Funciones de conveniencia para usar desde otros módulos
def start_woldvirtual():
    """Iniciar WoldVirtual desde otro módulo"""
    control = WoldVirtualControl()
    return control.execute_command('start')

def stop_woldvirtual():
    """Detener WoldVirtual desde otro módulo"""
    control = WoldVirtualControl()
    return control.execute_command('stop')

def get_woldvirtual_status():
    """Obtener estado desde otro módulo"""
    control = WoldVirtualControl()
    return control.execute_command('status')

if __name__ == "__main__":
    main()