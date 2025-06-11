import sys 
from PySide6.QtWidgets import QApplication
from views.Login import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Login_Window = LoginWindow()
    Login_Window.show()
    sys.exit(app.exec())
