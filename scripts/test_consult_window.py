#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para probar la ventana de consulta directamente.
"""

import sys
import os

# Agregar el directorio raíz al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide6.QtWidgets import QApplication
from views.Consult import ConsultWindow

def test_consult_window():
    """Prueba la ventana de consulta."""
    print("Probando ventana de consulta...")
    
    try:
        # Crear aplicación Qt
        app = QApplication(sys.argv)
        
        # Crear ventana de consulta
        window = ConsultWindow()
        
        # Mostrar ventana
        window.show()
        
        print("Ventana de consulta creada exitosamente")
        print("La ventana deberia mostrar los datos de la base de datos")
        print("Presiona Ctrl+C para cerrar")
        
        # Ejecutar aplicación
        app.exec()
        
    except Exception as e:
        print(f"Error creando ventana de consulta: {e}")
        return False
    
    return True

def main():
    """Función principal."""
    print("PRUEBA DE VENTANA DE CONSULTA")
    print("=" * 50)
    
    success = test_consult_window()
    
    if success:
        print("Prueba completada")
    else:
        print("Prueba fallida")

if __name__ == "__main__":
    main()
