"""
Corrector automático de errores basado en análisis de consola
"""
import shutil
from pathlib import Path
from typing import Dict, List
from error_analyzer import ConsoleErrorAnalyzer

class AutoCorrector:
    """Corrector automático de errores de código"""
    
    def __init__(self):
        self.reflex_dir = Path(__file__).parent.absolute()
        self.analyzer = ConsoleErrorAnalyzer()
        self.backup_dir = self.reflex_dir / 'backups'
        self.backup_dir.mkdir(exist_ok=True)
    
    def create_backup(self, file_path: Path) -> Path:
        """Crear backup del archivo"""
        if file_path.exists():
            backup_name = f"{file_path.stem}_{int(time.time())}.backup"
            backup_path = self.backup_dir / backup_name
            shutil.copy2(file_path, backup_path)
            return backup_path
        return None
    
    def fix_file_errors(self, file_path: Path, error_log: str) -> Dict[str, Any]:
        """Corregir errores de un archivo específico"""
        result = {
            'file': str(file_path),
            'backup_created': False,
            'errors_found': 0,
            'errors_fixed': 0,
            'success': False
        }
        
        if not file_path.exists():
            result['error'] = 'Archivo no existe'
            return result
        
        # Crear backup
        backup_path = self.create_backup(file_path)
        result['backup_created'] = backup_path is not None
        
        # Leer contenido original
        try:
            original_content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            result['error'] = f'Error leyendo archivo: {e}'
            return result
        
        # Analizar errores
        errors = self.analyzer.analyze_error_log(error_log)
        file_errors = [e for e in errors if e['file'] == file_path.name]
        result['errors_found'] = len(file_errors)
        
        if not file_errors:
            result['success'] = True
            return result
        
        # Aplicar correcciones
        fixed_content = original_content
        fixed_count = 0
        
        for error in file_errors:
            try:
                error_type = error['type']
                if error_type in self.analyzer.fixes:
                    new_content = self.analyzer.fixes[error_type](error, fixed_content)
                    if new_content != fixed_content:
                        fixed_content = new_content
                        fixed_count += 1
            except Exception as e:
                print(f"Error aplicando corrección: {e}")
        
        # Guardar archivo corregido
        try:
            file_path.write_text(fixed_content, encoding='utf-8')
            result['errors_fixed'] = fixed_count
            result['success'] = True
        except Exception as e:
            result['error'] = f'Error guardando archivo: {e}'
        
        return result
    
    def fix_all_errors(self, error_log: str) -> Dict[str, Any]:
        """Corregir todos los errores encontrados en el log"""
        results = {
            'total_files': 0,
            'files_processed': 0,
            'total_errors': 0,
            'total_fixes': 0,
            'file_results': {}
        }
        
        # Analizar errores
        errors = self.analyzer.analyze_error_log(error_log)
        results['total_errors'] = len(errors)
        
        # Agrupar por archivo
        files_with_errors = {}
        for error in errors:
            filename = error['file']
            if filename not in files_with_errors:
                files_with_errors[filename] = []
            files_with_errors[filename].append(error)
        
        results['total_files'] = len(files_with_errors)
        
        # Procesar cada archivo
        for filename, file_errors in files_with_errors.items():
            file_path = self.reflex_dir / filename
            
            if file_path.exists():
                fix_result = self.fix_file_errors(file_path, error_log)
                results['file_results'][filename] = fix_result
                results['total_fixes'] += fix_result.get('errors_fixed', 0)
                results['files_processed'] += 1
        
        return results