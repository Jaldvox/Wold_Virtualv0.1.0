#!/usr/bin/env python3
"""
Script para ejecutar WoldVirtual desde la ubicación específica
"""
import os
import sys
import subprocess

# Ruta específica donde debe ejecutarse SIEMPRE
SPECIFIC_PATH = r"C:\Users\Usuario\Desktop\Wold_Virtualv0.0.9\WoldVirtual_Crypto_3D\reflex\WoldVirtual_Crypto_3D"

def main():
    print(f"🎯 Cambiando a directorio específico: {SPECIFIC_PATH}")
    
    # Verificar que el directorio existe
    if not os.path.exists(SPECIFIC_PATH):
        print(f"❌ Error: El directorio no existe: {SPECIFIC_PATH}")
        sys.exit(1)
    
    # Cambiar al directorio específico
    os.chdir(SPECIFIC_PATH)
    print(f"✅ Directorio actual: {os.getcwd()}")
    
    # Verificar archivos necesarios
    required_files = ['WoldVirtual_Crypto_3D.py', 'rxconfig.py']
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ Error: Archivo faltante: {file}")
            sys.exit(1)
    
    print("🚀 Iniciando Reflex...")
    
    # Ejecutar Reflex
    try:
        subprocess.run(['reflex', 'run'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando Reflex: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ Reflex no está instalado. Ejecuta: pip install reflex")
        sys.exit(1)

if __name__ == "__main__":
    main()