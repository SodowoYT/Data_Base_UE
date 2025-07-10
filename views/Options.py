import os.path
from PySide6.QtWidgets import QPushButton, QMainWindow, QVBoxLayout, QWidget, QFileDialog, QMessageBox
import shutil
import os

class Options(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Opciones")
        self.setGeometry(100, 100, 300, 200)
        
        self.layout = QVBoxLayout()
        
        # Botones de Interacción
        
        self.Option1 = QPushButton("Respaldo", self)
        self.Option2 = QPushButton("Restaurar", self)
        
        # Conectar los botones a sus respectivas funciones
        self.Option1.clicked.connect(self.backup)
        self.Option2.clicked.connect(self.restore)
        
        self.layout.addWidget(self.Option1)
        self.layout.addWidget(self.Option2) 
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        
    def backup(self):
        origen = os.path.join("utilities", "db", "DataBaseUE.db")
        destino, _ = QFileDialog.getSaveFileName(self, "Guardar respaldo", "DataBaseUE_backup.db", "Archivos DB (*.db)")
        if destino:
            try:
                shutil.copy2(origen, destino)
                QMessageBox.information(self, "Backup", f"Respaldo guardado en: {destino}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al guardar el respaldo: {e}")

    def restore(self):
        origen, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo de respaldo", "", "Archivos DB (*.db)")
        destino = os.path.join("utilities", "db", "DataBaseUE.db")
        if origen:
            try:
                shutil.copy2(origen, destino)
                QMessageBox.information(self, "Restaurar Respaldo", f"Respaldo restaurado desde: {origen}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al restaurar el respaldo: {e}")