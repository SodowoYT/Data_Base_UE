from PySide6.QtWidgets import (QLineEdit, QPushButton, QMainWindow, QVBoxLayout, QMessageBox, QWidget, QLabel, QHBoxLayout,        QSpacerItem, QSizePolicy)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt

from views.Menu import MenuWindow

# Importar tu clase database de connections.py
from services.Connection import database

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = database()  # Inicializamos conexión con SQLite

        # Configuración de la ventana
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.setGeometry(100, 100, 750, 500)
        self.setFixedSize(750, 500)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        # Imagen de fondo
        self.background_label = QLabel(self)
        self.background_pixmap = QPixmap("utilities/resources/imgs/bg/BooksBg.png")
        self.background_label.setAlignment(Qt.AlignCenter)
        self.background_label.setContentsMargins(0, 0, 0, 0)
        self.background_label.setStyleSheet("border: none; margin: 0; padding: 0;")
        self.setCentralWidget(self.background_label)
        self.update_background()

        # Layout principal
        main_layout = QHBoxLayout(self.background_label)

        # Panel derecho
        right_widget = QWidget()
        right_layout = QVBoxLayout()

        # Logo de la aplicación
        self.logo = QLabel()
        self.logo.setMinimumHeight(240)
        self.logo.setMinimumWidth(240)
        logo_pixmap = QPixmap("utilities/resources/AElg.png")
        self.logo.setPixmap(logo_pixmap.scaled(240, 240, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(self.logo)

        # Campos de usuario y contraseña
        self.inputusername = QLineEdit(self)
        # Texto de nombre del sistema debajo del logo
        self.app_title_label = QLabel("Sistema G.R.U.E")
        self.app_title_label.setAlignment(Qt.AlignCenter)
        # Reservar algo de alto para la fuente grande
        self.app_title_label.setMinimumHeight(48)
        # Aplicar el estilo solicitado por el usuario
        self.app_title_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 32px;
                font-family:'Times New Roman', serif;
                font-weight: bold;
                letter-spacing: 2px;
                text-shadow: 0 2px 12px #1a237e, 0 0 8px #0c3f67;
                margin-top: 6px;
            }
        """)
        right_layout.addWidget(self.app_title_label)
        self.inputusername.setPlaceholderText("Username")
        self.inputusername.setStyleSheet("""
        QLineEdit {
            padding: 8px;
            border: 2px solid #0c3f67;
            border-radius: 10px;
            font-size: 14px;
        }
        """)
        self.inputpassword = QLineEdit(self)
        self.inputpassword.setPlaceholderText("Password")
        self.inputpassword.setEchoMode(QLineEdit.Password)
        self.inputpassword.setStyleSheet("""
        QLineEdit {
            padding: 8px;
            border: 2px solid #0c3f67;
            border-radius: 10px;
            font-size: 14px;
        }
        """)
        # Botón login
        self.Buttonlogin = QPushButton("Login", self)
        self.Buttonlogin.clicked.connect(self.handle_login)
        self.Buttonlogin.setStyleSheet("""
        QPushButton {
            background-color: #0c3f67;
            color: white;
            border-radius: 15px;
            padding: 8px 0px;
            font-size: 16px;
        }
        QPushButton:hover {
            background-color:  #14056d;
        }
        """)

        # Agregar widgets al layout derecho
        # Añadir un stretch arriba para empujar los campos hacia la parte inferior
        right_layout.addStretch(1)

        # Ajustar márgenes laterales para que los controles se extiendan hacia los lados
        right_layout.setContentsMargins(24, 12, 24, 24)
        # Permitir expansión horizontal para ocupar más espacio a los lados
        self.inputusername.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.inputpassword.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # Dar un mínimo para que se vean largos pero permitir expansión
        self.inputusername.setMinimumWidth(300)
        self.inputpassword.setMinimumWidth(300)

        # Botón también puede crecer horizontalmente
        self.Buttonlogin.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.Buttonlogin.setMinimumWidth(200)

        # Añadir los widgets sin alineación para que ocupen todo el ancho disponible
        right_layout.addWidget(self.inputusername)
        right_layout.addWidget(self.inputpassword)
        right_layout.addWidget(self.Buttonlogin)

        # Añadir un pequeño espacio al fondo para separación visual
        right_layout.addSpacing(24)

        right_widget.setLayout(right_layout)

        # Agregar al layout principal
        main_layout.addWidget(right_widget, 3)

        # Eventos de Enter
        self.inputusername.returnPressed.connect(self.handle_login)
        self.inputpassword.returnPressed.connect(self.handle_login)

    # Función para manejar el inicio de sesión
    def handle_login(self):
        username = self.inputusername.text().strip()
        password = self.inputpassword.text()

        ok, user_data = self.db.validate_user(username, password)
        if ok:
            nombre_completo = f"{user_data['name']} {user_data['lastname']}"
            cargo = user_data['post']
            QMessageBox.information(
                self, 
                "Bienvenido", 
                f"Bienvenido {nombre_completo}\nCargo: {cargo}"
            )
            self.menu_window = MenuWindow()
            self.menu_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")
            self.inputpassword.clear()
            self.inputpassword.setFocus()

    # Función para manejar el evento de redimensionar
    def resizeEvent(self, event):
        self.update_background()
        super().resizeEvent(event)

    # Función para actualizar el fondo
    def update_background(self):
        if not self.background_pixmap.isNull():
            scaled = self.background_pixmap.scaled(
                self.background_label.size(),
                Qt.IgnoreAspectRatio,
                Qt.SmoothTransformation
            )
            self.background_label.setPixmap(scaled)
