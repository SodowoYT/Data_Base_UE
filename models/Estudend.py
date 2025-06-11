class Estudend:
    def __init__(self, 
                # Datos Personales
                Nombre ="", Apellido ="", Cedula_Escolar ="", Edad ="", Genero ="", Fecha_de_Nacimiento ="", Lateralidad ="", Numero_de_Hermanos ="", Autorizado_para_Retirar_al_Niño ="",
                # Datos de Contacto
                Correo_Electronico ="", Telefono_de_Habitacion ="", Direccion_Actual ="",
                # Tallas
                Altura ="", Peso ="", Talla_Camisa ="", Talla_Pantalon ="", Talla_Zapatos ="",
                # Datos Medicos
                Alergico_a ="", Alguna_Dificultad ="", Especificar_Dificultad ="", Tipo_de_Sangre ="", Carton_Vacunas ="", Examen_de_Heces ="",
                # Ubicacion
                Nacionalidad ="", Estado ="", Municipio ="", Punto_de_Referencia =""):
      
      # Datos Personales
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Cedula_Escolar = Cedula_Escolar
        self.Edad = Edad
        self.Genero = Genero
        self.Fecha_de_Nacimiento = Fecha_de_Nacimiento 
        self.Lateralidad = Lateralidad
        self.Numero_de_Hermanos = Numero_de_Hermanos
        self.Autorizado_para_Retirar_al_Niño = Autorizado_para_Retirar_al_Niño
        
      # Datos de Contacto
        self.Correo_Electronico = Correo_Electronico 
        self.Telefono_de_Habitacion = Telefono_de_Habitacion
        self.Direccion_Actual = Direccion_Actual 
        
      # Tallas
        self.Altura = Altura
        self.Peso = Peso
        self.Talla_Camisa = Talla_Camisa
        self.Talla_Pantalon = Talla_Pantalon
        self.Talla_Zapatos = Talla_Zapatos
        
      # Datos Medicos
        self.Alergico_a = Alergico_a
        self.Alguna_Dificultad = Alguna_Dificultad
        self.Especificar_Dificultad = Especificar_Dificultad
        self.Tipo_de_Sangre = Tipo_de_Sangre
        self.Carton_Vacunas = Carton_Vacunas
        self.Examen_de_Heces = Examen_de_Heces
        
        # Ubicacion
        self.Nacionalidad = Nacionalidad
        self.Estado = Estado
        self.Municipio = Municipio
        self.Punto_de_Referencia = Punto_de_Referencia       