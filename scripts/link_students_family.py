#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para vincular estudiantes con representantes, padres y madres
usando las primary keys correspondientes.
"""

import sys
import os
import random
from datetime import datetime, timedelta

# Agregar el directorio raíz al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.Connection import database

class StudentFamilyLinker:
    def __init__(self):
        self.db = database("utilities\\db\\DataBaseUE.db")
        
        # Listas de datos para generar estudiantes
        self.nombres_hombres = [
            "Alejandro", "Andrés", "Antonio", "Carlos", "Daniel", "David", "Diego", "Eduardo", "Fernando", "Gabriel",
            "Gonzalo", "Héctor", "Iván", "Javier", "José", "Juan", "Luis", "Manuel", "Miguel", "Nicolás",
            "Pablo", "Pedro", "Rafael", "Ricardo", "Roberto", "Rubén", "Samuel", "Sergio", "Tomás", "Víctor"
        ]
        
        self.nombres_mujeres = [
            "Alejandra", "Ana", "Andrea", "Beatriz", "Camila", "Carla", "Carmen", "Claudia", "Cristina", "Daniela",
            "Elena", "Eva", "Isabella", "Isabel", "Laura", "Lucía", "María", "Marta", "Natalia", "Paula",
            "Rocío", "Sara", "Sofía", "Valentina", "Valeria", "Verónica", "Victoria", "Yolanda", "Zoe", "Adriana"
        ]
        
        self.apellidos = [
            "García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez", "Pérez", "Gómez", "Martín",
            "Jiménez", "Ruiz", "Hernández", "Díaz", "Moreno", "Muñoz", "Álvarez", "Romero", "Alonso", "Gutiérrez",
            "Navarro", "Torres", "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano", "Blanco", "Suárez"
        ]
        
        self.generos = ["Masculino", "Femenino"]
        self.lateralidades = ["Diestro", "Zurdo", "Ambidiestro"]
        self.nacionalidades = ["Venezolana", "Colombiana", "Ecuatoriana", "Peruana", "Chilena", "Argentina"]
        self.estados = ["Distrito Capital", "Miranda", "Vargas", "Aragua", "Carabobo", "Zulia", "Lara", "Táchira"]
        self.municipios = [
            "Libertador", "Chacao", "Baruta", "El Hatillo", "Sucre", "Petare", "Guarenas", "Guatire",
            "Los Teques", "Guacara", "Valencia", "Maracay", "Maracaibo", "Barquisimeto", "San Cristóbal"
        ]
        self.tipos_sangre = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        self.alergias = ["Ninguna", "Polen", "Lácteos", "Frutos secos", "Mariscos", "Medicamentos", "Polvo"]
        self.dificultades = ["Ninguna", "Visual", "Auditiva", "Motora", "Aprendizaje", "Comunicación"]

    def generar_cedula_escolar(self):
        """Genera una cédula escolar única."""
        return f"CE{random.randint(100000, 999999)}"

    def generar_fecha_nacimiento_estudiante(self, edad_min=5, edad_max=18):
        """Genera una fecha de nacimiento para estudiantes."""
        edad = random.randint(edad_min, edad_max)
        fecha_actual = datetime.now()
        fecha_nacimiento = fecha_actual - timedelta(days=edad * 365 + random.randint(0, 365))
        return fecha_nacimiento.strftime("%Y-%m-%d")

    def generar_direccion_estudiante(self):
        """Genera una dirección para estudiantes."""
        calles = [
            "Av. Francisco de Miranda", "Av. Libertador", "Av. Bolívar", "Calle Real", "Calle Principal",
            "Av. Universidad", "Av. Casanova", "Calle 3", "Calle 5", "Av. Sucre", "Calle Comercio",
            "Av. Páez", "Calle 1", "Calle 2", "Av. Fuerzas Armadas", "Calle 4", "Av. Urdaneta"
        ]
        return f"{random.choice(calles)}, {random.choice(['Edificio', 'Casa', 'Apartamento'])} {random.randint(1, 200)}"

    def generar_correo_estudiante(self, nombre, apellido):
        """Genera un correo electrónico para estudiantes."""
        dominios = ["gmail.com", "hotmail.com", "yahoo.com", "estudiante.edu.ve"]
        return f"{nombre.lower()}.{apellido.lower()}{random.randint(1, 99)}@{random.choice(dominios)}"

    def obtener_estadisticas_actuales(self):
        """Obtiene las estadísticas actuales de la base de datos."""
        try:
            # Contar estudiantes
            self.db.cursor.execute("SELECT COUNT(*) FROM Estudend")
            estudiantes_count = self.db.cursor.fetchone()[0]
            
            # Contar representantes
            self.db.cursor.execute("SELECT COUNT(*) FROM REPL")
            representantes_count = self.db.cursor.fetchone()[0]
            
            # Contar padres
            self.db.cursor.execute("SELECT COUNT(*) FROM DTP")
            padres_count = self.db.cursor.fetchone()[0]
            
            # Contar madres
            self.db.cursor.execute("SELECT COUNT(*) FROM DTM")
            madres_count = self.db.cursor.fetchone()[0]
            
            return {
                'estudiantes': estudiantes_count,
                'representantes': representantes_count,
                'padres': padres_count,
                'madres': madres_count
            }
        except Exception as e:
            print(f"❌ Error obteniendo estadísticas: {e}")
            return {'estudiantes': 0, 'representantes': 0, 'padres': 0, 'madres': 0}

    def obtener_ids_disponibles(self, tabla, limite=100):
        """Obtiene los IDs disponibles de una tabla."""
        try:
            if tabla == "REPL":
                self.db.cursor.execute("SELECT IDRPL FROM REPL ORDER BY IDRPL LIMIT ?", (limite,))
            elif tabla == "DTP":
                self.db.cursor.execute("SELECT IDP FROM DTP ORDER BY IDP LIMIT ?", (limite,))
            elif tabla == "DTM":
                self.db.cursor.execute("SELECT IDM FROM DTM ORDER BY IDM LIMIT ?", (limite,))
            
            ids = [row[0] for row in self.db.cursor.fetchall()]
            return ids
        except Exception as e:
            print(f"❌ Error obteniendo IDs de {tabla}: {e}")
            return []

    def crear_estudiante_vinculado(self, i, id_representante, id_padre, id_madre):
        """Crea un estudiante vinculado con representante, padre y madre."""
        genero = random.choice(self.generos)
        nombre = random.choice(self.nombres_hombres if genero == "Masculino" else self.nombres_mujeres)
        apellido = random.choice(self.apellidos)
        cedula_escolar = self.generar_cedula_escolar()
        edad = random.randint(5, 18)
        fecha_nacimiento = self.generar_fecha_nacimiento_estudiante(5, 18)
        lateralidad = random.choice(self.lateralidades)
        nacionalidad = random.choice(self.nacionalidades)
        estado = random.choice(self.estados)
        municipio = random.choice(self.municipios)
        direccion = self.generar_direccion_estudiante()
        punto_referencia = f"Cerca de {random.choice(['Plaza', 'Escuela', 'Hospital', 'Centro Comercial'])}"
        altura = random.randint(100, 180)
        peso = random.randint(20, 80)
        talla_zapatos = random.randint(25, 45)
        talla_camisa = random.choice(["XS", "S", "M", "L", "XL", "XXL"])
        talla_pantalon = random.choice(["XS", "S", "M", "L", "XL", "XXL"])
        numero_hermanos = random.randint(0, 5)
        autorizado_retirar = random.choice(["Sí", "No"])
        alergico_a = random.choice(self.alergias)
        alguna_dificultad = random.choice(self.dificultades)
        especificar_dificultad = "No especificado" if alguna_dificultad == "Ninguna" else f"Dificultad en {alguna_dificultad}"
        correo = self.generar_correo_estudiante(nombre, apellido)
        telefono_habitacion = f"0{random.randint(200, 999)}-{random.randint(1000000, 9999999)}"
        carton_vacunas = "Completo" if random.choice([True, False]) else "Pendiente"
        tipo_sangre = random.choice(self.tipos_sangre)
        examen_heces = "Negativo" if random.choice([True, False]) else "Pendiente"
        observaciones = "Estudiante regular" if random.choice([True, False]) else "Requiere atención especial"

        try:
            self.db.cursor.execute('''
                INSERT INTO Estudend (Nombre, Apellido, CedulaEscolar, Edad, Genero, FN, Lateralidad, Nacionalidad, 
                Estado, Municipio, DA, PTR, Altura, Peso, Zapatos, Camisa, Pantalon, NDH, APRN, AlergicoA, 
                AlgunaDificultad, EspecifiqueDificultad, CorreoElectronico, TelefonoHabitacion, CartonVacunas, 
                TipodeSangre, EDH, observaciones, IDRPL, IDP, IDM)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nombre, apellido, cedula_escolar, edad, genero, fecha_nacimiento, lateralidad, nacionalidad,
                  estado, municipio, direccion, punto_referencia, altura, peso, talla_zapatos, talla_camisa, 
                  talla_pantalon, numero_hermanos, autorizado_retirar, alergico_a, alguna_dificultad, 
                  especificar_dificultad, correo, telefono_habitacion, carton_vacunas, tipo_sangre, 
                  examen_heces, observaciones, id_representante, id_padre, id_madre))
            
            self.db.connection.commit()
            print(f"✅ Estudiante {i+1}/100 creado y vinculado: {nombre} {apellido}")
            return True
        except Exception as e:
            print(f"❌ Error creando estudiante {i+1}: {e}")
            return False

    def vincular_estudiantes_familias(self):
        """Vincula estudiantes con representantes, padres y madres."""
        print("🔗 Iniciando vinculación de estudiantes con familias...")
        print("=" * 60)
        
        # Obtener estadísticas actuales
        stats = self.obtener_estadisticas_actuales()
        print(f"📊 Estado actual:")
        print(f"   👨‍🎓 Estudiantes: {stats['estudiantes']}")
        print(f"   👨‍💼 Representantes: {stats['representantes']}")
        print(f"   👨 Padres: {stats['padres']}")
        print(f"   👩 Madres: {stats['madres']}")
        
        # Obtener IDs disponibles
        ids_representantes = self.obtener_ids_disponibles("REPL", 100)
        ids_padres = self.obtener_ids_disponibles("DTP", 100)
        ids_madres = self.obtener_ids_disponibles("DTM", 100)
        
        print(f"\n📋 IDs disponibles:")
        print(f"   👨‍💼 Representantes: {len(ids_representantes)}")
        print(f"   👨 Padres: {len(ids_padres)}")
        print(f"   👩 Madres: {len(ids_madres)}")
        
        if len(ids_representantes) < 100 or len(ids_padres) < 100 or len(ids_madres) < 100:
            print("❌ No hay suficientes registros de familia para vincular 100 estudiantes")
            return False
        
        # Calcular cuántos estudiantes necesitamos crear
        estudiantes_necesarios = 100 - stats['estudiantes']
        
        if estudiantes_necesarios <= 0:
            print("✅ Ya hay suficientes estudiantes. Vinculando los existentes...")
            estudiantes_necesarios = min(100, stats['estudiantes'])
        else:
            print(f"📝 Necesitamos crear {estudiantes_necesarios} estudiantes adicionales")
        
        print("\n" + "=" * 60)
        print("👨‍🎓 Creando y vinculando estudiantes...")
        
        # Crear y vincular estudiantes
        exitosos = 0
        for i in range(100):
            if i < len(ids_representantes) and i < len(ids_padres) and i < len(ids_madres):
                if self.crear_estudiante_vinculado(i+1, ids_representantes[i], ids_padres[i], ids_madres[i]):
                    exitosos += 1
        
        print("\n" + "=" * 60)
        print("✅ ¡Vinculación completada!")
        print(f"📈 Total de estudiantes vinculados: {exitosos}")
        
        # Mostrar estadísticas finales
        stats_finales = self.obtener_estadisticas_actuales()
        print("\n📊 ESTADÍSTICAS FINALES:")
        print(f"👨‍🎓 Estudiantes: {stats_finales['estudiantes']}")
        print(f"👨‍💼 Representantes: {stats_finales['representantes']}")
        print(f"👨 Padres: {stats_finales['padres']}")
        print(f"👩 Madres: {stats_finales['madres']}")
        
        return exitosos == 100

def main():
    """Función principal."""
    print("🔗 VINCULADOR DE ESTUDIANTES CON FAMILIAS")
    print("=" * 60)
    
    try:
        linker = StudentFamilyLinker()
        success = linker.vincular_estudiantes_familias()
        
        if success:
            print("\n🎉 ¡Proceso completado exitosamente!")
        else:
            print("\n⚠️ Proceso completado con advertencias")
            
    except Exception as e:
        print(f"❌ Error general: {e}")
    finally:
        print("\n🏁 Proceso finalizado.")

if __name__ == "__main__":
    main()
