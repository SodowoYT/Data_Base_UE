from PySide6.QtWidgets import QPushButton, QMainWindow, QVBoxLayout, QWidget, QTableView, QLineEdit, QMessageBox, QHBoxLayout, QDialog, QLabel, QScrollArea, QFormLayout, QFileDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
from services.Connection import database
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtGui import QPainter
import os

class ConsultWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consulta de Estudiantes")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.layout = QVBoxLayout()

        # Buscador por cédula
        buscador_layout = QHBoxLayout()
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Buscar por cédula escolar...")
        self.search_button = QPushButton("Buscar", self)
        self.search_button.clicked.connect(self.bpCI)
        buscador_layout.addWidget(self.search_input)
        buscador_layout.addWidget(self.search_button)
        self.layout.addLayout(buscador_layout)

        self.table_view = QTableView(self)
        self.layout.addWidget(self.table_view)

        # Botón de Consulta (opcional, puedes quitarlo si ya cargas todo al abrir)
        # self.button1 = QPushButton("Consulta", self)
        # self.button1.clicked.connect(self.cargarDatos)
        # self.layout.addWidget(self.button1)
        
    
        self.show_all_button = QPushButton("Mostrar todos", self)
        self.show_all_button.clicked.connect(self.mostrarTodos)
        self.layout.addWidget(self.show_all_button)
    
        self.print_pdf_button = QPushButton("Imprimir PDF", self)
        self.print_pdf_button.clicked.connect(self.imprimir_pdf)
        self.layout.addWidget(self.print_pdf_button)
    
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # Instancia de la base de datos
        self.database = database("utilities\\db\\DataBaseUE.db")
        # Mostrar todos los datos al abrir la ventana
        self.cargarDatos()

    def cargarDatos(self, filtroCedula=None):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["IDEST", "Nombre", "Apellido", "Cedula Escolar", "Edad", "Genero", "FN", "Lateralidad", "Nacionalidad", "Estado", "Municipio", "DA", "PTR", "Altura", "Peso", "Zapatos", "Camisa", "Pantalon", "NDH", "APRN", "AlergicoA", "AlgunaDificultad", "EspecifiqueDificultad", "CorreoElectronico", "TelefonoHabitacion", "CartonVacunas", "TipodeSangre", "EDH"])

        data = self.database.SelectEstudend()
        if filtroCedula:
            data = [row for row in data if str(row[3]).strip() == filtroCedula]  # Filtrar por Cedula Escolar

        if not data:
            QMessageBox.warning(self, "Advertencia", "No se encontraron registros.")
            self.table_view.setModel(model)
            return

        for row in data:
            # Desempaquetar la fila
            if len(row) < 28:
                continue 
            model.appendRow([
            QStandardItem(str(row[0])), # ID
            QStandardItem(str(row[1])), # Nombre  
            QStandardItem(str(row[2])), # Apellido
            QStandardItem(str(row[3])), # Cedula Escolar
            QStandardItem(str(row[4])), # Edad
            QStandardItem(str(row[5])), # Genero
            QStandardItem(str(row[6])), # Fecha de Nacimiento
            QStandardItem(str(row[7])), # Lateralidad
            QStandardItem(str(row[8])), # Numero de Hermanos
            QStandardItem(str(row[9])), # Autorizado para Retirar al Niño
            QStandardItem(str(row[10])), # Correo Electronico
            QStandardItem(str(row[11])), # Telefono de Habitacion
            QStandardItem(str(row[12])), # Direccion Actual
            QStandardItem(str(row[13])), # Altura
            QStandardItem(str(row[14])), # Peso
            QStandardItem(str(row[15])), # Talla Camisa
            QStandardItem(str(row[16])), # Talla Pantalon
            QStandardItem(str(row[17])), # Talla Zapatos
            QStandardItem(str(row[18])), # Alergico a
            QStandardItem(str(row[19])), # Alguna Dificultad
            QStandardItem(str(row[20])), # Especificar Dificultad
            QStandardItem(str(row[21])), # Tipo de Sangre
            QStandardItem(str(row[22])), # Carton Vacunas
            QStandardItem(str(row[23])), # Examen de Heces
            QStandardItem(str(row[24])), # Nacionalidad
            QStandardItem(str(row[25])), # Estado
            QStandardItem(str(row[26])), # Municipio
            QStandardItem(str(row[27]))  # Punto de Referencia
            ])

        self.table_view.setModel(model)
        self.table_view.selectionModel().selectionChanged.connect(self.on_selection_changed)

    def bpCI (self):
        self.cedula = self.search.text().strip()
        self.cargarDatos(filtrocedula=self.cedula)

    def on_selection_changed(self, selected, deselected):
        indexes = self.table_view.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            nombre = self.table_view.model().index(row, 0).data()
            print(f"Seleccionado: {nombre}")

    def mostrarTodos(self):
            self.ventana_todos = VentanaTodos(self.database)
            self.ventana_todos.show()

    def imprimir_pdf(self):
        indexes = self.table_view.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.warning(self, "Advertencia", "Seleccione una fila para imprimir.")
            return
        row = indexes[0].row()
        model = self.table_view.model()
        headers = [model.headerData(i, 1) for i in range(model.columnCount())]
        datos = [model.index(row, i).data() for i in range(model.columnCount())]

        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar PDF", "estudiante_seleccionado.pdf", "PDF Files (*.pdf)")
        if not file_path:
            return

        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(file_path)

        painter = QPainter(printer)
        y = 100
        # Intentar cargar el logo
        logo_path = os.path.join("utilities", "resources", "imgs", "Bg.png")
        if os.path.exists(logo_path):
            logo = QPixmap(logo_path)
            logo = logo.scaledToWidth(120)
            # Centrar el logo
            page_width = printer.pageRect().width()
            x_logo = (page_width - logo.width()) // 2
            painter.drawPixmap(x_logo, y, logo)
            y += logo.height() + 30
        painter.setFont(painter.font())
        painter.drawText(100, y, "Datos del Estudiante Seleccionado:")
        y += 40
        for header, dato in zip(headers, datos):
            painter.drawText(100, y, f"{header}: {dato}")
            y += 30
        painter.end()
        QMessageBox.information(self, "PDF generado", f"El PDF se ha guardado como '{file_path}'.")

