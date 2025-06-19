"""
Módulo de Control Maestro para WoldVirtual
Gestiona toda la aplicación desde un punto central
"""
import os
import sys
import time
import threading
import subprocess
import signal
from pathlib import Path
from typing import Dict, Any, Optional, Callable
import json
import logging

class WoldVirtualController:
    """Controlador maestro de WoldVirtual"""
    
    def __init__(self):
        self.reflex_dir = Path(__file__).parent.absolute()
        self.is_running = False
        self.reflex_process = None
        self.status = "stopped"
        self.logs = []
        self.config = self.load_config()
        self.setup_logging()
        
        # Módulos disponibles
        self.modules = {}
        self.load_modules()
    
    def setup_logging(self):
        """Configurar sistema de logs"""
        log_file = self.reflex_dir / 'woldvirtual.log'
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def load_config(self) -> Dict[str, Any]:
        """Cargar configuración"""
        config_file = self.reflex_dir / 'controller_config.json'
        default_config = {
            "app": {
                "name": "WoldVirtual_Crypto_3D",
                "version": "1.0.0",
                "auto_restart": True,
                "max_restart_attempts": 3
            },
            "ports": {
                "frontend": 3000,
                "backend": 8000
            },
            "modules": {
                "diagnostics": True,
                "auto_fix": True,
                "monitor": True,
                "smart_runner": True
            },
            "ui": {
                "theme": "violet",
                "auto_open_browser": True
            }
        }
        
        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    loaded_config = json.load(f)
                return {**default_config, **loaded_config}
            except:
                pass
        
        # Guardar config por defecto
        with open(config_file, 'w') as f:
            json.dump(default_config, f, indent=2)
        
        return default_config
    
    def load_modules(self):
        """Cargar módulos auxiliares"""
        module_files = {
            'diagnostics': 'diagnostics.py',
            'auto_fix': 'auto_fix.py',
            'smart_runner': 'smart_runner.py',
            'monitor': 'monitor.py'
        }
        
        for module_name, file_name in module_files.items():
            if self.config['modules'].get(module_name, False):
                try:
                    module_path = self.reflex_dir / file_name
                    if module_path.exists():
                        # Importar dinámicamente
                        spec = importlib.util.spec_from_file_location(module_name, module_path)
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        self.modules[module_name] = module
                        self.logger.info(f"✅ Módulo {module_name} cargado")
                    else:
                        self.logger.warning(f"⚠️ Archivo {file_name} no encontrado")
                except Exception as e:
                    self.logger.error(f"❌ Error cargando {module_name}: {e}")
    
    def get_status(self) -> Dict[str, Any]:
        """Obtener estado completo del sistema"""
        return {
            'status': self.status,
            'is_running': self.is_running,
            'process_id': self.reflex_process.pid if self.reflex_process else None,
            'uptime': time.time() - self.start_time if hasattr(self, 'start_time') else 0,
            'config': self.config,
            'modules_loaded': list(self.modules.keys()),
            'logs_count': len(self.logs)
        }
    
    def run_diagnostics(self) -> Dict[str, Any]:
        """Ejecutar diagnósticos usando módulo"""
        if 'diagnostics' in self.modules:
            try:
                diagnostics = self.modules['diagnostics'].SystemDiagnostics()
                return diagnostics.run_full_diagnosis()
            except Exception as e:
                self.logger.error(f"Error en diagnósticos: {e}")
                return {'error': str(e)}
        else:
            return {'error': 'Módulo de diagnósticos no disponible'}
    
    def apply_auto_fix(self) -> Dict[str, bool]:
        """Aplicar correcciones automáticas"""
        if 'auto_fix' in self.modules:
            try:
                fixer = self.modules['auto_fix'].AutoFixer()
                return fixer.run_auto_repair()
            except Exception as e:
                self.logger.error(f"Error en auto-reparación: {e}")
                return {'error': str(e)}
        else:
            return {'error': 'Módulo de auto-reparación no disponible'}
    
    def start_app(self, force_restart: bool = False) -> bool:
        """Iniciar aplicación"""
        if self.is_running and not force_restart:
            self.logger.info("Aplicación ya está corriendo")
            return True
        
        if force_restart and self.is_running:
            self.stop_app()
        
        self.logger.info("🚀 Iniciando WoldVirtual...")
        self.status = "starting"
        
        # Asegurar directorio correcto
        os.chdir(str(self.reflex_dir))
        
        # Ejecutar diagnósticos si está habilitado
        if self.config['modules'].get('diagnostics', False):
            self.logger.info("🔍 Ejecutando diagnósticos...")
            diag_results = self.run_diagnostics()
            
            # Auto-reparar si hay problemas
            if any(result.get('status') == 'error' for result in diag_results.values()):
                self.logger.info("🔧 Aplicando correcciones automáticas...")
                self.apply_auto_fix()
        
        try:
            # Iniciar proceso de Reflex
            self.reflex_process = subprocess.Popen(
                ['reflex', 'run'],
                cwd=str(self.reflex_dir),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Esperar un poco para verificar inicio
            time.sleep(3)
            
            if self.reflex_process.poll() is None:
                self.is_running = True
                self.status = "running"
                self.start_time = time.time()
                self.logger.info("✅ WoldVirtual iniciado exitosamente")
                
                # Abrir navegador automáticamente
                if self.config['ui'].get('auto_open_browser', False):
                    self.open_browser()
                
                return True
            else:
                stdout, stderr = self.reflex_process.communicate()
                self.logger.error(f"❌ Error iniciando: {stderr}")
                self.status = "error"
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Error crítico: {e}")
            self.status = "error"
            return False
    
    def stop_app(self) -> bool:
        """Detener aplicación"""
        if not self.is_running:
            self.logger.info("Aplicación no está corriendo")
            return True
        
        self.logger.info("🛑 Deteniendo WoldVirtual...")
        self.status = "stopping"
        
        try:
            if self.reflex_process:
                # Terminar proceso gradualmente
                self.reflex_process.terminate()
                
                # Esperar terminación
                try:
                    self.reflex_process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    # Force kill si no responde
                    self.reflex_process.kill()
                    self.reflex_process.wait()
                
                self.reflex_process = None
            
            self.is_running = False
            self.status = "stopped"
            self.logger.info("✅ WoldVirtual detenido")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Error deteniendo: {e}")
            return False
    
    def restart_app(self) -> bool:
        """Reiniciar aplicación"""
        self.logger.info("🔄 Reiniciando WoldVirtual...")
        self.stop_app()
        time.sleep(2)
        return self.start_app()
    
    def open_browser(self):
        """Abrir navegador"""
        url = f"http://localhost:{self.config['ports']['frontend']}"
        try:
            if os.name == 'nt':  # Windows
                os.startfile(url)
            else:  # Linux/Mac
                subprocess.run(['xdg-open', url])
            self.logger.info(f"🌐 Navegador abierto: {url}")
        except Exception as e:
            self.logger.error(f"Error abriendo navegador: {e}")
    
    def monitor_health(self) -> Dict[str, Any]:
        """Monitorear salud de la aplicación"""
        if 'monitor' in self.modules:
            try:
                monitor = self.modules['monitor'].AppMonitor()
                return monitor.get_status()
            except Exception as e:
                return {'error': str(e)}
        else:
            return {'basic_check': self.is_running}
    
    def get_logs(self, last_n: int = 50) -> list:
        """Obtener últimos logs"""
        return self.logs[-last_n:] if self.logs else []
    
    def save_state(self):
        """Guardar estado actual"""
        state_file = self.reflex_dir / 'app_state.json'
        state = {
            'last_run': time.time(),
            'config': self.config,
            'status': self.status
        }
        
        with open(state_file, 'w') as f:
            json.dump(state, f, indent=2)

# Instancia global del controlador
controller = WoldVirtualController()