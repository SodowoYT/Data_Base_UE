#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para insertar 100 registros de prueba de representantes, padres y madres
en la base de datos del sistema educativo.
"""

import sys
import os
import random
from datetime import datetime, timedelta

# Agregar el directorio raíz al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.Connection import database

class SampleDataGenerator:
    def __init__(self):
        self.db = database("utilities\\db\\DataBaseUE.db")
        
        # Listas de datos para generar registros realistas
        self.nombres_hombres = [
            "Carlos", "José", "Luis", "Miguel", "Antonio", "Francisco", "Manuel", "David", "Daniel", "Rafael",
            "Pedro", "Alejandro", "Roberto", "Fernando", "Diego", "Sergio", "Andrés", "Jorge", "Ricardo", "Eduardo",
            "Gabriel", "Mario", "Alberto", "Raúl", "Javier", "Rubén", "Víctor", "Héctor", "Oscar", "Iván",
            "Pablo", "Ángel", "Adrián", "Gonzalo", "César", "Emilio", "Felipe", "Nicolás", "Samuel", "Tomás"
        ]
        
        self.nombres_mujeres = [
            "María", "Carmen", "Ana", "Laura", "Isabel", "Pilar", "Dolores", "Teresa", "Rosa", "Francisca",
            "Antonia", "Mercedes", "Josefa", "Cristina", "Mónica", "Ángeles", "Lucía", "Elena", "Sara", "Paula",
            "Raquel", "Sandra", "Patricia", "Montserrat", "Alba", "Andrea", "Natalia", "Sonia", "Silvia", "Beatriz",
            "Nuria", "Rocío", "Marta", "Claudia", "Eva", "Lorena", "Miriam", "Noelia", "Cristina", "Verónica"
        ]
        
        self.apellidos = [
            "García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez", "Pérez", "Gómez", "Martín",
            "Jiménez", "Ruiz", "Hernández", "Díaz", "Moreno", "Muñoz", "Álvarez", "Romero", "Alonso", "Gutiérrez",
            "Navarro", "Torres", "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano", "Blanco", "Suárez",
            "Molina", "Morales", "Ortega", "Delgado", "Castro", "Ortiz", "Rubio", "Marín", "Sanz", "Iglesias"
        ]
        
        self.estados_civiles = ["Soltero", "Casado", "Divorciado", "Viudo", "Unión Libre"]
        self.nacionalidades = ["Venezolana", "Colombiana", "Ecuatoriana", "Peruana", "Chilena", "Argentina", "Mexicana", "Española"]
        self.afinidades = ["Padre", "Madre", "Abuelo", "Abuela", "Tío", "Tía", "Hermano", "Hermana", "Tutor Legal"]
        self.profesiones = [
            "Ingeniero", "Médico", "Abogado", "Contador", "Profesor", "Enfermero", "Técnico", "Comerciante", 
            "Empresario", "Arquitecto", "Psicólogo", "Administrador", "Vendedor", "Obrero", "Ama de Casa"
        ]
        self.ocupaciones = [
            "Empleado Público", "Empleado Privado", "Independiente", "Jubilado", "Desempleado", "Estudiante", 
            "Comerciante", "Empresario", "Trabajador por Cuenta Propia", "Ama de Casa"
        ]
        self.empresas = [
            "PDVSA", "Corporación Venezolana de Guayana", "Instituto Nacional de Estadística", "Banco de Venezuela",
            "Corporación Eléctrica Nacional", "Hidrocapital", "Metro de Caracas", "Alcaldía de Caracas",
            "Gobernación del Distrito Capital", "Ministerio de Educación", "Hospital Central", "Clínica Privada",
            "Universidad Central de Venezuela", "Universidad Simón Bolívar", "Instituto Venezolano de Investigaciones Científicas",
            "Empresa Privada", "Comercio Local", "Taller Mecánico", "Farmacia", "Supermercado"
        ]
        self.estados = ["Distrito Capital", "Miranda", "Vargas", "Aragua", "Carabobo", "Zulia", "Lara", "Táchira"]
        self.municipios = [
            "Libertador", "Chacao", "Baruta", "El Hatillo", "Sucre", "Petare", "Guarenas", "Guatire",
            "Los Teques", "Guacara", "Valencia", "Maracay", "Maracaibo", "Barquisimeto", "San Cristóbal"
        ]
        self.tipos_empleo = [
            "Tiempo Completo", "Medio Tiempo", "Por Horas", "Contrato", "Servicios Profesionales", 
            "Consultoría", "Freelance", "Jubilado", "Desempleado"
        ]
        self.causas_no_vive = [
            "Trabajo en el exterior", "Separación", "Fallecimiento", "Desconocido", "No aplica", 
            "Vive en otra ciudad", "Problemas familiares", "No especificado"
        ]

    def generar_cedula(self):
        """Genera una cédula venezolana válida."""
        return f"V-{random.randint(10000000, 99999999)}"

    def generar_rif(self):
        """Genera un RIF venezolano."""
        return f"J-{random.randint(10000000, 99999999)}-{random.randint(1, 9)}"

    def generar_telefono(self):
        """Genera un número de teléfono venezolano."""
        return f"0{random.randint(200, 999)}-{random.randint(1000000, 9999999)}"

    def generar_fecha_nacimiento(self, edad_min=25, edad_max=65):
        """Genera una fecha de nacimiento basada en la edad."""
        edad = random.randint(edad_min, edad_max)
        fecha_actual = datetime.now()
        fecha_nacimiento = fecha_actual - timedelta(days=edad * 365 + random.randint(0, 365))
        return fecha_nacimiento.strftime("%Y-%m-%d")

    def generar_direccion(self):
        """Genera una dirección venezolana."""
        calles = [
            "Av. Francisco de Miranda", "Av. Libertador", "Av. Bolívar", "Calle Real", "Calle Principal",
            "Av. Universidad", "Av. Casanova", "Calle 3", "Calle 5", "Av. Sucre", "Calle Comercio",
            "Av. Páez", "Calle 1", "Calle 2", "Av. Fuerzas Armadas", "Calle 4", "Av. Urdaneta",
            "Calle 6", "Av. Andrés Bello", "Calle 7"
        ]
        return f"{random.choice(calles)}, {random.choice(['Edificio', 'Casa', 'Apartamento'])} {random.randint(1, 200)}"

    def generar_codigo_patria(self):
        """Genera un código Patria."""
        return f"PAT{random.randint(100000, 999999)}"

    def generar_serial_patria(self):
        """Genera un serial Patria."""
        return f"SP{random.randint(100000, 999999)}"

    def generar_correo(self, nombre, apellido):
        """Genera un correo electrónico."""
        dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "cantv.net"]
        return f"{nombre.lower()}.{apellido.lower()}{random.randint(1, 99)}@{random.choice(dominios)}"

    def insertar_representante(self, i):
        """Inserta un representante con datos generados."""
        nombre = random.choice(self.nombres_hombres + self.nombres_mujeres)
        apellido = random.choice(self.apellidos)
        cedula = self.generar_cedula()
        fecha_nacimiento = self.generar_fecha_nacimiento(25, 65)
        edad = random.randint(25, 65)
        estado_civil = random.choice(self.estados_civiles)
        nacionalidad = random.choice(self.nacionalidades)
        afinidad = random.choice(self.afinidades)
        profesion = random.choice(self.profesiones)
        ocupacion = random.choice(self.ocupaciones)
        empresa = random.choice(self.empresas)
        direccion = self.generar_direccion()
        telefono_movil = self.generar_telefono()
        telefono_habitacion = self.generar_telefono()
        telefono_familiar = self.generar_telefono()
        correo = self.generar_correo(nombre, apellido)
        rif = self.generar_rif()
        planilla_sige = f"SIGE{random.randint(100000, 999999)}"
        codigo_patria = self.generar_codigo_patria()
        serial_patria = self.generar_serial_patria()

        try:
            self.db.insertRpl(
                nombre, apellido, cedula, fecha_nacimiento, edad, estado_civil, nacionalidad, afinidad,
                profesion, ocupacion, empresa, direccion, telefono_movil, telefono_habitacion, 
                telefono_familiar, correo, rif, planilla_sige, codigo_patria, serial_patria
            )
            print(f"✅ Representante {i+1}/100 insertado: {nombre} {apellido}")
            return cedula
        except Exception as e:
            print(f"❌ Error insertando representante {i+1}: {e}")
            return None

    def insertar_padre(self, i, cedula_representante):
        """Inserta un padre con datos generados."""
        nombre = random.choice(self.nombres_hombres)
        apellido = random.choice(self.apellidos)
        cedula = self.generar_cedula()
        fecha_nacimiento = self.generar_fecha_nacimiento(30, 70)
        edad = random.randint(30, 70)
        tipo_empleo = random.choice(self.tipos_empleo)
        empresa = random.choice(self.empresas)
        vive_con_nino = random.choice(["Sí", "No"])
        causa_no_vive = random.choice(self.causas_no_vive) if vive_con_nino == "No" else "No aplica"
        direccion = self.generar_direccion()
        telefono_movil = self.generar_telefono()

        try:
            self.db.insertDTP(
                nombre, apellido, cedula, fecha_nacimiento, edad, tipo_empleo, empresa,
                vive_con_nino, causa_no_vive, direccion, telefono_movil
            )
            print(f"✅ Padre {i+1}/100 insertado: {nombre} {apellido}")
        except Exception as e:
            print(f"❌ Error insertando padre {i+1}: {e}")

    def insertar_madre(self, i, cedula_representante):
        """Inserta una madre con datos generados."""
        nombre = random.choice(self.nombres_mujeres)
        apellido = random.choice(self.apellidos)
        cedula = self.generar_cedula()
        fecha_nacimiento = self.generar_fecha_nacimiento(25, 65)
        edad = random.randint(25, 65)
        tipo_empleo = random.choice(self.tipos_empleo)
        empresa = random.choice(self.empresas)
        vive_con_nino = random.choice(["Sí", "No"])
        causa_no_vive = random.choice(self.causas_no_vive) if vive_con_nino == "No" else "No aplica"
        direccion = self.generar_direccion()
        telefono_movil = self.generar_telefono()

        try:
            self.db.insertDTM(
                nombre, apellido, cedula, fecha_nacimiento, edad, tipo_empleo, empresa,
                vive_con_nino, causa_no_vive, direccion, telefono_movil
            )
            print(f"✅ Madre {i+1}/100 insertada: {nombre} {apellido}")
        except Exception as e:
            print(f"❌ Error insertando madre {i+1}: {e}")

    def insertar_datos_masivos(self):
        """Inserta 100 registros de representantes, padres y madres."""
        print("🚀 Iniciando inserción de 100 registros de prueba...")
        print("=" * 60)
        
        cedulas_representantes = []
        
        # Insertar 100 representantes
        for i in range(100):
            cedula = self.insertar_representante(i)
            if cedula:
                cedulas_representantes.append(cedula)
        
        print("\n" + "=" * 60)
        print("📊 Insertando padres...")
        
        # Insertar 100 padres
        for i in range(100):
            cedula_ref = cedulas_representantes[i] if i < len(cedulas_representantes) else None
            self.insertar_padre(i, cedula_ref)
        
        print("\n" + "=" * 60)
        print("👩 Insertando madres...")
        
        # Insertar 100 madres
        for i in range(100):
            cedula_ref = cedulas_representantes[i] if i < len(cedulas_representantes) else None
            self.insertar_madre(i, cedula_ref)
        
        print("\n" + "=" * 60)
        print("✅ ¡Inserción completada!")
        print(f"📈 Total de representantes insertados: {len(cedulas_representantes)}")
        print("📈 Total de padres insertados: 100")
        print("📈 Total de madres insertadas: 100")
        
        # Mostrar estadísticas finales
        stats = self.db.get_dashboard_stats()
        print("\n📊 ESTADÍSTICAS ACTUALES DE LA BASE DE DATOS:")
        print(f"👨‍🎓 Estudiantes: {stats['estudiantes']}")
        print(f"👨‍💼 Representantes: {stats['representantes']}")
        print(f"👨 Padres: {stats['padres']}")
        print(f"👩 Madres: {stats['madres']}")

def main():
    """Función principal."""
    print("🎯 GENERADOR DE DATOS DE PRUEBA - SISTEMA EDUCATIVO")
    print("=" * 60)
    
    try:
        generator = SampleDataGenerator()
        generator.insertar_datos_masivos()
    except Exception as e:
        print(f"❌ Error general: {e}")
    finally:
        print("\n🏁 Proceso finalizado.")

if __name__ == "__main__":
    main()
