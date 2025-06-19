"""
Script principal de inicio con sistema completo de corrección
"""
import sys
from pathlib import Path

def main():
    print("🚀 WoldVirtual Crypto 3D - Sistema de Inicio Inteligente")
    print("="*60)
    
    try:
        from smart_runner import SmartRunner
        runner = SmartRunner()
        runner.run_with_auto_repair()
    except ImportError:
        print("⚠️ Módulo smart_runner no disponible, usando inicio básico...")
        basic_start()

def basic_start():
    """Inicio básico sin módulos auxiliares"""
    import os
    import subprocess
    
    reflex_dir = Path(__file__).parent.absolute()
    os.chdir(str(reflex_dir))
    
    print(f"📁 Directorio: {reflex_dir}")
    
    try:
        subprocess.run(['reflex', 'run'], check=True)
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Intenta: pip install reflex")

if __name__ == "__main__":
    main()