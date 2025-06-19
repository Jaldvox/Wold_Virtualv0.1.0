"""
API de control para manejar WoldVirtual externamente
"""
import importlib.util
import json
import time
import logging
from typing import Dict, Any, Optional

# Configurar logging
logger = logging.getLogger(__name__)

class ControlAPI:
    """API para controlar WoldVirtual desde otros scripts"""
    
    def __init__(self):
        self.controller = None
        self._initialize_controller()
    
    def _initialize_controller(self) -> None:
        """Inicializar controlador de forma segura"""
        try:
            from app_controller import controller
            self.controller = controller
        except ImportError as e:
            logger.error(f"Error importando app_controller: {e}")
            self.controller = None
    
    def _check_controller(self) -> bool:
        """Verificar que el controlador esté disponible"""
        return self.controller is not None
    
    def _safe_response(self, success: bool, message: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Crear respuesta segura"""
        response = {
            'success': success,
            'message': message,
            'timestamp': time.time()
        }
        if data:
            response.update(data)
        return response
    
    # Métodos de control básico
    def start(self) -> Dict[str, Any]:
        """Iniciar aplicación"""
        if not self._check_controller():
            return self._safe_response(False, "Controlador no disponible")
        
        try:
            success = self.controller.start_app()
            status = getattr(self.controller, 'status', 'unknown')
            return self._safe_response(
                success, 
                'Aplicación iniciada' if success else 'Error iniciando aplicación',
                {'status': status}
            )
        except Exception as e:
            logger.error(f"Error en start(): {e}")
            return self._safe_response(False, f"Error inesperado: {str(e)}")
    
    def stop(self) -> Dict[str, Any]:
        """Detener aplicación"""
        if not self._check_controller():
            return self._safe_response(False, "Controlador no disponible")
        
        try:
            success = self.controller.stop_app()
            status = getattr(self.controller, 'status', 'unknown')
            return self._safe_response(
                success,
                'Aplicación detenida' if success else 'Error deteniendo aplicación',
                {'status': status}
            )
        except Exception as e:
            logger.error(f"Error en stop(): {e}")
            return self._safe_response(False, f"Error inesperado: {str(e)}")
    
    def restart(self) -> Dict[str, Any]:
        """Reiniciar aplicación"""
        if not self._check_controller():
            return self._safe_response(False, "Controlador no disponible")
        
        try:
            success = self.controller.restart_app()
            status = getattr(self.controller, 'status', 'unknown')
            return self._safe_response(
                success,
                'Aplicación reiniciada' if success else 'Error reiniciando aplicación',
                {'status': status}
            )
        except Exception as e:
            logger.error(f"Error en restart(): {e}")
            return self._safe_response(False, f"Error inesperado: {str(e)}")
    
    def status(self) -> Dict[str, Any]:
        """Obtener estado"""
        if not self._check_controller():
            return self._safe_response(False, "Controlador no disponible")
        
        try:
            if hasattr(self.controller, 'get_status'):
                return self.controller.get_status()
            else:
                return self._safe_response(False, "Método get_status no disponible")
        except Exception as e:
            logger.error(f"Error en status(): {e}")
            return self._safe_response(False, f"Error obteniendo estado: {str(e)}")
    
    def health(self) -> Dict[str, Any]:
        """Verificar salud"""
        if not self._check_controller():
            return self._safe_response(False, "Controlador no disponible")
        
        try:
            if hasattr(self.controller, 'monitor_health'):
                return self.controller.monitor_health()
            else:
                return self._safe_response(False, "Método monitor_health no disponible")
        except Exception as e:
            logger.error(f"Error en health(): {e}")
            return self._safe_response(False, f"Error verificando salud: {str(e)}")
    
    def diagnostics(self) -> Dict[str, Any]:
        """Ejecutar diagnósticos"""
        if not self._check_controller():
            return self._safe_response(False, "Controlador no disponible")
        
        try:
            if hasattr(self.controller, 'run_diagnostics'):
                return self.controller.run_diagnostics()
            else:
                return self._safe_response(False, "Método run_diagnostics no disponible")
        except Exception as e:
            logger.error(f"Error en diagnostics(): {e}")
            return self._safe_response(False, f"Error ejecutando diagnósticos: {str(e)}")
    
    def fix(self) -> Dict[str, Any]:
        """Aplicar correcciones"""
        if not self._check_controller():
            return self._safe_response(False, "Controlador no disponible")
        
        try:
            if hasattr(self.controller, 'apply_auto_fix'):
                return self.controller.apply_auto_fix()
            else:
                return self._safe_response(False, "Método apply_auto_fix no disponible")
        except Exception as e:
            logger.error(f"Error en fix(): {e}")
            return self._safe_response(False, f"Error aplicando correcciones: {str(e)}")
    
    def logs(self, count: int = 20) -> Dict[str, Any]:
        """Obtener logs"""
        if not self._check_controller():
            return self._safe_response(False, "Controlador no disponible")
        
        try:
            # Validar parámetro count
            if not isinstance(count, int) or count < 0:
                count = 20
            
            if hasattr(self.controller, 'get_logs'):
                logs = self.controller.get_logs(count)
                total = len(getattr(self.controller, 'logs', []))
                return self._safe_response(True, "Logs obtenidos", {'logs': logs, 'total': total})
            else:
                return self._safe_response(False, "Método get_logs no disponible")
        except Exception as e:
            logger.error(f"Error en logs(): {e}")
            return self._safe_response(False, f"Error obteniendo logs: {str(e)}")
    
    def configure(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Actualizar configuración"""
        if not self._check_controller():
            return self._safe_response(False, "Controlador no disponible")
        
        if not isinstance(config, dict):
            return self._safe_response(False, "La configuración debe ser un diccionario")
        
        try:
            if not hasattr(self.controller, 'config'):
                return self._safe_response(False, "Configuración no disponible en el controlador")
            
            # Crear copia de seguridad de la configuración actual
            backup_config = getattr(self.controller, 'config', {}).copy()
            
            try:
                self.controller.config.update(config)
                
                # Guardar estado si el método existe
                if hasattr(self.controller, 'save_state'):
                    self.controller.save_state()
                
                return self._safe_response(True, 'Configuración actualizada')
            except Exception as save_error:
                # Restaurar configuración en caso de error
                if hasattr(self.controller, 'config'):
                    self.controller.config = backup_config
                raise save_error
                
        except Exception as e:
            logger.error(f"Error en configure(): {e}")
            return self._safe_response(False, f"Error actualizando configuración: {str(e)}")

# Función para crear instancia de forma segura
def create_api() -> Optional[ControlAPI]:
    """Crear instancia de la API de forma segura"""
    try:
        return ControlAPI()
    except Exception as e:
        logger.error(f"Error creando instancia de ControlAPI: {e}")
        return None

# Instancia global de la API (creada de forma segura)
api = create_api()