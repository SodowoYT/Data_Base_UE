#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para debuggear la consulta SQL de la ventana de consulta.
"""

import sys
import os
import sqlite3

# Agregar el directorio raíz al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.Connection import database

def debug_consult_sql():
    """Debuggea la consulta SQL paso a paso."""
    print("DEBUGGING CONSULTA SQL")
    print("=" * 50)
    
    try:
        # 1. Verificar que el archivo de base de datos existe
        db_path = "utilities\\db\\DataBaseUE.db"
        if not os.path.exists(db_path):
            print(f"ERROR: El archivo {db_path} no existe")
            return False
        
        print(f"OK: Archivo de base de datos encontrado: {db_path}")
        
        # 2. Conectar directamente con sqlite3
        print("\n2. Conectando directamente con sqlite3...")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # 3. Ejecutar consulta directa
        print("3. Ejecutando consulta directa...")
        cursor.execute("SELECT COUNT(*) FROM Estudend")
        count = cursor.fetchone()[0]
        print(f"   Total de estudiantes (consulta directa): {count}")
        
        # 4. Obtener algunos registros
        cursor.execute("SELECT IDEST, Nombre, Apellido, CedulaEscolar FROM Estudend LIMIT 5")
        records = cursor.fetchall()
        print("   Primeros 5 registros:")
        for record in records:
            print(f"     ID: {record[0]}, Nombre: {record[1]}, Apellido: {record[2]}, Cedula: {record[3]}")
        
        conn.close()
        
        # 5. Probar con la clase database
        print("\n5. Probando con la clase database...")
        db = database(db_path)
        
        # 6. Ejecutar SelectEstudend
        print("6. Ejecutando SelectEstudend()...")
        data = db.SelectEstudend()
        print(f"   Total de estudiantes (clase database): {len(data)}")
        
        if data:
            print("   Primeros 3 registros:")
            for i, record in enumerate(data[:3]):
                print(f"     {i+1}. ID: {record[0]}, Nombre: {record[1]}, Apellido: {record[2]}, Cedula: {record[3]}")
        
        # 7. Verificar estructura de la tabla
        print("\n7. Verificando estructura de la tabla...")
        cursor = db.cursor
        cursor.execute("PRAGMA table_info(Estudend)")
        columns = cursor.fetchall()
        print(f"   Columnas de la tabla Estudend: {len(columns)}")
        for col in columns[:5]:  # Mostrar solo las primeras 5 columnas
            print(f"     {col[1]} ({col[2]})")
        
        print("\nRESULTADO: La base de datos y la clase database funcionan correctamente")
        print("Si la ventana de consulta no muestra datos, el problema está en la interfaz gráfica")
        
        return True
        
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Función principal."""
    debug_consult_sql()

if __name__ == "__main__":
    main()
