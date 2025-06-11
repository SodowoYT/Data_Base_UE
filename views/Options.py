from PySide6.QtWidgets import QPushButton, QMainWindow, QVBoxLayout, QWidget

class Options(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Opciones")
        self.setGeometry(100, 100, 300, 200)
        
        self.layout = QVBoxLayout()
        
        # Botones de Interacción
        
        self.Option1 = QPushButton("Respaldo", self)
        self.Option2 = QPushButton("Restaurar", self)
        
        self.layout.addWidget(self.Option1)
        self.layout.addWidget(self.Option2) 
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        
        
        
        