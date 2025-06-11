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
                Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Tipo_de_Sangre, Carton_Vacunas, Examen_de_Heces,
                # Ubicacion
                Nacionalidad, Estado, Municipio, Punto_de_Referencia):
      
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
      
      
      
      # Insert Data Base Comando
      self.database.insertEstudend(Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Correo_Electronico, Telefono_de_Habitacion, Direccion_Actual, Altura, Peso, Talla_Camisa, Talla_Pantalon, Talla_Zapatos, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Tipo_de_Sangre, Carton_Vacunas, Examen_de_Heces, Nacionalidad, Estado, Municipio, Punto_de_Referencia)
      
      
      
