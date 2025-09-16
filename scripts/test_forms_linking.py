#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para probar la vinculación automática en el registro de estudiantes.
"""

import sys
import os

# Agregar el directorio raíz al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from viewmodels.FormsW import EstudendViewModel

def test_forms_linking():
    """Prueba la vinculación automática de estudiantes con familia."""
    print("PROBANDO VINCULACIÓN AUTOMÁTICA DE ESTUDIANTES")
    print("=" * 60)
    
    try:
        print("Creando instancia del ViewModel...")
        # Crear instancia del ViewModel
        viewmodel = EstudendViewModel()
        print("ViewModel creado exitosamente")
        
        print("Iniciando registro de estudiante completo...")
        # Datos de prueba para un estudiante completo
        resultado = viewmodel.registrar_estudiante_completo(
            # Datos del estudiante
            "Juan Carlos", "Pérez García", "CE123456", 8, "Masculino", "2015-03-15", "Diestro", "Venezolana", "Miranda", "Chacao", "Av. Principal #123", "Frente al parque", "120", "25", "32", "M", "28", 2, "Sí", "Ninguna", "No", "", "juan.perez@email.com", "0212-1234567", "Completo", "O+", "Negativo", "Estudiante aplicado",
            # Datos del representante
            "María Elena", "García López", "V-12345678", "1980-05-20", 44, "Casada", "Venezolana", "Madre", "Ingeniera", "Ingeniera de Sistemas", "Empresa ABC", "Av. Principal #123", "0412-1234567", "0212-1234567", "0212-7654321", "maria.garcia@email.com", "J-12345678-9", "123456", "12345678", "ABC123456",
            # Datos del padre
            "Carlos Alberto", "Pérez Rodríguez", "V-87654321", "1978-08-10", 46, "Empleado", "Empresa XYZ", "Sí", "", "Av. Principal #123", "0414-9876543",
            # Datos de la madre
            "María Elena", "García López", "V-11223344", "1982-12-03", 42, "Empleada", "Empresa DEF", "Sí", "", "Av. Principal #123", "0416-5555555"
        )
        
        if resultado['success']:
            print("✅ REGISTRO EXITOSO")
            print(f"   • Estudiante ID: {resultado['estudiante_id']}")
            print(f"   • Representante ID: {resultado['representante_id']}")
            print(f"   • Padre ID: {resultado['padre_id']}")
            print(f"   • Madre ID: {resultado['madre_id']}")
            
            # Verificar la vinculación en la base de datos
            print("\n🔍 VERIFICANDO VINCULACIÓN EN LA BASE DE DATOS...")
            
            # Consultar directamente el estudiante específico
            cursor = viewmodel.database.cursor
            cursor.execute('SELECT * FROM Estudend WHERE IDEST = ?', (resultado['estudiante_id'],))
            estudiante_encontrado = cursor.fetchone()
            
            if estudiante_encontrado:
                print(f"✅ Estudiante encontrado en la BD:")
                print(f"   • ID: {estudiante_encontrado[0]}")
                print(f"   • Nombre: {estudiante_encontrado[1]}")
                print(f"   • Apellido: {estudiante_encontrado[2]}")
                print(f"   • Total de columnas: {len(estudiante_encontrado)}")
                print(f"   • IDRPL (Representante): {estudiante_encontrado[30] if len(estudiante_encontrado) > 30 else 'N/A'}")
                print(f"   • IDP (Padre): {estudiante_encontrado[31] if len(estudiante_encontrado) > 31 else 'N/A'}")
                print(f"   • IDM (Madre): {estudiante_encontrado[32] if len(estudiante_encontrado) > 32 else 'N/A'}")
                
                print(f"\n🔍 COMPARACIÓN DE IDs:")
                print(f"   • IDRPL esperado: {resultado['representante_id']}, encontrado: {estudiante_encontrado[30] if len(estudiante_encontrado) > 30 else 'N/A'}")
                print(f"   • IDP esperado: {resultado['padre_id']}, encontrado: {estudiante_encontrado[31] if len(estudiante_encontrado) > 31 else 'N/A'}")
                print(f"   • IDM esperado: {resultado['madre_id']}, encontrado: {estudiante_encontrado[32] if len(estudiante_encontrado) > 32 else 'N/A'}")
                
                # Verificar que las claves foráneas coincidan
                if (estudiante_encontrado[30] == resultado['representante_id'] and 
                    estudiante_encontrado[31] == resultado['padre_id'] and 
                    estudiante_encontrado[32] == resultado['madre_id']):
                    print("✅ VINCULACIÓN CORRECTA: Todas las claves foráneas coinciden")
                else:
                    print("❌ ERROR DE VINCULACIÓN: Las claves foráneas no coinciden")
            else:
                print("❌ ERROR: No se encontró el estudiante en la base de datos")
                
        else:
            print(f"❌ ERROR EN EL REGISTRO: {resultado['error']}")
            
    except Exception as e:
        print(f"❌ ERROR GENERAL: {e}")
        import traceback
        traceback.print_exc()

def main():
    """Función principal."""
    test_forms_linking()

if __name__ == "__main__":
    main()
