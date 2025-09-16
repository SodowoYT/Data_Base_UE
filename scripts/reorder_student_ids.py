#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para reordenar las primary keys de los estudiantes desde 1 hasta el final.
"""

import sys
import os

# Agregar el directorio raíz al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.Connection import database

class StudentIDReorderer:
    def __init__(self):
        self.db = database("utilities\\db\\DataBaseUE.db")

    def reordenar_estudiantes(self):
        """Reordena los IDs de los estudiantes desde 1 hasta el final."""
        print("🔄 Reordenando IDs de estudiantes...")
        
        try:
            # Obtener todos los estudiantes ordenados por ID actual
            self.db.cursor.execute("SELECT * FROM Estudend ORDER BY IDEST")
            estudiantes = self.db.cursor.fetchall()
            
            print(f"📊 Encontrados {len(estudiantes)} estudiantes")
            
            # Crear tabla temporal con nueva numeración
            self.db.cursor.execute("""
                CREATE TABLE Estudend_temp (
                    IDEST INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nombre TEXT,
                    Apellido TEXT,
                    CedulaEscolar TEXT,
                    Edad INTEGER,
                    Genero TEXT,
                    FN TEXT,
                    Lateralidad TEXT,
                    Nacionalidad TEXT,
                    Estado TEXT,
                    Municipio TEXT,
                    DA TEXT,
                    PTR TEXT,
                    Altura INTEGER,
                    Peso INTEGER,
                    Zapatos TEXT,
                    Camisa TEXT,
                    Pantalon TEXT,
                    NDH INTEGER,
                    APRN TEXT,
                    AlergicoA TEXT,
                    AlgunaDificultad TEXT,
                    EspecifiqueDificultad TEXT,
                    CorreoElectronico TEXT,
                    TelefonoHabitacion TEXT,
                    CartonVacunas TEXT,
                    TipodeSangre TEXT,
                    EDH TEXT,
                    observaciones TEXT,
                    IDRPL INTEGER,
                    IDP INTEGER,
                    IDM INTEGER,
                    FOREIGN KEY(IDM) REFERENCES DTM(IDM),
                    FOREIGN KEY(IDP) REFERENCES DTP(IDP),
                    FOREIGN KEY(IDRPL) REFERENCES REPL(IDRPL)
                )
            """)
            
            # Insertar estudiantes con nuevos IDs
            for i, estudiante in enumerate(estudiantes, 1):
                # Extraer todos los campos excepto el ID original
                datos = list(estudiante)[1:]  # Excluir el primer campo (IDEST original)
                
                self.db.cursor.execute("""
                    INSERT INTO Estudend_temp (Nombre, Apellido, CedulaEscolar, Edad, Genero, FN, Lateralidad, 
                    Nacionalidad, Estado, Municipio, DA, PTR, Altura, Peso, Zapatos, Camisa, Pantalon, NDH, 
                    APRN, AlergicoA, AlgunaDificultad, EspecifiqueDificultad, CorreoElectronico, TelefonoHabitacion, 
                    CartonVacunas, TipodeSangre, EDH, observaciones, IDRPL, IDP, IDM)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, datos)
                
                if i % 20 == 0:  # Mostrar progreso cada 20 registros
                    print(f"   ✅ Procesados {i}/{len(estudiantes)} estudiantes")
            
            # Reemplazar tabla original
            self.db.cursor.execute("DROP TABLE Estudend")
            self.db.cursor.execute("ALTER TABLE Estudend_temp RENAME TO Estudend")
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

    def ejecutar_reordenacion(self):
        """Ejecuta la reordenación completa."""
        print("🔄 REORDENACIÓN DE PRIMARY KEYS")
        print("=" * 60)
        
        # Verificar estado inicial
        print("📋 Estado inicial:")
        self.verificar_estado_final()
        
        # Reordenar estudiantes
        success = self.reordenar_estudiantes()
        
        if success:
            print("\n" + "=" * 60)
            print("✅ ¡REORDENACIÓN COMPLETADA EXITOSAMENTE!")
            
            # Verificar estado final
            print("\n📋 Estado final:")
            self.verificar_estado_final()
            
            # Mostrar estadísticas
            self.mostrar_estadisticas()
            
            print("\n🔑 CORRECCIONES REALIZADAS:")
            print("   ✅ Primary keys de estudiantes reordenadas desde 1 hasta el final")
            print("   ✅ Relaciones con representantes, padres y madres mantenidas")
            print("   ✅ Datos incorrectos corregidos anteriormente")
        else:
            print("\n❌ La reordenación tuvo errores.")
        
        return success

def main():
    """Función principal."""
    print("🔄 REORDENADOR DE PRIMARY KEYS")
    print("=" * 60)
    
    try:
        reorderer = StudentIDReorderer()
        success = reorderer.ejecutar_reordenacion()
        
        if success:
            print("\n🎉 ¡Base de datos reordenada exitosamente!")
        else:
            print("\n⚠️ Proceso completado con errores")
            
    except Exception as e:
        print(f"❌ Error general: {e}")
    finally:
        print("\n🏁 Proceso finalizado.")

if __name__ == "__main__":
    main()
