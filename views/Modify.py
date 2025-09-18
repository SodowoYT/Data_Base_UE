from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QButtonGroup, QMainWindow, QStackedWidget, QGridLayout, QGroupBox, QSizePolicy, QSpacerItem, QFileDialog
from viewmodels.ModifyW import ModifyViewModel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QIcon
from PySide6.QtWidgets import QDateEdit
from PySide6.QtCore import QDate
import sqlite3

# Clase para el widget de fondo
class BgWidget(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image = QPixmap(image_path)

    # Función para pintar el fondo
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

class ModifyData(QMainWindow):
    def __init__(self):
        super().__init__()

        # Inicializar el ViewModel
        self.viewmodel = ModifyViewModel()

        # Inicializar atributos de imagen para evitar AttributeError
        self.estudianteIMGpath = None
        self.vacunaIMGpath = None
        self.rpstIMGpath = None
        self.estudianteIMGdata = None
        self.vacunaIMGdata = None
        self.rpstIMGdata = None

        # Propiedades de la ventana
        self.setWindowTitle("Datos del Estudiante")
        self.setWindowIcon(QIcon("utilities/resources/imgs/ico/IconApp.ico"))
        self.setGeometry(100, 100, 1000, 600)
        # Establecer imagen de fondo
        ## Establecer el estilo de la ventana
        self.setStyleSheet("""
            .tituloz {
                color: white;
                font-family: Monotype Corsiva, Times, Serif; 
                font-size: 28px;
                font-weight: bold;
                padding: 8px 24px 8px 16px;
                border-top-left-radius: 10px;
                border-bottom-left-radius: 10px;
                border-top-right-radius: 0;
                border-bottom-right-radius: 0;
                background: qlineargradient(
                    x1:0, y1:0, x2:0.85, y2:0,
                    stop:0 #14056d, stop:0.85 #0c3f67, stop:0.85 #0d7acf, stop:1 transparent
                );
                margin-bottom: 8px;
            }
            .titulod {
                color: white;
                font-family: Monotype Corsiva, Times, Serif; 
                font-size: 28px;
                font-weight: bold;
                padding: 8px 24px 8px 16px;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
                border-top-left-radius: 0;
                border-bottom-left-radius: 0;
                background: qlineargradient(
                    x1:1, y1:0, x2:0.15, y2:0,
                    stop:0 #14056d, stop:0.85 #0c3f67, stop:0.85 #0d7acf, stop:1 transparent
                );
                margin-bottom: 8px;
            }
            QGroupBox {
                border: 1px solid white;
                border-radius: 8px;
                margin-top: 10px;
                background: transparent;
            }
            QGroupBox::title {
                color: white;
                font-weight: bold;
                font-size: 15px;
                subcontrol-origin: margin;
                subcontrol-position: top left;
            }
            
            QRadioButton {
                color: white;
                font-weight: bold;
            }
            
            QPushButton {
                background-color: #0c3f67;
                color: white;
                border-radius: 15px;
                padding: 8px 0px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color:  #14056d;
            }
            
        """)


        # Crear el widget de fondo
        self.bg_widget = BgWidget("utilities/resources/imgs/bg/BlueBgI.png")
        self.setCentralWidget(self.bg_widget)

        # Layout principal
        self.main_layout = QVBoxLayout(self.bg_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Widget principal de stacked
        self.Sc_Widget = QStackedWidget(self)
        self.main_layout.addWidget(self.Sc_Widget)

        
        # Crear la primera página
        self.page1 = QWidget()
        self.layoutP1 = QGridLayout()

        # Título centrado
        self.title_label1 = QLabel("Datos de Estudiante", self.page1)
        self.title_label1.setAlignment(Qt.AlignCenter)
        self.title_label1.setStyleSheet("""
            font-family: Monotype Corsiva, Times, Serif;
            font-size: 42px;
            font-weight: bold;
            color: #fff;
            background: rgba(12, 63, 103, 0.82);
            border-radius: 18px;
            padding: 18px 32px 18px 32px;
            margin-bottom: 16px;
            border: 2px solid #0d7acf;
            text-shadow: 2px 2px 8px #0c3f67, 0 2px 12px #000;
        """)
        self.layoutP1.addWidget(self.title_label1, 0, 0, 1, 3, Qt.AlignCenter)  # Ocupa 3 columnas

        # Fila 0: Títulos principales
        self.delabel = QLabel("Datos Personales", self)
        self.delabel.setProperty("class", "tituloz")
        self.delabel.setFixedSize(300, 45)
        self.delabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.dmlabel = QLabel("Datos Medicos", self)
        self.dmlabel.setProperty("class", "titulod")
        self.dmlabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.dmlabel.setFixedSize(300, 45)
        self.dmlabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP1.addWidget(self.delabel, 0, 0, Qt.AlignLeft)
        self.layoutP1.addWidget(self.dmlabel, 0, 2, Qt.AlignRight)

        # Fila 1: Grids principales
        self.grid1 = QGridLayout()
        self.nameS = QLineEdit(self)
        self.nameS.setPlaceholderText("Nombres")
        self.grid1.addWidget(self.nameS, 1, 0)
        self.ageS = QLineEdit(self)
        self.ageS.setPlaceholderText("Edad")
        self.grid1.addWidget(self.ageS, 2, 0)
        self.gbl = QGroupBox("Lateralidad", self)
        self.QrBD = QRadioButton("Derecho", self)
        self.QrBI = QRadioButton("Izquierdo", self)
        self.QrBD.setChecked(True)
        self.QhbL = QVBoxLayout()
        self.QhbL.addWidget(self.QrBD)
        self.QhbL.addWidget(self.QrBI)
        self.gbl.setLayout(self.QhbL)
        self.grid1.addWidget(self.gbl, 3, 0)
        self.lastNS = QLineEdit(self)
        self.lastNS.setPlaceholderText("Apellidos")
        self.grid1.addWidget(self.lastNS, 1, 1)
        self.dateofbirth = QDateEdit(self)
        self.dateofbirth.setCalendarPopup(True)          # Habilita el calendario
        self.dateofbirth.setDisplayFormat("dd/MM/yyyy")  # Formato de fecha
        self.dateofbirth.setDate(QDate.currentDate())    # Fecha actual por defecto
        self.grid1.addWidget(self.dateofbirth, 2, 1)
        self.dni = QLineEdit(self)
        self.dni.setPlaceholderText("Cedula Escolar")
        self.grid1.addWidget(self.dni, 1, 2)
        self.gbg = QGroupBox("Género", self)
        self.QrBM = QRadioButton("Masculino", self)
        self.QrBF = QRadioButton("Femenino", self)
        self.QrBM.setChecked(True)
        self.QhbG = QVBoxLayout()
        self.QhbG.addWidget(self.QrBM)
        self.QhbG.addWidget(self.QrBF)
        self.gbg.setLayout(self.QhbG)
        self.grid1.addWidget(self.gbg, 2, 2)
        self.Nofs = QLineEdit(self)
        self.Nofs.setPlaceholderText("Número de Hermanos")
        self.grid1.addWidget(self.Nofs, 3, 1)
        self.authorizeRC = QLineEdit(self)
        self.authorizeRC.setPlaceholderText("Autorizado para retirar al niño/a")
        self.grid1.addWidget(self.authorizeRC, 3, 2)
        self.layoutP1.addLayout(self.grid1, 1, 0, Qt.AlignTop)
        
        # Variable para la imagen del Estudiante
        self.EIMG = None
        self.PushbuttonEIMG = QPushButton("Subir Imagen de Estudiante", self)
        self.PushbuttonEIMG.clicked.connect(self.upload_estudiante_image)
        self.grid1.addWidget(self.PushbuttonEIMG, 4, 0,)

        self.estudianteIMG = QLabel(self)
        self.estudianteIMG.setFixedSize(100, 100)
        self.estudianteIMG.setScaledContents(True)
        self.grid1.addWidget(self.estudianteIMG, 4, 1 )
        
        # Fila 2: Título de Datos Médicos
        self.grid2 = QGridLayout()
        self.ala = QLineEdit(self)
        self.ala.setPlaceholderText("Alergico a")
        self.grid2.addWidget(self.ala, 1, 0)
        self.gbad = QGroupBox("¿Alguna dificultad?", self)
        self.QrBY = QRadioButton("Si", self)
        self.QrBN = QRadioButton("No", self)
        self.QrBY.setChecked(True)
        self.Qhbad = QVBoxLayout()
        self.Qhbad.addWidget(self.QrBY)
        self.Qhbad.addWidget(self.QrBN)
        self.gbad.setLayout(self.Qhbad)
        self.grid2.addWidget(self.gbad, 2, 0)
        self.epdf = QLineEdit(self)
        self.epdf.setPlaceholderText("Especificar Dificultad")
        self.grid2.addWidget(self.epdf, 2, 1)
        self.tds = QLineEdit(self)
        self.tds.setPlaceholderText("Tipo de Sangre")
        self.grid2.addWidget(self.tds, 1, 1)
        
        # Variable para la imagen de la vacuna
        self.vacunaIMGpath = None
        self.PushbuttonVacuna = QPushButton("Subir Imagen de Vacuna", self)
        self.PushbuttonVacuna.clicked.connect(self.upload_vacuna_image)
        self.grid2.addWidget(self.PushbuttonVacuna, 4, 1)
        
        self.vacunaIMG = QLabel(self)
        self.vacunaIMG.setFixedSize(100, 100)
        self.vacunaIMG.setScaledContents(True)
        self.grid2.addWidget(self.vacunaIMG, 4, 0, Qt.AlignRight)

        
        self.exdh = QLineEdit(self)
        self.exdh.setPlaceholderText("Examen de Heces")
        self.grid2.addWidget(self.exdh, 3, 1)
        self.layoutP1.addLayout(self.grid2, 1, 2, Qt.AlignTop)

        # Fila 3: Título de Datos de Contacto
        self.dclabel = QLabel("Datos de Contacto", self)
        self.dclabel.setProperty("class", "tituloz")
        self.dclabel.setFixedSize(300, 45)
        self.dclabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP1.addWidget(self.dclabel, 2, 0, Qt.AlignLeft)

        # Fila 4 Grid de Datos de Contacto
        self.grid3 = QGridLayout()
        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Correo Electrónico")
        self.grid3.addWidget(self.email, 1, 0)
        self.dra = QLineEdit(self)
        self.dra.setPlaceholderText("Dirección Actual")
        self.grid3.addWidget(self.dra, 2, 0)
        self.tfh = QLineEdit(self)
        self.tfh.setPlaceholderText("Teléfono de Habitación")
        self.grid3.addWidget(self.tfh, 1, 1)
        self.layoutP1.addLayout(self.grid3, 3, 0, Qt.AlignTop)

        # Fila 5: Título de Tallas
        self.tlabel = QLabel("Tallas", self)
        self.tlabel.setProperty("class", "tituloz")
        self.tlabel.setFixedSize(300, 45)
        self.tlabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP1.addWidget(self.tlabel, 4, 0, Qt.AlignLeft)

        # Fila 6: Grid de Tallas
        self.grid5 = QGridLayout()
        self.alt = QLineEdit(self)
        self.alt.setPlaceholderText("Altura")
        self.grid5.addWidget(self.alt, 1, 0)
        self.tza = QLineEdit(self)
        self.tza.setPlaceholderText("Talla de Zapatos")
        self.grid5.addWidget(self.tza, 2, 0)
        self.tpan = QLineEdit(self)
        self.tpan.setPlaceholderText("Talla de Pantalón")
        self.grid5.addWidget(self.tpan, 3, 0)
        self.kg = QLineEdit(self)
        self.kg.setPlaceholderText("Peso")
        self.grid5.addWidget(self.kg, 1, 1)
        self.tca = QLineEdit(self)
        self.tca.setPlaceholderText("Talla de Camisa")
        self.grid5.addWidget(self.tca, 2, 1)
        self.layoutP1.addLayout(self.grid5, 5, 0, Qt.AlignTop)

        # Fila 7: Título de Ubicación
        self.ulabel = QLabel("Ubicación", self)
        self.ulabel.setProperty("class", "titulod")
        self.ulabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.ulabel.setFixedSize(300, 45)
        self.ulabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP1.addWidget(self.ulabel, 2, 2, Qt.AlignRight)

        # Fila 8: Grid de Ubicación
        self.grid4 = QGridLayout()
        self.ncl = QLineEdit(self)
        self.ncl.setPlaceholderText("Nacionalidad")
        self.grid4.addWidget(self.ncl, 1, 1)
        self.est = QLineEdit(self)
        self.est.setPlaceholderText("Estado")
        self.grid4.addWidget(self.est, 2, 1)
        self.mun = QLineEdit(self)
        self.mun.setPlaceholderText("Municipio")
        self.grid4.addWidget(self.mun, 3, 1)
        self.pdr = QLineEdit(self)
        self.pdr.setPlaceholderText("Punto de Referencia")
        self.grid4.addWidget(self.pdr, 1, 0)
        self.layoutP1.addLayout(self.grid4, 3, 2, Qt.AlignTop)
        
        # Fila 9: Titulo Observaciones
        self.olabel = QLabel("Observaciones", self)
        self.olabel.setProperty("class", "titulod")
        self.olabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.olabel.setFixedSize(300, 45)
        self.olabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP1.addWidget(self.olabel, 4, 2, Qt.AlignRight)
        
        # Fila 10: Grid de Observaciones
        self.grid15 = QGridLayout()
        self.obs1 = QTextEdit(self)
        self.obs1.setPlaceholderText("Observaciones")
        self.obs1.setFixedHeight(80)
        self.grid15.addWidget(self.obs1, 1, 0)
        self.layoutP1.addLayout(self.grid15, 5, 2, Qt.AlignTop)

        # Boton de Next a la Pagina 2
        self.NextP = QPushButton("Siguiente Pagina")
        self.NextP.clicked.connect(self.RegisterPage2)
        self.layoutP1.addWidget(self.NextP, 9, 1)
        self.page1.setLayout(self.layoutP1)

        # Espaciador entre columnas si lo necesitas
        self.layoutP1.addItem(QSpacerItem(200, 20, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1, 8, 1)

        # Muestra los items en la ventana 1
        self.page1.setLayout(self.layoutP1)
        self.Sc_Widget.addWidget(self.page1)


        # Crear la segunda página
        self.page2 = QWidget()
        self.layoutP2 = QGridLayout()
        
        # Título centrado
        self.title_label2 = QLabel("Datos del Representante", self.page2)
        self.title_label2.setAlignment(Qt.AlignCenter)
        self.title_label2.setStyleSheet("""
            font-family: Monotype Corsiva, Times, Serif;
            font-size: 42px;
            font-weight: bold;
            color: #fff;
            background: rgba(12, 63, 103, 0.82);
            border-radius: 18px;
            padding: 18px 32px 18px 32px;
            margin-bottom: 16px;
            border: 2px solid #0d7acf;
            text-shadow: 2px 2px 8px #0c3f67, 0 2px 12px #000;
        """)
        self.layoutP2.addWidget(self.title_label2, 0, 0, 1, 3, Qt.AlignCenter)  # Ocupa 3 columnas

        
        # Fila 0: Títulos Tabla Representante
        self.Rplabel = QLabel("Datos Personales", self)
        self.Rplabel.setProperty("class", "tituloz")
        self.Rplabel.setFixedSize(400, 45)
        self.Rplabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.dclabel = QLabel("Datos de Contacto", self)
        self.dclabel.setProperty("class", "titulod")
        self.dclabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.dclabel.setFixedSize(400, 45)
        self.dclabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP2.addWidget(self.Rplabel, 0, 0, Qt.AlignLeft)
        self.layoutP2.addWidget(self.dclabel, 0, 2, Qt.AlignRight)
        
        # Fila 1: Grid 6 Datos Personales Representante
        self.grid6 = QGridLayout()
        self.nameR = QLineEdit(self)
        self.nameR.setPlaceholderText("Nombres")
        self.grid6.addWidget(self.nameR, 1, 0)
        self.lastNR = QLineEdit(self)
        self.lastNR.setPlaceholderText("Apellidos")
        self.grid6.addWidget(self.lastNR, 1, 1)
        self.ageR = QLineEdit(self)
        self.ageR.setPlaceholderText("Edad")
        self.grid6.addWidget(self.ageR, 2, 0)
        self.dniR = QLineEdit(self)
        self.dniR.setPlaceholderText("Cedula")
        self.grid6.addWidget(self.dniR, 2, 1)
        self.dateofbirthR = QDateEdit(self)
        self.dateofbirthR.setCalendarPopup(True)
        self.dateofbirthR.setDisplayFormat("dd/MM/yyyy")
        self.dateofbirthR.setDate(QDate.currentDate())
        self.grid6.addWidget(self.dateofbirthR, 2, 2)

        #### FOTO DEL REPRESENTANTE ####

        self.rpstIMGpath = None
        self.Pushbuttonrpst = QPushButton("Subir foto de representante", self)
        self.Pushbuttonrpst.clicked.connect(self.upload_representante_image)
        self.grid6.addWidget(self.Pushbuttonrpst, 5, 0)

        self.rpstIMG = QLabel(self)
        self.rpstIMG.setFixedSize(100, 100)
        self.rpstIMG.setScaledContents(True)
        self.grid6.addWidget(self.rpstIMG, 5, 1)

        # Boton Marital Status
        self.MaritalStatus = QGroupBox("Estado Civil", self)
        self.QrBS = QRadioButton("Soltero", self)
        self.QrBC = QRadioButton("Casado", self)
        self.QrBD = QRadioButton("Divorciado", self)
        self.QrBS.setChecked(True)
        self.QvbMaritalStatus = QVBoxLayout()
        self.QvbMaritalStatus.addWidget(self.QrBS)
        self.QvbMaritalStatus.addWidget(self.QrBC)
        self.QvbMaritalStatus.addWidget(self.QrBD)
        self.MaritalStatus.setLayout(self.QvbMaritalStatus)
        self.grid6.addWidget(self.MaritalStatus, 3, 0)
        # Final del Boton Marital Status
        
        self.Affi = QLineEdit(self)
        self.Affi.setPlaceholderText("Afinidad")
        self.grid6.addWidget(self.Affi, 4, 1)
        self.Rif = QLineEdit(self)
        self.Rif.setPlaceholderText("RIF")
        self.grid6.addWidget(self.Rif, 4, 0)
        
        # Boton Planilla Sige
        self.Sheet = QGroupBox("Planilla Sige", self)
        self.QrBSi = QRadioButton("Si", self)
        self.QrBNo = QRadioButton("No", self)
        self.QrBSi.setChecked(True)
        self.QvbSheet = QVBoxLayout()
        self.QvbSheet.addWidget(self.QrBSi)
        self.QvbSheet.addWidget(self.QrBNo)
        self.Sheet.setLayout(self.QvbSheet)
        self.grid6.addWidget(self.Sheet, 3, 1)
        self.layoutP2.addLayout(self.grid6, 1, 0, Qt.AlignTop)
        # Final del Boton Planilla Sige
        
        # Fila 2: Grid 7 Datos de Contacto Representante
        self.grid7 = QGridLayout()
        self.PhoneM = QLineEdit(self)
        self.PhoneM.setPlaceholderText("Teléfono Móvil")
        self.grid7.addWidget(self.PhoneM, 1, 0)
        self.PhoneR = QLineEdit(self)
        self.PhoneR.setPlaceholderText("Teléfono Habitación")
        self.grid7.addWidget(self.PhoneR, 1, 1)
        self.EmailR = QLineEdit(self)
        self.EmailR.setPlaceholderText("Correo Electronico")
        self.grid7.addWidget(self.EmailR, 2, 0)
        self.PhoneF = QLineEdit(self)
        self.PhoneF.setPlaceholderText("Teléfono de un Familiar")
        self.grid7.addWidget(self.PhoneF, 2, 1)
        self.NclR = QLineEdit(self)
        self.NclR.setPlaceholderText("Nacionalidad")
        self.grid7.addWidget(self.NclR, 3, 0)
        self.DrR = QLineEdit(self)
        self.DrR.setPlaceholderText("Dirección")
        self.grid7.addWidget(self.DrR, 3, 1)
        self.CodeP = QLineEdit(self)
        self.CodeP.setPlaceholderText("Codigo Patria")
        self.grid7.addWidget(self.CodeP, 4, 0)
        self.Serial = QLineEdit(self)
        self.Serial.setPlaceholderText("Serial de la Patria")
        self.grid7.addWidget(self.Serial, 4, 1)
        self.layoutP2.addLayout(self.grid7, 1, 2, Qt.AlignTop)
        
        # Fila 3: Grid 8 Datos de Profesión
        ## Titulo Grid 8
        self.Rplabel = QLabel("Datos de Profesión")
        self.Rplabel.setProperty("class", "tituloz")
        self.Rplabel.setFixedSize(300, 45)
        self.Rplabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP2.addWidget(self.Rplabel, 2, 0, Qt.AlignLeft)
        # Elementos Grid 8
        self.grid8 = QGridLayout()
        self.Pfson = QLineEdit(self)
        self.Pfson.setPlaceholderText("Profesión")
        self.grid8.addWidget(self.Pfson, 1, 0)
        self.Occu = QLineEdit()
        self.Occu.setPlaceholderText("Ocupación")
        self.grid8.addWidget(self.Occu, 1, 1)
        self.Epdt = QLineEdit()
        self.Epdt.setPlaceholderText("Empresa donde Trabaja")
        self.grid8.addWidget(self.Epdt, 2, 0)
        self.layoutP2.addLayout(self.grid8, 3, 0, Qt.AlignTop)
        
        
        # Boton de Back a la Pagina 1
        self.backBt = QPushButton("Pagina Anterior")
        self.backBt.clicked.connect(self.RegisterPage1)
        self.layoutP2.addWidget(self.backBt, 5, 1)  # Agrega el botón después de crearlo
        self.page2.setLayout(self.layoutP2)
        
        # Boton de Next a la Pagina 2
        self.NextP3 = QPushButton("Siguiente Pagina")
        self.NextP3.clicked.connect(self.RegisterPage3)
        self.layoutP2.addWidget(self.NextP3, 4, 1)
        self.page2.setLayout(self.layoutP2)
        
        # Espaciador entre columnas 
        self.layoutP2.addItem(QSpacerItem(200, 20, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1, 5, 1)
        
        # Muestra los Items en la Ventana 2
        self.page2.setLayout(self.layoutP2)
        self.Sc_Widget.addWidget(self.page2)
        
        # Crear La Tercera Pagina
        self.page3 = QWidget()
        self.layoutP3 = QGridLayout()
        
        # Título centrado 
        self.title_label3 = QLabel("Datos del Padre", self.page3)
        self.title_label3.setAlignment(Qt.AlignCenter)
        self.title_label3.setStyleSheet("""
            font-family: Monotype Corsiva, Times, Serif;
            font-size: 42px;
            font-weight: bold;
            color: #fff;
            background: rgba(12, 63, 103, 0.82);
            border-radius: 18px;
            padding: 18px 32px 18px 32px;
            margin-bottom: 16px;
            border: 2px solid #0d7acf;
            text-shadow: 2px 2px 8px #0c3f67, 0 2px 12px #000;
        """)
        self.layoutP3.addWidget(self.title_label3, 0, 0, 1, 3, Qt.AlignCenter)  # Ocupa 3 columnas
        
        # Fila 0: Titulos Tabla Datos del Padre.
        self.dpLabel = QLabel("Datos Personales", self)
        self.dpLabel.setProperty("class", "tituloz")
        self.dpLabel.setFixedSize(300, 45)
        self.dpLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.dclabel = QLabel("Datos de Contacto", self)
        self.dclabel.setProperty("class", "titulod")
        self.dclabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.dclabel.setFixedSize(300, 45)
        self.dclabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP3.addWidget(self.dpLabel, 0, 0, Qt.AlignLeft)
        self.layoutP3.addWidget(self.dclabel, 0, 2, Qt.AlignRight)
        
        # Fila 1: Grid 9 Datos Personales
        self.grid9 = QGridLayout()
        self.nameP = QLineEdit(self)
        self.nameP.setPlaceholderText("Nombres")
        self.grid9.addWidget(self.nameP, 1, 0)
        self.lastNP = QLineEdit(self)
        self.lastNP.setPlaceholderText("Apellidos")
        self.grid9.addWidget(self.lastNP, 1, 1)
        self.ageP = QLineEdit(self)
        self.ageP.setPlaceholderText("Edad")
        self.grid9.addWidget(self.ageP, 2, 0)
        self.dniP = QLineEdit(self)
        self.dniP.setPlaceholderText("Cedula")
        self.grid9.addWidget(self.dniP, 2, 1)
        self.dateofbirthP = QDateEdit(self)
        self.dateofbirthP.setCalendarPopup(True)
        self.dateofbirthP.setDisplayFormat("dd/MM/yyyy")
        self.dateofbirthP.setDate(QDate.currentDate())
        self.grid9.addWidget(self.dateofbirthP, 2, 2)

        # Boton Vive Con el Niño
        self.lwtc = QGroupBox("¿Vive Con el Niño?")
        self.QrPSi = QRadioButton("Si")
        self.QrPNo = QRadioButton("No")
        self.QrPSi.setChecked(True)
        self.QvLwtc = QVBoxLayout()
        self.QvLwtc.addWidget(self.QrPSi)
        self.QvLwtc.addWidget(self.QrPNo)
        self.lwtc.setLayout(self.QvLwtc)
        self.grid9.addWidget(self.lwtc, 3, 0)
        # Final del Boton Vive Con el Niño
        
        self.Cnn = QLineEdit(self)
        self.Cnn.setPlaceholderText("¿Causa por la que no vive con el Niño?")
        self.grid9.addWidget(self.Cnn, 4, 0)
        self.layoutP3.addLayout(self.grid9, 1, 0, Qt.AlignLeft)
        
        # Fila 2: Grid 10 Datos de Contacto
        self.grid10 = QGridLayout()
        self.PhoneMp = QLineEdit(self)
        self.PhoneMp.setPlaceholderText("Telélefono Móvil")
        self.grid10.addWidget(self.PhoneMp, 1, 0)
        self.Dcp = QLineEdit(self)
        self.Dcp.setPlaceholderText("Dirección")
        self.grid10.addWidget(self.Dcp, 2, 0)
        self.layoutP3.addLayout(self.grid10, 1, 2, Qt.AlignTop)
        
        # Fila 3: Titulo Datos de Profesion
        self.Plabel = QLabel("Datos de Profesión")
        self.Plabel.setProperty("class", "tituloz")
        self.Plabel.setFixedSize(300, 45)
        self.Plabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP3.addWidget(self.Plabel, 2, 0, Qt.AlignLeft)
        
        # Fila 3: Grid 11 Datos de Profesion
        self.grid11 = QGridLayout()
        self.Empdt = QLineEdit(self)
        self.Empdt.setPlaceholderText("Emprensa donde Trabaja")
        self.grid11.addWidget(self.Empdt, 1, 0)
        self.Ted = QLineEdit(self)
        self.Ted.setPlaceholderText("Tipo de Empleo que Desempeña")
        self.grid11.addWidget(self.Ted, 2, 0)
        self.layoutP3.addLayout(self.grid11, 3, 0, Qt.AlignTop)
        
        # Boton de Back a la Pagina 2
        self.backP2 = QPushButton("Pagina Anterior")
        self.backP2.clicked.connect(self.RegisterPage2)
        self.layoutP3.addWidget(self.backP2, 6, 1)
        self.page3.setLayout(self.layoutP3)
        
        # Boton de Next a la Pagina 4
        self.NextP4 = QPushButton("Siguiente Pagina")
        self.NextP4.clicked.connect(self.RegisterPage4)
        self.layoutP3.addWidget(self.NextP4, 5, 1)
        self.page3.setLayout(self.layoutP3)
        
        # Espaciador entre columnas
        self.layoutP3.addItem(QSpacerItem(200, 20, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1, 6, 1)
        
        # Muestra los Items en la Ventana 3
        self.page3.setLayout(self.layoutP3)
        self.Sc_Widget.addWidget(self.page3)
        
        
        # Crear La Cuarta Pagina
        self.page4 = QWidget()
        self.layoutP4 = QGridLayout()
        
        # Título centrado
        self.title_label4 = QLabel("Datos de Madre", self.page4)
        self.title_label4.setAlignment(Qt.AlignCenter)
        self.title_label4.setStyleSheet("""
            font-family: Monotype Corsiva, Times, Serif;
            font-size: 42px;
            font-weight: bold;
            color: #fff;
            background: rgba(12, 63, 103, 0.82);
            border-radius: 18px;
            padding: 18px 32px 18px 32px;
            margin-bottom: 16px;
            border: 2px solid #0d7acf;
            text-shadow: 2px 2px 8px #0c3f67, 0 2px 12px #000;
        """)
        self.layoutP4.addWidget(self.title_label4, 0, 0, 1, 3, Qt.AlignCenter)  # Ocupa 3 columnas
        # Fila 0: Titutlos Tabla Datos del Madre.
        self.dpLabel = QLabel("Datos Personales", self)
        self.dpLabel.setProperty("class", "tituloz")
        self.dpLabel.setFixedSize(300, 45)
        self.dpLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.dclabel = QLabel("Datos de Contacto", self)
        self.dclabel.setProperty("class", "titulod")
        self.dclabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.dclabel.setFixedSize(300, 45)
        self.dclabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP4.addWidget(self.dpLabel, 0, 0, Qt.AlignLeft)
        self.layoutP4.addWidget(self.dclabel, 0, 2, Qt.AlignRight)
        
        # Fila 1: Grid 12 Datos Personales
        self.grid12 = QGridLayout()
        self.nameM = QLineEdit(self)
        self.nameM.setPlaceholderText("Nombres")
        self.grid12.addWidget(self.nameM, 1, 0)
        self.lastNM = QLineEdit(self)
        self.lastNM.setPlaceholderText("Apellidos")
        self.grid12.addWidget(self.lastNM, 1, 1)
        self.ageM = QLineEdit(self)
        self.ageM.setPlaceholderText("Edad")
        self.grid12.addWidget(self.ageM, 2, 0)
        self.dniM = QLineEdit(self)
        self.dniM.setPlaceholderText("Cedula")
        self.grid12.addWidget(self.dniM, 2, 1)
        self.dateofbirthM = QDateEdit(self)
        self.dateofbirthM.setCalendarPopup(True)
        self.dateofbirthM.setDisplayFormat("dd/MM/yyyy")
        self.dateofbirthM.setDate(QDate.currentDate())
        self.grid12.addWidget(self.dateofbirthM, 2, 2)


        # Boton Vive Con el Niño
        self.lwtc = QGroupBox("¿Vive Con el Niño?")
        self.QrPSi = QRadioButton("Si")
        self.QrPNo = QRadioButton("No")
        self.QrPSi.setChecked(True)
        self.QvLwtc = QVBoxLayout()
        self.QvLwtc.addWidget(self.QrPSi)
        self.QvLwtc.addWidget(self.QrPNo)
        self.lwtc.setLayout(self.QvLwtc)
        self.grid12.addWidget(self.lwtc, 3, 0)
        # Final del Boton Vive Con el Niño
        
        self.CnnM = QLineEdit(self)
        self.CnnM.setPlaceholderText("¿Causa por la que no vive con el Niño?")
        self.grid12.addWidget(self.CnnM, 4, 0)
        self.layoutP4.addLayout(self.grid12, 1, 0, Qt.AlignLeft)
        
        # Fila 2: Grid 13 Datos de Contacto
        self.grid13 = QGridLayout()
        self.PhoneMM = QLineEdit(self)
        self.PhoneMM.setPlaceholderText("Telélefono Móvil")
        self.grid13.addWidget(self.PhoneMM, 1, 0)
        self.DcpM = QLineEdit(self)
        self.DcpM.setPlaceholderText("Dirección")
        self.grid13.addWidget(self.DcpM, 2, 0)
        self.layoutP4.addLayout(self.grid13, 1, 2, Qt.AlignTop)

        # Fila 3: Titulo Datos de Profesion
        self.Mlabel = QLabel("Datos de Profesión")
        self.Mlabel.setProperty("class", "tituloz")
        self.Mlabel.setFixedSize(300, 45)
        self.Mlabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP4.addWidget(self.Mlabel, 2, 0, Qt.AlignLeft)
        
        # Fila 3: Grid 14 Datos de Profesion
        self.grid14 = QGridLayout()
        self.EmpdtM = QLineEdit(self)
        self.EmpdtM.setPlaceholderText("Emprensa donde Trabaja")
        self.grid14.addWidget(self.EmpdtM, 1, 0)
        self.TedM = QLineEdit(self)
        self.TedM.setPlaceholderText("Tipo de Empleo que Desempeña")
        self.grid14.addWidget(self.TedM, 2, 0)
        self.layoutP4.addLayout(self.grid14, 3, 0, Qt.AlignTop)
        
        # Boton de Back a la Pagina 3
        self.backP3 = QPushButton("Pagina Anterior")
        self.backP3.clicked.connect(self.RegisterPage3)
        self.layoutP4.addWidget(self.backP3, 6, 1)
        self.page4.setLayout(self.layoutP4)
        
        # Boton de Registro Final
        self.registerBton = QPushButton("Finalizar Registro")
        self.registerBton.clicked.connect(self.register_estudend)
        self.layoutP4.addWidget(self.registerBton, 5, 1)
        
        # Espaciador entre columnas
        self.layoutP4.addItem(QSpacerItem(200, 20, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1, 6, 1)
        
        # Muestra los Items en la Ventana 3
        self.page4.setLayout(self.layoutP4)
        self.Sc_Widget.addWidget(self.page4)
        
    # Def de Pagina 1
    ## Comando Funcion de Registro en la Pagina 1
    def RegisterPage1(self):
        self.Sc_Widget.setCurrentIndex(0)
        
    # Def de Pagina 2
    ## Comando Funcion de Registro en la Pagina 2
    def RegisterPage2(self):
        self.Sc_Widget.setCurrentIndex(1)
        
    # Def de Pagina 3
    ## Comando Funcion de Registro en la Pagina 3
    def RegisterPage3(self):
        self.Sc_Widget.setCurrentIndex(2)
        
    # Def de Pagina 4
    ## Comando Funcion de Registro en la Pagina 4
    def RegisterPage4(self):
        self.Sc_Widget.setCurrentIndex(3)
    
    # Funcion para registrar estudiante
    def register_estudend(self):
        # Inicio Pagina Estudiante Pagina 1
        nombre = self.nameS.text()
        apellido = self.lastNS.text()
        cedulaEscolar = self.dni.text()
        edad = self.ageS.text()
        genero = "Masculino" if self.QrBM.isChecked() else "Femenino"
        fechaDNacimiento = self.dateofbirth.date().toString("dd/MM/yyyy")
        lateralidad = "Derecho" if self.QrBD.isChecked() else "Izquierdo"
        nacionalidad = self.ncl.text()
        estado = self.est.text()
        municipio = self.mun.text()
        direccionActual = self.dra.text()
        puntoDReferencia = self.pdr.text()
        altura = self.alt.text()
        peso = self.kg.text()
        tallaZapatos = self.tza.text()
        tallaCamisa = self.tca.text()
        tallaPantalon = self.tpan.text()
        numeroDHermanos = self.Nofs.text()
        autorizadoPRetirarANiño = self.authorizeRC.text()
        alergicoA = self.ala.text()
        algunaDificultad = "Si" if self.QrBY.isChecked() else "No"
        especificarDificultad = self.epdf.text() 
        correoElectronico = self.email.text()
        telefonoDHabitacion = self.tfh.text()
        
        # Priorizar nueva imagen si existe, si no, usar la existente
        estIMG = self.estudianteIMGdata
        if self.estudianteIMGpath:
            with open(self.estudianteIMGpath, 'rb') as f:
                estIMG = f.read()

        cartonVacunas = self.vacunaIMGdata
        if self.vacunaIMGpath:
            with open(self.vacunaIMGpath, 'rb') as f:
                cartonVacunas = f.read()

        rpstIMG = self.rpstIMGdata
        if self.rpstIMGpath:
            with open(self.rpstIMGpath, 'rb') as f:
                rpstIMG = f.read()

        tipoDSangre = self.tds.text()
        examenDHeces = self.exdh.text()
        observaciones = self.obs1.toPlainText()
        # Final Pagina Estudiante Pagina 1
        
        # Inicio Pagina Representante Pagina 2
        NombreR = self.nameR.text()
        ApellidoR = self.lastNR.text()
        EdadR = self.ageR.text()
        CedulaR = self.dniR.text()
        FechaDeNacimientoR = self.dateofbirthR.date().toString("dd/MM/yyyy")
        EstadoCivil = "Soltero" if self.QrBS.isChecked() else "Casado" if self.QrBC.isChecked() else "Divorciado"
        Afinidad = self.Affi.text()
        RifR = self.Rif.text()
        PlanillaSigeR = "Si" if self.QrBSi.isChecked() else "No"
        TelefonoMovilR = self.PhoneM.text()
        TelefonoHabitacionR = self.PhoneR.text()
        CorreoElectronicoR = self.EmailR.text()
        TelefonoFamiliarR = self.PhoneF.text()
        NacionalidadR = self.NclR.text()
        DireccionR = self.DrR.text()
        CodigoPatriaR = self.CodeP.text()
        SerialPatriaR = self.Serial.text()
        ProfesionR = self.Pfson.text()
        OcupacionR = self.Occu.text()
        EmpresaDTrabajaR = self.Epdt.text()
        
        # Final Pagina Representante Pagina 2
        
        # Inicio Pagina Padre Pagina 3
        NombreP = self.nameP.text()
        ApellidoP = self.lastNP.text()
        EdadP = self.ageP.text()
        CedulaP = self.dniP.text()
        FechaDNacimientoP = self.dateofbirthP.date().toString("dd/MM/yyyy")
        ViveConElNiñoP = "Si" if self.QrPSi.isChecked() else "No"
        CausaPNoViveP = self.Cnn.text()
        EmpresaDTrabajaP = self.Empdt.text()
        TipoEmpleoqDesempeñaP = self.Ted.text()
        TelefonoMovilP = self.PhoneMp.text()
        DireccionP = self.Dcp.text()
        # Final Pagina Padre Pagina 3
        
        # Inicio Pagina Madre Pagina 4
        NombreM = self.nameM.text()
        ApellidoM = self.lastNM.text()
        EdadM = self.ageM.text()
        CedulaM = self.dniM.text()
        FechaDNacimientoM = self.dateofbirthM.date().toString("dd/MM/yyyy")
        ViveConElNiñoM = "Si" if self.QrPSi.isChecked() else "No"
        CausaPNoViveM = self.CnnM.text()
        EmpresaDTrabajaM = self.EmpdtM.text()
        TipoEmpleoqDesempeñaM = self.TedM.text()
        DireccionM = self.DcpM.text()
        TelefonoMovilM = self.PhoneMM.text()
    
        # Final Pagina Madre Pagina 4
        

        # Validar campos
        if nombre and apellido and cedulaEscolar and edad and fechaDNacimiento and lateralidad and nacionalidad and estado and municipio and direccionActual and puntoDReferencia and altura and peso and tallaZapatos and tallaCamisa and tallaPantalon and numeroDHermanos and autorizadoPRetirarANiño and alergicoA and algunaDificultad and especificarDificultad and correoElectronico and telefonoDHabitacion and estIMG and cartonVacunas and tipoDSangre and examenDHeces and observaciones \
        and NombreR and ApellidoR and EdadR and CedulaR and FechaDeNacimientoR and rpstIMG and EstadoCivil and Afinidad and RifR and PlanillaSigeR and TelefonoMovilR and TelefonoHabitacionR and CorreoElectronicoR and TelefonoFamiliarR and NacionalidadR and DireccionR and CodigoPatriaR and SerialPatriaR \
            and NombreP and ApellidoP and EdadP and CedulaP and FechaDNacimientoP and ViveConElNiñoP and CausaPNoViveP and EmpresaDTrabajaP and TipoEmpleoqDesempeñaP and TelefonoMovilP and DireccionP  \
                and NombreM and ApellidoM and CedulaM and FechaDNacimientoM and EdadM and TipoEmpleoqDesempeñaM and EmpresaDTrabajaM and ViveConElNiñoM and CausaPNoViveM and DireccionM and TelefonoMovilM:

            try:
                # Modificar estudiante
                self.viewmodel.modificar_estudiante(
                    nombre, apellido, cedulaEscolar, edad, genero, fechaDNacimiento, lateralidad, nacionalidad, estado, municipio, direccionActual, puntoDReferencia, altura, peso, tallaZapatos, tallaCamisa, tallaPantalon, numeroDHermanos, autorizadoPRetirarANiño, alergicoA, algunaDificultad, especificarDificultad, correoElectronico, telefonoDHabitacion, estIMG, cartonVacunas, tipoDSangre, examenDHeces, observaciones
                )
                # Modificar representante
                self.viewmodel.modificar_representante(
                    NombreR, ApellidoR, CedulaR, FechaDeNacimientoR, rpstIMG, EdadR, EstadoCivil, NacionalidadR, Afinidad, ProfesionR, OcupacionR, EmpresaDTrabajaR, DireccionR, TelefonoMovilR, TelefonoHabitacionR, TelefonoFamiliarR, CorreoElectronicoR, RifR, PlanillaSigeR, CodigoPatriaR, SerialPatriaR
                )
                # Modificar padre
                self.viewmodel.modificar_padre(
                    NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP, ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP
                )
                # Modificar madre
                self.viewmodel.modificar_madre(
                    NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM
                )
                QMessageBox.information(self, "Éxito", "Datos modificados correctamente.")
                self.close()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar: {e}")
        else:
            QMessageBox.warning(self, "Campos Vacíos", "Por favor, complete todos los campos obligatorios.")
    
    
    ## Funcinamiento correcto     
    # Función para subir la imagen del estudiante
    def upload_estudiante_image(self):
        file_est = QFileDialog(self)
        file_est.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp)")
        if file_est.exec():
            filepath = file_est.selectedFiles()[0]
            self.estudianteIMGpath = filepath
            pixmap = QPixmap(filepath)
            self.estudianteIMG.setPixmap(pixmap.scaled(self.estudianteIMG.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    # Función para subir la imagen del representante
    def upload_representante_image(self):
        file_name_rpst = QFileDialog(self)
        file_name_rpst.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp)")
        if file_name_rpst.exec():
            filepathrpst = file_name_rpst.selectedFiles()[0]
            self.rpstIMGpath = filepathrpst
            pixmaprpst = QPixmap(filepathrpst)
            self.rpstIMG.setPixmap(pixmaprpst.scaled(self.rpstIMG.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))


    # Función para subir la imagen de la vacuna
    def upload_vacuna_image(self):
        file_name = QFileDialog(self)
        file_name.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp)")
        if file_name.exec():
            filepath = file_name.selectedFiles()[0]
            self.vacunaIMGpath = filepath
            pixmap = QPixmap(filepath)
            self.vacunaIMG.setPixmap(pixmap.scaled(self.vacunaIMG.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def cargar_datos_estudiante(self, database, cedula):
        self.database = database
        self.cedula = cedula
        self.datos = self.database.obtener_datos_por_cedula(self.cedula)
        print("Datos cargados:", self.datos)  # Verifica en la consola
        if self.datos:
            # Página 1 (Estudiante)
            self.nameS.setText(str(self.datos.get('NombreS', '')))
            self.lastNS.setText(str(self.datos.get('apellido', '')))
            self.dni.setText(str(self.datos.get('cedulaEscolar', '')))
            self.ageS.setText(str(self.datos.get('edad', '')))
            self.ncl.setText(str(self.datos.get('nacionalidad', '')))
            self.est.setText(str(self.datos.get('estado', '')))
            self.mun.setText(str(self.datos.get('municipio', '')))
            self.dra.setText(str(self.datos.get('direccionActual', '')))
            self.pdr.setText(str(self.datos.get('puntoDReferencia', '')))
            self.alt.setText(str(self.datos.get('altura', '')))
            self.kg.setText(str(self.datos.get('peso', '')))
            self.tza.setText(str(self.datos.get('tallaZapatos', '')))
            self.tca.setText(str(self.datos.get('tallaCamisa', '')))
            self.tpan.setText(str(self.datos.get('tallaPantalon', '')))
            self.Nofs.setText(str(self.datos.get('numeroDHermanos', '')))
            self.authorizeRC.setText(str(self.datos.get('autorizadoPRetirarANiño', '')))
            self.ala.setText(str(self.datos.get('alergicoA', '')))
            self.epdf.setText(str(self.datos.get('especificarDificultad', '')))
            # Cargar imagen del estudiante
            est_img_data = self.datos.get('estIMG', None)
            if est_img_data:
                pixmap = QPixmap()
                pixmap.loadFromData(est_img_data)
                self.estudianteIMG.setPixmap(pixmap)
                self.estudianteIMGdata = est_img_data
            else:
                self.estudianteIMGdata = None

            # Cargar imagen de la vacuna
            vacuna_img_data = self.datos.get('cartonVacunas', None)
            if vacuna_img_data:
                pixmap = QPixmap()
                pixmap.loadFromData(vacuna_img_data)
                self.vacunaIMG.setPixmap(pixmap)
                self.vacunaIMGdata = vacuna_img_data
            else:
                self.vacunaIMGdata = None

            # Cargar imagen del representante
            rpst_img_data = self.datos.get('rpstIMG', None)
            if rpst_img_data:
                pixmap = QPixmap()
                pixmap.loadFromData(rpst_img_data)
                self.rpstIMG.setPixmap(pixmap)
                self.rpstIMGdata = rpst_img_data
            else:
                self.rpstIMGdata = None
            self.tds.setText(str(self.datos.get('tipoDSangre', '')))
            self.exdh.setText(str(self.datos.get('examenDHeces', '')))
            self.email.setText(str(self.datos.get('correoElectronico', '')))
            self.tfh.setText(str(self.datos.get('telefonoDHabitacion', '')))
            self.obs1.setPlainText(str(self.datos.get('observaciones', '')))
            
            # Configurar radio buttons del estudiante
            genero = str(self.datos.get('genero', ''))
            if genero.lower() == 'femenino':
                self.QrBF.setChecked(True)
            else:
                self.QrBM.setChecked(True)
                
            lateralidad = str(self.datos.get('lateralidad', ''))
            if lateralidad.lower() == 'izquierdo':
                self.QrBI.setChecked(True)
            else:
                self.QrBD.setChecked(True)
                
            alguna_dificultad = str(self.datos.get('algunaDificultad', ''))
            if alguna_dificultad.lower() == 'no':
                self.QrBN.setChecked(True)
            else:
                self.QrBY.setChecked(True)
            
            # Página 2 (Representante)
            self.nameR.setText(str(self.datos.get('nombreR', '')))
            self.lastNR.setText(str(self.datos.get('apellidoR', '')))
            self.dateofbirthR.setDate(QDate.fromString(self.datos.get('fechaDeNacimientoR', ''), "dd/MM/yyyy"))
            self.rpstIMG.setText(str(self.datos.get('rpstIMG', '')))
            self.ageR.setText(str(self.datos.get('edadR', '')))
            self.dniR.setText(str(self.datos.get('cedulaR', '')))
            self.Affi.setText(str(self.datos.get('afinidad', '')))
            self.Rif.setText(str(self.datos.get('rifR', '')))
            self.PhoneM.setText(str(self.datos.get('telefonoMovilR', '')))
            self.PhoneR.setText(str(self.datos.get('telefonoHabitacionR', '')))
            self.EmailR.setText(str(self.datos.get('correoElectronicoR', '')))
            self.PhoneF.setText(str(self.datos.get('telefonoFamiliarR', '')))
            self.NclR.setText(str(self.datos.get('nacionalidadR', '')))
            self.DrR.setText(str(self.datos.get('direccionR', '')))
            self.CodeP.setText(str(self.datos.get('codigoPatriaR', '')))
            self.Serial.setText(str(self.datos.get('serialPatriaR', '')))
            self.Pfson.setText(str(self.datos.get('profesionR', '')))
            self.Occu.setText(str(self.datos.get('ocupacionR', '')))
            self.Epdt.setText(str(self.datos.get('empresaDTrabajaR', '')))
            
            # Configurar radio buttons del representante
            estado_civil = str(self.datos.get('estadoCivilR', ''))
            if estado_civil.lower() == 'casado':
                self.QrBC.setChecked(True)
            elif estado_civil.lower() == 'divorciado':
                self.QrBD.setChecked(True)
            else:
                self.QrBS.setChecked(True)
                
            planilla_sige = str(self.datos.get('planillaSigeR', ''))
            if planilla_sige.lower() == 'no':
                self.QrBNo.setChecked(True)
            else:
                self.QrBSi.setChecked(True)
            
            # Página 3 (Padre)
            self.nameP.setText(str(self.datos.get('nombreP', '')))
            self.lastNP.setText(str(self.datos.get('apellidoP', '')))
            self.ageP.setText(str(self.datos.get('edadP', '')))
            self.dniP.setText(str(self.datos.get('cedulaP', '')))
            self.Cnn.setText(str(self.datos.get('causaPNoViveP', '')))
            self.PhoneMp.setText(str(self.datos.get('telefonoMovilP', '')))
            self.Dcp.setText(str(self.datos.get('direccionP', '')))
            self.Empdt.setText(str(self.datos.get('empresaDTrabajaP', '')))
            self.Ted.setText(str(self.datos.get('tipoEmpleoP', '')))
            
            # Configurar radio buttons del padre
            vive_con_nino = str(self.datos.get('viveConNinoP', ''))
            if vive_con_nino.lower() == 'no':
                self.QrPNo.setChecked(True)
            else:
                self.QrPSi.setChecked(True)
            
            # Página 4 (Madre)
            self.nameM.setText(str(self.datos.get('nombreM', '')))
            self.lastNM.setText(str(self.datos.get('apellidoM', '')))
            self.ageM.setText(str(self.datos.get('edadM', '')))
            self.dniM.setText(str(self.datos.get('cedulaM', '')))
            self.CnnM.setText(str(self.datos.get('causaPNoViveM', '')))
            self.PhoneMM.setText(str(self.datos.get('telefonoMovilM', '')))
            self.DcpM.setText(str(self.datos.get('direccionM', '')))
            self.EmpdtM.setText(str(self.datos.get('empresaDTrabajaM', '')))
            self.TedM.setText(str(self.datos.get('tipoEmpleoM', '')))
            
            # Configurar radio buttons de la madre
            vive_con_nino_m = str(self.datos.get('viveConNinoM', ''))
            if vive_con_nino_m.lower() == 'no':
                self.QrPNo.setChecked(True)
            else:
                self.QrPSi.setChecked(True)
                
        else:
            QMessageBox.warning(self, "Error", "No se encontraron datos para la cédula seleccionada.")

    def guardar_cambios(self):
        # Recoge los datos editados de todos los QLineEdit
        datos_editados = {
            'NombreS': self.nameS.text(),
            'apellido': self.lastNS.text(),
            'cedulaEscolar': self.dni.text(),
            'edad': self.ageS.text(),
            'nacionalidad': self.ncl.text(),
            'estado': self.est.text(),
            'municipio': self.mun.text(),
            'direccionActual': self.dra.text(),
            'puntoDReferencia': self.pdr.text(),
            'altura': self.alt.text(),
            'peso': self.kg.text(),
            'tallaZapatos': self.tza.text(),
            'tallaCamisa': self.tca.text(),
            'tallaPantalon': self.tpan.text(),
            'numeroDHermanos': self.Nofs.text(),
            'autorizadoPRetirarANiño': self.authorizeRC.text(),
            'alergicoA': self.ala.text(),
            'especificarDificultad': self.epdf.text(),
            'estIMG': self.estudianteIMG.text(),
            'cartonVacunas': self.vacunaIMG.text(),
            'tipoDSangre': self.tds.text(),
            'examenDHeces': self.exdh.text(),
            'correoElectronico': self.email.text(),
            'telefonoDHabitacion': self.tfh.text(),
            'observaciones': self.obs1.toPlainText(),
            # Representante
            'nombreR': self.nameR.text(),
            'apellidoR': self.lastNR.text(),
            'edadR': self.ageR.text(),
            'rpstIMG': self.rpstIMG.text(),
            'cedulaR': self.dniR.text(),
            'afinidad': self.Affi.text(),
            'rifR': self.Rif.text(),
            'telefonoMovilR': self.PhoneM.text(),
            'telefonoHabitacionR': self.PhoneR.text(),
            'correoElectronicoR': self.EmailR.text(),
            'telefonoFamiliarR': self.PhoneF.text(),
            'nacionalidadR': self.NclR.text(),
            'direccionR': self.DrR.text(),
            'codigoPatriaR': self.CodeP.text(),
            'serialPatriaR': self.Serial.text(),
            'profesionR': self.Pfson.text(),
            'ocupacionR': self.Occu.text(),
            'empresaDTrabajaR': self.Epdt.text(),
            # Padre
            'nombreP': self.nameP.text(),
            'apellidoP': self.lastNP.text(),
            'edadP': self.ageP.text(),
            'cedulaP': self.dniP.text(),
            'causaPNoViveP': self.Cnn.text(),
            'telefonoMovilP': self.PhoneMp.text(),
            'direccionP': self.Dcp.text(),
            'empresaDTrabajaP': self.Empdt.text(),
            'tipoEmpleoqDesempeñaP': self.Ted.text(),
            # Madre
            'nombreM': self.nameM.text(),
            'apellidoM': self.lastNM.text(),
            'edadM': self.ageM.text(),
            'cedulaM': self.dniM.text(),
            'causaPNoViveM': self.CnnM.text(),
            'telefonoMovilM': self.PhoneMM.text(),
            'direccionM': self.DcpM.text(),
            'empresaDTrabajaM': self.EmpdtM.text(),
            'tipoEmpleoqDesempeñaM': self.TedM.text(),
        }
        try:
            self.database.ModifyEstudend(
                datos_editados['NombreS'], datos_editados['apellido'], datos_editados['cedulaEscolar'],
                datos_editados['edad'], '', '', '', datos_editados['nacionalidad'], datos_editados['estado'], datos_editados['municipio'],
                datos_editados['direccionActual'], datos_editados['puntoDReferencia'], datos_editados['altura'], datos_editados['peso'],
                datos_editados['tallaZapatos'], datos_editados['tallaCamisa'], datos_editados['tallaPantalon'], datos_editados['numeroDHermanos'],
                datos_editados['autorizadoPRetirarANiño'], datos_editados['alergicoA'], '', datos_editados['especificarDificultad'],
                datos_editados['correoElectronico'], datos_editados['telefonoDHabitacion'], '', datos_editados['estIMG'], datos_editados['cartonVacunas'], datos_editados['tipoDSangre'], datos_editados['examenDHeces']
            )
            self.database.ModifyRpl(
                datos_editados['nombreR'], datos_editados['apellidoR'], datos_editados['cedulaR'], '', datos_editados['edadR'], '', datos_editados['nacionalidadR'], datos_editados['afinidad'], datos_editados['profesionR'], datos_editados['ocupacionR'], datos_editados['empresaDTrabajaR'], datos_editados['direccionR'], datos_editados['telefonoMovilR'], datos_editados['telefonoHabitacionR'], datos_editados['telefonoFamiliarR'], datos_editados['correoElectronicoR'], datos_editados['rifR'], '', datos_editados['codigoPatriaR'], datos_editados['serialPatriaR']
            )
            self.database.ModifyDTP(
                datos_editados['nombreP'], datos_editados['apellidoP'], datos_editados['cedulaP'], '', datos_editados['edadP'], datos_editados['tipoEmpleoqDesempeñaP'], datos_editados['empresaDTrabajaP'], '', datos_editados['causaPNoViveP'], datos_editados['direccionP'], datos_editados['telefonoMovilP']
            )
            self.database.ModifyDTM(
                datos_editados['nombreM'], datos_editados['apellidoM'], datos_editados['cedulaM'], '', datos_editados['edadM'], datos_editados['tipoEmpleoqDesempeñaM'], datos_editados['empresaDTrabajaM'], '', datos_editados['causaPNoViveM'], datos_editados['direccionM'], datos_editados['telefonoMovilM']
            )
            QMessageBox.information(self, "Éxito", "Datos modificados correctamente.")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar: {e}")
