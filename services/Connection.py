import sqlite3
import os
import hashlib

class database:
    def __init__(self, db_name=None):
        # Mantener tu base existente
        self.db_path = db_name or "utilities\\db\\DataBaseUE.db"
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.__create_users_table()

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
    # Métodos que ya tenías (sin cambios)
    # -----------------------------------
    def insertEstudend(self, Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Nacionalidad, Estado, Municipio, Direccion_Actual, Punto_de_Referencia, Altura, Peso, Talla_Zapatos, Talla_Camisa, Talla_Pantalon, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Correo_Electronico, Telefono_de_Habitacion, Carton_Vacunas, Tipo_de_Sangre, Examen_de_Heces):
        self.cursor.execute('''
          INSERT INTO Estudend (Nombre, Apellido, CedulaEscolar, Edad, Genero, FN, Lateralidad,  Nacionalidad, Estado, Municipio, DA, PTR, Altura, Peso, Zapatos, Camisa, Pantalon, NDH, APRN, AlergicoA, AlgunaDificultad, EspecifiqueDificultad, CorreoElectronico, TelefonoHabitacion, CartonVacunas, TipodeSangre, EDH)
          VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (Nombre, Apellido, Cedula_Escolar, Edad, Genero, Fecha_de_Nacimiento, Lateralidad, Nacionalidad, Estado, Municipio, Direccion_Actual, Punto_de_Referencia, Altura, Peso, Talla_Zapatos, Talla_Camisa, Talla_Pantalon, Numero_de_Hermanos, Autorizado_para_Retirar_al_Niño, Alergico_a, Alguna_Dificultad, Especificar_Dificultad, Correo_Electronico, Telefono_de_Habitacion, Carton_Vacunas, Tipo_de_Sangre, Examen_de_Heces))
        self.connection.commit()

    def insertRpl(self, nombre, apellido, cedula, fecha_nacimiento, edad, estado_civil, nacionalidad, afinidad, profesion, ocupacion, empresaDTrabaja, direccion, telefonoMovil, telefonoHabitacion, telefonoFamiliar, correoElectronico, rif, planillaSige, codigoPatria, serialPatria):
        self.cursor.execute('''
          INSERT INTO REPL (Nombre, Apellido, Cedula, FN, Edad, EC, Nacionalidad, Afinidad,  Profesion, Ocupacion, EMPDT,  Direccion, TelefonoMovil, TelefonoHabitacion, TelefonoDFamiliar, CorreoElectronico, RIF, PlanillaSige, CodigoPatria, SerialPatria)
          VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nombre, apellido, cedula, fecha_nacimiento, edad, estado_civil, nacionalidad, afinidad, profesion, ocupacion, empresaDTrabaja, direccion, telefonoMovil, telefonoHabitacion, telefonoFamiliar, correoElectronico, rif, planillaSige, codigoPatria, serialPatria))
        self.connection.commit()

    def insertDTP (self,  NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP,  ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP):
        self.cursor.execute('''
          INSERT INTO DTP (NombreP, ApellidoP, CedulaP, FNP, EdadP, TEDP, EMDTP, VCNP, CPNVCNP, DireccionP, TelefonoMovilP)
          VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP,  ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP))
        self.connection.commit()

    def insertDTM (self, NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM):
        self.cursor.execute('''
          INSERT INTO DTM (NombreM, ApellidoM, CedulaM, FNM, EdadM, TEDM, EMDTM, VCNM, CPNVCNM, DireccionM, TelefonoMovilM)
          VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM))
        self.connection.commit()

    def SelectEstudend(self):
        self.cursor.execute('''
          SELECT * FROM Estudend
        ''')
        return self.cursor.fetchall()

  
