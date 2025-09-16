import sqlite3, os, hashlib

class database:
    def __init__(self, db_name=None):

        # -----------------------------
        # Conexión a la base de datos y creación de tablas
        # -----------------------------

        ## Conexión a la base de datos
        self.db_path = db_name or "utilities\\db\\DataBaseUE.db"
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

        ## Crear tabla
        self.__create_users_table()


    # -----------------------------
    # Creación de tablas
    # -----------------------------

    ## Crear tabla de usuarios
    def __create_users_table(self):
        """Crea la tabla de usuarios si no existe."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt BLOB NOT NULL
            )
        ''')
        self.connection.commit()

    # -----------------------------
    # Gestión de usuarios (Login)
    # -----------------------------

    ## Inserción de usuario y contraseña
    def _hash_password(self, password: str, salt: bytes) -> str:
        """Genera un hash seguro (PBKDF2)."""
        return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 200_000).hex()

    def insert_user(self, username, password, name, lastname, ci, post):
            """Inserta un usuario con datos en texto plano."""
            self.cursor.execute(
                "INSERT INTO users (Username, Password, Name, SecondName, CI, Post) VALUES (?, ?, ?, ?, ?, ?)",
                (username, password, name, lastname, ci, post)
            )
            self.connection.commit()

    ## Validación de usuario y contraseña
    def validate_user(self, username, password) -> tuple[bool, dict | None]:
        """Valida usuario y contraseña en texto plano."""
        self.cursor.execute(
            "SELECT Username, Password, Name, SecondName, CI, Post FROM users WHERE Username=? AND Password=?",
            (username, password)
        )
        row = self.cursor.fetchone()

        if row:
            return True, {
                "username": row[0],
                "password": row[1],
                "name": row[2],
                "lastname": row[3],
                "ci": row[4],
                "post": row[5]
            }
        return False, None

    # -----------------------------------
    # Métodos de Registros
    # -----------------------------------

    ## Registro de Estudiante
    def insertEstudend(self, Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Nacionalidad, Estado, Municipio, Direccion_Actual, Punto_de_Referencia, Altura, Peso, Talla_Zapatos, Talla_Camisa, Talla_Pantalon, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Correo_Electronico, Telefono_de_Habitacion, estIMG, Carton_Vacunas, Tipo_de_Sangre, Examen_de_Heces, observaciones):
        self.cursor.execute('''
            INSERT INTO Estudend (Nombre, Apellido, CedulaEscolar, Edad, Genero, FN, Lateralidad,  Nacionalidad, Estado, Municipio, DA, PTR, Altura, Peso, Zapatos, Camisa, Pantalon, NDH, APRN, AlergicoA, AlgunaDificultad, EspecifiqueDificultad, CorreoElectronico, TelefonoHabitacion, estIMG, CartonVacunas, TipodeSangre, EDH, observaciones)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Nacionalidad, Estado, Municipio, Direccion_Actual, Punto_de_Referencia, Altura, Peso, Talla_Zapatos, Talla_Camisa, Talla_Pantalon, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Correo_Electronico, Telefono_de_Habitacion, estIMG, Carton_Vacunas, Tipo_de_Sangre, Examen_de_Heces, observaciones))
        self.connection.commit()
        return self.cursor.lastrowid

    ## Registro de Representante
    def insertRpl(self, nombre, apellido, cedula, fecha_nacimiento, rpstIMG, edad, estado_civil, nacionalidad, afinidad, profesion, ocupacion, empresaDTrabaja, direccion, telefonoMovil, telefonoHabitacion, telefonoFamiliar, correoElectronico, rif, planillaSige, codigoPatria, serialPatria):
        self.cursor.execute('''
            INSERT INTO REPL (Nombre, Apellido, Cedula, FN, rpstIMG, Edad, EC, Nacionalidad, Afinidad,  Profesion, Ocupacion, EMPDT,  Direccion, TelefonoMovil, TelefonoHabitacion, TelefonoDFamiliar, CorreoElectronico, RIF, PlanillaSige, CodigoPatria, SerialPatria)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nombre, apellido, cedula, fecha_nacimiento, rpstIMG, edad, estado_civil, nacionalidad, afinidad, profesion, ocupacion, empresaDTrabaja, direccion, telefonoMovil, telefonoHabitacion, telefonoFamiliar, correoElectronico, rif, planillaSige, codigoPatria, serialPatria))
        self.connection.commit()
        return self.cursor.lastrowid

    ## Registro de Datos del Padre
    def insertDTP (self,  NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP,  ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP):
        self.cursor.execute('''
            INSERT INTO DTP (NombreP, ApellidoP, CedulaP, FNP, EdadP, TEDP, EMDTP, VCNP, CPNVCNP, DireccionP, TelefonoMovilP)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP,  ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP))
        self.connection.commit()
        return self.cursor.lastrowid

    ## Registro de Datos de la Madre
    def insertDTM (self, NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM):
        self.cursor.execute('''
            INSERT INTO DTM (NombreM, ApellidoM, CedulaM, FNM, EdadM, TEDM, EMDTM, VCNM, CPNVCNM, DireccionM, TelefonoMovilM)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM))
        self.connection.commit()
        return self.cursor.lastrowid

    ## Actualizar claves foráneas del estudiante
    def updateEstudendForeignKeys(self, estudiante_id, representante_id, padre_id, madre_id):
        """Actualiza las claves foráneas de un estudiante para vincularlo con su representante, padre y madre."""
        self.cursor.execute('''
            UPDATE Estudend 
            SET IDRPL = ?, IDP = ?, IDM = ?
            WHERE IDEST = ?
        ''', (representante_id, padre_id, madre_id, estudiante_id))
        self.connection.commit()

    # -----------------------------------
    # Métodos de Modificaciones
    # -----------------------------------

    ## Modificación de Estudiante
    def ModifyEstudend (self, Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Nacionalidad, Estado, Municipio, Direccion_Actual, Punto_de_Referencia, Altura, Peso, Talla_Zapatos, Talla_Camisa, Talla_Pantalon, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Correo_Electronico, Telefono_de_Habitacion, estIMG,  Carton_Vacunas, Tipo_de_Sangre, Examen_de_Heces):
        self.cursor.execute('''
            UPDATE Estudend SET Nombre=?, Apellido=?, CedulaEscolar=?, Edad=?, Genero=?, FN=?, Lateralidad=?, Nacionalidad=?, Estado=?, Municipio=?, DA=?, PTR=?, Altura=?, Peso=?, Zapatos=?, Camisa=?, Pantalon=?, NDH=?, APRN=?, AlergicoA=?, AlgunaDificultad=?, EspecifiqueDificultad=?, CorreoElectronico=?, TelefonoHabitacion=?, estIMG=?, CartonVacunas=?, TipodeSangre=?, EDH=? WHERE CedulaEscolar=?
        ''', (Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Nacionalidad, Estado, Municipio, Direccion_Actual, Punto_de_Referencia, Altura, Peso, Talla_Zapatos, Talla_Camisa, Talla_Pantalon, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Correo_Electronico, Telefono_de_Habitacion, estIMG, Carton_Vacunas, Tipo_de_Sangre, Examen_de_Heces))
        self.connection.commit()

    ## Modificación de Representante
    def ModifyRpl (self, nombre, apellido, cedula, fecha_nacimiento, rpstIMG, edad, estado_civil, nacionalidad, afinidad, profesion, ocupacion, empresaDTrabaja, direccion, telefonoMovil, telefonoHabitacion, telefonoFamiliar, correoElectronico, rif, planillaSige, codigoPatria, serialPatria):
        self.cursor.execute('''
            UPDATE REPL SET Nombre=?, Apellido=?, Cedula=?, FN=?, rpstIMG=?, Edad=?, EC=?, Nacionalidad=?, Afinidad=?, Profesion=?, Ocupacion=?, EMPDT=?, Direccion=?, TelefonoMovil=?, TelefonoHabitacion=?, TelefonoDFamiliar=?, CorreoElectronico=?, RIF=?, PlanillaSige=?, CodigoPatria=?, SerialPatria=? WHERE Cedula=?
        ''', (nombre, apellido, cedula, fecha_nacimiento, rpstIMG, edad, estado_civil, nacionalidad, afinidad, profesion, ocupacion, empresaDTrabaja, direccion, telefonoMovil, telefonoHabitacion, telefonoFamiliar, correoElectronico, rif, planillaSige, codigoPatria, serialPatria, cedula))
        self.connection.commit()

    ## Modificación de Datos de la Madre
    def ModifyDTM (self, NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM):
        self.cursor.execute('''
            UPDATE DTM SET NombreM=?, ApellidoM=?, CedulaM=?, FNM=?, EdadM=?, TEDM=?, EMDTM=?, VCNM=?, CPNVCNM=?, DireccionM=?, TelefonoMovilM=? WHERE CedulaM=?
        ''', (NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM, CedulaM))
        self.connection.commit()

    ## Modificación de Datos del Padre
    def ModifyDTP (self, NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP, ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP):
        self.cursor.execute('''
            UPDATE DTP SET NombreP=?, ApellidoP=?, CedulaP=?, FNP=?, EdadP=?, TEP=?, EMPDTP=?, VCNTP=?, CPNVCNT=?, DireccionP=?, TelefonoMovilP=? WHERE CedulaP=?
        ''', (NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP, ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP, CedulaP))
        self.connection.commit()

    # -----------------------------------
    # Métodos de Consultas
    # -----------------------------------

    ## Consulta de Estudiante
    def SelectEstudend(self):
        self.cursor.execute('''
          SELECT * FROM Estudend
        ''')
        return self.cursor.fetchall()

    def obtener_datos_por_cedula(self, cedula):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Obtener datos del estudiante
        cursor.execute("""
            SELECT *
            FROM Estudend WHERE TRIM(CedulaEscolar)=?
        """, (cedula.strip(),))
        estudiante = cursor.fetchone()
        
        if not estudiante:
            conn.close()
            return None
            
        # Obtener datos del representante (asumiendo que hay una relación por cédula)
        cursor.execute("""
            SELECT *
            FROM REPL WHERE TRIM(Cedula)=?
        """, (cedula.strip(),))
        representante = cursor.fetchone()
        
        # Obtener datos del padre (asumiendo que hay una relación por cédula)
        cursor.execute("""
            SELECT *
            FROM DTP WHERE TRIM(CedulaP)=?
        """, (cedula.strip(),))
        padre = cursor.fetchone()
        
        # Obtener datos de la madre (asumiendo que hay una relación por cédula)
        cursor.execute("""
            SELECT *
            FROM DTM WHERE TRIM(CedulaM)=?
        """, (cedula.strip(),))
        madre = cursor.fetchone()
        
        conn.close()
        
        # Crear diccionario con todos los datos
        datos = {}
        
        # Datos del estudiante (primeros 28 campos)
        if estudiante:
            estudiante_keys = [
                'id', 'NombreS', 'apellido', 'cedulaEscolar', 'edad', 'genero', 'fechaNacimiento', 
                'lateralidad', 'nacionalidad', 'estado', 'municipio', 'direccionActual', 'puntoDReferencia', 
                'altura', 'peso', 'tallaZapatos', 'tallaCamisa', 'tallaPantalon', 'numeroDHermanos', 
                'autorizadoPRetirarANiño', 'alergicoA', 'algunaDificultad', 'especificarDificultad', 
                'correoElectronico', 'telefonoDHabitacion', 'estIMG', 'cartonVacunas', 'tipoDSangre', 'examenDHeces', 'observaciones'
            ]
            for i, key in enumerate(estudiante_keys):
                if i < len(estudiante):
                    datos[key] = estudiante[i]
        
        # Datos del representante
        if representante:
            representante_keys = [
                'idR', 'nombreR', 'apellidoR', 'cedulaR', 'fechaNacimientoR', 'rpstIMG', 'edadR', 'estadoCivilR', 
                'nacionalidadR', 'afinidad', 'profesionR', 'ocupacionR', 'empresaDTrabajaR', 'direccionR', 
                'telefonoMovilR', 'telefonoHabitacionR', 'telefonoFamiliarR', 'correoElectronicoR', 
                'rifR', 'planillaSigeR', 'codigoPatriaR', 'serialPatriaR'
            ]
            for i, key in enumerate(representante_keys):
                if i < len(representante):
                    datos[key] = representante[i]
        
        # Datos del padre
        if padre:
            padre_keys = [
                'idP', 'nombreP', 'apellidoP', 'cedulaP', 'fechaNacimientoP', 'edadP', 'tipoEmpleoP', 
                'empresaDTrabajaP', 'viveConNinoP', 'causaPNoViveP', 'direccionP', 'telefonoMovilP'
            ]
            for i, key in enumerate(padre_keys):
                if i < len(padre):
                    datos[key] = padre[i]
        
        # Datos de la madre
        if madre:
            madre_keys = [
                'idM', 'nombreM', 'apellidoM', 'cedulaM', 'fechaNacimientoM', 'edadM', 'tipoEmpleoM', 
                'empresaDTrabajaM', 'viveConNinoM', 'causaPNoViveM', 'direccionM', 'telefonoMovilM'
            ]
            for i, key in enumerate(madre_keys):
                if i < len(madre):
                    datos[key] = madre[i]
        
        return datos

    # -----------------------------------
    # Métodos de Estadísticas para Dashboard
    # -----------------------------------

    ## Contar estudiantes registrados
    def count_estudiantes(self):
        """Retorna el número total de estudiantes registrados."""
        try:
            self.cursor.execute("SELECT COUNT(*) FROM Estudend")
            return self.cursor.fetchone()[0]
        except:
            return 0

    ## Contar representantes registrados
    def count_representantes(self):
        """Retorna el número total de representantes registrados."""
        try:
            self.cursor.execute("SELECT COUNT(*) FROM REPL")
            return self.cursor.fetchone()[0]
        except:
            return 0

    ## Contar padres registrados
    def count_padres(self):
        """Retorna el número total de padres registrados."""
        try:
            self.cursor.execute("SELECT COUNT(*) FROM DTP")
            return self.cursor.fetchone()[0]
        except:
            return 0

    ## Contar madres registradas
    def count_madres(self):
        """Retorna el número total de madres registradas."""
        try:
            self.cursor.execute("SELECT COUNT(*) FROM DTM")
            return self.cursor.fetchone()[0]
        except:
            return 0

    ## Obtener todas las estadísticas
    def get_dashboard_stats(self):
        """Retorna un diccionario con todas las estadísticas del dashboard."""
        return {
            'estudiantes': self.count_estudiantes(),
            'representantes': self.count_representantes(),
            'padres': self.count_padres(),
            'madres': self.count_madres()
        }