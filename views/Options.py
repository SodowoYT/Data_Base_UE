import os.path
from PySide6.QtWidgets import QPushButton, QMainWindow, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QLabel
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
import shutil
import os
from views.RegsUser import RgtrUser
class Options(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Opciones")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.setGeometry(100, 100, 950, 650)
        self.setFixedSize(950, 650)
        
        from PySide6.QtWidgets import QStackedLayout
        from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
        self.layout = QVBoxLayout()

        # Fondo de la ventana con QLabel
        self.background_label = QLabel()
        self.right_pixmap = QPixmap("utilities/resources/imgs/bg/OptiBg.png")
        self.background_label.setPixmap(self.right_pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.setAlignment(Qt.AlignCenter)
        self.background_label.setContentsMargins(0, 0, 0, 0)


        # Logo grande, centrado y superpuesto sobre el fondo
        self.logo = QLabel()
        self.logo.setMinimumHeight(270)
        self.logo.setMinimumWidth(270)
        logo_pixmap = QPixmap("utilities/resources/LogoBG.png")
        self.logo.setPixmap(logo_pixmap.scaled(270, 270, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setStyleSheet("background: transparent; border: none;")

        # Layout para centrar el logo un poco más abajo de la parte superior
        logo_vbox = QVBoxLayout()
        logo_vbox.addSpacing(40)
        logo_vbox.addWidget(self.logo, alignment=Qt.AlignHCenter)
        logo_vbox.addStretch(1)
        logo_container = QWidget()
        logo_container.setLayout(logo_vbox)
        logo_container.setAttribute(Qt.WA_TranslucentBackground)
        
        
        # Botones de Interacción
        self.Option1 = QPushButton("Respaldo", self)
        self.Option2 = QPushButton("Restaurar", self)
        self.Option3 = QPushButton("Registrar Usuario", self)

        # Conectar los botones a sus respectivas funciones
        self.Option1.clicked.connect(self.backup)
        self.Option2.clicked.connect(self.restore)
        self.Option3.clicked.connect(self.register_user)

        # Apilar los botones en columna, centrados en la parte inferior
        # Hacer que todos los botones tengan el mismo tamaño
        button_width = 220
        button_height = 48
        for btn in [self.Option1, self.Option2, self.Option3]:
            btn.setFixedSize(button_width, button_height)

        buttons_vbox = QVBoxLayout()
        buttons_vbox.addStretch(1)
        buttons_vbox.addWidget(self.Option1, alignment=Qt.AlignHCenter)
        buttons_vbox.addSpacing(10)
        buttons_vbox.addWidget(self.Option2, alignment=Qt.AlignHCenter)
        buttons_vbox.addSpacing(10)
        buttons_vbox.addWidget(self.Option3, alignment=Qt.AlignHCenter)
        buttons_vbox.addSpacing(32)  # Separación desde el borde inferior

        # Widget contenedor para los botones
        buttons_container = QWidget()
        buttons_container.setLayout(buttons_vbox)
        buttons_container.setAttribute(Qt.WA_TranslucentBackground)

        # StackedLayout para fondo, logo y botones
        stacked = QStackedLayout()
        stacked.setStackingMode(QStackedLayout.StackAll)
        stacked.addWidget(self.background_label)
        stacked.addWidget(logo_container)
        stacked.addWidget(buttons_container)

        container = QWidget()
        container.setLayout(stacked)
        self.setCentralWidget(container)

        self.Option1.setStyleSheet("""
QPushButton {
    background-color: #0c3f67;
    color: white;
    border-radius: 15px;
    padding: 6px 0px;
    font-size: 15px;
    min-height: 28px;
}
QPushButton:hover {
    background-color: #14056d;
}
""")
        self.Option2.setStyleSheet(self.Option1.styleSheet())
        self.Option3.setStyleSheet(self.Option1.styleSheet())
        
    def backup(self):
        origen = os.path.join("utilities", "db", "DataBaseUE.db")
        destino, _ = QFileDialog.getSaveFileName(self, "Guardar respaldo", "DataBaseUE_backup.db", "Archivos DB (*.db)")
        if destino:
            try:
                shutil.copy2(origen, destino)
                QMessageBox.information(self, "Backup", f"Respaldo guardado en: {destino}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al guardar el respaldo: {e}")

    def restore(self):
        origen, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo de respaldo", "", "Archivos DB (*.db)")
        destino = os.path.join("utilities", "db", "DataBaseUE.db")
        if origen:
            try:
                shutil.copy2(origen, destino)
                QMessageBox.information(self, "Restaurar Respaldo", f"Respaldo restaurado desde: {origen}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al restaurar el respaldo: {e}")
                
    def register_user(self):
        self.rg_Window = RgtrUser()
        self.rg_Window.show()