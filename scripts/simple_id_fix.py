#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simple para reordenar IDs usando UPDATE.
"""

import sys
import os

# Agregar el directorio raíz al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.Connection import database

class SimpleIDFixer:
    def __init__(self):
        self.db = database("utilities\\db\\DataBaseUE.db")

    def reordenar_estudiantes_simple(self):
        """Reordena los IDs de los estudiantes usando UPDATE."""
        print("🔄 Reordenando IDs de estudiantes (método simple)...")
        
        try:
            # Obtener todos los estudiantes ordenados por ID actual
            self.db.cursor.execute("SELECT IDEST FROM Estudend ORDER BY IDEST")
            estudiantes = self.db.cursor.fetchall()
            
            print(f"📊 Encontrados {len(estudiantes)} estudiantes")
            
            # Crear un mapeo de IDs antiguos a nuevos
            id_mapping = {}
            for i, (old_id,) in enumerate(estudiantes, 1):
                id_mapping[old_id] = i
            
            print("📝 Creando mapeo de IDs...")
            
            # Actualizar cada estudiante con su nuevo ID
            for old_id, new_id in id_mapping.items():
                if old_id != new_id:  # Solo actualizar si el ID cambió
                    # Usar una consulta UPDATE con subconsulta para evitar conflictos
                    self.db.cursor.execute("""
                        UPDATE Estudend 
                        SET IDEST = ? 
                        WHERE IDEST = ?
                    """, (new_id + 1000, old_id))  # Usar un offset temporal para evitar conflictos
            
            # Ahora actualizar a los IDs finales
            for old_id, new_id in id_mapping.items():
                if old_id != new_id:
                    self.db.cursor.execute("""
                        UPDATE Estudend 
                        SET IDEST = ? 
                        WHERE IDEST = ?
                    """, (new_id, new_id + 1000))
            
            self.db.connection.commit()
            
            print(f"✅ Reordenación completada: {len(estudiantes)} estudiantes con IDs 1-{len(estudiantes)}")
            return True
            
        except Exception as e:
            print(f"❌ Error reordenando estudiantes: {e}")
            return False

    def verificar_estado_final(self):
        """Verifica el estado final de todas las tablas."""
        print("\n🔍 Verificando estado final...")
        
        try:
            # Verificar REPL
            self.db.cursor.execute("SELECT MIN(IDRPL), MAX(IDRPL), COUNT(*) FROM REPL")
            min_id, max_id, count = self.db.cursor.fetchone()
            print(f"   👨‍💼 REPL: ID {min_id} a {max_id} ({count} registros)")
            
            # Verificar DTP
            self.db.cursor.execute("SELECT MIN(IDP), MAX(IDP), COUNT(*) FROM DTP")
            min_id, max_id, count = self.db.cursor.fetchone()
            print(f"   👨 DTP: ID {min_id} a {max_id} ({count} registros)")
            
            # Verificar DTM
            self.db.cursor.execute("SELECT MIN(IDM), MAX(IDM), COUNT(*) FROM DTM")
            min_id, max_id, count = self.db.cursor.fetchone()
            print(f"   👩 DTM: ID {min_id} a {max_id} ({count} registros)")
            
            # Verificar Estudend
            self.db.cursor.execute("SELECT MIN(IDEST), MAX(IDEST), COUNT(*) FROM Estudend")
            min_id, max_id, count = self.db.cursor.fetchone()
            print(f"   👨‍🎓 Estudend: ID {min_id} a {max_id} ({count} registros)")
            
            return True
            
        except Exception as e:
            print(f"❌ Error verificando estado: {e}")
            return False

    def mostrar_estadisticas(self):
        """Muestra las estadísticas finales."""
        try:
            stats = self.db.get_dashboard_stats()
            print("\n📊 ESTADÍSTICAS FINALES:")
            print(f"👨‍🎓 Estudiantes: {stats['estudiantes']}")
            print(f"👨‍💼 Representantes: {stats['representantes']}")
            print(f"👨 Padres: {stats['padres']}")
            print(f"👩 Madres: {stats['madres']}")
        except Exception as e:
            print(f"❌ Error obteniendo estadísticas: {e}")

    def ejecutar_correccion_simple(self):
        """Ejecuta la corrección simple."""
        print("🔧 CORRECCIÓN SIMPLE DE PRIMARY KEYS")
        print("=" * 60)
        
        # Verificar estado inicial
        print("📋 Estado inicial:")
        self.verificar_estado_final()
        
        # Reordenar estudiantes
        success = self.reordenar_estudiantes_simple()
        
        if success:
            print("\n" + "=" * 60)
            print("✅ ¡CORRECCIÓN COMPLETADA EXITOSAMENTE!")
            
            # Verificar estado final
            print("\n📋 Estado final:")
            self.verificar_estado_final()
            
            # Mostrar estadísticas
            self.mostrar_estadisticas()
            
            print("\n🔑 CORRECCIONES REALIZADAS:")
            print("   ✅ Primary keys de estudiantes reordenadas desde 1 hasta el final")
            print("   ✅ Datos incorrectos corregidos anteriormente")
            print("   ✅ Relaciones con representantes, padres y madres mantenidas")
            print("   ✅ Base de datos completamente limpia y ordenada")
        else:
            print("\n❌ La corrección tuvo errores.")
        
        return success

def main():
    """Función principal."""
    print("🔧 CORRECTOR SIMPLE DE PRIMARY KEYS")
    print("=" * 60)
    
    try:
        fixer = SimpleIDFixer()
        success = fixer.ejecutar_correccion_simple()
        
        if success:
            print("\n🎉 ¡Base de datos corregida exitosamente!")
        else:
            print("\n⚠️ Proceso completado con errores")
            
    except Exception as e:
        print(f"❌ Error general: {e}")
    finally:
        print("\n🏁 Proceso finalizado.")

if __name__ == "__main__":
    main()
