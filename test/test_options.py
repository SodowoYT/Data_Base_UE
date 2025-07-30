import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PySide6.QtWidgets import QApplication
from views.Options import Options

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Options()
    ventana.show()
    sys.exit(app.exec())
