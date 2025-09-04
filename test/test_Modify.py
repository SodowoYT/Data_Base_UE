import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PySide6.QtWidgets import QApplication
from views.Modify import ModifyData

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ModifyData()
    ventana.show()
    sys.exit(app.exec())
