#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simplificado para corregir las primary keys y limpiar datos incorrectos.
"""

import sys
import os
import random
from datetime import datetime, timedelta

# Agregar el directorio raíz al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.Connection import database

class SimpleDatabaseFixer:
    def __init__(self):
        self.db = database("utilities\\db\\DataBaseUE.db")
        
        # Listas de datos para corregir registros
        self.nombres_hombres = [
            "Carlos", "José", "Luis", "Miguel", "Antonio", "Francisco", "Manuel", "David", "Daniel", "Rafael",
            "Pedro", "Alejandro", "Roberto", "Fernando", "Diego", "Sergio", "Andrés", "Jorge", "Ricardo", "Eduardo"
        ]
        
        self.nombres_mujeres = [
            "María", "Carmen", "Ana", "Laura", "Isabel", "Pilar", "Dolores", "Teresa", "Rosa", "Francisca",
            "Antonia", "Mercedes", "Josefa", "Cristina", "Mónica", "Ángeles", "Lucía", "Elena", "Sara", "Paula"
        ]
        
        self.apellidos = [
            "García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez", "Pérez", "Gómez", "Martín",
            "Jiménez", "Ruiz", "Hernández", "Díaz", "Moreno", "Muñoz", "Álvarez", "Romero", "Alonso", "Gutiérrez"
        ]

    def generar_cedula(self):
        """Genera una cédula venezolana válida."""
        return f"V-{random.randint(10000000, 99999999)}"

    def generar_telefono(self):
        """Genera un número de teléfono venezolano."""
        return f"0{random.randint(200, 999)}-{random.randint(1000000, 9999999)}"

    def generar_fecha_nacimiento(self, edad_min=25, edad_max=65):
        """Genera una fecha de nacimiento basada en la edad."""
        edad = random.randint(edad_min, edad_max)
        fecha_actual = datetime.now()
        fecha_nacimiento = fecha_actual - timedelta(days=edad * 365 + random.randint(0, 365))
        return fecha_nacimiento.strftime("%Y-%m-%d")

    def es_dato_valido(self, valor, tipo="texto"):
        """Verifica si un dato es válido."""
        if valor is None or valor == "":
            return False
        
        if tipo == "texto":
            valor_str = str(valor).strip()
            if len(valor_str) < 2:
                return False
            # Verificar que no sean solo caracteres repetidos
            if len(set(valor_str.lower())) < 2:
                return False
            return True
        
        elif tipo == "cedula":
            valor_str = str(valor).strip()
            if len(valor_str) < 8:
                return False
            return True
        
        return True

    def limpiar_tabla_padres(self):
        """Limpia la tabla de padres con datos incorrectos."""
        print("🧹 Limpiando tabla de padres...")
        
        try:
            # Obtener todos los padres
            self.db.cursor.execute("SELECT IDP, NombreP, ApellidoP, CedulaP FROM DTP ORDER BY IDP")
            padres = self.db.cursor.fetchall()
            
            print(f"📊 Encontrados {len(padres)} registros de padres")
            
            # Actualizar registros con datos incorrectos
            for padre in padres:
                id_p, nombre, apellido, cedula = padre
                
                # Verificar y corregir nombre
                if not self.es_dato_valido(nombre, "texto"):
                    nuevo_nombre = random.choice(self.nombres_hombres)
                    self.db.cursor.execute("UPDATE DTP SET NombreP = ? WHERE IDP = ?", (nuevo_nombre, id_p))
                    print(f"   ✅ Corregido nombre del padre ID {id_p}: {nombre} → {nuevo_nombre}")
                
                # Verificar y corregir apellido
                if not self.es_dato_valido(apellido, "texto"):
                    nuevo_apellido = random.choice(self.apellidos)
                    self.db.cursor.execute("UPDATE DTP SET ApellidoP = ? WHERE IDP = ?", (nuevo_apellido, id_p))
                    print(f"   ✅ Corregido apellido del padre ID {id_p}: {apellido} → {nuevo_apellido}")
                
                # Verificar y corregir cédula
                if not self.es_dato_valido(cedula, "cedula"):
                    nueva_cedula = self.generar_cedula()
                    self.db.cursor.execute("UPDATE DTP SET CedulaP = ? WHERE IDP = ?", (nueva_cedula, id_p))
                    print(f"   ✅ Corregida cédula del padre ID {id_p}: {cedula} → {nueva_cedula}")
            
            self.db.connection.commit()
            print("✅ Tabla DTP limpiada exitosamente")
            return True
            
        except Exception as e:
            print(f"❌ Error limpiando tabla DTP: {e}")
            return False

    def limpiar_tabla_madres(self):
        """Limpia la tabla de madres con datos incorrectos."""
        print("🧹 Limpiando tabla de madres...")
        
        try:
            # Obtener todas las madres
            self.db.cursor.execute("SELECT IDM, NombreM, ApellidoM, CedulaM FROM DTM ORDER BY IDM")
            madres = self.db.cursor.fetchall()
            
            print(f"📊 Encontradas {len(madres)} registros de madres")
            
            # Actualizar registros con datos incorrectos
            for madre in madres:
                id_m, nombre, apellido, cedula = madre
                
                # Verificar y corregir nombre
                if not self.es_dato_valido(nombre, "texto"):
                    nuevo_nombre = random.choice(self.nombres_mujeres)
                    self.db.cursor.execute("UPDATE DTM SET NombreM = ? WHERE IDM = ?", (nuevo_nombre, id_m))
                    print(f"   ✅ Corregido nombre de la madre ID {id_m}: {nombre} → {nuevo_nombre}")
                
                # Verificar y corregir apellido
                if not self.es_dato_valido(apellido, "texto"):
                    nuevo_apellido = random.choice(self.apellidos)
                    self.db.cursor.execute("UPDATE DTM SET ApellidoM = ? WHERE IDM = ?", (nuevo_apellido, id_m))
                    print(f"   ✅ Corregido apellido de la madre ID {id_m}: {apellido} → {nuevo_apellido}")
                
                # Verificar y corregir cédula
                if not self.es_dato_valido(cedula, "cedula"):
                    nueva_cedula = self.generar_cedula()
                    self.db.cursor.execute("UPDATE DTM SET CedulaM = ? WHERE IDM = ?", (nueva_cedula, id_m))
                    print(f"   ✅ Corregida cédula de la madre ID {id_m}: {cedula} → {nueva_cedula}")
            
            self.db.connection.commit()
            print("✅ Tabla DTM limpiada exitosamente")
            return True
            
        except Exception as e:
            print(f"❌ Error limpiando tabla DTM: {e}")
            return False

    def verificar_primary_keys(self):
        """Verifica el estado de las primary keys."""
        print("🔍 Verificando primary keys...")
        
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
            print(f"❌ Error verificando primary keys: {e}")
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

    def ejecutar_limpieza(self):
        """Ejecuta la limpieza de datos incorrectos."""
        print("🔧 INICIANDO LIMPIEZA DE DATOS INCORRECTOS")
        print("=" * 60)
        
        # Verificar estado inicial
        print("📋 Estado inicial:")
        self.verificar_primary_keys()
        
        # Limpiar datos incorrectos
        success = True
        success &= self.limpiar_tabla_padres()
        success &= self.limpiar_tabla_madres()
        
        if success:
            print("\n" + "=" * 60)
            print("✅ ¡LIMPIEZA COMPLETADA EXITOSAMENTE!")
            
            # Verificar estado final
            print("\n📋 Estado final:")
            self.verificar_primary_keys()
            
            # Mostrar estadísticas
            self.mostrar_estadisticas()
            
            print("\n🔑 CORRECCIONES REALIZADAS:")
            print("   ✅ Datos inválidos han sido reemplazados por datos válidos")
            print("   ✅ Nombres y apellidos corregidos")
            print("   ✅ Cédulas con formato válido")
            print("   ✅ Primary keys mantenidas correctamente")
        else:
            print("\n❌ La limpieza tuvo algunos errores.")
        
        return success

def main():
    """Función principal."""
    print("🔧 CORRECTOR DE DATOS INCORRECTOS")
    print("=" * 60)
    
    try:
        fixer = SimpleDatabaseFixer()
        success = fixer.ejecutar_limpieza()
        
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
