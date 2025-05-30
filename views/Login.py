from PySide6.QtWidgets import QLineEdit, QPushButton, QMainWindow, QVBoxLayout, QMessageBox, QWidget
from views.Menu import MenuWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 200)
        
        self.layaout = QVBoxLayout()
        self.inputusername = QLineEdit(self)
        self.inputusername.setPlaceholderText("Username")
        self.inputpassword = QLineEdit(self)
        self.inputpassword.setPlaceholderText("Password")
        self.Buttonlogin = QPushButton("Login", self)
        self.Buttonlogin.clicked.connect(self.handle_login)
        
        self.layaout.addWidget(self.inputusername)
        self.layaout.addWidget(self.inputpassword)
        self.layaout.addWidget(self.Buttonlogin)
        container = QWidget()
        container.setLayout(self.layaout)
        self.setCentralWidget(container)        
        
    def handle_login(self):
        username = self.inputusername.text()
        password = self.inputpassword.text()
        
        if username == "admin" and password == "admin":
            QMessageBox.information(self, "Login Successful", "Welcome to the application!")
            self.menu_window = MenuWindow()
            self.menu_window.show()
            self.close()
      