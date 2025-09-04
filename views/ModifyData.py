from PySide6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Qt

class ModifyData(QDialog):
    def __init__(self, database, cedula):
        super().__init__()
        self.setWindowTitle("Modificar datos del estudiante")
        self.setGeometry(200, 200, 700, 700)
        self.database = database
        self.cedula = cedula
        self.datos = self.database.obtener_datos_por_cedula(self.cedula)

        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        layout.addLayout(form_layout)

        # --- CAMPOS ESTUDIANTE ---
        self.fields = {}
        campos_estudiante = [
            ("Nombre", 'NombreS'),
            ("Apellido", 'apellido'),
            ("Cédula Escolar", 'cedulaEscolar'),
            ("Edad", 'edad'),
            ("Nacionalidad", 'nacionalidad'),
            ("Estado", 'estado'),
            ("Municipio", 'municipio'),
            ("Dirección", 'direccionActual'),
            ("Punto de Referencia", 'puntoDReferencia'),
            ("Altura", 'altura'),
            ("Peso", 'peso'),
            ("Talla Zapatos", 'tallaZapatos'),
            ("Talla Camisa", 'tallaCamisa'),
            ("Talla Pantalón", 'tallaPantalon'),
            ("N° Hermanos", 'numeroDHermanos'),
            ("Autorizado Retiro", 'autorizadoPRetirarANiño'),
            ("Alergias", 'alergicoA'),
            ("Dificultad", 'especificarDificultad'),
            ("Tipo Sangre", 'tipoDSangre'),
            ("Examen Heces", 'examenDHeces'),
            ("Correo", 'correoElectronico'),
            ("Teléfono Habitación", 'telefonoDHabitacion'),
            ("Observaciones", 'observaciones'),
        ]
        for label, key in campos_estudiante:
            line = QLineEdit(self)
            line.setText(str(self.datos.get(key, '')))
            self.fields[key] = line
            form_layout.addRow(label, line)

        # --- CAMPOS REPRESENTANTE ---
        campos_representante = [
            ("Nombre Rep.", 'nombreR'),
            ("Apellido Rep.", 'apellidoR'),
            ("Edad Rep.", 'edadR'),
            ("Cédula Rep.", 'cedulaR'),
            ("Afinidad", 'afinidad'),
            ("RIF", 'rifR'),
            ("Teléfono Móvil Rep.", 'telefonoMovilR'),
            ("Teléfono Habitación Rep.", 'telefonoHabitacionR'),
            ("Correo Rep.", 'correoElectronicoR'),
            ("Teléfono Familiar Rep.", 'telefonoFamiliarR'),
            ("Nacionalidad Rep.", 'nacionalidadR'),
            ("Dirección Rep.", 'direccionR'),
            ("Código Patria", 'codigoPatriaR'),
            ("Serial Patria", 'serialPatriaR'),
            ("Profesión Rep.", 'profesionR'),
            ("Ocupación Rep.", 'ocupacionR'),
            ("Empresa Trabaja Rep.", 'empresaDTrabajaR'),
        ]
        for label, key in campos_representante:
            line = QLineEdit(self)
            line.setText(str(self.datos.get(key, '')))
            self.fields[key] = line
            form_layout.addRow(label, line)

        # --- CAMPOS PADRE ---
        campos_padre = [
            ("Nombre Padre", 'nombreP'),
            ("Apellido Padre", 'apellidoP'),
            ("Edad Padre", 'edadP'),
            ("Cédula Padre", 'cedulaP'),
            ("Causa No Vive Padre", 'causaPNoViveP'),
            ("Teléfono Móvil Padre", 'telefonoMovilP'),
            ("Dirección Padre", 'direccionP'),
            ("Empresa Trabaja Padre", 'empresaDTrabajaP'),
            ("Tipo Empleo Padre", 'tipoEmpleoqDesempeñaP'),
        ]
        for label, key in campos_padre:
            line = QLineEdit(self)
            line.setText(str(self.datos.get(key, '')))
            self.fields[key] = line
            form_layout.addRow(label, line)

        # --- CAMPOS MADRE ---
        campos_madre = [
            ("Nombre Madre", 'nombreM'),
            ("Apellido Madre", 'apellidoM'),
            ("Edad Madre", 'edadM'),
            ("Cédula Madre", 'cedulaM'),
            ("Causa No Vive Madre", 'causaPNoViveM'),
            ("Teléfono Móvil Madre", 'telefonoMovilM'),
            ("Dirección Madre", 'direccionM'),
            ("Empresa Trabaja Madre", 'empresaDTrabajaM'),
            ("Tipo Empleo Madre", 'tipoEmpleoqDesempeñaM'),
        ]
        for label, key in campos_madre:
            line = QLineEdit(self)
            line.setText(str(self.datos.get(key, '')))
            self.fields[key] = line
            form_layout.addRow(label, line)

        # --- BOTÓN GUARDAR ---
        self.save_button = QPushButton("Guardar cambios", self)
        self.save_button.clicked.connect(self.guardar_cambios)
        layout.addWidget(self.save_button)

    def guardar_cambios(self):
        # Recoge los datos editados
        datos_editados = {k: v.text() for k, v in self.fields.items()}
        # Actualiza solo los datos del estudiante (puedes extender para padres y representante)
        try:
            self.database.ModifyEstudend(
                datos_editados['NombreS'], datos_editados['apellido'], datos_editados['cedulaEscolar'],
                datos_editados['edad'], '', '', '', datos_editados['nacionalidad'], datos_editados['estado'], datos_editados['municipio'],
                datos_editados['direccionActual'], datos_editados['puntoDReferencia'], datos_editados['altura'], datos_editados['peso'],
                datos_editados['tallaZapatos'], datos_editados['tallaCamisa'], datos_editados['tallaPantalon'], datos_editados['numeroDHermanos'],
                datos_editados['autorizadoPRetirarANiño'], datos_editados['alergicoA'], '', datos_editados['especificarDificultad'],
                datos_editados['correoElectronico'], datos_editados['telefonoDHabitacion'], '', datos_editados['tipoDSangre'], datos_editados['examenDHeces']
            )
            # Actualiza representante
            self.database.ModifyRpl(
                datos_editados['nombreR'], datos_editados['apellidoR'], datos_editados['cedulaR'], '', datos_editados['edadR'], '', datos_editados['nacionalidadR'], datos_editados['afinidad'], datos_editados['profesionR'], datos_editados['ocupacionR'], datos_editados['empresaDTrabajaR'], datos_editados['direccionR'], datos_editados['telefonoMovilR'], datos_editados['telefonoHabitacionR'], datos_editados['telefonoFamiliarR'], datos_editados['correoElectronicoR'], datos_editados['rifR'], '', datos_editados['codigoPatriaR'], datos_editados['serialPatriaR']
            )
            # Actualiza padre
            self.database.ModifyDTP(
                datos_editados['nombreP'], datos_editados['apellidoP'], datos_editados['cedulaP'], '', datos_editados['edadP'], datos_editados['tipoEmpleoqDesempeñaP'], datos_editados['empresaDTrabajaP'], '', datos_editados['causaPNoViveP'], datos_editados['direccionP'], datos_editados['telefonoMovilP']
            )
            # Actualiza madre
            self.database.ModifyDTM(
                datos_editados['nombreM'], datos_editados['apellidoM'], datos_editados['cedulaM'], '', datos_editados['edadM'], datos_editados['tipoEmpleoqDesempeñaM'], datos_editados['empresaDTrabajaM'], '', datos_editados['causaPNoViveM'], datos_editados['direccionM'], datos_editados['telefonoMovilM']
            )
            QMessageBox.information(self, "Éxito", "Datos modificados correctamente.")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar: {e}")
