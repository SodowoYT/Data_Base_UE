from PySide6.QtWidgets import (
    QPushButton, QMainWindow, QVBoxLayout, QWidget, QTableView, QLineEdit,
    QMessageBox, QHBoxLayout, QDialog, QLabel, QScrollArea, QFormLayout, QFileDialog, QApplication,
    QHeaderView, QGroupBox
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
    c.drawString(250, y, f"Apellidos: {datos.get('apellido', '') or ''}")
    c.drawString(450, y, f"Cédula Escolar: {datos.get('cedulaEscolar', '') or ''}")
    y -= 14
    c.drawString(45, y, f"F.N.: {datos.get('fechaNacimiento', '') or ''}")
    c.drawString(120, y, f"Edad: {datos.get('edad', '') or ''}")
    c.drawString(180, y, f"Género: {datos.get('genero', '') or ''}")
    c.drawString(250, y, f"Lateralidad: {datos.get('lateralidad', '') or ''}")
    c.drawString(350, y, f"Nacionalidad: {datos.get('nacionalidad', '') or ''}")
    c.drawString(470, y, f"Estado: {datos.get('estado', '') or ''}")
    y -= 14
    c.drawString(45, y, f"Municipio: {datos.get('municipio', '') or ''}")
    c.drawString(200, y, f"Dirección Actual: {datos.get('direccionActual', '') or ''}")
    y -= 14
    c.drawString(45, y, f"Punto de Referencia: {datos.get('puntoDReferencia', '') or ''}")
    y -= 14
    c.drawString(45, y, f"Altura: {datos.get('altura', '') or ''}")
    c.drawString(120, y, f"Peso: {datos.get('peso', '') or ''}")
    c.drawString(180, y, f"Zapatos: {datos.get('tallaZapatos', '') or ''}")
    c.drawString(250, y, f"Camisa: {datos.get('tallaCamisa', '') or ''}")
    c.drawString(320, y, f"Pantalón: {datos.get('tallaPantalon', '') or ''}")
    c.drawString(400, y, f"N° de Hermanos: {datos.get('numeroDHermanos', '') or ''}")
    y -= 14
    c.drawString(45, y, f"Autorizado para retirar al niño(a): {datos.get('autorizadoPRetirarANiño', '') or ''}")
    c.drawString(250, y, f"Alérgico a: {datos.get('alergicoA', '') or ''}")
    y -= 14
    c.drawString(45, y, f"Alguna Dificultad: {datos.get('algunaDificultad', '') or ''}")
    c.drawString(200, y, f"Especifique: {datos.get('especificarDificultad', '') or ''}")
    y -= 14
    c.drawString(45, y, f"Correo Electrónico: {datos.get('correoElectronico', '') or ''}")
    c.drawString(250, y, f"Teléfono de Habitación: {datos.get('telefonoDHabitacion', '') or ''}")
    y -= 14
    c.drawString(45, y, f"Cartón de Vacunas: {'Presentado' if datos.get('cartonVacunas') else 'No presentado'}")
    c.drawString(200, y, f"Tipo de Sangre: {datos.get('tipoDSangre', '') or ''}")
    c.drawString(320, y, f"Examen de Heces: {datos.get('examenDHeces', '') or ''}")

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
    c.drawString(45, y, f"Nombre y Apellido: {datos.get('nombreR', '') or ''} {datos.get('apellidoR', '') or ''}")
    c.drawString(250, y, f"Cédula: {datos.get('cedulaR', '') or ''}")
    c.drawString(350, y, f"F.N.: {datos.get('fechaNacimientoR', '') or ''}")
    c.drawString(420, y, f"Edad: {datos.get('edadR', '') or ''}")
    y -= 14
    c.drawString(45, y, f"Estado Civil: {datos.get('estadoCivilR', '') or ''}")
    c.drawString(150, y, f"Nacionalidad: {datos.get('nacionalidadR', '') or ''}")
    c.drawString(250, y, f"Afinidad: {datos.get('afinidad', '') or ''}")
    c.drawString(350, y, f"Profesión: {datos.get('profesionR', '') or ''}")
    c.drawString(450, y, f"Ocupación: {datos.get('ocupacionR', '') or ''}")
    y -= 14
    c.drawString(45, y, f"Empresa donde Trabaja: {datos.get('empresaDTrabajaR', '') or ''}")
    c.drawString(250, y, f"Dirección: {datos.get('direccionR', '') or ''}")
    y -= 14
    c.drawString(45, y, f"Teléfono Móvil: {datos.get('telefonoMovilR', '') or ''}")
    c.drawString(200, y, f"Teléfono Habitación: {datos.get('telefonoHabitacionR', '') or ''}")
    c.drawString(350, y, f"Teléfono Familiar: {datos.get('telefonoFamiliarR', '') or ''}")
    y -= 14
    c.drawString(45, y, f"Correo Electrónico: {datos.get('correoElectronicoR', '') or ''}")
    c.drawString(250, y, f"Rif: {datos.get('rifR', '') or ''}")
    c.drawString(350, y, f"Planilla Sige: {datos.get('planillaSigeR', '') or ''}")
    y -= 14
    c.drawString(45, y, f"Código de la patria: {datos.get('codigoPatriaR', '') or ''}")
    c.drawString(200, y, f"Serial de la patria: {datos.get('serialPatriaR', '') or ''}")

    if y < 120:
        c.showPage()
        y = height - 80

    # --- Sección: Datos del Padre ---
    y -= 24
    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, y, "Datos del Padre:")
    y -= 18
    c.setFont("Helvetica", 9)
    c.drawString(45, y, f"Nombre y Apellido: {datos.get('nombreP', '') or ''} {datos.get('apellidoP', '') or ''}")
    c.drawString(250, y, f"Cédula: {datos.get('cedulaP', '') or ''}")
    c.drawString(350, y, f"F.N.: {datos.get('fechaNacimientoP', '') or ''}")
    c.drawString(420, y, f"Edad: {datos.get('edadP', '') or ''}")
    y -= 14
    c.drawString(45, y, f"Tipo de Empleo: {datos.get('tipoEmpleoP', '') or ''}")
    c.drawString(200, y, f"Empresa donde Trabaja: {datos.get('empresaDTrabajaP', '') or ''}")
    y -= 14
    c.drawString(45, y, f"¿Vive con el niño(a)?: {datos.get('viveConNinoP', '') or ''}")
    c.drawString(200, y, f"Causa: {datos.get('causaPNoViveP', '') or ''}")
    c.drawString(350, y, f"Dirección: {datos.get('direccionP', '') or ''}")
    c.drawString(500, y, f"Teléfono Móvil: {datos.get('telefonoMovilP', '') or ''}")

    if y < 120:
        c.showPage()
        y = height - 80

    # --- Sección: Datos de la Madre (si no es representante) ---
    y -= 24
    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, y, "Datos de la Madre en caso de no ser la Representante:")
    y -= 18
    c.setFont("Helvetica", 9)
    c.drawString(45, y, f"Nombre y Apellido: {datos.get('nombreM', '') or ''} {datos.get('apellidoM', '') or ''}")
    c.drawString(250, y, f"Cédula: {datos.get('cedulaM', '') or ''}")
    c.drawString(350, y, f"F.N.: {datos.get('fechaNacimientoM', '') or ''}")
    c.drawString(420, y, f"Edad: {datos.get('edadM', '') or ''}")
    y -= 14
    c.drawString(45, y, f"Tipo de Empleo: {datos.get('tipoEmpleoM', '') or ''}")
    c.drawString(200, y, f"Empresa donde Trabaja: {datos.get('empresaDTrabajaM', '') or ''}")
    y -= 14
    c.drawString(45, y, f"¿Vive con el niño(a)?: {datos.get('viveConNinoM', '') or ''}")
    c.drawString(200, y, f"Causa: {datos.get('causaPNoViveM', '') or ''}")
    c.drawString(350, y, f"Dirección: {datos.get('direccionM', '') or ''}")
    c.drawString(500, y, f"Teléfono Móvil: {datos.get('telefonoMovilM', '') or ''}")

    if y < 120:
        c.showPage()
        y = height - 80

    # --- Sección: Observaciones (dividir por salto de línea) ---
    y -= 30
    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, y, "OBSERVACIONES:")
    y -= 18
    c.setFont("Helvetica", 9)
    obs = (datos.get('observaciones', '') or '').split('\n')
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
        
        self.eliminar = QPushButton("Eliminar", self)
        self.eliminar.setStyleSheet(self.button_style())
        self.eliminar.clicked.connect(self.eliminarRegistro)  # Por implementar

        botones_layout.addStretch()
        botones_layout.addWidget(self.show_all_button)
        botones_layout.addWidget(self.print_pdf_button)
        botones_layout.addWidget(self.modificar)
        botones_layout.addWidget(self.eliminar)
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

        self.ventana_todos = VentanaTodos(self.database, cedula, parent=self)
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
        
    def eliminarRegistro(self):
        indexes = self.table_view.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.warning(self, "Advertencia", "Seleccione una fila para eliminar.")
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
    def __init__(self, database, cedula, parent=None):
        super().__init__(parent)
        self.bg_image = QPixmap("utilities/resources/imgs/bg/CsltBg.png")
        self.setStyleSheet("""
            QDialog {
                background-color: #0c3f67; /* Fallback color */
            }
            QGroupBox {
                background: rgba(0, 0, 0, 0.85 ); /* Fondo negro más oscuro y translúcido */
                border: 1px solid #0d7acf;
                border-radius: 8px;
                margin-top: 10px;
                font-weight: bold;
                padding-top: 25px; /* Espacio entre el título y el contenido */
            }
            QGroupBox::title {
                color: white;
                font-weight: bold;
                font-size: 16px;
                font-family: 'Segoe UI', Arial, sans-serif;
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 4px 10px;
                background-color: #1a237e;
                border-top-left-radius: 8px;
                border-bottom-right-radius: 8px;
            }
            QLabel {
                color: #e0e0e0; /* Un blanco más suave */
                font-size: 14px;
                font-weight: bold;
                background: transparent;
            }
            QLabel#valor {
                font-weight: bold;
                color: #ffffff;
            }
            QLabel#foto {
                border: 2px solid #c0d0e0;
                border-radius: 4px;
                background-color: transparent;
            }
            QLabel#titulo_principal {
                font-family: 'Georgia', serif;
                font-size: 28px;
                font-weight: bold;
                color: #fff;
                padding: 10px;
            }
            QPushButton {
                background-color: #0c3f67;
                color: white;
                border-radius: 8px;
                padding: 6px 12px;
                font-size: 14px;
            }
        """)
        
        # Obtener todos los datos usando el método mejorado
        self.datos = database.obtener_datos_por_cedula(cedula)
        
        nombre_estudiante = self.datos.get('NombreS', 'Desconocido') if self.datos else 'Desconocido'
        self.setWindowTitle(f"Detalles Completos de: {nombre_estudiante}")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.setGeometry(100, 100, 1100, 800) # Ventana más grande

        # Layout para botones de la ventana
        top_layout = QHBoxLayout()
        self.fullscreen_button = QPushButton("Pantalla Completa")
        self.fullscreen_button.clicked.connect(self.toggle_fullscreen)
        top_layout.addStretch()
        top_layout.addWidget(self.fullscreen_button, alignment=Qt.AlignTop | Qt.AlignRight)
        
        # Layout principal y área de scroll
        main_layout = QVBoxLayout(self)
        main_layout.addLayout(top_layout)

        # --- Título principal con logo ---
        title_area_layout = QHBoxLayout()
        title_area_layout.setAlignment(Qt.AlignCenter)
        title_area_layout.setContentsMargins(0, 10, 0, 10)

        # Logo
        logo_label = QLabel()
        logo_pixmap = QPixmap("utilities/resources/LogoBG.png").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(logo_pixmap)

        # Título
        title_label = QLabel("Detalles del Registro")
        title_label.setObjectName("titulo_principal")

        title_area_layout.addWidget(logo_label)
        title_area_layout.addSpacing(15)
        title_area_layout.addWidget(title_label)
        main_layout.addLayout(title_area_layout)

        scroll = QScrollArea(self)
        scroll.setStyleSheet("background: transparent; border: none;")
        scroll.setWidgetResizable(True)
        main_layout.addWidget(scroll)

        # Contenedor para todos los datos
        container_widget = QWidget()
        container_layout = QVBoxLayout(container_widget)
        scroll.setWidget(container_widget)

        if not self.datos:
            container_layout.addWidget(QLabel("No se encontraron datos para la cédula proporcionada."))
            return

        # --- SECCIÓN ESTUDIANTE ---
        self.crear_seccion_estudiante(container_layout, self.datos)

        # --- SECCIÓN REPRESENTANTE ---
        self.crear_seccion_representante(container_layout, self.datos)

        # --- SECCIÓN PADRE ---
        self.crear_seccion_padre(container_layout, self.datos)

        # --- SECCIÓN MADRE ---
        self.crear_seccion_madre(container_layout, self.datos)

    def crear_campo(self, layout, etiqueta, valor_key, datos, es_imagen=False):
        """Función auxiliar para crear un campo de etiqueta y valor."""
        valor = str(datos.get(valor_key, 'N/A'))
        etiqueta_label = QLabel(f"{etiqueta}:")
        valor_label = QLabel(valor)
        valor_label.setObjectName("valor")
        valor_label.setWordWrap(True)
        layout.addRow(etiqueta_label, valor_label)

    def paintEvent(self, event):
        painter = QPainter(self)
        if not self.bg_image.isNull():
            painter.drawPixmap(self.rect(), self.bg_image)

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
            self.fullscreen_button.setText("Pantalla Completa")
        else:
            self.showFullScreen()
            self.fullscreen_button.setText("Salir de Pantalla Completa")

    def crear_seccion_estudiante(self, parent_layout, datos):
        group_box = QGroupBox("Datos del Estudiante")
        layout = QHBoxLayout(group_box)
        
        form_layout = QFormLayout() # Layout para los campos de texto
        
        estudiante_keys = [
            ('ID', 'IDEST'), ('Nombre', 'NombreS'), ('Apellido', 'apellido'), ('Cédula Escolar', 'cedulaEscolar'),
            ('Edad', 'edad'), ('Género', 'genero'), ('Fecha Nacimiento', 'fechaNacimiento'), ('Lateralidad', 'lateralidad'),
            ('Nacionalidad', 'nacionalidad'), ('Estado', 'estado'), ('Municipio', 'municipio'), ('Dirección', 'direccionActual'),
            ('Punto de Referencia', 'puntoDReferencia'), ('Altura', 'altura'), ('Peso', 'peso'), ('Talla Zapatos', 'tallaZapatos'),
            ('Talla Camisa', 'tallaCamisa'), ('Talla Pantalón', 'tallaPantalon'), ('N° Hermanos', 'numeroDHermanos'),
            ('Autorizado para Retirar', 'autorizadoPRetirarANiño'), ('Alérgico a', 'alergicoA'), ('Alguna Dificultad', 'algunaDificultad'),
            ('Especificar Dificultad', 'especificarDificultad'), ('Correo', 'correoElectronico'),
            ('Teléfono Habitación', 'telefonoDHabitacion'), ('Tipo de Sangre', 'tipoDSangre'),
            ('Examen de Heces', 'examenDHeces'), ('Observaciones', 'observaciones')
        ]

        for etiqueta, clave in estudiante_keys:
            self.crear_campo(form_layout, etiqueta, clave, datos)

        # Layout para las imágenes
        fotos_layout = QVBoxLayout()
        fotos_layout.setAlignment(Qt.AlignTop)

        # Foto del Estudiante
        self.crear_campo_imagen(fotos_layout, "Foto del Estudiante", 'estIMG', datos)
        
        # Cartón de Vacunas
        self.crear_campo_imagen(fotos_layout, "Cartón de Vacunas", 'cartonVacunas', datos)
        
        layout.addLayout(form_layout, 3)
        layout.addLayout(fotos_layout, 1)
        parent_layout.addWidget(group_box)

    def crear_campo_imagen(self, layout, titulo, clave_datos, datos):
        """Función auxiliar para crear un campo de imagen con título."""
        # Título de la imagen
        titulo_label = QLabel(titulo) 
        titulo_label.setStyleSheet("font-weight: bold; color: white; font-size: 14px; margin-top: 10px;")
        titulo_label.setAlignment(Qt.AlignCenter)
        
        # Contenedor de la imagen
        foto_label = QLabel()
        foto_label.setObjectName("foto")
        foto_label.setFixedSize(150, 150)
        foto_label.setAlignment(Qt.AlignCenter)
        
        foto_data = datos.get(clave_datos)
        if foto_data:
            pixmap = QPixmap()
            pixmap.loadFromData(foto_data)
            foto_label.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            foto_label.setText("Sin Imagen")
        
        layout.addWidget(titulo_label)
        layout.addWidget(foto_label)

    def crear_seccion_representante(self, parent_layout, datos):
        group_box = QGroupBox("Datos del Representante Legal")
        layout = QHBoxLayout(group_box)

        form_layout = QFormLayout()
        
        representante_keys = [
            ('ID', 'IDRPL'), ('Nombre', 'nombreR'), ('Apellido', 'apellidoR'), ('Cédula', 'cedulaR'),
            ('Fecha Nacimiento', 'fechaNacimientoR'), ('Edad', 'edadR'), ('Estado Civil', 'estadoCivilR'),
            ('Nacionalidad', 'nacionalidadR'), ('Afinidad', 'afinidad'), ('Profesión', 'profesionR'),
            ('Ocupación', 'ocupacionR'), ('Empresa donde Trabaja', 'empresaDTrabajaR'), ('Dirección', 'direccionR'),
            ('Teléfono Móvil', 'telefonoMovilR'), ('Teléfono Habitación', 'telefonoHabitacionR'),
            ('Teléfono Familiar', 'telefonoFamiliarR'), ('Correo', 'correoElectronicoR'), ('RIF', 'rifR'),
            ('Planilla Sige', 'planillaSigeR'), ('Código Patria', 'codigoPatriaR'), ('Serial Patria', 'serialPatriaR')
        ]
        for etiqueta, clave in representante_keys:
            self.crear_campo(form_layout, etiqueta, clave, datos)

        # Layout para la imagen del representante
        foto_layout = QVBoxLayout()
        foto_layout.setAlignment(Qt.AlignTop)
        self.crear_campo_imagen(foto_layout, "Foto del Representante", 'rpstIMG', datos)

        layout.addLayout(form_layout, 3)
        layout.addLayout(foto_layout, 1)
        parent_layout.addWidget(group_box)

    def crear_seccion_padre(self, parent_layout, datos):
        group_box = QGroupBox("Datos del Padre")
        form_layout = QFormLayout(group_box)
        
        padre_keys = [
            ('ID', 'IDP'), ('Nombre', 'nombreP'), ('Apellido', 'apellidoP'), ('Cédula', 'cedulaP'),
            ('Fecha Nacimiento', 'fechaNacimientoP'), ('Edad', 'edadP'), ('Tipo de Empleo', 'tipoEmpleoP'),
            ('Empresa donde Trabaja', 'empresaDTrabajaP'), ('Vive con el niño(a)', 'viveConNinoP'),
            ('Causa si no vive', 'causaPNoViveP'), ('Dirección', 'direccionP'), ('Teléfono Móvil', 'telefonoMovilP')
        ]
        for etiqueta, clave in padre_keys:
            self.crear_campo(form_layout, etiqueta, clave, datos)
            
        parent_layout.addWidget(group_box)

    def crear_seccion_madre(self, parent_layout, datos):
        group_box = QGroupBox("Datos de la Madre")
        form_layout = QFormLayout(group_box)
        
        madre_keys = [
            ('ID', 'IDM'), ('Nombre', 'nombreM'), ('Apellido', 'apellidoM'), ('Cédula', 'cedulaM'),
            ('Fecha Nacimiento', 'fechaNacimientoM'), ('Edad', 'edadM'), ('Tipo de Empleo', 'tipoEmpleoM'),
            ('Empresa donde Trabaja', 'empresaDTrabajaM'), ('Vive con el niño(a)', 'viveConNinoM'),
            ('Causa si no vive', 'causaPNoViveM'), ('Dirección', 'direccionM'), ('Teléfono Móvil', 'telefonoMovilM')
        ]
        for etiqueta, clave in madre_keys:
            self.crear_campo(form_layout, etiqueta, clave, datos)
            
        parent_layout.addWidget(group_box)
