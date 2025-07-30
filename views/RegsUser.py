from PySide6.QtWidgets import (
    QLineEdit, QPushButton, QMainWindow, QVBoxLayout, QMessageBox, QWidget, QLabel, QGridLayout
)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt

# Importar tu clase de conexión
from services.Connection import database


class RgtrUser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.setGeometry(200, 200, 650, 500)

        # Conexión con la base de datos
        self.db = database()

        # Widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Fondo
        self.background_label = QLabel(central_widget)
        self.background_pixmap = QPixmap("utilities/resources/imgs/bg/RgtrBg.png")
        self.background_label.setAlignment(Qt.AlignCenter)
        self.background_label.setScaledContents(True)

        # Layout del formulario
        form_layout = QVBoxLayout()
        form_layout.setSpacing(10)
        form_layout.setContentsMargins(40, 40, 40, 40)

        # Entradas
        self.Username = QLineEdit()
        self.Username.setPlaceholderText("Nombre de Usuario")
        self.Username.setMinimumHeight(38)
        self.Username.setMinimumWidth(320)

        self.Password = QLineEdit()
        self.Password.setPlaceholderText("Contraseña")
        self.Password.setMinimumHeight(38)
        self.Password.setMinimumWidth(320)
        self.Password.setEchoMode(QLineEdit.Password)

        self.Name = QLineEdit()
        self.Name.setPlaceholderText("Nombre")
        self.Name.setMinimumHeight(38)
        self.Name.setMinimumWidth(320)

        self.SecondName = QLineEdit()
        self.SecondName.setPlaceholderText("Apellido")
        self.SecondName.setMinimumHeight(38)
        self.SecondName.setMinimumWidth(320)

        self.Ci = QLineEdit()
        self.Ci.setPlaceholderText("Cédula de Identidad")
        self.Ci.setMinimumHeight(38)
        self.Ci.setMinimumWidth(320)

        self.Post = QLineEdit()
        self.Post.setPlaceholderText("Cargo")
        self.Post.setMinimumHeight(38)
        self.Post.setMinimumWidth(320)

        # Botón registrar
        self.button = QPushButton("Registrar")
        self.button.setStyleSheet("""
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
        self.button.clicked.connect(self.register_user)  # Conectar al método

        # Logo
        self.logo_pixmap = QPixmap("utilities/resources/imgs/ico/IconApp.ico")
        self.logo_label = QLabel()
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setPixmap(self.logo_pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        form_layout.addWidget(self.logo_label)

        # Agregar al layout
        form_layout.addWidget(self.Username)
        form_layout.addWidget(self.Password)
        form_layout.addWidget(self.Name)
        form_layout.addWidget(self.SecondName)
        form_layout.addWidget(self.Ci)
        form_layout.addWidget(self.Post)
        form_layout.addWidget(self.button)

        form_widget = QWidget()
        form_widget.setLayout(form_layout)
        form_widget.setAttribute(Qt.WA_TranslucentBackground)

        # Layout general
        grid = QGridLayout(central_widget)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.background_label, 0, 0)
        grid.addWidget(form_widget, 0, 0, alignment=Qt.AlignCenter)

    def resizeEvent(self, event):
        if not self.background_pixmap.isNull():
            self.background_label.setPixmap(
                self.background_pixmap.scaled(
                    self.centralWidget().size(),
                    Qt.IgnoreAspectRatio,
                    Qt.SmoothTransformation
                )
            )
        super().resizeEvent(event)

    # ----------------------
    # Registro de usuarios
    # ----------------------

    def register_user(self):
        username = self.Username.text().strip()
        password = self.Password.text().strip()
        name = self.Name.text().strip()
        lastname = self.SecondName.text().strip()
        ci = self.Ci.text().strip()
        post = self.Post.text().strip()

        if not username or not password or not name or not lastname or not ci or not post:
            QMessageBox.warning(self, "Campos incompletos", "Debes completar todos los campos.")
            return

        try:
            self.db.insert_user(username, password, name, lastname, ci, post)
            QMessageBox.information(self, "Usuario registrado", f"Usuario {username} creado correctamente.")
            self.Username.clear()
            self.Password.clear()
            self.Name.clear()
            self.SecondName.clear()
            self.Ci.clear()
            self.Post.clear()
        except Exception as e:
            if "UNIQUE constraint failed" in str(e):
                QMessageBox.warning(self, "Error", "Ese usuario ya existe.")
            else:
                QMessageBox.critical(self, "Error", f"No se pudo registrar el usuario:\n{e}")

