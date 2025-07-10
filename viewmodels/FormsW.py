from models.Estudend import Estudend
from services.Connection import database

class EstudendViewModel:
    def __init__(self):
      self.database = database("utilities\\db\\DataBaseUE.db")
      self.Estudend = Estudend()
      
    def set_date(self,
                # Datos Personales
                Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño,
                # Datos de Contacto
                Correo_Electronico, Telefono_de_Habitacion, Direccion_Actual,
                # Tallas
                Altura, Peso, Talla_Camisa, Talla_Pantalon, Talla_Zapatos,
                # Datos Medicos
                Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Tipo_de_Sangre, Examen_de_Heces,
                # Ubicacion
                Nacionalidad, Estado, Municipio, Punto_de_Referencia, 
                # Datos del Representante
                nombre, apellido, cedula, fecha_nacimiento, edad, estado_civil, nacionalidad, afinidad, profesion, ocupacion, empresaDTrabaja, direccion, telefonoMovil, telefonoHabitacion, telefonoFamiliar, correoElectronico, rif, planillaSige, codigoPatria, serialPatria,
                # Datos del Padre
                nombre_padre, apellido_padre, cedula_padre, fecha_nacimiento_padre, edad_padre, tipo_empleo_padre, empresa_trabaja_padre, vive_con_el_nino_padre, causa_no_vive_padre, direccion_padre, telefono_movil_padre,
                # Datos de la Madre
                nombre_madre, apellido_madre, cedula_madre, fecha_nacimiento_madre, edad_madre, tipo_empleo_madre, empresa_trabaja_madre, vive_con_el_nino_madre, causa_no_vive_madre, direccion_madre, telefono_movil_madre, Carton_Vacunas=None,
                ):
      
      # Tabla de Estudend
      # Datos Personales
      self.Estudend.Nombre = Nombre
      self.Estudend.Apellido = Apellido
      self.Estudend.Cedula_Escolar = Cedula_Escolar
      self.Estudend.Edad = Edad
      self.Estudend.Genero = Genero
      self.Estudend.Fecha_de_Nacimiento = Fecha_de_Nacimiento
      self.Estudend.Lateralidad = Lateralidad
      self.Estudend.Numero_de_Hermanos = Numero_de_Hermanos
      self.Estudend.Autorizado_para_Retirar_al_Niño = Autorizado_para_Retirar_al_Niño
      
      # Datos de Contacto
      self.Estudend.Correo_Electronico = Correo_Electronico
      self.Estudend.Telefono_de_Habitacion = Telefono_de_Habitacion
      self.Estudend.Direccion_Actual = Direccion_Actual
      
      # Tallas
      self.Estudend.Altura = Altura
      self.Estudend.Peso = Peso
      self.Estudend.Talla_Camisa = Talla_Camisa
      self.Estudend.Talla_Pantalon = Talla_Pantalon
      self.Estudend.Talla_Zapatos = Talla_Zapatos
      
      # Datos Medicos
      self.Estudend.Alergico_a = Alergico_a
      self.Estudend.Alguna_Dificultad = Alguna_Dificultad
      self.Estudend.Especificar_Dificultad = Especificar_Dificultad
      self.Estudend.Tipo_de_Sangre = Tipo_de_Sangre
      self.Estudend.Carton_Vacunas = Carton_Vacunas
      self.Estudend.Examen_de_Heces = Examen_de_Heces
      
      # Ubicacion
      self.Estudend.Nacionalidad = Nacionalidad
      self.Estudend.Estado = Estado
      self.Estudend.Municipio = Municipio
      self.Estudend.Punto_de_Referencia = Punto_de_Referencia
      
      # Tabla de Representante
      # Datos Personales
      self.Estudend.nombre = nombre
      self.Estudend.apellido = apellido
      self.Estudend.cedula = cedula
      self.Estudend.fecha_nacimiento = fecha_nacimiento
      self.Estudend.edad = edad
      self.Estudend.estado_civil = estado_civil
      self.Estudend.nacionalidad = nacionalidad
      self.Estudend.afinidad = afinidad
      self.Estudend.profesion = profesion
      self.Estudend.ocupacion = ocupacion
      self.Estudend.empresaDTrabaja = empresaDTrabaja
      self.Estudend.direccion = direccion
      self.Estudend.telefonoMovil = telefonoMovil
      self.Estudend.telefonoHabitacion = telefonoHabitacion
      self.Estudend.telefonoFamiliar = telefonoFamiliar
      self.Estudend.correoElectronico = correoElectronico
      self.Estudend.rif = rif
      self.Estudend.planillaSige = planillaSige
      self.Estudend.codigoPatria = codigoPatria
      self.Estudend.serialPatria = serialPatria
      
      # Tabla del Padre
      self.Estudend.nombre_padre = nombre_padre
      self.Estudend.apellido_padre = apellido_padre
      self.Estudend.cedula_padre = cedula_padre
      self.Estudend.fecha_nacimiento_padre = fecha_nacimiento_padre
      self.Estudend.edad_padre = edad_padre
      self.Estudend.tipo_empleo_padre = tipo_empleo_padre
      self.Estudend.empresa_trabaja_padre = empresa_trabaja_padre
      self.Estudend.vive_con_el_nino_padre = vive_con_el_nino_padre
      self.Estudend.causa_no_vive_padre = causa_no_vive_padre
      self.Estudend.direccion_padre = direccion_padre
      self.Estudend.telefono_movil_padre = telefono_movil_padre
      
      # Tabla de la Madre
      self.Estudend.nombre_madre = nombre_madre
      self.Estudend.apellido_madre = apellido_madre
      self.Estudend.cedula_madre = cedula_madre
      self.Estudend.fecha_nacimiento_madre = fecha_nacimiento_madre
      self.Estudend.edad_madre = edad_madre
      self.Estudend.tipo_empleo_madre = tipo_empleo_madre
      self.Estudend.empresa_trabaja_madre = empresa_trabaja_madre
      self.Estudend.vive_con_el_nino_madre = vive_con_el_nino_madre
      self.Estudend.causa_no_vive_madre = causa_no_vive_madre
      self.Estudend.direccion_madre = direccion_madre
      self.Estudend.telefono_movil_madre = telefono_movil_madre
      self.Estudend.Carton_Vacunas = Carton_Vacunas
      
      # Insert Data Base Comando
      self.database.insertEstudend(Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Correo_Electronico, Telefono_de_Habitacion, Direccion_Actual, Altura, Peso, Talla_Camisa, Talla_Pantalon, Talla_Zapatos, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Tipo_de_Sangre, Carton_Vacunas, Examen_de_Heces, Nacionalidad, Estado, Municipio, Punto_de_Referencia, nombre, apellido, cedula, fecha_nacimiento, edad, estado_civil, nacionalidad, afinidad, profesion, ocupacion, empresaDTrabaja, direccion, telefonoMovil, telefonoHabitacion, telefonoFamiliar, correoElectronico, rif, planillaSige, codigoPatria, serialPatria,nombre_padre, apellido_padre, cedula_padre, fecha_nacimiento_padre, edad_padre, tipo_empleo_padre, empresa_trabaja_padre, vive_con_el_nino_padre, causa_no_vive_padre, direccion_padre, telefono_movil_padre,nombre_madre, apellido_madre, cedula_madre, fecha_nacimiento_madre, edad_madre, tipo_empleo_madre, empresa_trabaja_madre, vive_con_el_nino_madre, causa_no_vive_madre, direccion_madre, telefono_movil_madre)
      
      
      
