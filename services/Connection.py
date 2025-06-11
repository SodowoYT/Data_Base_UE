import sqlite3 
class database:
  def __init__(self, db_name):
    self.connection = sqlite3.connect("utilities\\db\\DataBaseUE.db")
    self.cursor = self.connection.cursor()
    
  def insertEstudend(self, Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Correo_Electronico, Telefono_de_Habitacion, Direccion_Actual, Altura, Peso, Talla_Camisa, Talla_Pantalon, Talla_Zapatos, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Tipo_de_Sangre, Carton_Vacunas, Examen_de_Heces, Nacionalidad, Estado, Municipio, Punto_de_Referencia):
    
    self.cursor.execute('''
      INSERT INTO Estudend (Nombre, Apellido, CedulaEscolar, Edad, Genero, FN, Lateralidad, NDH, APRN, CorreoElectronico, TelefonoHabitacion, DA, Altura, Peso, Camisa, Pantalon, Zapatos, AlergicoA, AlgunaDificultad, EspecifiqueDificultad, TipodeSangre, CartonVacunas, EDH, Nacionalidad, Estado, Municipio, PTR)
      VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
      
    ''', (Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Correo_Electronico, Telefono_de_Habitacion, Direccion_Actual, Altura, Peso, Talla_Camisa, Talla_Pantalon, Talla_Zapatos, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Tipo_de_Sangre, Carton_Vacunas, Examen_de_Heces, Nacionalidad, Estado, Municipio, Punto_de_Referencia))
    
    self.connection.commit()
    