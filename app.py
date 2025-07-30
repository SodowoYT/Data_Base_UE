import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PySide6.QtWidgets import QApplication
from views.Login import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Login_Window = LoginWindow()
    Login_Window.show()
    sys.exit(app.exec())
