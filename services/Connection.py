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
    def insertEstudend(self, Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Nacionalidad, Estado, Municipio, Direccion_Actual, Punto_de_Referencia, Altura, Peso, Talla_Zapatos, Talla_Camisa, Talla_Pantalon, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Correo_Electronico, Telefono_de_Habitacion, estIMG, Carton_Vacunas, Tipo_de_Sangre, Examen_de_Heces, observaciones, grado, turno):
        self.cursor.execute('''
            INSERT INTO Estudend (Nombre, Apellido, CedulaEscolar, Edad, Genero, FN, Lateralidad,  Nacionalidad, Estado, Municipio, DA, PTR, Altura, Peso, Zapatos, Camisa, Pantalon, NDH, APRN, AlergicoA, AlgunaDificultad, EspecifiqueDificultad, CorreoElectronico, TelefonoHabitacion, estIMG, CartonVacunas, TipodeSangre, EDH, observaciones, grado, turno)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Nacionalidad, Estado, Municipio, Direccion_Actual, Punto_de_Referencia, Altura, Peso, Talla_Zapatos, Talla_Camisa, Talla_Pantalon, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Correo_Electronico, Telefono_de_Habitacion, estIMG, Carton_Vacunas, Tipo_de_Sangre, Examen_de_Heces, observaciones, grado, turno))
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
    def ModifyEstudend (self, Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Nacionalidad, Estado, Municipio, Direccion_Actual, Punto_de_Referencia, Altura, Peso, Talla_Zapatos, Talla_Camisa, Talla_Pantalon, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Correo_Electronico, Telefono_de_Habitacion, estIMG, Carton_Vacunas, Tipo_de_Sangre, Examen_de_Heces, observaciones, grado, turno):
        self.cursor.execute('''
    UPDATE Estudend SET Nombre=?, Apellido=?, CedulaEscolar=?, Edad=?, Genero=?, FN=?, Lateralidad=?, Nacionalidad=?, Estado=?, Municipio=?, DA=?, PTR=?, Altura=?, Peso=?, Zapatos=?, Camisa=?, Pantalon=?, NDH=?, APRN=?, AlergicoA=?, AlgunaDificultad=?, EspecifiqueDificultad=?, CorreoElectronico=?, TelefonoHabitacion=?, estIMG=?, CartonVacunas=?, TipodeSangre=?, EDH=?, observaciones=?, grado=?, turno=? WHERE CedulaEscolar=?
    ''', (Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Nacionalidad, Estado, Municipio, Direccion_Actual, Punto_de_Referencia, Altura, Peso, Talla_Zapatos, Talla_Camisa, Talla_Pantalon, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Correo_Electronico, Telefono_de_Habitacion, estIMG, Carton_Vacunas, Tipo_de_Sangre, Examen_de_Heces, observaciones, grado, turno, Cedula_Escolar))
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
            UPDATE DTP SET NombreP=?, ApellidoP=?, CedulaP=?, FNP=?, EdadP=?, TEDP=?, EMDTP=?, VCNP=?, CPNVCNP=?, DireccionP=?, TelefonoMovilP=? WHERE CedulaP=?
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
        return self.cursor.fetchall() # Considera usar fetchone() si solo esperas un resultado

    def obtener_datos_por_cedula(self, cedula):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Obtener datos del estudiante
        cursor.execute("SELECT * FROM Estudend WHERE TRIM(CedulaEscolar)=?", (cedula.strip(),))
        estudiante = cursor.fetchone()
        
        if not estudiante:
            conn.close()
            return None

        # Obtener IDs de la familia desde el registro del estudiante
        # Asumiendo que las FKs están al final de la tabla Estudend
        # IDEST(0), ..., grado(30), turno(31), IDRPL(32), IDP(33), IDM(34)
        id_representante = estudiante[32] if len(estudiante) > 32 else None
        id_padre = estudiante[33] if len(estudiante) > 33 else None
        id_madre = estudiante[34] if len(estudiante) > 34 else None

        # Obtener datos del representante, padre y madre usando sus IDs
        cursor.execute("SELECT * FROM REPL WHERE IDRPL=?", (id_representante,))
        representante = cursor.fetchone()

        cursor.execute("SELECT * FROM DTP WHERE IDP=?", (id_padre,))
        padre = cursor.fetchone()

        cursor.execute("SELECT * FROM DTM WHERE IDM=?", (id_madre,))
        madre = cursor.fetchone()

        # Obtener datos del padre (asumiendo que hay una relación por cédula)
        conn.close()
        
        # Crear diccionario con todos los datos
        datos = {}
        
        # Datos del estudiante (primeros 28 campos)
        if estudiante:
            estudiante_keys = [ # Asegúrate que el orden y cantidad coincida con tu tabla
                'IDEST', 'NombreS', 'apellido', 'cedulaEscolar', 'edad', 'genero', 'FN', 'lateralidad',
                'nacionalidad', 'estado', 'municipio', 'DA', 'PTR', 'altura', 'peso', 'Zapatos',
                'Camisa', 'Pantalon', 'NDH', 'APRN', 'alergicoA', 'algunaDificultad',
                'especificarDificultad', 'correoElectronico', 'telefonoHabitacion', 'estIMG',
                'cartonVacunas', 'tipoDSangre',
                'EDH', 'observaciones', 'grado', 'turno'
            ]
            for i, key in enumerate(estudiante_keys):
                if i < len(estudiante):
                    datos[key] = estudiante[i]
        
        # Datos del representante
        if representante:
            representante_keys = [ # Asegúrate que el orden y cantidad coincida con tu tabla
                'IDRPL', 'nombreR', 'apellidoR', 'cedulaR', 'FN', 'rpstIMG', 'edadR', 'EC',
                'nacionalidadR', 'afinidad', 'profesionR', 'ocupacionR', 'EMPDT', 'direccionR', 'telefonoMovilR',
                'telefonoHabitacionR', 'telefonoDFamiliar', 'correoElectronicoR', 'RIF', 'planillaSigeR',
                'codigoPatriaR', 'serialPatriaR'
            ]
            for i, key in enumerate(representante_keys):
                if i < len(representante):
                    datos[key] = representante[i]
        
        # Datos del padre
        if padre:
            padre_keys = [ # Asegúrate que el orden y cantidad coincida con tu tabla
                'IDP', 'nombreP', 'apellidoP', 'cedulaP', 'FNP', 'edadP', 'TEDP',
                'EMDTP', 'VCNP', 'CPNVCNP', 'direccionP', 'telefonoMovilP'
            ]
            for i, key in enumerate(padre_keys):
                if i < len(padre):
                    datos[key] = padre[i]
        
        # Datos de la madre
        if madre:
            madre_keys = [
                'IDM', 'nombreM', 'apellidoM', 'cedulaM', 'FNM', 'edadM', 'TEDM',
                'EMDTM', 'VCNM', 'CPNVCNM', 'direccionM', 'telefonoMovilM'
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

    # -----------------------------------
    # Métodos de Eliminación
    # -----------------------------------

    def delete_student_full(self, id_estudiante, id_representante, id_padre, id_madre):
        """
        Elimina un estudiante y sus familiares asociados (representante, padre, madre).
        El orden de eliminación es importante para evitar problemas de claves foráneas.
        """
        try:
            # 1. Eliminar el estudiante. Esto rompe la relación.
            if id_estudiante:
                self.cursor.execute("DELETE FROM Estudend WHERE IDEST = ?", (id_estudiante,))

            # 2. Eliminar los familiares asociados.
            if id_representante:
                self.cursor.execute("DELETE FROM REPL WHERE IDRPL = ?", (id_representante,))
            if id_padre:
                self.cursor.execute("DELETE FROM DTP WHERE IDP = ?", (id_padre,))
            if id_madre:
                self.cursor.execute("DELETE FROM DTM WHERE IDM = ?", (id_madre,))

            self.connection.commit()
            return True, "Registro eliminado exitosamente."
        except Exception as e:
            self.connection.rollback()
            return False, f"Error al eliminar el registro: {e}"