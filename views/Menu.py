from PySide6.QtWidgets import QPushButton, QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QSizePolicy
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
from views.Forms import FormsStudend
from views.Consult import ConsultWindow
from views.Options import Options

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.setGeometry(100, 100, 500, 300)
        self.setFixedSize(500, 300)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        # Layout principal horizontal
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Layout izquierdo (botones)
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(30, 30, 30, 30)
        left_layout.setSpacing(15)

        self.button1 = QPushButton("Registrar", self)
        self.button2 = QPushButton("Consultar", self)
        self.button5 = QPushButton("Mantenimiento", self)
        self.button6 = QPushButton("Salir", self)

        for btn in [self.button1, self.button2, self.button5, self.button6]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #0c3f67;
                    color: white;
                    border-radius: 15px;
                    padding: 6px 0px;
                    font-size: 15px;
                    min-height: 28px;
                }
                QPushButton:hover {
                    background-color: #14056d;
                }
            """)
            left_layout.addWidget(btn)

        self.button1.clicked.connect(self.rg)
        self.button2.clicked.connect(self.Csl)
        self.button5.clicked.connect(self.Opt)
        self.button6.clicked.connect(self.Exit)

        left_widget.setLayout(left_layout)
        main_layout.addWidget(left_widget, stretch=3)

        # Imagen derecha
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        self.right_image = QLabel()
        self.right_pixmap = QPixmap("utilities/resources/imgs/bg/MenuBg.png")
        self.right_image.setAlignment(Qt.AlignCenter)
        self.right_image.setContentsMargins(0, 0, 0, 0)
        self.right_image.setStyleSheet("border: none; margin: 0; padding: 0;")
        self.right_image.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if self.right_pixmap.isNull():
            self.right_image.setText("Imagen no encontrada")
        else:
            self.right_image.setPixmap(self.right_pixmap)
        right_layout.addWidget(self.right_image, stretch=1)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)
        right_widget.setContentsMargins(0, 0, 0, 0)
        right_widget.setStyleSheet("border: none; margin: 0; padding: 0;")
        right_widget.setLayout(right_layout)
        main_layout.addWidget(right_widget, stretch=2)

        def resize_right_image(event):
            if not self.right_pixmap.isNull():
                size = self.right_image.size()
                scaled = self.right_pixmap.scaled(size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                self.right_image.setPixmap(scaled)
            QWidget.resizeEvent(self.right_image, event)
        self.right_image.resizeEvent = resize_right_image

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def rg (self):
        self.rg_Window = FormsStudend()
        self.rg_Window.show()
    def Csl (self):
        self.Csl_Window = ConsultWindow()
        self.Csl_Window.show()
    def Opt (self):
        self.Opt_Window = Options()
        self.Opt_Window.show()
    def Exit(self):
        self.close()
