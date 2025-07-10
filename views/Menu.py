from PySide6.QtWidgets import QPushButton, QMainWindow, QVBoxLayout, QWidget
from views.Forms import FormsStudend
from views.Consult import ConsultWindow
from views.Options import Options
from views.Modify import ModifyWindow
from views.Print import PrintWindow
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
        self.button2.clicked.connect(self.Csl)
        self.button3.clicked.connect(self.Mdfy)
        self.button4.clicked.connect(self.Print)
        self.button5.clicked.connect(self.Opt)
        self.button6.clicked.connect(self.Exit)
        
        
    
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container) 
        
        # Definicion Para llamada a la Ventana registro
    def rg (self):
        self.rg_Window = FormsStudend()
        self.rg_Window.show()
        # Definicion Para llamada a la Ventana Consulta
    def Csl (self):
        self.Csl_Window = ConsultWindow()
        self.Csl_Window.show()
        # Definicion Para llamada a la Ventana Modificar
    def Mdfy (self):
        self.Mdfy_Window = ModifyWindow()
        self.Mdfy_Window.show()
        # Definicion Para llamada a la Ventana Imprimir
    def Print (self):
        self.Print_Window = PrintWindow()
        self.Print_Window.show()
        # Definicion Para llamada a la Ventana Opciones
    def Opt (self):
        self.Opt_Window = Options()
        self.Opt_Window.show()
        # Definicion para Cierre de Ventana Menu
    def Exit(self):
        self.close()
