import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PySide6.QtWidgets import QApplication
from views.Forms import FormsStudend

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = FormsStudend()
    ventana.show()
    sys.exit(app.exec())
