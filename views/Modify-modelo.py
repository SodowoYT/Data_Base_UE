from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QButtonGroup, QMainWindow, QStackedWidget, QGridLayout, QGroupBox, QSizePolicy, QSpacerItem, QFileDialog, QDialog, QFormLayout, QScrollArea
from viewmodels.ModifyW import ModifyViewModel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QIcon
from PySide6.QtWidgets import QDateEdit
from PySide6.QtCore import QDate

import sqlite3

class BgWidget(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image = QPixmap(image_path)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

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

class ModifyData(QDialog):
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
