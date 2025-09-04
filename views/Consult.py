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
        buscador_layout.addWidget(self.search_input)
        buscador_layout.addWidget(self.search_button)
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

        # Instancia de la base de datos
        self.database = database("utilities\\db\\DataBaseUE.db")
        self.cargarDatos()

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
        # Crear el modelo
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels([
            "ID", "Nombre", "Apellido", "Cédula Escolar", "Edad", "Género", "Fecha Nac."
        ])

        # Obtener datos de la BD
        data = self.database.SelectEstudend()
        if filtroCedula:
            data = [row for row in data if str(row[3]).strip() == filtroCedula]

        if not data:
            QMessageBox.warning(self, "Advertencia", "No se encontraron registros.")
            self.table_view.setModel(model)
            return

        # Bloquear actualizaciones mientras se carga
        self.table_view.setUpdatesEnabled(False)

        for row in data:
            if len(row) < 8:
                continue
            # Solo mostrar los primeros 8 campos
            model.appendRow([QStandardItem(str(col)) for col in row[:7]])

        # Asignar el modelo una sola vez
        self.table_view.setModel(model)

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
        indexes = self.table_view.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.warning(self, "Advertencia", "Seleccione una fila para imprimir.")
            return
        
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
        self.Mreg_Window = ModifyData(self.database, cedula)
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

