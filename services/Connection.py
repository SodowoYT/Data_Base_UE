import sqlite3 
class database:
  def __init__(self, db_name):
    self.connection = sqlite3.connect("utilities\\db\\DataBaseUE.db")
    self.cursor = self.connection.cursor()

# Insertado de datos del estudiante
  def insertEstudend(self, Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Nacionalidad, Estado, Municipio, Direccion_Actual, Punto_de_Referencia, Altura, Peso, Talla_Zapatos, Talla_Camisa, Talla_Pantalon, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Correo_Electronico, Telefono_de_Habitacion, Tipo_de_Sangre, Examen_de_Heces, Carton_Vacunas=None):
    
    self.cursor.execute('''
      INSERT INTO Estudend (Nombre, Apellido, CedulaEscolar, Edad, Genero, FN, Lateralidad,  Nacionalidad, Estado, Municipio, DA, PTR, Altura, Peso, Zapatos, Camisa, Pantalon, NDH, APRN, AlergicoA, AlgunaDificultad, EspecifiqueDificultad, CorreoElectronico, TelefonoHabitacion, CartonVacunas, TipodeSangre, EDH)
      VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
      
    ''', (Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Nacionalidad, Estado, Municipio, Direccion_Actual, Punto_de_Referencia, Altura, Peso, Talla_Zapatos, Talla_Camisa, Talla_Pantalon, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Correo_Electronico, Telefono_de_Habitacion, Carton_Vacunas, Tipo_de_Sangre, Examen_de_Heces))
    
    self.connection.commit()

# Insertado de datos de representante
  def insertRpl(self, nombre, apellido, cedula, fecha_nacimiento, edad, estado_civil, nacionalidad, afinidad, profesion, ocupacion, empresaDTrabaja, direccion, telefonoMovil, telefonoHabitacion, telefonoFamiliar, correoElectronico, rif, planillaSige, codigoPatria, serialPatria):
    self.cursor.execute('''
      INSERT INTO REPL (Nombre, Apellido, Cedula, FN, Edad, EC, Nacionalidad, Afinidad,  Profesion, Ocupacion, EMPDT,  Direccion, TelefonoMovil, TelefonoHabitacion, TelefonoDFamiliar, CorreoElectronico, RIF, PlanillaSige, CodigoPatria, SerialPatria)
      VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nombre, apellido, cedula, fecha_nacimiento, edad, estado_civil, nacionalidad, afinidad, profesion, ocupacion, empresaDTrabaja, direccion, telefonoMovil, telefonoHabitacion, telefonoFamiliar, correoElectronico, rif, planillaSige, codigoPatria, serialPatria))
    self.connection.commit()

# Insertaddo de datos del padre

  def insertDTP (self, nombre, apellido, cedula, fechaDNacimiento, edad, tipoEmpleoqDesempeña, empresaDTrabaja, viveConElNiño, causaPNoVive,   direccion, telefonoMovil):
    self.cursor.execute('''
      INSERT INTO DTP (Nombre, Apellido, Cedula, FN, Edad, TED,EMDT, VCN, CPNVCN, Direccion, TelefonoMovil )
      VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nombre, apellido, cedula, fechaDNacimiento, edad, tipoEmpleoqDesempeña, empresaDTrabaja, viveConElNiño, causaPNoVive,   direccion, telefonoMovil))
    self.connection.commit()

# Insertado de datos de la madre

  def insertDTM (self, nombre, apellido, cedula, fechaDNacimiento, edad, tipoEmpleoqDesempeña, empresaDTrabaja, viveConElNiño, causaPNoVive,   direccion, telefonoMovil):
    self.cursor.execute('''
      INSERT INTO DTM (Nombre, Apellido, Cedula, FN, Edad, TED,EMDT, VCN, CPNVCN, Direccion, TelefonoMovil )
      VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nombre, apellido, cedula, fechaDNacimiento, edad, tipoEmpleoqDesempeña, empresaDTrabaja, viveConElNiño, causaPNoVive,   direccion, telefonoMovil))
    self.connection.commit()

# Consultar datos de estudiante
  def SelectEstudend(self):
    self.cursor.execute('''
      SELECT * FROM Estudend
    ''')
    return self.cursor.fetchall()
