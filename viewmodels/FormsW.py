from models.Estudend import Estudend
from services.Connection import database

class EstudendViewModel:
    def __init__(self):
        self.database = database("utilities\\db\\DataBaseUE.db")

    def registrar_estudiante(self,
                            nombre, apellido, cedulaEscolar, edad, genero, fechaDNacimiento, lateralidad, nacionalidad,  estado, municipio, direccionActual, puntoDReferencia, altura, peso,tallaZapatos,  tallaCamisa, tallaPantalon, numeroDHermanos, autorizadoPRetirarANiño,  alergicoA, algunaDificultad, especificarDificultad, correoElectronico, telefonoDHabitacion,  cartonVacunas, tipoDSangre, examenDHeces ):
            self.database.insertEstudend(
                                        nombre, apellido, cedulaEscolar, edad, genero, fechaDNacimiento, lateralidad, numeroDHermanos, autorizadoPRetirarANiño, correoElectronico, telefonoDHabitacion, direccionActual, altura, peso, tallaCamisa, tallaPantalon, tallaZapatos, alergicoA, algunaDificultad, especificarDificultad, cartonVacunas, tipoDSangre, examenDHeces, nacionalidad, estado, municipio, puntoDReferencia
                                        )

    def registrar_representante(self,
                                NombreR, ApellidoR, CedulaR, FechaDeNacimientoR, EdadR, EstadoCivil, NacionalidadR, Afinidad, ProfesionR, OcupacionR, EmpresaDTrabajaR, DireccionR, TelefonoMovilR, TelefonoHabitacionR, TelefonoFamiliarR, CorreoElectronicoR, RifR, PlanillaSigeR, CodigoPatriaR, SerialPatriaR):
            self.database.insertRpl(
                                    NombreR, ApellidoR, CedulaR, FechaDeNacimientoR, EdadR, EstadoCivil, NacionalidadR, Afinidad, ProfesionR, OcupacionR, EmpresaDTrabajaR, DireccionR, TelefonoMovilR, TelefonoHabitacionR, TelefonoFamiliarR, CorreoElectronicoR, RifR, PlanillaSigeR, CodigoPatriaR, SerialPatriaR
                                    )

    def registrar_padre(self,
                            NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP,  ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP):
            self.database.insertDTP(
                                    NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP,  ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP
                                    )

    def registrar_madre(self,
                            NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM):
            self.database.insertDTM(
                                    NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM
                                    )



