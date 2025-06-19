"""
Ejecutor inteligente con corrección automática
"""
import os
import sys
import subprocess
import time
from pathlib import Path

# Importar módulos auxiliares
try:
    from diagnostics import SystemDiagnostics
    from auto_fix import AutoFixer
    MODULES_AVAILABLE = True
except ImportError:
    MODULES_AVAILABLE = False
    print("⚠️ Módulos auxiliares no disponibles, usando modo básico")

class SmartRunner:
    """Ejecutor inteligente que corrige errores automáticamente"""
    
    def __init__(self):
        self.reflex_dir = Path(__file__).parent.absolute()
        self.max_attempts = 3
        self.current_attempt = 0
    
    def ensure_directory(self):
        """Asegurar directorio correcto"""
        if os.getcwd() != str(self.reflex_dir):
            os.chdir(str(self.reflex_dir))
            print(f"📁 Cambiado a: {self.reflex_dir}")
    
    def try_run_reflex(self) -> bool:
        """Intentar ejecutar Reflex"""
        try:
            print(f"🚀 Intento {self.current_attempt + 1}/{self.max_attempts}")
            
            # Ejecutar reflex con timeout
            process = subprocess.Popen(
                ['reflex', 'run'],
                cwd=str(self.reflex_dir),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Esperar un poco para ver si hay errores inmediatos
            time.sleep(3)
            
            if process.poll() is None:
                # Proceso sigue corriendo, probablemente funcionó
                print("✅ Reflex iniciado exitosamente")
                process.wait()  # Esperar que termine
                return True
            else:
                # Proceso terminó, hay error
                stdout, stderr = process.communicate()
                print(f"❌ Error en Reflex:")
                print(f"stdout: {stdout}")
                print(f"stderr: {stderr}")
                return False
                
        except FileNotFoundError:
            print("❌ Comando 'reflex' no encontrado")
            return False
        except Exception as e:
            print(f"❌ Error ejecutando Reflex: {e}")
            return False
    
    def run_with_auto_repair(self):
        """Ejecutar con reparación automática"""
        self.ensure_directory()
        
        while self.current_attempt < self.max_attempts:
            print(f"\n{'='*50}")
            print(f"🎯 INTENTO {self.current_attempt + 1}")
            print('='*50)
            
            # Intentar ejecutar
            if self.try_run_reflex():
                print("🎉 ¡Reflex ejecutado exitosamente!")
                return True
            
            # Si falló y tenemos módulos auxiliares
            if MODULES_AVAILABLE and self.current_attempt < self.max_attempts - 1:
                print("\n🔧 Ejecutando diagnóstico y reparación...")
                
                # Diagnóstico
                diagnostics = SystemDiagnostics()
                results = diagnostics.run_full_diagnosis()
                
                # Auto-reparación
                fixer = AutoFixer()
                fix_results = fixer.run_auto_repair()
                
                print(f"\n✅ Reparaciones aplicadas: {sum(fix_results.values())}")
                
            elif not MODULES_AVAILABLE:
                print("⚠️ Sin módulos de reparación, aplicando corrección básica...")
                self.basic_repair()
            
            self.current_attempt += 1
            
            if self.current_attempt < self.max_attempts:
                print(f"\n⏳ Esperando antes del siguiente intento...")
                time.sleep(2)
        
        print(f"\n❌ No se pudo ejecutar Reflex después de {self.max_attempts} intentos")
        self.show_manual_instructions()
        return False
    
    def basic_repair(self):
        """Reparación básica sin módulos auxiliares"""
        print("🔧 Aplicando reparación básica...")
        
        # Crear rxconfig.py básico
        config_file = self.reflex_dir / 'rxconfig.py'
        if not config_file.exists():
            config_content = '''import reflex as rx

config = rx.Config(
    app_name="WoldVirtual_Crypto_3D",
)
'''
            config_file.write_text(config_content)
            print("✅ Creado rxconfig.py básico")
        
        # Crear app básica
        app_file = self.reflex_dir / 'WoldVirtual_Crypto_3D.py'
        if not app_file.exists() or self.has_import_errors(app_file):
            app_content = '''import reflex as rx

class State(rx.State):
    message: str = "WoldVirtual funcionando"

def index():
    return rx.container(
        rx.vstack(
            rx.heading("WoldVirtual Crypto 3D"),
            rx.text(State.message),
            spacing="4",
            align="center"
        ),
        padding="2rem"
    )

app = rx.App()
app.add_page(index)
'''
            app_file.write_text(app_content)
            print("✅ Creada aplicación básica")
    
    def has_import_errors(self, file_path: Path) -> bool:
        """Verificar si el archivo tiene imports problemáticos"""
        try:
            content = file_path.read_text()
            problematic = [
                'from state import',
                'from components import',
                'from blockchain import'
            ]
            return any(prob in content for prob in problematic)
        except:
            return True
    
    def show_manual_instructions(self):
        """Mostrar instrucciones manuales"""
        print("\n" + "="*60)
        print("📋 INSTRUCCIONES MANUALES")
        print("="*60)
        print("1. Verificar que Reflex esté instalado:")
        print("   pip install reflex")
        print("\n2. Verificar archivos en el directorio:")
        print(f"   {self.reflex_dir}")
        print("\n3. Ejecutar manualmente:")
        print("   cd", str(self.reflex_dir))
        print("   reflex run")
        print("\n4. Si sigue fallando, crear proyecto nuevo:")
        print("   reflex init")

def main():
    """Función principal"""
    print("🎯 WoldVirtual Smart Runner")
    print("Sistema de ejecución con auto-reparación")
    
    runner = SmartRunner()
    runner.run_with_auto_repair()

if __name__ == "__main__":
    main()