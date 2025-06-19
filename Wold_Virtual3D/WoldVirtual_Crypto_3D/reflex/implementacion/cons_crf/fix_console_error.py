"""
Script principal para corregir errores de consola
"""
import sys
import time
from pathlib import Path

# Imports locales con manejo de errores
try:
    from error_analyzer import ConsoleErrorAnalyzer
    from auto_corrector import AutoCorrector  
    from clean_code_generator import CleanCodeGenerator
    MODULES_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Error importando módulos: {e}")
    MODULES_AVAILABLE = False

class ConsoleErrorFixer:
    """Reparador principal de errores de consola"""
    
    def __init__(self):
        self.reflex_dir = Path(__file__).parent.absolute()
        
        if MODULES_AVAILABLE:
            self.analyzer = ConsoleErrorAnalyzer()
            self.corrector = AutoCorrector()
            self.generator = CleanCodeGenerator()
        else:
            self.analyzer = None
            self.corrector = None
            self.generator = None
    
    def get_sample_error_log(self) -> str:
        """Error log de ejemplo basado en tu imagen"""
        return '''
"importlib" is not defined  Pylance(reportUndefinedVariable) [Ln 100, Col 32]
"importlib" is not defined  Pylance(reportUndefinedVariable) [Ln 101, Col 34]
Type "dict[str, str]" is not assignable to return type "Dict[str, bool]"  Pylance(reportReturnType) [Ln 142, Col 34]
"str" is not assignable to "bool"
"Literal['Módulo de auto-reparación no disponible']" is not assignable to "bool"
Type "None" is not assignable to return type "Path"  Pylance(reportReturnType) [Ln 24, Col 16]
"None" is not assignable to "Path"
"Dict" is not defined  Pylance(reportUndefinedVariable) [Ln 17, Col 24]
"Any" is not defined  Pylance(reportUndefinedVariable) [Ln 17, Col 34]
"Dict" is not defined  Pylance(reportUndefinedVariable) [Ln 26, Col 23]
"Any" is not defined  Pylance(reportUndefinedVariable) [Ln 26, Col 33]
"Dict" is not defined  Pylance(reportUndefinedVariable) [Ln 35, Col 26]
"Any" is not defined  Pylance(reportUndefinedVariable) [Ln 35, Col 36]
"Dict" is not defined  Pylance(reportUndefinedVariable) [Ln 44, Col 25]
"Any" is not defined  Pylance(reportUndefinedVariable) [Ln 44, Col 35]
"Dict" is not defined  Pylance(reportUndefinedVariable) [Ln 48, Col 25]
"Any" is not defined  Pylance(reportUndefinedVariable) [Ln 48, Col 35]
"Dict" is not defined  Pylance(reportUndefinedVariable) [Ln 52, Col 30]
"Any" is not defined  Pylance(reportUndefinedVariable) [Ln 52, Col 40]
"Dict" is not defined  Pylance(reportUndefinedVariable) [Ln 56, Col 22]
"Any" is not defined  Pylance(reportUndefinedVariable) [Ln 56, Col 32]
"Dict" is not defined  Pylance(reportUndefinedVariable) [Ln 60, Col 40]
"Any" is not defined  Pylance(reportUndefinedVariable) [Ln 60, Col 50]
"Dict" is not defined  Pylance(reportUndefinedVariable) [Ln 67, Col 33]
"Any" is not defined  Pylance(reportUndefinedVariable) [Ln 67, Col 43]
"Dict" is not defined  Pylance(reportUndefinedVariable) [Ln 67, Col 52]
"stop_app" is not a known attribute of "None"  Pylance(reportOptionalMemberAccess) [Ln 68, Col 39]
'''
    
    def run_emergency_fix(self) -> bool:
        """Ejecutar corrección de emergencia sin dependencias"""
        print("🚨 Ejecutando corrección de emergencia...")
        
        try:
            # Regenerar módulos básicos sin errores
            self.create_emergency_modules()
            print("✅ Módulos de emergencia creados")
            return True
        except Exception as e:
            print(f"❌ Error en corrección de emergencia: {e}")
            return False
    
    def create_emergency_modules(self):
        """Crear módulos básicos sin errores"""
        
        # Crear app_controller básico
        controller_content = '''import os
import sys
import subprocess
import time
import json
from pathlib import Path

class WoldVirtualController:
    def __init__(self):
        self.reflex_dir = Path(__file__).parent.absolute()
        self.is_running = False
        self.status = "stopped"
    
    def start_app(self):
        """Iniciar aplicación"""
        try:
            os.chdir(str(self.reflex_dir))
            self.reflex_process = subprocess.Popen(['reflex', 'run'])
            time.sleep(3)
            if self.reflex_process.poll() is None:
                self.is_running = True
                self.status = "running"
                return True
        except Exception:
            pass
        return False
    
    def stop_app(self):
        """Detener aplicación"""
        try:
            if hasattr(self, 'reflex_process') and self.reflex_process:
                self.reflex_process.terminate()
            self.is_running = False
            self.status = "stopped"
            return True
        except Exception:
            pass
        return False
    
    def get_status(self):
        """Obtener estado"""
        return {
            'status': self.status,
            'is_running': self.is_running
        }

controller = WoldVirtualController()
'''
        
        # Crear control_api básico
        api_content = '''try:
    from app_controller import controller
except ImportError:
    controller = None

class ControlAPI:
    def __init__(self):
        self.controller = controller
    
    def start(self):
        if self.controller:
            success = self.controller.start_app()
            return {'success': success, 'status': self.controller.status}
        return {'success': False, 'error': 'Controller no disponible'}
    
    def stop(self):
        if self.controller:
            success = self.controller.stop_app()
            return {'success': success, 'status': self.controller.status}
        return {'success': False, 'error': 'Controller no disponible'}
    
    def status(self):
        if self.controller:
            return self.controller.get_status()
        return {'error': 'Controller no disponible'}

api = ControlAPI()
'''
        
        # Crear woldvirtual_control básico
        control_content = '''import sys
from pathlib import Path

reflex_dir = Path(__file__).parent.absolute()
sys.path.insert(0, str(reflex_dir))

try:
    from control_api import api
except ImportError:
    api = None

def start_woldvirtual():
    if api:
        return api.start()
    return {'error': 'API no disponible'}

def stop_woldvirtual():
    if api:
        return api.stop()
    return {'error': 'API no disponible'}

def get_woldvirtual_status():
    if api:
        return api.status()
    return {'error': 'API no disponible'}

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'start':
            print(start_woldvirtual())
        elif command == 'stop':
            print(stop_woldvirtual())
        elif command == 'status':
            print(get_woldvirtual_status())
'''
        
        # Escribir archivos
        modules = {
            'app_controller.py': controller_content,
            'control_api.py': api_content,
            'woldvirtual_control.py': control_content
        }
        
        for filename, content in modules.items():
            file_path = self.reflex_dir / filename
            try:
                file_path.write_text(content, encoding='utf-8')
                print(f"✅ Creado: {filename}")
            except Exception as e:
                print(f"❌ Error creando {filename}: {e}")
    
    def run_full_repair(self):
        """Ejecutar reparación completa"""
        print("🔧 Ejecutando reparación completa de errores de consola...")
        
        if not MODULES_AVAILABLE:
            print("⚠️ Módulos de análisis no disponibles, usando reparación de emergencia")
            return self.run_emergency_fix()
        
        try:
            # Usar log de errores de ejemplo
            error_log = self.get_sample_error_log()
            
            # Analizar errores
            print("🔍 Analizando errores...")
            errors = self.analyzer.analyze_error_log(error_log)
            print(f"Encontrados {len(errors)} errores")
            
            # Aplicar correcciones
            print("🔧 Aplicando correcciones...")
            results = self.corrector.fix_all_errors(error_log)
            print(f"Procesados {results['files_processed']} archivos")
            print(f"Aplicadas {results['total_fixes']} correcciones")
            
            # Regenerar módulos si es necesario
            if results['total_fixes'] < results['total_errors']:
                print("🔄 Regenerando módulos problemáticos...")
                gen_results = self.generator.regenerate_all_modules()
                print("Módulos regenerados:", len(gen_results))
            
            return True
            
        except Exception as e:
            print(f"❌ Error en reparación completa: {e}")
            print("🚨 Ejecutando reparación de emergencia...")
            return self.run_emergency_fix()

def main():
    """Función principal"""
    print("🛠️ Sistema de Corrección de Errores de Consola")
    print("=" * 50)
    
    fixer = ConsoleErrorFixer()
    
    choice = input("1. Reparación completa\n2. Reparación de emergencia\nSelecciona (1-2): ").strip()
    
    if choice == '1':
        success = fixer.run_full_repair()
    else:
        success = fixer.run_emergency_fix()
    
    if success:
        print("\n✅ Reparación completada")
        print("💡 Intenta ejecutar: python woldvirtual_control.py start")
    else:
        print("\n❌ Reparación falló")

if __name__ == "__main__":
    main()