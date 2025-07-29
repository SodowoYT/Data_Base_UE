from PySide6.QtWidgets import QLineEdit, QPushButton, QMainWindow, QVBoxLayout, QMessageBox, QWidget, QLabel, QHBoxLayout, QSizePolicy
from PySide6.QtGui import QPixmap, QIcon
from views.Menu import MenuWindow
from PySide6.QtCore import Qt

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.setGeometry(100, 100, 500, 300)
        self.setFixedSize(500, 300)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        # Imagen de fondo que ocupa toda la ventana
        self.background_label = QLabel(self)
        self.background_pixmap = QPixmap("utilities/resources/imgs/bg/BooksBg.png")
        self.background_label.setAlignment(Qt.AlignCenter)
        self.background_label.setContentsMargins(0, 0, 0, 0)
        self.background_label.setStyleSheet("border: none; margin: 0; padding: 0;")
        self.setCentralWidget(self.background_label)

        # Mostrar imagen ajustada al tamaño del label
        self.update_background()

        # Layout principal sobre el background_label
        main_layout = QHBoxLayout(self.background_label)

        # Layout derecho (formulario)
        right_widget = QWidget()
        right_layout = QVBoxLayout()

        # Logo arriba del formulario
        self.logo = QLabel()
        self.logo.setMinimumHeight(140)
        self.logo.setMinimumWidth(140)
        logo_pixmap = QPixmap("utilities/resources/LogoBG.png")  # Cambia por tu logo si tienes otro
        self.logo.setPixmap(logo_pixmap.scaled(140, 140, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(self.logo)

        self.inputusername = QLineEdit(self)
        self.inputusername.setPlaceholderText("Username")
        self.inputpassword = QLineEdit(self)
        self.inputpassword.setPlaceholderText("Password")
        self.inputpassword.setEchoMode(QLineEdit.Password)
        self.Buttonlogin = QPushButton("Login", self)
        self.Buttonlogin.clicked.connect(self.handle_login)
        # Estilos para el botón
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

        right_layout.addWidget(self.inputusername)
        right_layout.addWidget(self.inputpassword)
        right_layout.addWidget(self.Buttonlogin)
        right_widget.setLayout(right_layout)

        main_layout.addWidget(right_widget, 3)  # El factor de estiramiento va como segundo argumento

        self.inputusername.returnPressed.connect(self.handle_login)
        self.inputpassword.returnPressed.connect(self.handle_login)

    def handle_login(self):
        username = self.inputusername.text()
        password = self.inputpassword.text()

        if not username or not password:
            QMessageBox.warning(self, "Campos requeridos", "Debes ingresar usuario y contraseña.")
            return

        if username == "admin" and password == "admin":
            QMessageBox.information(self, "Inicio de Sesion Correcto", "¡Bienvenido A Sistema G.R.U.E!")
            self.menu_window = MenuWindow()
            self.menu_window.show()
            self.close()

    def resizeEvent(self, event):
        self.update_background()
        super().resizeEvent(event)

    def update_background(self):
        if not self.background_pixmap.isNull():
            scaled = self.background_pixmap.scaled(
                self.background_label.size(),
                Qt.IgnoreAspectRatio,  # Cambia aquí
                Qt.SmoothTransformation
            )
            self.background_label.setPixmap(scaled)
