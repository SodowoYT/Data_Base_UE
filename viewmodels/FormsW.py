from models.Estudend import Estudend
from services.Connection import database

class EstudendViewModel:
    def __init__(self):
        self.database = database("utilities\\db\\DataBaseUE.db")

    # Función para registrar un estudiante
    def registrar_estudiante(self,
                            nombre, apellido, cedulaEscolar, edad, genero, fechaDNacimiento, lateralidad, nacionalidad,  estado, municipio, direccionActual, puntoDReferencia, altura, peso,tallaZapatos,  tallaCamisa, tallaPantalon, numeroDHermanos, autorizadoPRetirarANiño,  alergicoA, algunaDificultad, especificarDificultad, correoElectronico, telefonoDHabitacion, estIMG, cartonVacunas, tipoDSangre, examenDHeces, observaciones, grado, turno, tipoStudiante):
            return self.database.insertEstudend(
                                        nombre, apellido, cedulaEscolar, edad, genero, fechaDNacimiento, lateralidad, nacionalidad,  estado, municipio, direccionActual, puntoDReferencia, altura, peso,tallaZapatos,  tallaCamisa, tallaPantalon, numeroDHermanos, autorizadoPRetirarANiño,  alergicoA, algunaDificultad, especificarDificultad, correoElectronico, telefonoDHabitacion,  estIMG, cartonVacunas, tipoDSangre, examenDHeces, observaciones, grado, turno, tipoStudiante
                                        )

    # Función para registrar un representante
    def registrar_representante(self,
                                NombreR, ApellidoR, CedulaR, FechaDeNacimientoR, rpstIMG, EdadR, EstadoCivil, NacionalidadR, Afinidad, ProfesionR, OcupacionR, EmpresaDTrabajaR, DireccionR, TelefonoMovilR, TelefonoHabitacionR, TelefonoFamiliarR, CorreoElectronicoR, RifR, PlanillaSigeR, CodigoPatriaR, SerialPatriaR):
            return self.database.insertRpl(
                                    NombreR, ApellidoR, CedulaR, FechaDeNacimientoR, rpstIMG, EdadR, EstadoCivil, NacionalidadR, Afinidad, ProfesionR, OcupacionR, EmpresaDTrabajaR, DireccionR, TelefonoMovilR, TelefonoHabitacionR, TelefonoFamiliarR, CorreoElectronicoR, RifR, PlanillaSigeR, CodigoPatriaR, SerialPatriaR
                                    )

    # Función para registrar un padre
    def registrar_padre(self,
                            NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP,  ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP):
            return self.database.insertDTP(
                                    NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP,  ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP
                                    )

    # Función para registrar una madre
    def registrar_madre(self,
                            NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM):
            return self.database.insertDTM(
                                    NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM
                                    )


    # Se anexo este campo en solucion a la problematica que los registros se crean pero no se vinculan automaticamente
    # Función para registrar estudiante completo con vinculación automática
    def registrar_estudiante_completo(self, 
                                    # Datos del estudiante
                                    nombre, apellido, cedulaEscolar, edad, genero, fechaDNacimiento, lateralidad, nacionalidad, estado, municipio, direccionActual, puntoDReferencia, altura, peso, tallaZapatos, tallaCamisa, tallaPantalon, numeroDHermanos, autorizadoPRetirarANiño, alergicoA, algunaDificultad, especificarDificultad, correoElectronico, telefonoDHabitacion, estIMG, cartonVacunas, tipoDSangre, examenDHeces, observaciones, grado, turno, tipoStudiante,
                                    # Datos del representante
                                    NombreR, ApellidoR, CedulaR, FechaDeNacimientoR, rpstIMG, EdadR, EstadoCivil, NacionalidadR, Afinidad, ProfesionR, OcupacionR, EmpresaDTrabajaR, DireccionR, TelefonoMovilR, TelefonoHabitacionR, TelefonoFamiliarR, CorreoElectronicoR, RifR, PlanillaSigeR, CodigoPatriaR, SerialPatriaR,
                                    # Datos del padre
                                    NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP, ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP,
                                    # Datos de la madre
                                    NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM):
        """Registra un estudiante completo con su representante, padre y madre, y los vincula automáticamente."""
        try:
            # 1. Registrar representante
            representante_id = self.registrar_representante(
                NombreR, ApellidoR, CedulaR, FechaDeNacimientoR, rpstIMG, EdadR, EstadoCivil, NacionalidadR, Afinidad, ProfesionR, OcupacionR, EmpresaDTrabajaR, DireccionR, TelefonoMovilR, TelefonoHabitacionR, TelefonoFamiliarR, CorreoElectronicoR, RifR, PlanillaSigeR, CodigoPatriaR, SerialPatriaR
            )
            
            # 2. Registrar padre
            padre_id = self.registrar_padre(
                NombreP, ApellidoP, CedulaP, FechaDNacimientoP, EdadP, TipoEmpleoqDesempeñaP, EmpresaDTrabajaP, ViveConElNiñoP, CausaPNoViveP, DireccionP, TelefonoMovilP
            )
            
            # 3. Registrar madre
            madre_id = self.registrar_madre(
                NombreM, ApellidoM, CedulaM, FechaDNacimientoM, EdadM, TipoEmpleoqDesempeñaM, EmpresaDTrabajaM, ViveConElNiñoM, CausaPNoViveM, DireccionM, TelefonoMovilM
            )
            
            # 4. Registrar estudiante
            estudiante_id = self.registrar_estudiante(
                nombre, apellido, cedulaEscolar, edad, genero, fechaDNacimiento, lateralidad, nacionalidad, estado, municipio, direccionActual, puntoDReferencia, altura, peso, tallaZapatos, tallaCamisa, tallaPantalon, numeroDHermanos, autorizadoPRetirarANiño, alergicoA, algunaDificultad, especificarDificultad, correoElectronico, telefonoDHabitacion, estIMG, cartonVacunas, tipoDSangre, examenDHeces, observaciones, grado, turno, tipoStudiante
            )
            
            # 5. Vincular estudiante con su familia
            self.database.updateEstudendForeignKeys(estudiante_id, representante_id, padre_id, madre_id)
            
            return {
                'estudiante_id': estudiante_id,
                'representante_id': representante_id,
                'padre_id': padre_id,
                'madre_id': madre_id,
                'success': True
            }
            
        except Exception as e:
            print(f"Error registrando estudiante completo: {e}")
            return {
                'success': False,
                'error': str(e)
            }