class VentanaTodos(QDialog):
    def __init__(self, database):  # <-- aquí el cambio
        super().__init__()         # <-- aquí el cambio
        self.setWindowTitle("Todos los estudiantes registrados")
        self.setGeometry(150, 150, 600, 600)
        layout = QVBoxLayout()
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        content = QWidget()
        form_layout = QFormLayout(content)
        data = database.SelectEstudend()
        headers = ["IDEST", "Nombre", "Apellido", "CedulaEscolar", "Edad", "Genero", "FN", "Lateralidad", "Nacionalidad", "Estado", "Municipio", "DA", "PTR", "Altura", "Peso", "Zapatos", "Camisa", "Pantalon", "NDH", "APRN", "AlergicoA", "AlgunaDificultad", "EspecifiqueDificultad", "CorreoElectronico", "TelefonoHabitacion", "CartonVacunas", "TipodeSangre", "EDH"]
        for idx, row in enumerate(data):
            if len(row) < 28:
                continue
            nombre = str(row[1])
            apellido = str(row[2])
            cedula = str(row[3])
            encabezado = f"--- Estudiante: {nombre} {apellido} ({cedula}) ---"
            form_layout.addRow(QLabel(encabezado), QLabel(""))
            for i, header in enumerate(headers):
                if i >= len(row):
                    break
                if header == "CartonVacunas":
                    foto_path = str(row[i])
                    if foto_path and os.path.exists(foto_path):
                        pixmap = QPixmap(foto_path)
                        pixmap = pixmap.scaledToWidth(200)
                        foto_label = QLabel()
                        foto_label.setPixmap(pixmap)
                        form_layout.addRow(QLabel(header+":"), foto_label)
                    else:
                        form_layout.addRow(QLabel(header+":"), QLabel("Sin imagen"))
                else:
                    form_layout.addRow(QLabel(header+":"), QLabel(str(row[i])))
        content.setLayout(form_layout)
        scroll.setWidget(content)
        layout.addWidget(scroll)
        self.setLayout(layout)
