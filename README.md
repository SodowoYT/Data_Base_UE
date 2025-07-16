# Data Base UE

Este proyecto es una aplicación de escritorio desarrollada en Python que permite la gestión y registro de estudiantes, representantes, padres y madres en una institución educativa. La aplicación facilita el almacenamiento, consulta, modificación, impresión y respaldo de los datos, todo a través de una interfaz gráfica intuitiva.

## Características principales

- **Registro de estudiantes y representantes:** Formulario completo para ingresar datos personales, médicos, de contacto y familiares.
- **Consulta y filtrado:** Visualización de los registros almacenados, con opción de búsqueda por cédula escolar.
- **Modificación de datos:** Permite actualizar la información de los registros existentes.
- **Impresión de registros:** Generación de reportes en PDF de los datos de los estudiantes.
- **Respaldo y restauración:** Funcionalidad para crear copias de seguridad y restaurar la base de datos.
- **Gestión de imágenes:** Permite adjuntar imágenes (como el cartón de vacunas y fotos de representado y representante) a los registros.

## Tecnologías y herramientas utilizadas

- **Python 3.13**
- **[PySide6](https://doc.qt.io/qtforpython/):** Framework para la creación de interfaces gráficas (Qt).
- **SQLite:** Motor de base de datos local.
- **QPixmap, QPainter, QPrinter:** Para manejo de imágenes y generación de PDF.
- **shutil, os:** Para operaciones de respaldo/restauración de archivos.

## Estructura del proyecto

```
app.py
docs/
models/
services/
test/
utilities/
    db/
    resources/
        imgs/
viewmodels/
views/
```

- **app.py:** Punto de entrada de la aplicación.
- **models/:** Clases de datos (Estudiante, Madre, Padre, Representante).
- **services/:** Lógica de conexión y operaciones con la base de datos.
- **viewmodels/:** Lógica de negocio y comunicación entre la vista y los servicios.
- **views/:** Interfaces gráficas de usuario (ventanas y formularios).
- **utilities/db/:** Base de datos SQLite.
- **utilities/resources/imgs/:** Imágenes utilizadas por la aplicación.
- **test/:** Scripts para pruebas manuales de las ventanas.
- **docs/:** Documentación adicional de guia para el diseño del proyecto.

## Instalación

1. Clona este repositorio.
2. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
   O instala manualmente PySide6:
   ```sh
   pip install pyside6
   ```
3. Ejecuta la aplicación:
   ```sh
   python app.py
   ```

## Créditos

Desarrollado por **[Dalvin Josue Ramirez Andrews](https://github.com/SodowoYT)**
