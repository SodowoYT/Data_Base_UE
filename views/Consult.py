from PySide6.QtWidgets import (
    QPushButton, QMainWindow, QVBoxLayout, QWidget, QTableView, QLineEdit,
    QMessageBox, QHBoxLayout, QDialog, QLabel, QScrollArea, QFormLayout, QFileDialog,
    QHeaderView
)
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap, QIcon, QPainter
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtCore import Qt
import os

from services.Connection import database
from views.Modify import ModifyData

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors  # Asegurarse de importar colors
from reportlab.lib import colors
import tempfile

def generar_planilla_inscripcion_pdf(
    file_path,
    datos,
    logo1_path="utilities/resources/LgAERJ.png",
    logo2_path="utilities/resources/LogoBG.png"
):
    print("Entrando a generar_planilla_inscripcion_pdf")
    print("Datos recibidos:", datos)
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # --- Cabecera con logos y título ---
    try:
        c.drawImage(logo1_path, 40, height-90, width=70, height=70, preserveAspectRatio=True, mask='auto')
    except Exception as e:
        print("Error dibujando logo1:", e)
    try:
        c.drawImage(logo2_path, width-110, height-90, width=70, height=70, preserveAspectRatio=True, mask='auto')
    except Exception as e:
        print("Error dibujando logo2:", e)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, height-50, "PLANILLA DE INSCRIPCIÓN")
    c.setFont("Helvetica-BoldOblique", 12)
    c.drawCentredString(width/2, height-70, "EDUCACIÓN INICIAL")

    # --- Cuadros para fotos ---
    c.rect(130, height-110, 60, 60)  # Foto izquierda
    c.rect(width-190, height-110, 60, 60)  # Foto derecha

    # --- Sección: Datos del Niño(a) ---
    y = height-130
    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, y, "Datos del Niño(a):")
    y -= 18
    c.setFont("Helvetica", 9)
    c.drawString(45, y, f"Nombres: {datos.get('NombreS', '')}")
    c.drawString(250, y, f"Apellidos: {datos.get('apellido', '')}")
    c.drawString(450, y, f"Cédula Escolar: {datos.get('cedulaEscolar', '')}")
    y -= 14
    c.drawString(45, y, f"F.N.: {datos.get('fechaNacimiento', '')}")
    c.drawString(120, y, f"Edad: {datos.get('edad', '')}")
    c.drawString(180, y, f"Género: {datos.get('genero', '')}")
    c.drawString(250, y, f"Lateralidad: {datos.get('lateralidad', '')}")
    c.drawString(350, y, f"Nacionalidad: {datos.get('nacionalidad', '')}")
    c.drawString(470, y, f"Estado: {datos.get('estado', '')}")
    y -= 14
    c.drawString(45, y, f"Municipio: {datos.get('municipio', '')}")
    c.drawString(200, y, f"Dirección Actual: {datos.get('direccionActual', '')}")
    y -= 14
    c.drawString(45, y, f"Punto de Referencia: {datos.get('puntoDReferencia', '')}")
    y -= 14
    c.drawString(45, y, f"Altura: {datos.get('altura', '')}")
    c.drawString(120, y, f"Peso: {datos.get('peso', '')}")
    c.drawString(180, y, f"Zapatos: {datos.get('tallaZapatos', '')}")
    c.drawString(250, y, f"Camisa: {datos.get('tallaCamisa', '')}")
    c.drawString(320, y, f"Pantalón: {datos.get('tallaPantalon', '')}")
    c.drawString(400, y, f"N° de Hermanos: {datos.get('numeroDHermanos', '')}")
    y -= 14
    c.drawString(45, y, f"Autorizado para retirar al niño(a): {datos.get('autorizadoPRetirarANiño', '')}")
    c.drawString(250, y, f"Alérgico a: {datos.get('alergicoA', '')}")
    y -= 14
    c.drawString(45, y, f"Alguna Dificultad: {datos.get('algunaDificultad', '')}")
    c.drawString(200, y, f"Especifique: {datos.get('especificarDificultad', '')}")
    y -= 14
    c.drawString(45, y, f"Correo Electrónico: {datos.get('correoElectronico', '')}")
    c.drawString(250, y, f"Teléfono de Habitación: {datos.get('telefonoDHabitacion', '')}")
    y -= 14
    c.drawString(45, y, f"Cartón de Vacunas: {datos.get('cartonVacunas', '')}")
    c.drawString(200, y, f"Tipo de Sangre: {datos.get('tipoDSangre', '')}")
    c.drawString(320, y, f"Examen de Heces: {datos.get('examenDHeces', '')}")

    # --- Salto de página si es necesario ---
    if y < 120:
        c.showPage()
        y = height - 80

    # --- Sección: Datos del Representante Legal ---
    y -= 24
    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, y, "Datos del Representante Legal:")
    y -= 18
    c.setFont("Helvetica", 9)
    c.drawString(45, y, f"Nombre y Apellido: {datos.get('nombreR', '')} {datos.get('apellidoR', '')}")
    c.drawString(250, y, f"Cédula: {datos.get('cedulaR', '')}")
    c.drawString(350, y, f"F.N.: {datos.get('fechaNacimientoR', '')}")
    c.drawString(420, y, f"Edad: {datos.get('edadR', '')}")
    y -= 14
    c.drawString(45, y, f"Estado Civil: {datos.get('estadoCivilR', '')}")
    c.drawString(150, y, f"Nacionalidad: {datos.get('nacionalidadR', '')}")
    c.drawString(250, y, f"Afinidad: {datos.get('afinidad', '')}")
    c.drawString(350, y, f"Profesión: {datos.get('profesionR', '')}")
    c.drawString(450, y, f"Ocupación: {datos.get('ocupacionR', '')}")
    y -= 14
    c.drawString(45, y, f"Empresa donde Trabaja: {datos.get('empresaDTrabajaR', '')}")
    c.drawString(250, y, f"Dirección: {datos.get('direccionR', '')}")
    y -= 14
    c.drawString(45, y, f"Teléfono Móvil: {datos.get('telefonoMovilR', '')}")
    c.drawString(200, y, f"Teléfono Habitación: {datos.get('telefonoHabitacionR', '')}")
    c.drawString(350, y, f"Teléfono Familiar: {datos.get('telefonoFamiliarR', '')}")
    y -= 14
    c.drawString(45, y, f"Correo Electrónico: {datos.get('correoElectronicoR', '')}")
    c.drawString(250, y, f"Rif: {datos.get('rifR', '')}")
    c.drawString(350, y, f"Planilla Sige: {datos.get('planillaSigeR', '')}")
    y -= 14
    c.drawString(45, y, f"Código de la patria: {datos.get('codigoPatriaR', '')}")
    c.drawString(200, y, f"Serial de la patria: {datos.get('serialPatriaR', '')}")

    if y < 120:
        c.showPage()
        y = height - 80

    # --- Sección: Datos del Padre ---
    y -= 24
    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, y, "Datos del Padre:")
    y -= 18
    c.setFont("Helvetica", 9)
    c.drawString(45, y, f"Nombre y Apellido: {datos.get('nombreP', '')} {datos.get('apellidoP', '')}")
    c.drawString(250, y, f"Cédula: {datos.get('cedulaP', '')}")
    c.drawString(350, y, f"F.N.: {datos.get('fechaNacimientoP', '')}")
    c.drawString(420, y, f"Edad: {datos.get('edadP', '')}")
    y -= 14
    c.drawString(45, y, f"Tipo de Empleo: {datos.get('tipoEmpleoP', '')}")
    c.drawString(200, y, f"Empresa donde Trabaja: {datos.get('empresaDTrabajaP', '')}")
    y -= 14
    c.drawString(45, y, f"¿Vive con el niño(a)?: {datos.get('viveConNinoP', '')}")
    c.drawString(200, y, f"Causa: {datos.get('causaPNoViveP', '')}")
    c.drawString(350, y, f"Dirección: {datos.get('direccionP', '')}")
    c.drawString(500, y, f"Teléfono Móvil: {datos.get('telefonoMovilP', '')}")

    if y < 120:
        c.showPage()
        y = height - 80

    # --- Sección: Datos de la Madre (si no es representante) ---
    y -= 24
    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, y, "Datos de la Madre en caso de no ser la Representante:")
    y -= 18
    c.setFont("Helvetica", 9)
    c.drawString(45, y, f"Nombre y Apellido: {datos.get('nombreM', '')} {datos.get('apellidoM', '')}")
    c.drawString(250, y, f"Cédula: {datos.get('cedulaM', '')}")
    c.drawString(350, y, f"F.N.: {datos.get('fechaNacimientoM', '')}")
    c.drawString(420, y, f"Edad: {datos.get('edadM', '')}")
    y -= 14
    c.drawString(45, y, f"Tipo de Empleo: {datos.get('tipoEmpleoM', '')}")
    c.drawString(200, y, f"Empresa donde Trabaja: {datos.get('empresaDTrabajaM', '')}")
    y -= 14
    c.drawString(45, y, f"¿Vive con el niño(a)?: {datos.get('viveConNinoM', '')}")
    c.drawString(200, y, f"Causa: {datos.get('causaPNoViveM', '')}")
    c.drawString(350, y, f"Dirección: {datos.get('direccionM', '')}")
    c.drawString(500, y, f"Teléfono Móvil: {datos.get('telefonoMovilM', '')}")

    if y < 120:
        c.showPage()
        y = height - 80

    # --- Sección: Observaciones (dividir por salto de línea) ---
    y -= 30
    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, y, "OBSERVACIONES:")
    y -= 18
    c.setFont("Helvetica", 9)
    obs = datos.get('observaciones', '').split('\n')
    c.drawString(45, y, f"I SALA: {obs[0] if len(obs) > 0 else ''}")
    y -= 14
    c.drawString(45, y, f"II SALA: {obs[1] if len(obs) > 1 else ''}")
    y -= 14
    c.drawString(45, y, f"III SALA: {obs[2] if len(obs) > 2 else ''}")

    # --- Compromiso ---
    y -= 30
    c.setFont("Helvetica", 8)
    c.drawString(45, y, "Los datos planteados en esta planilla son verdaderos, me comprometo a trabajar junto a la maestra colaborando con el material necesario para el bienestar y desarrollo de mi hijo(a) y de la institución.")

    # --- Firmas ---
    y -= 40
    c.setFont("Helvetica", 9)
    c.line(100, y, 250, y)
    c.drawString(130, y-12, "Firma del Representante")
    c.line(350, y, 500, y)
    c.drawString(400, y-12, "Firma del Docente")

    c.save()

