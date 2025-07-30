from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt

class CreditosWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Créditos")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.setGeometry(100, 100, 870, 650)
        self.setFixedSize(870, 650)

        # Fondo
        self.background_label = QLabel()
        pixmap = QPixmap("utilities/resources/imgs/bg/MenuBg.png")
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.setAlignment(Qt.AlignCenter)

        # Contenido de créditos
        content = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(18)

        # Logo y título integrados en un solo bloque
        from PySide6.QtWidgets import QHBoxLayout, QFrame
        logo_label = QLabel()
        logo_pixmap = QPixmap("utilities/resources/LogoBG.png")
        logo_label.setPixmap(logo_pixmap.scaled(90, 90, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo_label.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        title = QLabel("Créditos del Proyecto")
        title.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        title.setStyleSheet("font-size: 38px; font-weight: bold; color: #0c3f67; background: transparent; padding-left: 10px;")

        # Contenedor visual integrado
        title_logo_frame = QFrame()
        title_logo_frame.setStyleSheet("background: rgba(255,255,255,0.8); border-radius: 16px; padding: 16px 24px;")
        title_logo_layout = QHBoxLayout()
        title_logo_layout.setSpacing(24)
        title_logo_layout.setContentsMargins(18, 8, 18, 8)
        title_logo_layout.addWidget(logo_label)
        title_logo_layout.addWidget(title)
        title_logo_frame.setLayout(title_logo_layout)
        layout.addWidget(title_logo_frame, alignment=Qt.AlignHCenter)

        autores = QLabel("""
Desarrollado por:

• Dalvin Ramirez (Desarrollador principal)(Diseñador de UI/UX)
• Aliribet Gonzalez (Diseñadora Gráfica y Colaboradora)
• Jose Mora (Documentación y Colaborador)
• Genesis Cordero (Tester y Colaboradora)
• Auditoría Recibida por: Bill Anthony Nino Riera (Guia de Pyside6)

• Agradecimientos especiales a todos los que contribuyeron al proyecto.
• A la comunidad de código abierto por su inspiración y recursos.

• Desarrollado por Estudiantes de la Universidad Experimental Rafael María Baralt (UERMB) de Venezuela.

Gracias por usar nuestra aplicación.
        """)
        autores.setAlignment(Qt.AlignCenter)
        autores.setStyleSheet("font-size: 20px; color: #222; background: rgba(255,255,255,0.85); border-radius: 10px; padding: 18px 12px;")
        layout.addWidget(autores)

        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.setStyleSheet("background-color: #0c3f67; color: white; border-radius: 12px; padding: 8px 32px; font-size: 16px;")
        btn_cerrar.clicked.connect(self.close)
        layout.addWidget(btn_cerrar, alignment=Qt.AlignCenter)

        content.setLayout(layout)
        content.setAttribute(Qt.WA_TranslucentBackground)

        # Superponer fondo y contenido
        from PySide6.QtWidgets import QStackedLayout
        stacked = QStackedLayout()
        stacked.setStackingMode(QStackedLayout.StackAll)
        stacked.addWidget(self.background_label)
        stacked.addWidget(content)

        container = QWidget()
        container.setLayout(stacked)
        self.setCentralWidget(container)
