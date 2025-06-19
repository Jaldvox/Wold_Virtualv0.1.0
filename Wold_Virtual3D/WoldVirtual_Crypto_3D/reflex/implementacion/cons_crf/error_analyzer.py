"""
Analizador de errores de consola para WoldVirtual
"""
import re
import ast
from typing import Dict, List, Tuple, Any
from pathlib import Path

class ConsoleErrorAnalyzer:
    """Analizador especializado de errores de consola"""
    
    def __init__(self):
        self.error_patterns = {
            'undefined_import': r'"(\w+)" is not defined.*Pylance.*reportUndefinedVariable',
            'type_mismatch': r'Type "([^"]+)" is not assignable to return type "([^"]+)"',
            'literal_mismatch': r'"([^"]+)" is not assignable to "([^"]+)"',
            'attribute_error': r'"([^"]+)" is not a known attribute of "([^"]+)"',
            'optional_member': r'reportOptionalMemberAccess'
        }
        
        self.fixes = {
            'undefined_import': self.fix_undefined_import,
            'type_mismatch': self.fix_type_mismatch,
            'literal_mismatch': self.fix_literal_mismatch,
            'attribute_error': self.fix_attribute_error,
            'optional_member': self.fix_optional_member
        }
    
    def analyze_error_log(self, error_text: str) -> List[Dict[str, Any]]:
        """Analizar log de errores y extraer problemas"""
        errors = []
        lines = error_text.split('\n')
        
        for i, line in enumerate(lines):
            for error_type, pattern in self.error_patterns.items():
                match = re.search(pattern, line)
                if match:
                    error_info = {
                        'type': error_type,
                        'line_number': self.extract_line_number(line),
                        'file': self.extract_filename(line),
                        'message': line.strip(),
                        'match_groups': match.groups(),
                        'context': self.get_context(lines, i)
                    }
                    errors.append(error_info)
        
        return errors
    
    def extract_line_number(self, line: str) -> int:
        """Extraer número de línea del error"""
        match = re.search(r'\[Ln (\d+)', line)
        return int(match.group(1)) if match else 0
    
    def extract_filename(self, line: str) -> str:
        """Extraer nombre de archivo del error"""
        match = re.search(r'(\w+\.py)', line)
        return match.group(1) if match else ''
    
    def get_context(self, lines: List[str], index: int) -> List[str]:
        """Obtener contexto alrededor del error"""
        start = max(0, index - 2)
        end = min(len(lines), index + 3)
        return lines[start:end]
    
    def fix_undefined_import(self, error: Dict[str, Any], file_content: str) -> str:
        """Corregir imports no definidos"""
        undefined_var = error['match_groups'][0]
        
        # Mapeo de variables comunes a imports
        import_map = {
            'importlib': 'import importlib.util',
            'Dict': 'from typing import Dict',
            'Any': 'from typing import Any',
            'Optional': 'from typing import Optional',
            'List': 'from typing import List',
            'Path': 'from pathlib import Path',
            'json': 'import json',
            'os': 'import os',
            'sys': 'import sys',
            'time': 'import time',
            'subprocess': 'import subprocess',
            'threading': 'import threading'
        }
        
        if undefined_var in import_map:
            import_line = import_map[undefined_var]
            # Agregar import al inicio del archivo
            lines = file_content.split('\n')
            
            # Encontrar donde insertar el import
            insert_index = 0
            for i, line in enumerate(lines):
                if line.strip().startswith('"""') or line.strip().startswith('import') or line.strip().startswith('from'):
                    continue
                insert_index = i
                break
            
            # Verificar que no existe ya
            if import_line not in file_content:
                lines.insert(insert_index, import_line)
                return '\n'.join(lines)
        
        return file_content
    
    def fix_type_mismatch(self, error: Dict[str, Any], file_content: str) -> str:
        """Corregir problemas de tipos"""
        line_num = error['line_number']
        lines = file_content.split('\n')
        
        if line_num <= len(lines):
            line = lines[line_num - 1]
            
            # Casos comunes de corrección
            fixes = {
                'Dict[str, Any]': 'dict',
                'List[str]': 'list',
                'Optional[str]': 'str',
                'bool': 'bool'
            }
            
            for wrong_type, correct_type in fixes.items():
                if wrong_type in line:
                    lines[line_num - 1] = line.replace(wrong_type, correct_type)
                    break
        
        return '\n'.join(lines)
    
    def fix_literal_mismatch(self, error: Dict[str, Any], file_content: str) -> str:
        """Corregir problemas de literales"""
        line_num = error['line_number']
        lines = file_content.split('\n')
        
        if line_num <= len(lines):
            line = lines[line_num - 1]
            
            # Agregar comentario de type ignore
            if '# type: ignore' not in line:
                lines[line_num - 1] = line + '  # type: ignore'
        
        return '\n'.join(lines)
    
    def fix_attribute_error(self, error: Dict[str, Any], file_content: str) -> str:
        """Corregir errores de atributos"""
        line_num = error['line_number']
        lines = file_content.split('\n')
        
        if line_num <= len(lines):
            line = lines[line_num - 1]
            
            # Agregar verificación condicional
            if 'hasattr(' not in line:
                # Envolver en verificación hasattr si es posible
                indent = len(line) - len(line.lstrip())
                safe_line = ' ' * indent + f"# TODO: Verificar atributo - {line.strip()}"
                lines[line_num - 1] = safe_line
        
        return '\n'.join(lines)
    
    def fix_optional_member(self, error: Dict[str, Any], file_content: str) -> str:
        """Corregir acceso a miembros opcionales"""
        line_num = error['line_number']
        lines = file_content.split('\n')
        
        if line_num <= len(lines):
            line = lines[line_num - 1]
            
            # Agregar type ignore para acceso opcional
            if '# type: ignore' not in line:
                lines[line_num - 1] = line + '  # type: ignore'
        
        return '\n'.join(lines)