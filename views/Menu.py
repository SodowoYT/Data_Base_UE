from PySide6.QtWidgets import QPushButton, QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QSizePolicy, QGridLayout, QFrame
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtCore import Qt, QTimer, QDateTime
from views.Forms import FormsStudend
from views.Consult import ConsultWindow
from views.Options import Options 
from views.Creditos import CreditosWindow
from PySide6.QtWidgets import QStackedLayout, QVBoxLayout as QVBoxLayout2, QHBoxLayout as QHBoxLayout2
from services.Connection import database
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.setGeometry(100, 100, 1000, 850)
        self.setFixedSize(1000, 850)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        # Inicializar base de datos para estadísticas
        self.db = database("utilities\\db\\DataBaseUE.db")

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

        # Botones del menú
        self.button1 = QPushButton("Registrar", self)
        self.button2 = QPushButton("Consultar", self)
        self.button3 = QPushButton("Mantenimiento", self)
        self.button4 = QPushButton("Creditos", self)
        self.button5 = QPushButton("Salir", self)

        # Establecer estilos para los botones
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

        # Conectar botones a funciones
        self.button1.clicked.connect(self.rg)
        self.button2.clicked.connect(self.Csl)
        self.button3.clicked.connect(self.Opt)
        self.button4.clicked.connect(self.Crdt)
        self.button5.clicked.connect(self.Exit)

        # Establecer estilos para el panel izquierdo
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

        # Panel derecho (fondo visible con dashboard compacto)
        right_container = QWidget()
        right_layout = QVBoxLayout2()
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)
        
        # Layout principal del lado derecho
        main_right_layout = QHBoxLayout()
        main_right_layout.setContentsMargins(0, 0, 0, 0)
        main_right_layout.setSpacing(0)
        
        # Espacio para mostrar el fondo (lado izquierdo del panel derecho)
        background_space = QWidget()
        background_space.setMinimumWidth(400)  # Espacio para mostrar el fondo
        main_right_layout.addWidget(background_space, stretch=2)
        
        # Contenedor para centrar verticalmente el dashboard
        center_container = QWidget()
        center_layout = QVBoxLayout()
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.setSpacing(0)
        
        # Espaciador superior para centrar
        center_layout.addStretch(1)
        
        # Dashboard compacto centrado
        dashboard_container = QWidget()
        dashboard_container.setMaximumWidth(300)  # Limitar ancho del dashboard
        dashboard_container.setMinimumWidth(280)
        dashboard_layout = QVBoxLayout()
        dashboard_layout.setContentsMargins(10, 15, 20, 15)
        dashboard_layout.setSpacing(12)
        
        # Crear dashboard compacto
        self.create_compact_dashboard(dashboard_layout)
        
        # Fecha/hora en la parte inferior del dashboard
        date_time_layout = QVBoxLayout2()
        date_time_layout.addStretch(1)
        h_layout = QHBoxLayout2()
        h_layout.addStretch(1)
        self.date_time_label = QLabel()
        self.date_time_label.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.date_time_label.setStyleSheet("""
            color: #e3e8f7;
            font-size: 14px;
            font-weight: bold;
            background: rgba(20, 30, 60, 0.65);
            border-radius: 8px;
            padding: 6px 12px;
            margin: 0;
            letter-spacing: 1px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.12);
        """)
        h_layout.addWidget(self.date_time_label, alignment=Qt.AlignRight | Qt.AlignBottom)
        date_time_layout.addLayout(h_layout)
        
        dashboard_layout.addLayout(date_time_layout)
        dashboard_container.setLayout(dashboard_layout)
        
        # Agregar dashboard al centro
        center_layout.addWidget(dashboard_container)
        
        # Espaciador inferior para centrar
        center_layout.addStretch(1)
        
        center_container.setLayout(center_layout)
        # Título superior derecho
        self.right_title = QLabel()
        self.right_title.setText('<span style="color:#e3e8f7; font-size:18px; font-weight:600; letter-spacing:1.2px;">Unidad Educativa</span><br>'
                                 '<span style="color:white; font-size:32px; font-family:Georgia,\'Times New Roman\',serif; font-weight:bold; letter-spacing:2px; text-shadow: 0 2px 12px #1a237e, 0 0 8px #0c3f67;">Angel Emiro Araujo</span>')
        self.right_title.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.right_title.setStyleSheet("""
            QLabel {
                margin-top: 38px;
                margin-bottom: 0px;
                background: transparent;
            }
        """)
        right_layout.addWidget(self.right_title, alignment=Qt.AlignHCenter | Qt.AlignTop)

        # Logo superior derecho
        self.right_logo = QLabel()
        self.right_logo.setMinimumSize(260, 260)
        self.right_logo.setMaximumSize(260, 260)
        right_logo_pixmap = QPixmap("utilities/resources/LgAERJ.png")
        self.right_logo.setPixmap(right_logo_pixmap.scaled(260, 260, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.right_logo.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.right_logo.setStyleSheet("background: transparent; border: none; margin-top: 05px; margin-bottom: 05px;")
        right_layout.addWidget(self.right_logo, alignment=Qt.AlignHCenter | Qt.AlignTop)
        main_right_layout.addWidget(center_container, stretch=1)
        
        right_layout.addLayout(main_right_layout)
        right_container.setLayout(right_layout)

        # Layout principal sobre el fondo
        overlay_layout = QHBoxLayout()
        overlay_layout.setContentsMargins(0, 0, 0, 0)
        overlay_layout.setSpacing(0)
        overlay_layout.addWidget(left_widget, stretch=1)
        overlay_layout.addWidget(right_container, stretch=5)

        # StackedLayout para fondo y paneles
        stacked = QStackedLayout()
        stacked.setStackingMode(QStackedLayout.StackAll)
        stacked.addWidget(self.background_label)
        overlay_widget = QWidget()
        overlay_widget.setLayout(overlay_layout)
        stacked.addWidget(overlay_widget)

        # Contenedor principal
        container = QWidget()
        container.setLayout(stacked)
        self.setCentralWidget(container)

        # Actualización de fecha y hora
        self.update_date_time()
        timer = QTimer(self)
        timer.timeout.connect(self.update_date_time)
        timer.start(1000)  # Cada 1 segundo

        # Actualización de estadísticas del dashboard
        self.update_dashboard_stats()
        stats_timer = QTimer(self)
        stats_timer.timeout.connect(self.update_dashboard_stats)
        stats_timer.start(5000)  # Cada 5 segundos

        # Redimensionar imagen de fondo
        def resize_background(event):
            if not self.right_pixmap.isNull():
                size = self.background_label.size()
                scaled = self.right_pixmap.scaled(size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                self.background_label.setPixmap(scaled)
            QWidget.resizeEvent(self.background_label, event)
        self.background_label.resizeEvent = resize_background

    # Funcion Actualizar fecha y hora
    def update_date_time(self):
        current = QDateTime.currentDateTime()
        # Formato 12 horas con AM/PM
        self.date_time_label.setText(current.toString("dd/MM/yyyy hh:mm:ss AP"))

    # Función para abrir el formulario de registro
    def rg (self):
        self.rg_Window = FormsStudend()
        self.rg_Window.show()

    # Función para abrir la ventana de consulta
    def Csl (self):
        self.Csl_Window = ConsultWindow()
        self.Csl_Window.show()

    # Función para abrir la ventana de opciones
    def Opt (self):
        self.Opt_Window = Options()
        self.Opt_Window.show()

    # Función para abrir la ventana de créditos
    def Crdt(self):
        self.Crdt_Window = CreditosWindow()
        self.Crdt_Window.show()

    # Función para salir de la aplicación
    def Exit(self):
        self.close()

    # Crear dashboard compacto con estadísticas
    def create_compact_dashboard(self, parent_layout):
        """Crea el dashboard compacto con las estadísticas de la base de datos."""
        # Contenedor principal del dashboard
        dashboard_frame = QFrame()
        dashboard_frame.setStyleSheet("""
            QFrame {
                background: rgba(255, 255, 255, 0.75);
                border-radius: 15px;
                border: 2px solid rgba(26, 35, 126, 0.3);
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
            }
        """)
        dashboard_layout = QVBoxLayout()
        dashboard_layout.setContentsMargins(12, 12, 12, 12)
        dashboard_layout.setSpacing(12)
        
        # Título del dashboard 
        title_label = QLabel("📊 ESTADÍSTICAS")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                color: #1a237e;
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 5px;
                letter-spacing: 1px;
            }
        """)
        dashboard_layout.addWidget(title_label)
        
        # Grid para las tarjetas de estadísticas 
        stats_grid = QGridLayout()
        stats_grid.setSpacing(8)
        
        # Obtener estadísticas
        stats = self.db.get_dashboard_stats()
        turno_stats = self.db.get_students_by_turno()  # {'Mañana': X, 'Tarde': Y}
        
        # Crear tarjetas para cada estadística 
        self.stats_cards = {}
        cards_data = [
            ("👨‍🎓", "ESTUDIANTES", stats['estudiantes'], "#4CAF50"),
            ("👨‍💼", "REPRESENTANTES", stats['representantes'], "#2196F3"),
            ("👨", "PADRES", stats['padres'], "#FF9800"),
            ("👩", "MADRES", stats['madres'], "#E91E63"),
            ("🌅", "MAÑANA", turno_stats.get('Mañana', 0), "#1A82F8"),
            ("🌇", "TARDE", turno_stats.get('Tarde', 0), "#9010F8")
        ]
        for i, (icon, title, count, color) in enumerate(cards_data):
            card = self.create_compact_stat_card(icon, title, count, color)
            self.stats_cards[title.lower()] = card
            row = i // 2
            col = i % 2
            stats_grid.addWidget(card, row, col)
        
        dashboard_layout.addLayout(stats_grid)
        
        # Información adicional 
        info_label = QLabel("💡 Datos Actuales")
        info_label.setAlignment(Qt.AlignCenter)
        info_label.setStyleSheet("""
            QLabel {
                color: #666;
                font-size: 10px;
                font-style: italic;
                margin-top: 5px;
            }
        """)
        dashboard_layout.addWidget(info_label)
        
        dashboard_frame.setLayout(dashboard_layout)
        parent_layout.addWidget(dashboard_frame)

    def create_turno_chart(self, turno_counts):
        """Crea un gráfico de barras con la cantidad de niños por turno (mañana/tarde)."""
        fig = Figure(figsize=(3, 1.2), dpi=100)
        ax = fig.add_subplot(111)
        labels = list(turno_counts.keys())
        values = list(turno_counts.values())
        bars = ax.bar(labels, values, color=['#1976D2', '#F57C00'])
        ax.set_ylabel('Cantidad')
        ax.set_title('Niños por Turno')
        ax.set_ylim(0, max(values) + 2)
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points",
                        ha='center', va='bottom', fontsize=9, color='black')
        fig.tight_layout()
        canvas = FigureCanvas(fig)
        return canvas

    def create_compact_stat_card(self, icon, title, count, color):
        """Crea una tarjeta compacta individual para mostrar una estadística."""
        card = QFrame()
        card.setStyleSheet(f"""
            QFrame {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 {self.add_transparency(color, 0.8)}, stop:1 {self.add_transparency(self.darken_color(color), 0.8)});
                border-radius: 10px;
                border: 1px solid rgba(255, 255, 255, 0.3);
                box-shadow: 0 3px 10px rgba(0, 0, 0, 0.06);
            }}
            QFrame:hover {{
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            }}
        """)
        
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(10, 10, 10, 10)
        card_layout.setSpacing(6)
        
        # Icono (más pequeño)
        icon_label = QLabel(icon)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                color: white;
                margin-bottom: 2px;
            }
        """)
        card_layout.addWidget(icon_label)
        
        # Número (más pequeño)
        count_label = QLabel(str(count))
        count_label.setAlignment(Qt.AlignCenter)
        count_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 20px;
                font-weight: bold;
                margin: 2px 0;
            }
        """)
        card_layout.addWidget(count_label)
        
        # Título (más pequeño)
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 10px;
                font-weight: bold;
                letter-spacing: 0.5px;
            }
        """)
        card_layout.addWidget(title_label)
        
        card.setLayout(card_layout)
        return card

    def create_stat_card(self, icon, title, count, color):
        """Crea una tarjeta individual para mostrar una estadística."""
        card = QFrame()
        card.setStyleSheet(f"""
            QFrame {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 {color}, stop:1 {self.darken_color(color)});
                border-radius: 15px;
                border: 1px solid rgba(255, 255, 255, 0.2);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            }}
            QFrame:hover {{
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
                transform: translateY(-2px);
            }}
        """)
        
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(15, 15, 15, 15)
        card_layout.setSpacing(10)
        
        # Icono
        icon_label = QLabel(icon)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("""
            QLabel {
                font-size: 40px;
                color: white;
                margin-bottom: 5px;
            }
        """)
        card_layout.addWidget(icon_label)
        
        # Número
        count_label = QLabel(str(count))
        count_label.setAlignment(Qt.AlignCenter)
        count_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 36px;
                font-weight: bold;
                margin: 5px 0;
            }
        """)
        card_layout.addWidget(count_label)
        
        # Título
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 14px;
                font-weight: bold;
                letter-spacing: 1px;
            }
        """)
        card_layout.addWidget(title_label)
        
        card.setLayout(card_layout)
        return card

    def darken_color(self, color):
        """Oscurece un color hexadecimal para crear gradientes."""
        color_map = {
            "#4CAF50": "#388E3C",
            "#2196F3": "#1976D2", 
            "#FF9800": "#F57C00",
            "#E91E63": "#C2185B"
        }
        return color_map.get(color, color)

    def add_transparency(self, color, alpha):
        """Convierte un color hexadecimal a rgba con transparencia."""
        # Convertir hex a RGB
        hex_color = color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        
        # Aplicar transparencia
        alpha_int = int(alpha * 255)
        return f"rgba({r}, {g}, {b}, {alpha})"

    def update_dashboard_stats(self):
        """Actualiza las estadísticas del dashboard."""
        try:
            stats = self.db.get_dashboard_stats()
            turno_stats = self.db.get_students_by_turno()  # Añadido para actualizar tarjetas de turnos
            # Actualizar cada tarjeta
            if hasattr(self, 'stats_cards') and self.stats_cards:
                # Buscar y actualizar los labels de conteo en cada tarjeta
                for card_name, card in self.stats_cards.items():
                    labels = card.findChildren(QLabel)
                    if len(labels) >= 2:
                        count_label = labels[1]
                        if card_name == 'estudiantes':
                            count_label.setText(str(stats['estudiantes']))
                        elif card_name == 'representantes':
                            count_label.setText(str(stats['representantes']))
                        elif card_name == 'mañana':
                            count_label.setText(str(turno_stats.get('Mañana', 0)))
                        elif card_name == 'tarde':
                            count_label.setText(str(turno_stats.get('Tarde', 0)))
        except Exception as e:
            print(f"Error actualizando estadísticas: {e}")