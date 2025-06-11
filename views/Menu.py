from PySide6.QtWidgets import QPushButton, QMainWindow, QVBoxLayout, QWidget
from views.Forms import FormsStudend

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 300, 200)
        
        self.layout = QVBoxLayout()
        
        self.button1 = QPushButton("Registrar", self)
        self.button2 = QPushButton("Consultar", self)
        self.button3 = QPushButton("Modificar", self)
        self.button4 = QPushButton("Imprimir", self)
        self.button5 = QPushButton("Mantenimiento", self)
        self.button6 = QPushButton("Salir", self)
        
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.layout.addWidget(self.button5) 
        self.layout.addWidget(self.button6)
        
        self.button1.clicked.connect(self.rg)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container) 
        
    def rg (self):
        self.rg_Window = FormsStudend()
        self.rg_Window.show()
