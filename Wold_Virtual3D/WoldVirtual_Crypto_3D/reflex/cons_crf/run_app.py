#!/usr/bin/env python3
"""
Launcher para ejecutar WoldVirtual desde la estructura /reflex
"""
import os
import sys
import subprocess
from pathlib import Path

def main():
    # Obtener directorio reflex (donde está este script)
    reflex_dir = Path(__file__).parent.absolute()
    project_root = reflex_dir.parent
    
    print("🎯 WoldVirtual Reflex - Estructura Limpia")
    print("=" * 45)
    print(f"📁 Directorio Reflex: {reflex_dir}")
    print(f"📁 Proyecto Principal: {project_root}")
    
    # SIEMPRE cambiar al directorio reflex
    os.chdir(str(reflex_dir))
    print(f"✅ Ejecutando desde: {os.getcwd()}")
    
    # Verificar estructura
    required_files = [
        'WoldVirtual_Crypto_3D.py',
        'rxconfig.py',
        'requirements.txt'
    ]
    
    print("\n📋 Verificando archivos:")
    for file in required_files:
        if (reflex_dir / file).exists():
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file} - FALTANTE")
            return False
    
    # Verificar que .web esté en reflex
    web_dir = reflex_dir / ".web"
    if web_dir.exists():
        print(f"  ✅ .web/ (en reflex)")
    else:
        print(f"  📁 .web/ se creará automáticamente")
    
    # Verificar Reflex
    try:
        import reflex
        print(f"\n✅ Reflex {reflex.__version__} disponible")
    except ImportError:
        print("\n❌ Reflex no está instalado")
        print("💡 Instalar con: pip install reflex")
        return False
    
    print("\n🚀 Iniciando WoldVirtual...")
    print("🔒 Todo contenido se mantendrá en /reflex")
    print("-" * 45)
    
    try:
        subprocess.run(['reflex', 'run'], check=True, cwd=str(reflex_dir))
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error ejecutando Reflex: {e}")
        return False
    except KeyboardInterrupt:
        print("\n👋 Aplicación cerrada")
        return True
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        input("\nPresiona Enter para continuar...")
@echo off
title WoldVirtual - Estructura Reflex
echo ==========================================
echo  🚀 WoldVirtual Crypto 3D - Reflex App
echo ==========================================
echo.

cd /d "%~dp0\reflex"
echo 📁 Ejecutando desde: %CD%
echo.

if not exist "WoldVirtual_Crypto_3D.py" (
    echo ❌ Error: Archivo principal no encontrado
    echo 💡 Asegurate de que la estructura este correcta
    pause
    exit /b 1
)

echo ✅ Estructura verificada
echo 🚀 Iniciando aplicación...
echo.

python run_app.py

if %ERRORLEVEL% neq 0 (
    echo.
    echo ❌ Error en la aplicación
    pause
)