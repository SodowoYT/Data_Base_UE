from models.Estudend import Estudend
from services.Connection import database

class ModifyViewModel:
    def __init__(self):
        self.database = database("utilities\\db\\DataBaseUE.db")

    # Función para modificar un estudiante
    def modificar_estudiante(self,
                            nombre, apellido, cedulaEscolar, edad, genero, fechaDNacimiento, lateralidad, nacionalidad,  estado, municipio, direccionActual, puntoDReferencia, altura, peso,tallaZapatos,  tallaCamisa, tallaPantalon, numeroDHermanos, autorizadoPRetirarANiño,  alergicoA, algunaDificultad, especificarDificultad, correoElectronico, telefonoDHabitacion, estIMG, cartonVacunas, tipoDSangre, examenDHeces, observaciones ):
            self.database.insertEstudend(
                                        nombre, apellido, cedulaEscolar, edad, genero, fechaDNacimiento, lateralidad, nacionalidad,  estado, municipio, direccionActual, puntoDReferencia, altura, peso,tallaZapatos,  tallaCamisa, tallaPantalon, numeroDHermanos, autorizadoPRetirarANiño,  alergicoA, algunaDificultad, especificarDificultad, correoElectronico, telefonoDHabitacion, estIMG, cartonVacunas, tipoDSangre, examenDHeces, observaciones
                                        )
    
    # Función para modificar un representante
    def modificar_representante(self,
                                NombreR, ApellidoR, CedulaR, FechaDeNacimientoR, rpstIMG, EdadR, EstadoCivil, NacionalidadR, Afinidad, ProfesionR, OcupacionR, EmpresaDTrabajaR, DireccionR, TelefonoMovilR, TelefonoHabitacionR, TelefonoFamiliarR, CorreoElectronicoR, RifR, PlanillaSigeR, CodigoPatriaR, SerialPatriaR):
            self.database.insertRpl(
                                    NombreR, ApellidoR, CedulaR, FechaDeNacimientoR, rpstIMG, EdadR, EstadoCivil, NacionalidadR, Afinidad, ProfesionR, OcupacionR, EmpresaDTrabajaR, DireccionR, TelefonoMovilR, TelefonoHabitacionR, TelefonoFamiliarR, CorreoElectronicoR, RifR, PlanillaSigeR, CodigoPatriaR, SerialPatriaR
                                    )

    # Función para modificar un padre
    def modificar_padre(self,
                            NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP,  ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP):
            self.database.insertDTP(
                                    NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP,  ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP
                                    )

    # Función para modificar una madre
    def modificar_madre(self,
                            NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM):
            self.database.insertDTM(
                                    NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM
                                    )