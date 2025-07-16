from PySide6.QtWidgets import QLineEdit, QPushButton, QMainWindow, QVBoxLayout, QMessageBox, QWidget

class RgtrUser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 300, 200)

        # Widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(10)      # Espaciado entre widgets
        self.layout.setContentsMargins(20, 20, 20, 20)  # Márgenes alrededor

        # Datos de Registro
        self.Username = QLineEdit(self)
        self.Username.setPlaceholderText("Nombre de Usuario")

        self.Password = QLineEdit(self)
        self.Password.setPlaceholderText("Contraseña")

        self.Name = QLineEdit(self)
        self.Name.setPlaceholderText("Nombre")

        self.SecondName = QLineEdit(self)
        self.SecondName.setPlaceholderText("Apellido")

        self.Ci = QLineEdit(self)
        self.Ci.setPlaceholderText("Cédula de Identidad")

        self.Post = QLineEdit(self)
        self.Post.setPlaceholderText("Cargo")

        self.button = QPushButton("Registrar", self)

        self.layout.addWidget(self.Username)
        self.layout.addWidget(self.Password)
        self.layout.addWidget(self.Name)
        self.layout.addWidget(self.SecondName)
        self.layout.addWidget(self.Ci)
        self.layout.addWidget(self.Post)
        self.layout.addWidget(self.button)

        central_widget.setLayout(self.layout)
