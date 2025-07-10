from PySide6.QtWidgets import QPushButton, QMainWindow, QVBoxLayout, QWidget

class ModifyWindow(QMainWindow):
  def __init__(self):
      super().__init__()
      self.setWindowTitle("Modificar")
      self.setGeometry(100, 100, 300, 200)
      
      self.layout = QVBoxLayout()
      
      self.button1 = QPushButton("Modificar", self)
      self.layout.addWidget(self.button1)
      
      container = QWidget()
      container.setLayout(self.layout)
      self.setCentralWidget(container)