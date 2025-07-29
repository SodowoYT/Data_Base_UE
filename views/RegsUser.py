from PySide6.QtWidgets import QLineEdit, QPushButton, QMainWindow, QVBoxLayout, QMessageBox, QWidget, QLabel, QGridLayout
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt

class RgtrUser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.setGeometry(100, 100, 500, 400)

        # Widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Fondo con QLabel y QPixmap
        self.background_label = QLabel(central_widget)
        self.background_pixmap = QPixmap("utilities/resources/imgs/bg/RgtrBg.png")
        self.background_label.setAlignment(Qt.AlignCenter)
        self.background_label.setScaledContents(True)

        # Layout del formulario
        form_layout = QVBoxLayout()
        form_layout.setSpacing(10)
        form_layout.setContentsMargins(40, 40, 40, 40)

        self.Username = QLineEdit()
        self.Username.setPlaceholderText("Nombre de Usuario")
        self.Username.setMinimumHeight(38)
        self.Username.setMinimumWidth(320)
        self.Password = QLineEdit()
        self.Password.setPlaceholderText("Contraseña")
        self.Password.setMinimumHeight(38)
        self.Password.setMinimumWidth(320)
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

        # Logo arriba del formulario
        self.logo_pixmap = QPixmap("utilities/resources/imgs/ico/IconApp.ico")
        self.logo_label = QLabel()
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setPixmap(self.logo_pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        form_layout.addWidget(self.logo_label)

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

        # GridLayout para superponer fondo y formulario
        grid = QGridLayout(central_widget)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.background_label, 0, 0)
        grid.addWidget(form_widget, 0, 0, alignment=Qt.AlignCenter)

    def resizeEvent(self, event):
        # Escala la imagen de fondo al tamaño del widget central
        if not self.background_pixmap.isNull():
            self.background_label.setPixmap(
                self.background_pixmap.scaled(
                    self.centralWidget().size(),
                    Qt.IgnoreAspectRatio,
                    Qt.SmoothTransformation
                )
            )
        super().resizeEvent(event)
