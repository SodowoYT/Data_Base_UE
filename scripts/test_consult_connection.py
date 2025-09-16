#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para probar la conexión de la ventana de consulta.
"""

import sys
import os

# Agregar el directorio raíz al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.Connection import database

def test_consult_connection():
    """Prueba la conexión de la ventana de consulta."""
    print("🔍 Probando conexión de la ventana de consulta...")
    
    try:
        # Crear instancia de la base de datos como lo hace la ventana de consulta
        db = database("utilities\\db\\DataBaseUE.db")
        
        # Probar el método SelectEstudend
        print("📊 Ejecutando SelectEstudend()...")
        estudiantes = db.SelectEstudend()
        
        print(f"✅ Se encontraron {len(estudiantes)} estudiantes")
        
        if estudiantes:
            print("\n📋 Primeros 5 estudiantes:")
            for i, estudiante in enumerate(estudiantes[:5], 1):
                print(f"   {i}. ID: {estudiante[0]}, Nombre: {estudiante[1]}, Apellido: {estudiante[2]}, Cédula: {estudiante[3]}")
        
        # Probar el método obtener_datos_por_cedula
        if estudiantes:
            cedula_prueba = estudiantes[0][3]  # Cédula del primer estudiante
            print(f"\n🔍 Probando obtener_datos_por_cedula con cédula: {cedula_prueba}")
            datos_completos = db.obtener_datos_por_cedula(cedula_prueba)
            
            if datos_completos:
                print("✅ Datos completos obtenidos correctamente")
                print(f"   Campos disponibles: {len(datos_completos)}")
            else:
                print("❌ No se pudieron obtener los datos completos")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en la conexión: {e}")
        return False

def main():
    """Función principal."""
    print("🧪 PRUEBA DE CONEXIÓN - VENTANA DE CONSULTA")
    print("=" * 60)
    
    success = test_consult_connection()
    
    if success:
        print("\n✅ La conexión funciona correctamente")
        print("💡 Si la ventana de consulta no muestra datos, puede ser un problema de:")
        print("   - Cache de la aplicación")
        print("   - Conexión no refrescada")
        print("   - Error en la interfaz gráfica")
    else:
        print("\n❌ Hay un problema con la conexión")
    
    print("\n🏁 Prueba finalizada.")

if __name__ == "__main__":
    main()
