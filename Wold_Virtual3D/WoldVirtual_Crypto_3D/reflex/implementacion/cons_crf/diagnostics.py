"""
Módulo de diagnóstico y corrección automática de errores
"""
import sys
import subprocess
from pathlib import Path
from typing import Dict, List, Any

class SystemDiagnostics:
    """Diagnosticar y corregir problemas del sistema"""
    
    def __init__(self):
        self.reflex_dir = Path(__file__).parent.absolute()
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.fixes: List[str] = []
    
    def run_full_diagnosis(self) -> Dict[str, Any]:
        """Ejecutar diagnóstico completo"""
        print("🔍 Iniciando diagnóstico completo...")
        
        results = {
            'python_check': self.check_python_environment(),
            'reflex_check': self.check_reflex_installation(),
            'directory_check': self.check_directory_structure(),
            'imports_check': self.check_imports(),
            'config_check': self.check_configuration(),
            'permissions_check': self.check_permissions(),
        }
        
        self.generate_report(results)
        return results
    
    def check_python_environment(self) -> Dict[str, Any]:
        """Verificar entorno Python"""
        result: Dict[str, Any] = {'status': 'ok', 'details': [], 'fixes': []}
        
        try:
            # Verificar versión Python
            python_version = sys.version_info
            if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
                result['status'] = 'error'
                result['details'].append(f"Python {python_version.major}.{python_version.minor} demasiado antiguo")
                result['fixes'].append("Actualizar a Python 3.8+")
            else:
                result['details'].append(f"Python {python_version.major}.{python_version.minor} ✅")
            
            # Verificar PYTHONPATH
            current_path = str(self.reflex_dir)
            if current_path not in sys.path:
                if 'warnings' not in result:
                    result['warnings'] = []
                result['warnings'].append("Directorio actual no en PYTHONPATH")
                result['fixes'].append("Agregar directorio al PYTHONPATH")
                
        except Exception as e:
            result['status'] = 'error'
            result['details'].append(f"Error verificando Python: {e}")
            
        return result
    
    def check_reflex_installation(self) -> Dict[str, Any]:
        """Verificar instalación de Reflex"""
        result: Dict[str, Any] = {'status': 'ok', 'details': [], 'fixes': []}
        
        try:
            import reflex as rx
        try:
            import reflex as rx
            try:
                version = getattr(rx, '__version__', 'unknown')
            except:
                version = 'unknown'
            result['details'].append(f"Reflex {version} ✅")
            try:
                subprocess.run(['reflex', '--version'], 
                             capture_output=True, check=True, timeout=10)
                result['details'].append("Comando 'reflex' disponible ✅")
            except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
                result['status'] = 'warning'
                result['details'].append("Comando 'reflex' no disponible")
                result['fixes'].append("Reinstalar Reflex")
                
        except ImportError as e:
            result['status'] = 'error'
            result['details'].append(f"Reflex no instalado: {e}")
            result['fixes'].append("pip install reflex")
            
        return result
    
    def check_directory_structure(self) -> Dict[str, Any]:
        """Verificar estructura de directorios"""
        result: Dict[str, Any] = {'status': 'ok', 'details': [], 'fixes': []}
        
        required_files = [
            'WoldVirtual_Crypto_3D.py',
            'rxconfig.py'
        ]
        
        optional_files = [
            '__init__.py',
            'requirements.txt',
            '.env'
        ]
        
        # Verificar archivos requeridos
        for file in required_files:
            file_path = self.reflex_dir / file
            if not file_path.exists():
                result['status'] = 'error'
                result['details'].append(f"Archivo faltante: {file}")
                result['fixes'].append(f"Crear {file}")
            else:
                result['details'].append(f"{file} ✅")
        
        # Verificar archivos opcionales
        for file in optional_files:
            file_path = self.reflex_dir / file
            if not file_path.exists():
                if 'warnings' not in result:
                    result['warnings'] = []
                result['warnings'].append(f"Archivo opcional faltante: {file}")
                result['fixes'].append(f"Crear {file}")
            else:
                result['details'].append(f"{file} ✅")
                
        return result
    
    def check_imports(self) -> Dict[str, Any]:
        """Verificar imports problemáticos"""
        result: Dict[str, Any] = {'status': 'ok', 'details': [], 'fixes': []}
        
        main_file = self.reflex_dir / 'WoldVirtual_Crypto_3D.py'
        if not main_file.exists():
            result['status'] = 'error'
            result['details'].append("Archivo principal no existe")
            return result
        
        try:
            # Leer archivo y buscar imports problemáticos
            with open(main_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            problematic_imports = [
                'from state import',
                'from components import',
                'from blockchain import',
                'from utils import'
            ]
            
            for imp in problematic_imports:
                if imp in content:
                    if 'warnings' not in result:
                        result['warnings'] = []
                    result['warnings'].append(f"Import problemático encontrado: {imp}")
                    result['fixes'].append(f"Reemplazar o condicionalizar: {imp}")
            
            # Verificar import de reflex
            if 'import reflex as rx' not in content:
                result['status'] = 'error'
                result['details'].append("Import de reflex faltante")
                result['fixes'].append("Agregar 'import reflex as rx'")
            else:
                result['details'].append("Import de reflex ✅")
                
        except Exception as e:
            result['status'] = 'error'
            result['details'].append(f"Error leyendo archivo principal: {e}")
            
        return result
    
    def check_configuration(self) -> Dict[str, Any]:
        """Verificar configuración"""
        result: Dict[str, Any] = {'status': 'ok', 'details': [], 'fixes': []}
        
        config_file = self.reflex_dir / 'rxconfig.py'
        if not config_file.exists():
            result['status'] = 'error'
            result['details'].append("rxconfig.py no existe")
            result['fixes'].append("Crear rxconfig.py básico")
            return result
        
        try:
            # Verificar contenido básico
            with open(config_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'import reflex as rx' not in content:
                result['status'] = 'error'
                result['details'].append("rxconfig.py sin import de reflex")
                result['fixes'].append("Agregar import de reflex")
            
            if 'config = rx.Config' not in content:
                result['status'] = 'error'
                result['details'].append("rxconfig.py sin configuración")
                result['fixes'].append("Agregar configuración básica")
            
            if result['status'] == 'ok':
                result['details'].append("rxconfig.py ✅")
                
        except Exception as e:
            result['status'] = 'error'
            result['details'].append(f"Error leyendo rxconfig.py: {e}")
            
        return result
    
    def check_permissions(self) -> Dict[str, Any]:
        """Verificar permisos"""
        result: Dict[str, Any] = {'status': 'ok', 'details': [], 'fixes': []}
        
        try:
            # Verificar escritura en directorio
            test_file = self.reflex_dir / 'test_write.tmp'
            test_file.write_text('test')
            test_file.unlink()
            result['details'].append("Permisos de escritura ✅")
            
        except Exception as e:
            result['status'] = 'error'
            result['details'].append(f"Sin permisos de escritura: {e}")
            result['fixes'].append("Ejecutar como administrador")
            
        return result
    
    def generate_report(self, results: Dict[str, Any]) -> None:
        """Generar reporte de diagnóstico"""
        print("\n" + "="*50)
        print("📋 REPORTE DE DIAGNÓSTICO")
        print("="*50)
        
        for check_name, result in results.items():
            status_emoji = {
                'ok': '✅',
                'warning': '⚠️',
                'error': '❌'
            }.get(result['status'], '❓')
            
            print(f"\n{status_emoji} {check_name.replace('_', ' ').title()}")
            
            for detail in result.get('details', []):
                print(f"  • {detail}")
            
            for warning in result.get('warnings', []):
                print(f"  ⚠️ {warning}")
            
            if result.get('fixes'):
                print("  💡 Soluciones:")
                for fix in result['fixes']:
                    print(f"    - {fix}")