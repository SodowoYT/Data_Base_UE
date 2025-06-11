from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QButtonGroup, QMainWindow, QStackedWidget, QGridLayout, QGroupBox, QSizePolicy, QSpacerItem
from viewmodels.FormsW import EstudendViewModel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter

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
        self.inputcartondevacunas = QLineEdit(self)
        self.inputcartondevacunas.setPlaceholderText("Cartón de Vacunas")
        self.grid2.addWidget(self.inputcartondevacunas, 2, 1)
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
        self.Rplabel.setFixedSize(300, 45)
        self.Rplabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.dclabel = QLabel("Datos de Contacto", self)
        self.dclabel.setProperty("class", "titulod")
        self.dclabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.dclabel.setFixedSize(300, 45)
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
        
        
        # Espaciador entre columnas 
        self.layoutP2.addItem(QSpacerItem(200, 20, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1, 5, 1)
        
        # Muestra los Items en la Ventana 2
        self.page2.setLayout(self.layoutP2)
        self.Sc_Widget.addWidget(self.page2)
        
        # Def de Pagina 1
        ## Comando Funcion de Registro en la Pagina 1
    def RegisterPage1(self):
        self.Sc_Widget.setCurrentIndex(0)
        
        # Def de Pagina 2
        ## Comando Funcion de Registro en la Pagina 2
    def RegisterPage2(self):
        self.Sc_Widget.setCurrentIndex(1)

        # # columna 7
        # self.inputNdHermanos = QLineEdit(self)
        # self.inputNdHermanos.setPlaceholderText("Número de Hermanos")
        # self.layaoutMargenIzquierdo.addWidget(self.inputNdHermanos)
        # # columna 8
        # self.inputautorizadoPRetirarAlNiño = QLineEdit(self)
        # self.inputautorizadoPRetirarAlNiño.setPlaceholderText("Autorizado para Retirar al Niño")
        # self.layaoutMargenIzquierdo.addWidget(self.inputautorizadoPRetirarAlNiño)
        
        # self.layaoutvistaEstudiante.addLayout(self.layaoutMargenIzquierdo)
        # self.VaistaEstudiante.setLayout(self.layaoutvistaEstudiante)
        # self.alternador.addWidget(self.VaistaEstudiante)

    #     self.inputalgunadificultad= QLineEdit(self)
    #     self.inputalgunadificultad.setPlaceholderText("Alguna Dificultad")
    #     self.layaoutVistaEstudiante.addWidget(self.inputalgunadificultad, 3, 1)
    #     # columna 19
    #     self.inputespecifiquedificultad = QLineEdit(self)
    #     self.inputespecifiquedificultad.setPlaceholderText("Especificar Dificultad")
    #     self.layaoutVistaEstudiante.addWidget(self.inputespecifiquedificultad, 3, 2)
    #     # columna 20
    #     self.inputtipodesangre = QLineEdit(self)

    #     # columna 24
    #     self.inputestado = QLineEdit(self)
    #     self.inputestado.setPlaceholderText("Estado")
    #     self.layaoutVistaEstudiante.addWidget(self.inputestado, 4, 1)
    #     # columna 25
    #     self.inputmunicipio = QLineEdit(self)
    #     self.inputmunicipio.setPlaceholderText("Municipio")
    #     self.layaoutVistaEstudiante.addWidget(self.inputmunicipio, 4, 2)
    #     # columna 26
    #     self.inputpuntodereferencia = QLineEdit(self)
    #     self.inputpuntodereferencia.setPlaceholderText("Punto de Referencia")
    #     self.layaoutVistaEstudiante.addWidget(self.inputpuntodereferencia, 4, 3)
        
    #     self.VistaEstudiante.setLayout(self.layaoutVistaEstudiante)
    #     self.alternador.addWidget(self.VistaEstudiante)
     
    #     # Boton Registrar
    #     # self.buttonsubmit = QPushButton("Registrar Estudiante", self)
    #     # self.buttonsubmit.clicked.connect(self.register_estudend)
    #     # # self.layaout.addWidget(self.buttonsubmit)
    #     # self.setLayout(self.layaout)
        
        
    #     # container = QWidget()
    #     # container.setLayout(self.layaout)
    #     # self.setCentralWidget(container)
    #     self.viewmodel = EstudendViewModel()
    
    # def register_estudend(self):
    #     # Datos Personales
    #     nombre = self.inputnombre.text()
    #     apellido = self.inputapellido.text()
    #     edad = self.inputedad.text()
    #     cedulaescolar = self.inputcedulaescolar.text()
    #     fechadenacimiento = self.inputfechadenacimiento.text()
    #     lateralidad = self.inputlateralidad.text()
    #     genero = self.inputgenero.text()
    #     NdHermanos = self.inputNdHermanos.text()
    #     autorizadoPRetirarAlNiño = self.inputautorizadoPRetirarAlNiño.text()
        
    #     # Datos de Contacto
    #     correo = self.inputcorreo.text()
    #     telefonoHabitacion = self.inputtelefonoHabitacion.text()
    #     direccionActual = self.inputdireccionActual.text()
        
    #     # Tallas
    #     altura = self.inputaltura.text()
    #     peso = self.inputpeso.text()
    #     tallaCamisa = self.inputtallaCamisa.text()
    #     tallaPantalon = self.inputtallaPantalon.text()
    #     tallaZapatos = self.inputtallaZapatos.text()
        
    #     # Datos Médicos
    #     alergicoa = self.inputalergicoa.text()
    #     algunadificultad = self.inputalgunadificultad.text()
    #     especifiquedificultad = self.inputespecifiquedificultad.text()
    #     tipodesangre = self.inputtipodesangre.text()
    #     cartondevacunas = self.inputcartondevacunas.text()
    #     examendeheces = self.inputexamendeheces.text()
        
    #     # Ubicación
    #     nacionalidad = self.inputnacionalidad.text()
    #     estado = self.inputestado.text()
    #     municipio = self.inputmunicipio.text()
    #     puntodereferencia = self.inputpuntodereferencia.text()
        
        
    #     if nombre and apellido and edad and cedulaescolar and fechadenacimiento and lateralidad and genero and NdHermanos and autorizadoPRetirarAlNiño and correo and telefonoHabitacion and direccionActual and altura and peso and tallaCamisa and tallaPantalon and tallaZapatos and alergicoa and algunadificultad and especifiquedificultad and tipodesangre and cartondevacunas and examendeheces and nacionalidad and estado and municipio and puntodereferencia: 
    #         self.viewmodel.set_date(
    #             nombre, 
    #             apellido, 
    #             cedulaescolar, 
    #             edad, 
    #             genero, 
    #             fechadenacimiento, 
    #             lateralidad, 
    #             NdHermanos, 
    #             autorizadoPRetirarAlNiño,
    #             correo,
    #             telefonoHabitacion,
    #             direccionActual,
    #             altura,
    #             peso,
    #             tallaCamisa,
    #             tallaPantalon,
    #             tallaZapatos,
    #             alergicoa,
    #             algunadificultad,
    #             especifiquedificultad,
    #             tipodesangre,
    #             cartondevacunas,
    #             examendeheces,
    #             nacionalidad,
    #             estado,
    #             municipio,
    #             puntodereferencia
    #         )
    #         QMessageBox.information(self, "Registro Exitoso", "Estudiante registrado exitosamente.")
    #         self.close()
            
    #     else:
    #         QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")