# --- Clase para el fondo ---
class BgWidget(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image = QPixmap(image_path)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)  # Fondo ocupa toda la ventana


class ConsultWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consulta de Estudiantes")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.resize(900, 600)

        # --- Layout principal ---
        main_layout = QVBoxLayout()

        # --- HEADER con icono y título ---
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 5, 0, 15)

        icon_label = QLabel()
        icon_pixmap = QPixmap("utilities/resources/imgs/ico/IconApp.ico").scaled(
            40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        icon_label.setPixmap(icon_pixmap)

        title_label = QLabel("Consulta de Estudiantes")
        title_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 22px;
                font-weight: bold;
            }
        """)

        header_layout.addStretch()
        header_layout.addWidget(icon_label)
        header_layout.addSpacing(10)
        header_layout.addWidget(title_label)
        header_layout.addStretch()

        main_layout.addLayout(header_layout)

        # --- Buscador con estilo ---
        buscador_layout = QHBoxLayout()
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("🔍 Buscar por cédula escolar...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 8px;
                font-size: 14px;
                background: rgba(255,255,255,0.6); /* Más translúcido */
                color: black;
            }
        """)
        self.search_button = QPushButton("Buscar", self)
        self.search_button.setStyleSheet(self.button_style())
        self.search_button.clicked.connect(self.bpCI)
        
        # Botón de actualizar
        self.refresh_button = QPushButton("Actualizar", self)
        self.refresh_button.setStyleSheet(self.button_style())
        self.refresh_button.clicked.connect(self.actualizar_datos)
        
        buscador_layout.addWidget(self.search_input)
        buscador_layout.addWidget(self.search_button)
        buscador_layout.addWidget(self.refresh_button)
        main_layout.addLayout(buscador_layout)

        # --- Tabla con texto negro ---
        self.table_view = QTableView(self)
        self.table_view.setStyleSheet("""
            QTableView {
                background: rgba(255,255,255,0.50); /* Más translúcido */
                border: 1px solid #ccc;
                border-radius: 8px;
                gridline-color: #ccc;
                font-size: 13px;
                color: black;  /* TEXTO NEGRO */
            }
            QHeaderView::section {
                background: #0c3f67;
                color: white;
                padding: 5px;
                border: none;
                font-weight: bold;
            }
            QTableView::item:selected {
                background: #0d7acf;
                color: white;
            }
        """)
        main_layout.addWidget(self.table_view)

        # --- Botones inferiores ---
        botones_layout = QHBoxLayout()
        self.show_all_button = QPushButton("Ver detalles", self)
        self.show_all_button.setStyleSheet(self.button_style())
        self.show_all_button.clicked.connect(self.mostrarTodos)

        self.print_pdf_button = QPushButton("Imprimir PDF", self)
        self.print_pdf_button.setStyleSheet(self.button_style())
        self.print_pdf_button.clicked.connect(self.imprimir_pdf)

        self.modificar = QPushButton("Modificar", self)
        self.modificar.setStyleSheet(self.button_style())
        self.modificar.clicked.connect(self.modificarRegistro)  

        botones_layout.addStretch()
        botones_layout.addWidget(self.show_all_button)
        botones_layout.addWidget(self.print_pdf_button)
        botones_layout.addWidget(self.modificar)
        botones_layout.addStretch()

        main_layout.addLayout(botones_layout)

        # --- Contenedor con fondo ---
        self.bg_widget = BgWidget("utilities/resources/imgs/bg/CsltBg.png")  # Imagen de fondo
        self.bg_widget.setLayout(main_layout)
        self.setCentralWidget(self.bg_widget)

        # Instancia de la base de datos - crear nueva conexión
        self.database = None
        self.crear_conexion_bd()
        self.cargarDatos()

    def crear_conexion_bd(self):
        """Crea una nueva conexión a la base de datos."""
        try:
            print("Creando nueva conexion a la base de datos...")
            self.database = database("utilities\\db\\DataBaseUE.db")
            print("Conexion creada exitosamente")
        except Exception as e:
            print(f"Error creando conexion: {e}")
            QMessageBox.critical(self, "Error", f"Error conectando a la base de datos: {e}")

    def button_style(self):
        return """
            QPushButton {
                background-color: #0c3f67;
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0d7acf;
            }
        """

    # --- Método optimizado ---
    def cargarDatos(self, filtroCedula=None):
        print(f"Cargando datos... Filtro: {filtroCedula}")
        
        # Verificar que la conexión esté disponible
        if not self.database:
            print("Error: No hay conexion a la base de datos")
            QMessageBox.critical(self, "Error", "No hay conexión a la base de datos")
            return
        
        # Crear el modelo
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels([
            "ID", "Nombre", "Apellido", "Cédula Escolar", "Edad", "Género", "Fecha Nac."
        ])

        # Obtener datos de la BD
        try:
            data = self.database.SelectEstudend()
            print(f"Datos obtenidos de la BD: {len(data)} registros")
            
            # Debug: mostrar información del primer registro
            if data:
                print(f"Primer registro: {data[0]}")
                print(f"Tipo de datos en primer registro: {[type(col) for col in data[0]]}")
            
            if filtroCedula:
                data = [row for row in data if str(row[3]).strip() == filtroCedula]
                print(f"Despues del filtro: {len(data)} registros")

            if not data:
                print("ADVERTENCIA: No se encontraron registros para mostrar")
                QMessageBox.warning(self, "Advertencia", "No se encontraron registros.")
                self.table_view.setModel(model)
                return
        except Exception as e:
            print(f"Error obteniendo datos: {e}")
            import traceback
            traceback.print_exc()
            QMessageBox.critical(self, "Error", f"Error al cargar datos: {e}")
            return

        # Bloquear actualizaciones mientras se carga
        self.table_view.setUpdatesEnabled(False)

        for row in data:
            if len(row) < 8:
                continue
            
            # Procesar cada campo individualmente para manejar BLOB
            processed_row = []
            for i, col in enumerate(row[:7]):
                if i == 2 and isinstance(col, bytes):  # Campo Apellido (BLOB)
                    # Convertir BLOB a string
                    try:
                        col_str = col.decode('utf-8') if col else ""
                    except:
                        col_str = str(col) if col else ""
                else:
                    col_str = str(col) if col is not None else ""
                
                processed_row.append(QStandardItem(col_str))
            
            model.appendRow(processed_row)

        # Asignar el modelo una sola vez
        self.table_view.setModel(model)
        
        # Mostrar información de debug
        print(f"Tabla actualizada con {len(data)} registros")

        # Scroll fluido
        self.table_view.setHorizontalScrollMode(QTableView.ScrollPerPixel)
        self.table_view.setVerticalScrollMode(QTableView.ScrollPerPixel)

        # Anchos fijos de columnas (para evitar cálculos costosos)
        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)  # <-- cambio corregido
        self.table_view.setColumnWidth(0, 50)   # ID
        self.table_view.setColumnWidth(1, 120)  # Nombre
        self.table_view.setColumnWidth(2, 120)  # Apellido
        self.table_view.setColumnWidth(3, 120)  # Cédula Escolar

        # Reactivar actualizaciones
        self.table_view.setUpdatesEnabled(True)

        # Conectar selección
        self.table_view.selectionModel().selectionChanged.connect(self.on_selection_changed)

    def bpCI(self):
        cedula = self.search_input.text().strip()
        self.cargarDatos(filtroCedula=cedula)
    
    def actualizar_datos(self):
        """Actualiza los datos de la tabla refrescando la conexión."""
        print("Actualizando datos...")
        # Crear nueva conexión para asegurar datos actualizados
        self.crear_conexion_bd()
        # Recargar datos
        self.cargarDatos()
        print("Datos actualizados")

    def on_selection_changed(self, selected, deselected):
        indexes = self.table_view.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            nombre = self.table_view.model().index(row, 1).data()
            print(f"Seleccionado: {nombre}")

    def mostrarTodos(self):
        indexes = self.table_view.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.warning(self, "Advertencia", "Seleccione una fila.")
            return

        row = indexes[0].row()
        cedula = self.table_view.model().index(row, 3).data()  # La cédula está en la columna 3

        self.ventana_todos = VentanaTodos(self.database, cedula)
        self.ventana_todos.show()

    def imprimir_pdf(self):
        print("Entrando a imprimir_pdf")
        indexes = self.table_view.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.warning(self, "Advertencia", "Seleccione una fila para imprimir.")
            return

        row = indexes[0].row()
        cedula = self.table_view.model().index(row, 3).data()  # Columna de cédula
        cedula = str(cedula).strip()
        datos_completos = self.database.obtener_datos_por_cedula(cedula)
        print("DATOS PARA PDF:", datos_completos)
        if not datos_completos:
            QMessageBox.warning(self, "Advertencia", "No se encontraron datos completos para el estudiante.")
            return

        # Selección de archivo destino
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar PDF", f"Estudiante_{cedula}.pdf", "PDF Files (*.pdf)")
        if not file_path:
            return

        # Llamar a la función que genera la planilla con formato
        generar_planilla_inscripcion_pdf(file_path, datos_completos)
        QMessageBox.information(self, "PDF generado", f"El PDF se ha guardado en:\n{file_path}")

    def modificarRegistro(self):
        indexes = self.table_view.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.warning(self, "Advertencia", "Seleccione una fila para modificar.")
            return

        row = indexes[0].row()
        cedula = self.table_view.model().index(row, 3).data()  # Columna de cédula
        cedula = str(cedula).strip()  # Elimina espacios
        print("Cédula seleccionada para modificar:", cedula)
        # Consulta todos los datos del estudiante usando la cédula
        datos_completos = self.database.obtener_datos_por_cedula(cedula)
        print("Datos completos:", datos_completos)
        if not datos_completos:
            QMessageBox.warning(self, "Advertencia", "No se encontraron datos completos para el estudiante.")
            return
        # Abre la ventana de formulario editable
        self.Mreg_Window = ModifyData()
        self.Mreg_Window.cargar_datos_estudiante(self.database, cedula)
        self.Mreg_Window.show()

