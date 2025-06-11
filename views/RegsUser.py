from PySide6.QtWidgets import QLineEdit, QPushButton, QMainWindow, QVBoxLayout, QMessageBox, QWidget

class RgtrUser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 300, 200)
        
        self.layout = QVBoxLayout()
        
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
        
        
        