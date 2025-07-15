from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QButtonGroup, QMainWindow, QStackedWidget, QGridLayout, QGroupBox, QSizePolicy, QSpacerItem, QFileDialog
from viewmodels.FormsW import EstudendViewModel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter
import sqlite3


class BgWidget(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image = QPixmap(image_path)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

class FormsStudend(QMainWindow):
    def __init__(self):
        super().__init__()

        self.viewmodel = EstudendViewModel()  

        # Propiedades de la ventana
        self.setWindowTitle("Datos del Estudiante")
        self.setGeometry(100, 100, 1000, 600)

        # Establecer imagen de fondo
        self.setStyleSheet("""
            .tituloz {
                color: black;
                font-family: Arial, sans-serif;
                font-size: 20px;
                font-weight: bold;
                padding: 8px 24px 8px 16px;
                border-top-left-radius: 10px;
                border-bottom-left-radius: 10px;
                border-top-right-radius: 0;
                border-bottom-right-radius: 0;
                background: qlineargradient(
                    x1:0, y1:0, x2:0.85, y2:0,
                    stop:0 #ff9800, stop:0.85 #ffb74d, stop:0.85 #ffb74d, stop:1 transparent
                );
                margin-bottom: 8px;
            }
            .titulod {
                color: black;
                font-family: Arial, sans-serif;
                font-size: 20px;
                font-weight: bold;
                padding: 8px 24px 8px 16px;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
                border-top-left-radius: 0;
                border-bottom-left-radius: 0;
                background: qlineargradient(
                    x1:1, y1:0, x2:0.15, y2:0,
                    stop:0 #ff9800, stop:0.85 #ffb74d, stop:0.85 #ffb74d, stop:1 transparent
                );
                margin-bottom: 8px;
            }
            QGroupBox {
                border: 1px solid black;
                border-radius: 8px;
                margin-top: 10px;
                background: transparent;
            }
            QGroupBox::title {
                color: black;
                font-weight: bold;
                font-size: 15px;
                subcontrol-origin: margin;
                subcontrol-position: top left;
            }
            
            QRadioButton {
                color: black;
                font-weight: bold;
            }
        """)

        # Crear el widget de fondo
        self.bg_widget = BgWidget("utilities/resources/imgs/Bg.png")
        self.setCentralWidget(self.bg_widget)

        self.main_layout = QVBoxLayout(self.bg_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Widget principal de stacked
        self.Sc_Widget = QStackedWidget(self)
        self.main_layout.addWidget(self.Sc_Widget)

        
        # Crear la primera página
        self.page1 = QWidget()
        self.layoutP1 = QGridLayout()

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
        self.dateofbirth = QLineEdit(self)
        self.dateofbirth.setPlaceholderText("Fecha de Nacimiento")
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
        

        self.grid2 = QGridLayout()
        self.ala = QLineEdit(self)
        self.ala.setPlaceholderText("Alergico a")
        self.grid2.addWidget(self.ala, 1, 0)
        self.gbad = QGroupBox("¿Alguna discapacidad?", self)
        self.QrBY = QRadioButton("Si", self)
        self.QrBN = QRadioButton("No", self)
        self.QrBY.setChecked(True)
        self.Qhbad = QVBoxLayout()
        self.Qhbad.addWidget(self.QrBY)
        self.Qhbad.addWidget(self.QrBN)
        self.gbad.setLayout(self.Qhbad)
        self.grid2.addWidget(self.gbad, 2, 0)
        self.tds = QLineEdit(self)
        self.tds.setPlaceholderText("Tipo de Sangre")
        self.grid2.addWidget(self.tds, 1, 1)
        
        # Variable para la imagen de la vacuna
        self.vacunaIMGpath = None
        self.PushbuttonVacuna = QPushButton("Subir Imagen de Vacuna", self)
        self.PushbuttonVacuna.clicked.connect(self.upload_vacuna_image)
        self.grid2.addWidget(self.PushbuttonVacuna, 2, 1)
        
        self.vacunaIMG = QLabel(self)
        self.vacunaIMG.setFixedSize(100, 100)
        self.vacunaIMG.setScaledContents(True)
        self.grid2.addWidget(self.vacunaIMG, 2, 2)

        
        self.exdh = QLineEdit(self)
        self.exdh.setPlaceholderText("Examen de Heces")
        self.grid2.addWidget(self.exdh, 3, 1)
        self.layoutP1.addLayout(self.grid2, 1, 2, Qt.AlignTop)

        # Fila 2: Título de Datos de Contacto
        self.dclabel = QLabel("Datos de Contacto", self)
        self.dclabel.setProperty("class", "tituloz")
        self.dclabel.setFixedSize(300, 45)
        self.dclabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP1.addWidget(self.dclabel, 2, 0, Qt.AlignLeft)

        # Fila 3: Grid de Datos de Contacto
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

        # Fila 4: Título de Tallas
        self.tlabel = QLabel("Tallas", self)
        self.tlabel.setProperty("class", "tituloz")
        self.tlabel.setFixedSize(300, 45)
        self.tlabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP1.addWidget(self.tlabel, 4, 0, Qt.AlignLeft)

        # Fila 5: Grid de Tallas
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

        # Fila 6: Título de Ubicación
        self.ulabel = QLabel("Ubicación", self)
        self.ulabel.setProperty("class", "titulod")
        self.ulabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.ulabel.setFixedSize(300, 45)
        self.ulabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP1.addWidget(self.ulabel, 2, 2, Qt.AlignRight)

        # Fila 7: Grid de Ubicación
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
        
        # Boton de Next a la Pagina 1
        self.NextP = QPushButton("Siguiente Pagina")
        self.NextP.clicked.connect(self.RegisterPage2)
        self.layoutP1.addWidget(self.NextP, 9, 1)
        self.page1.setLayout(self.layoutP1)

        # Espaciador entre columnas si lo necesitas
        self.layoutP1.addItem(QSpacerItem(200, 20, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1, 8, 1)

        # Muestra los items en la ventana 1
        self.page1.setLayout(self.layoutP1)
        self.Sc_Widget.addWidget(self.page1)

        
        # Crear la segundasel página
        self.page2 = QWidget()
        self.layoutP2 = QGridLayout()
        
        # Fila 0: Títulos Tabla Representante
        self.Rplabel = QLabel("Datos Personales", self)
        self.Rplabel.setProperty("class", "tituloz")
        self.Rplabel.setFixedSize(40, 45)
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
        self.dateofbirthR = QLineEdit(self)
        self.dateofbirthR.setPlaceholderText("Fecha de Nacimiento")
        self.grid6.addWidget(self.dateofbirthR, 2, 2)
        
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
        # Final del Boton Planilla Sige
        self.layoutP2.addLayout(self.grid6, 1, 0, Qt.AlignTop)
        
        
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
        # Titulo Grid 8
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
        self.layoutP2.addWidget(self.backBt, 5, 1)
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
        
        #Fila 0: Titutlos Tabla Datos del Padre.
        self.dpLabel = QLabel("Datos Personales del Padre", self)
        self.dpLabel.setProperty("class", "tituloz")
        self.dpLabel.setFixedSize(300, 45)
        self.dpLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.dclabel = QLabel("Datos de Contacto del Padre", self)
        self.dclabel.setProperty("class", "tituloz")
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
        self.dateofbirthP = QLineEdit(self)
        self.dateofbirthP.setPlaceholderText("Fecha de Nacimiento")
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
        
        #Fila 3: Titulo Datos de Profesion
        self.Plabel = QLabel("Datos de Profesión del Padre")
        self.Plabel.setProperty("class", "tituloz")
        self.Plabel.setFixedSize(300, 45)
        self.Plabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP3.addWidget(self.Plabel, 2, 0, Qt.AlignLeft)
        
        # Fila 3:Grid 11 Datos de Profesion
        self.grid11 = QGridLayout()
        self.Empdt = QLineEdit(self)
        self.Empdt.setPlaceholderText("Emprensa donde Trabaja")
        self.grid11.addWidget(self.Empdt, 1, 0)
        self.Ted = QLineEdit(self)
        self.Ted.setPlaceholderText("Tipo de Empleo que Desempeña")
        self.grid11.addWidget(self.Ted, 2, 0)
        self.layoutP3.addLayout(self.grid11, 3, 0, Qt.AlignTop)
        
        #Boton de Back a la Pagina 2
        self.backP2 = QPushButton("Pagina Anterior")
        self.backP2.clicked.connect(self.RegisterPage2)
        self.layoutP3.addWidget(self.backP2, 6, 1)
        self.page3.setLayout(self.layoutP3)
        
        # Boton de Next a la Pagina 2
        self.NextP4 = QPushButton("Siguiente Pagina")
        self.NextP4.clicked.connect(self.RegisterPage4)
        self.layoutP3.addWidget(self.NextP4, 5, 1)
        self.page3.setLayout(self.layoutP3)
        
        
        # Espaciador entre columnas
        self.layoutP3.addItem(QSpacerItem(200, 20, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1, 6, 1)
        
        #Muestra los Items en la Ventana 3
        self.page3.setLayout(self.layoutP3)
        self.Sc_Widget.addWidget(self.page3)
        
        
        # Crear La Cuarta Pagina
        self.page4 = QWidget()
        self.layoutP4 = QGridLayout()
        
        #Fila 0: Titutlos Tabla Datos del Madre.
        self.dpLabel = QLabel("Datos Personales de la Madre", self)
        self.dpLabel.setProperty("class", "tituloz")
        self.dpLabel.setFixedSize(300, 45)
        self.dpLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.dclabel = QLabel("Datos de Contacto de la Madre", self)
        self.dclabel.setProperty("class", "tituloz")
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
        self.dateofbirthM = QLineEdit(self)
        self.dateofbirthM.setPlaceholderText("Fecha de Nacimiento")
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
        
        self.Cnn = QLineEdit(self)
        self.Cnn.setPlaceholderText("¿Causa por la que no vive con el Niño?")
        self.grid12.addWidget(self.Cnn, 4, 0)
        self.layoutP4.addLayout(self.grid12, 1, 0, Qt.AlignLeft)
        
        # Fila 2: Grid 13 Datos de Contacto
        self.grid13 = QGridLayout()
        self.PhoneMM = QLineEdit(self)
        self.PhoneMM.setPlaceholderText("Telélefono Móvil")
        self.grid13.addWidget(self.PhoneMM, 1, 0)
        self.Dcp = QLineEdit(self)
        self.Dcp.setPlaceholderText("Dirección")
        self.grid13.addWidget(self.Dcp, 2, 0)
        self.layoutP4.addLayout(self.grid13, 1, 2, Qt.AlignTop)
        
        #Fila 3: Titulo Datos de Profesion
        self.Mlabel = QLabel("Datos de Profesión de la Madre")
        self.Mlabel.setProperty("class", "tituloz")
        self.Mlabel.setFixedSize(300, 45)
        self.Mlabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layoutP4.addWidget(self.Mlabel, 2, 0, Qt.AlignLeft)
        
        # Fila 3:Grid 14 Datos de Profesion
        self.grid14 = QGridLayout()
        self.Empdt = QLineEdit(self)
        self.Empdt.setPlaceholderText("Emprensa donde Trabaja")
        self.grid14.addWidget(self.Empdt, 1, 0)
        self.Ted = QLineEdit(self)
        self.Ted.setPlaceholderText("Tipo de Empleo que Desempeña")
        self.grid14.addWidget(self.Ted, 2, 0)
        self.layoutP4.addLayout(self.grid14, 3, 0, Qt.AlignTop)
        
        #Boton de Back a la Pagina 3
        self.backP3 = QPushButton("Pagina Anterior")
        self.backP3.clicked.connect(self.RegisterPage3)
        self.layoutP4.addWidget(self.backP3, 5, 1)
        self.page4.setLayout(self.layoutP4)
        
        # Boton de Registro Final
        self.registerBton = QPushButton("Finalizar Registro")
        self.registerBton.clicked.connect(self.register_estudend)
        self.layoutP4.addWidget(self.registerBton, 6, 1)
        
        # Espaciador entre columnas
        self.layoutP4.addItem(QSpacerItem(200, 20, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1, 6, 1)
        
        #Muestra los Items en la Ventana 3
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
    
    def register_estudend(self):
        # Inicio Pagina Estudiante Pagina 1
        nombre = self.nameS.text()
        apellido = self.lastNS.text()
        cedulaEscolar = self.dni.text()
        edad = self.ageS.text()
        genero = "Masculino" if self.QrBM.isChecked() else "Femenino"
        fechaDNacimiento = self.dateofbirth.text()
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
        especificarDificultad = self.tds.text() if algunaDificultad == "Si" else ""
        correoElectronico = self.email.text()
        telefonoDHabitacion = self.tfh.text()
        cartonVacunas = None
        if self.vacunaIMGpath:
            with open(self.vacunaIMGpath, 'rb') as f:
                cartonVacunas = f.read()
        tipoDSangre = self.tds.text()
        examenDHeces = self.exdh.text()
        # Final Pagina Estudiante Pagina 1
        
        # Inicio Pagina Representante Pagina 2
        NombreR = self.nameR.text()
        ApellidoR = self.lastNR.text()
        EdadR = self.ageR.text()
        CedulaR = self.dniR.text()
        FechaDeNacimientoR = self.dateofbirthR.text()
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
        FechaDNacimientoP = self.dateofbirthP.text()
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
        FechaDNacimientoM = self.dateofbirthM.text()
        ViveConElNiñoM = "Si" if self.QrPSi.isChecked() else "No"
        CausaPNoViveM = self.Cnn.text()
        EmpresaDTrabajaM = self.Empdt.text()
        TipoEmpleoqDesempeñaM = self.PhoneMM.text()
        DireccionM = self.Dcp.text()
        TelefonoMovilM = self.PhoneMM.text()
    
        # Final Pagina Madre Pagina 4
        


        if nombre and apellido and cedulaEscolar and edad and fechaDNacimiento and lateralidad and numeroDHermanos and autorizadoPRetirarANiño and correoElectronico and telefonoDHabitacion and direccionActual and altura and peso and tallaZapatos and tallaCamisa and tallaPantalon and alergicoA and algunaDificultad and tipoDSangre and cartonVacunas and examenDHeces and nacionalidad and estado and municipio and puntoDReferencia \
        and NombreR and ApellidoR and EdadR and CedulaR and FechaDeNacimientoR and EstadoCivil and Afinidad and RifR and PlanillaSigeR and TelefonoMovilR and TelefonoHabitacionR and CorreoElectronicoR and TelefonoFamiliarR and NacionalidadR and DireccionR and CodigoPatriaR and SerialPatriaR \
            and NombreP and ApellidoP and EdadP and CedulaP and FechaDNacimientoP and ViveConElNiñoP and CausaPNoViveP and EmpresaDTrabajaP and TipoEmpleoqDesempeñaP and TelefonoMovilP and DireccionP  \
                and NombreM and ApellidoM and EdadM and CedulaM and FechaDNacimientoM and ViveConElNiñoM and CausaPNoViveM and EmpresaDTrabajaM and TipoEmpleoqDesempeñaM and TelefonoMovilM and DireccionM:
            
                
            self.viewmodel.registrar_estudiante(
            nombre, apellido, cedulaEscolar, edad, genero, fechaDNacimiento, lateralidad, numeroDHermanos, autorizadoPRetirarANiño, correoElectronico, telefonoDHabitacion, direccionActual, altura, peso, tallaCamisa, tallaPantalon, tallaZapatos, alergicoA, algunaDificultad, especificarDificultad, cartonVacunas, tipoDSangre, examenDHeces, nacionalidad, estado, municipio, puntoDReferencia 
            )
            self.viewmodel.registrar_representante(
            NombreR, ApellidoR, CedulaR, FechaDeNacimientoR, EdadR, EstadoCivil, NacionalidadR, Afinidad, ProfesionR, OcupacionR, EmpresaDTrabajaR, DireccionR, TelefonoMovilR, TelefonoHabitacionR, TelefonoFamiliarR, CorreoElectronicoR, RifR, PlanillaSigeR, CodigoPatriaR, SerialPatriaR

            )
            self.viewmodel.registrar_padre(
                NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP,  ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP
            )
            self.viewmodel.registrar_madre(
                NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM
            )
            QMessageBox.information(self, "Registro Exitoso", "El estudiante ha sido registrado exitosamente.")
            
            self.close()
        else:
            QMessageBox.warning(self, "Campos Vacíos", "Por favor, complete todos los campos obligatorios.")
    
    def upload_vacuna_image(self):
        file_name = QFileDialog(self)
        file_name.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp)")
        if file_name.exec():
            filepath = file_name.selectedFiles()[0]
            self.vacunaIMGpath = filepath
            pixmap = QPixmap(filepath)
            self.vacunaIMG.setPixmap(pixmap.scaled(self.vacunaIMG.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