class ImagenGrandeDialog(QDialog):
    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Foto ampliada")
        self.setGeometry(200, 200, 600, 600)
        layout = QVBoxLayout(self)
        label = QLabel(self)
        label.setPixmap(pixmap.scaled(550, 550, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(label)
        self.setLayout(layout)

class VentanaTodos(QDialog):
    def __init__(self, database, cedula):
        super().__init__()
        self.setWindowTitle("Datos del estudiante seleccionado")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.setGeometry(150, 150, 600, 600)

        layout = QVBoxLayout()
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)

        content = QWidget()
        form_layout = QFormLayout(content)

        # Filtrar por la cédula recibida
        data = database.SelectEstudend()
        data = [row for row in data if str(row[3]).strip() == str(cedula)]

        headers = [
            "ID", "Nombre", "Apellido", "Cédula Escolar", "Edad", "Género", "Fecha Nac.",
            "Lateralidad", "Nacionalidad", "Estado", "Municipio", "Dirección", "Punto Ref.",
            "Altura", "Peso", "Zapatos", "Camisa", "Pantalón", "Hermanos", "Autorizado Retiro",
            "Alergias", "Dificultad", "Detalle Dificultad", "Correo", "Teléfono", "Vacunas",
            "Tipo Sangre", "Examen Heces"
        ]

        # Fondo oscuro y texto blanco en toda la ventana
        self.setStyleSheet("""
            QWidget {
                background-color: #0c3f67;
                color: white;
                font-size: 14px;
            }
            QLabel {
                color: white;
            }
        """)

        for row in data:
            encabezado = f"--- Estudiante: {row[1]} {row[2]} ({row[3]}) ---"
            encabezado_label = QLabel(f"<b>{encabezado}</b>")
            form_layout.addRow(encabezado_label, QLabel(""))

            for i, header in enumerate(headers):
                if i >= len(row):
                    break

                # CAMBIO: Mostrar BLOB como imagen y permitir click para ampliar
                if header == "Vacunas":
                    blob_data = row[i]
                    if blob_data:
                        pixmap_original = QPixmap()
                        pixmap_original.loadFromData(blob_data)
                        if not pixmap_original.isNull():
                            pixmap_preview = pixmap_original.scaledToWidth(200, Qt.SmoothTransformation)
                            foto_label = QLabel()
                            foto_label.setPixmap(pixmap_preview)
                            foto_label.setCursor(Qt.PointingHandCursor)
                            def mostrar_grande(event, pixmap=pixmap_original):
                                dlg = ImagenGrandeDialog(pixmap, self)
                                dlg.exec()
                            foto_label.mousePressEvent = mostrar_grande
                            form_layout.addRow(QLabel(f"<b>{header}:</b>"), foto_label)
                        else:
                            form_layout.addRow(QLabel(f"<b>{header}:</b>"), QLabel("Sin imagen"))
                    else:
                        form_layout.addRow(QLabel(f"<b>{header}:</b>"), QLabel("Sin imagen"))
                else:
                    form_layout.addRow(
                        QLabel(f"<b>{header}:</b>"),
                        QLabel(f"{str(row[i])}")
                    )

        content.setLayout(form_layout)
        scroll.setWidget(content)
        layout.addWidget(scroll)
        self.setLayout(layout)

