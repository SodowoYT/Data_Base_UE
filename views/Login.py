from PySide6.QtWidgets import (
    QLineEdit, QPushButton, QMainWindow, QVBoxLayout, QMessageBox,
    QWidget, QLabel, QHBoxLayout
)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
from views.Menu import MenuWindow

# Importar tu clase database de connections.py
from services.Connection import database


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = database()  # Inicializamos conexión con SQLite

        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.setGeometry(100, 100, 500, 300)
        self.setFixedSize(500, 300)
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

        # Logo
        self.logo = QLabel()
        self.logo.setMinimumHeight(140)
        self.logo.setMinimumWidth(140)
        logo_pixmap = QPixmap("utilities/resources/LogoBG.png")
        self.logo.setPixmap(logo_pixmap.scaled(140, 140, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(self.logo)

        # Campos de usuario y contraseña
        self.inputusername = QLineEdit(self)
        self.inputusername.setPlaceholderText("Username")
        self.inputpassword = QLineEdit(self)
        self.inputpassword.setPlaceholderText("Password")
        self.inputpassword.setEchoMode(QLineEdit.Password)

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
        right_layout.addWidget(self.inputusername)
        right_layout.addWidget(self.inputpassword)
        right_layout.addWidget(self.Buttonlogin)
        right_widget.setLayout(right_layout)

        # Agregar al layout principal
        main_layout.addWidget(right_widget, 3)

        # Eventos de Enter
        self.inputusername.returnPressed.connect(self.handle_login)
        self.inputpassword.returnPressed.connect(self.handle_login)

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

    def resizeEvent(self, event):
        self.update_background()
        super().resizeEvent(event)

    def update_background(self):
        if not self.background_pixmap.isNull():
            scaled = self.background_pixmap.scaled(
                self.background_label.size(),
                Qt.IgnoreAspectRatio,
                Qt.SmoothTransformation
            )
            self.background_label.setPixmap(scaled)
