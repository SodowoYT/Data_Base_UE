from PySide6.QtWidgets import QPushButton, QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QSizePolicy
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt, QTimer, QDateTime
from views.Forms import FormsStudend
from views.Consult import ConsultWindow
from views.Options import Options 
from views.Creditos import CreditosWindow
from PySide6.QtWidgets import QStackedLayout, QVBoxLayout as QVBoxLayout2, QHBoxLayout as QHBoxLayout2
class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.setGeometry(100, 100, 950, 650)
        self.setFixedSize(950, 650)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        # Fondo de la ventana
        self.background_label = QLabel()
        self.right_pixmap = QPixmap("utilities/resources/imgs/bg/MenuBg.png")
        self.background_label.setPixmap(self.right_pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.setAlignment(Qt.AlignCenter)
        self.background_label.setContentsMargins(0, 0, 0, 0)

        # Panel izquierdo (botones y logo)
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(8, 18, 8, 18)
        left_layout.setSpacing(8)
        self.logo = QLabel()
        self.logo.setMinimumHeight(140)
        self.logo.setMinimumWidth(140)
        logo_pixmap = QPixmap("utilities/resources/LogoBG.png")
        self.logo.setPixmap(logo_pixmap.scaled(140, 140, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setStyleSheet("background: transparent; border: none;")
        left_layout.addWidget(self.logo, alignment=Qt.AlignHCenter)
        
        
        self.button1 = QPushButton("Registrar", self)
        self.button2 = QPushButton("Consultar", self)
        self.button3 = QPushButton("Mantenimiento", self)
        self.button4 = QPushButton("Creditos", self)
        self.button5 = QPushButton("Salir", self)
        for btn in [self.button1, self.button2, self.button3, self.button4, self.button5]:
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
        self.button3.clicked.connect(self.Opt)
        self.button4.clicked.connect(self.Crdt)
        self.button5.clicked.connect(self.Exit)
        
        left_widget.setStyleSheet("""
            background-color: rgba(26,35,126,0.75);
            border-top-left-radius: 30px;
            border-bottom-left-radius: 30px;
            background-image:
                repeating-linear-gradient(135deg, rgba(255,255,255,0.06) 0px, rgba(255,255,255,0.06) 2px, transparent 2px, transparent 20px),
                repeating-linear-gradient(225deg, rgba(255,255,255,0.06) 0px, rgba(255,255,255,0.06) 2px, transparent 2px, transparent 20px),
                repeating-linear-gradient(45deg, rgba(0,0,0,0.06) 0px, rgba(0,0,0,0.06) 2px, transparent 2px, transparent 20px),
                repeating-linear-gradient(315deg, rgba(0,0,0,0.06) 0px, rgba(0,0,0,0.06) 2px, transparent 2px, transparent 20px);
        """)
        left_widget.setLayout(left_layout)

        # Panel derecho (fecha/hora)
        date_time_container = QWidget()
        date_time_layout = QVBoxLayout2()
        date_time_layout.setContentsMargins(0, 0, 15, 15)
        date_time_layout.addStretch(1)
        h_layout = QHBoxLayout2()
        h_layout.addStretch(1)
        self.date_time_label = QLabel()
        self.date_time_label.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.date_time_label.setStyleSheet("""
            color: #e3e8f7;
            font-size: 16px;
            font-weight: bold;
            background: rgba(20, 30, 60, 0.65);
            border-radius: 12px;
            padding: 8px 18px;
            margin: 0;
            letter-spacing: 1px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.12);
        """)
        h_layout.addWidget(self.date_time_label, alignment=Qt.AlignRight | Qt.AlignBottom)
        date_time_layout.addLayout(h_layout)
        date_time_container.setLayout(date_time_layout)

        # Layout principal sobre el fondo
        overlay_layout = QHBoxLayout()
        overlay_layout.setContentsMargins(0, 0, 0, 0)
        overlay_layout.setSpacing(0)
        overlay_layout.addWidget(left_widget, stretch=1)
        overlay_layout.addWidget(date_time_container, stretch=5)

        # StackedLayout para fondo y paneles
        stacked = QStackedLayout()
        stacked.setStackingMode(QStackedLayout.StackAll)
        stacked.addWidget(self.background_label)
        overlay_widget = QWidget()
        overlay_widget.setLayout(overlay_layout)
        stacked.addWidget(overlay_widget)

        container = QWidget()
        container.setLayout(stacked)
        self.setCentralWidget(container)

        # Actualización de fecha y hora
        self.update_date_time()
        timer = QTimer(self)
        timer.timeout.connect(self.update_date_time)
        timer.start(1000)  # Cada 1 segundo

        # Redimensionar imagen de fondo
        def resize_background(event):
            if not self.right_pixmap.isNull():
                size = self.background_label.size()
                scaled = self.right_pixmap.scaled(size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                self.background_label.setPixmap(scaled)
            QWidget.resizeEvent(self.background_label, event)
        self.background_label.resizeEvent = resize_background

    def update_date_time(self):
        current = QDateTime.currentDateTime()
        # Formato 12 horas con AM/PM
        self.date_time_label.setText(current.toString("dd/MM/yyyy hh:mm:ss AP"))

    def rg (self):
        self.rg_Window = FormsStudend()
        self.rg_Window.show()
    def Csl (self):
        self.Csl_Window = ConsultWindow()
        self.Csl_Window.show()
    def Opt (self):
        self.Opt_Window = Options()
        self.Opt_Window.show()
    def Crdt(self):
        self.Crdt_Window = CreditosWindow()
        self.Crdt_Window.show()
    def Exit(self):
        self.close()
