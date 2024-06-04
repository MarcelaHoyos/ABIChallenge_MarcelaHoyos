# ABIChallenge_MarcelaHoyos

## Descripción del Proyecto

Este proyecto es parte de un desafío de MLOps que incluye la creación, prueba, análisis y despliegue de una API utilizando FastAPI, Docker, GitHub Actions y SonarCloud.

## Estructura del Proyecto

- `.github/workflows/main.yml`: Archivo de configuración de GitHub Actions para CI/CD.
- `diagrams/`: Carpeta que contiene diagramas del proyecto.
- `.dockerignore`: Archivo para excluir archivos y directorios sensibles al construir la imagen Docker.
- `Dockerfile`: Archivo de configuración de Docker para la construcción de la imagen del contenedor.
- `README.md`: Documentación del proyecto.
- `docker-compose.yml`: Archivo de configuración para Docker Compose.
- `main.py`: Código fuente de la API en FastAPI.
- `requirements.txt`: Archivo de dependencias de Python.
- `sonar-project.properties`: Archivo de configuración para SonarCloud.
- `test_sample.py`: Archivo de pruebas unitarias utilizando `pytest`.

## Pasos del Desafío

### 1. Configuración del Repositorio

- Creación del repositorio en GitHub.
- Configuración de los secrets necesarios en GitHub Actions:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION`
  - `SONAR_PROJECT_KEY`
  - `SONAR_ORGANIZATION`
  - `SONAR_TOKEN`

### 2. Creación del Diagrama de Arquitectura

- Creación de un diagrama que muestra el flujo de datos y componentes utilizados en AWS y GitHub Actions.

### 3. Configuración del Flujo de Trabajo en GitHub Actions

- Creación y configuración del archivo `.github/workflows/main.yml` para definir el pipeline de CI/CD.

### 4. Verificación y Ejecución del Flujo de Trabajo

- Verificación de que el pipeline de CI/CD se ejecuta correctamente, incluyendo pruebas unitarias y análisis de SonarCloud.

### 5. Despliegue de la API

#### Creación de la API en Python

- Desarrollo de la API utilizando FastAPI.
- Documentación inline y uso de POO.

#### Dockerización de la API

- Creación del archivo Dockerfile para construir la imagen del contenedor.
- Uso de un archivo `.dockerignore` para excluir archivos sensibles.
- Creación del archivo `docker-compose.yml` para facilitar el despliegue.

### 6. Documentación y Presentación

#### Documentar el Proceso

- Descripción detallada de cada paso del proceso en este archivo `README.md`.

#### Desafíos Encontrados y Soluciones

- **Security Hotspots en Dockerfile**:
  - **Problema**: Copia recursiva de archivos al contenedor.
  - **Solución**: Creación de un archivo `.dockerignore` para excluir archivos sensibles y especificación de archivos necesarios en Dockerfile.

- **Cobertura de Pruebas Insuficiente**:
  - **Problema**: Cobertura de pruebas menor al 80%.
  - **Solución**: Adición de pruebas unitarias adicionales en `test_sample.py`.

- **Problemas de Permisos en Docker**:
  - **Problema**: Ejecución del contenedor como root.
  - **Solución**: Creación y uso de un usuario no root en Dockerfile.

## Cómo Ejecutar el Proyecto

### Requisitos Previos

- Docker
- Python 3.8

### Pasos para Ejecutar

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/MarcelaHoyos/ABIChallenge_MarcelaHoyos.git
   cd ABIChallenge_MarcelaHoyos

2. Construir la Imagen Docker:

   docker build -t my-fastapi-app .
   
3. Ejecutar el Contenedor Docker:
   docker run -d -p 8000:80 my-fastapi-app

4. Acceder a la API:
   La API estará disponible en http://localhost:8000

### Uso de Docker Compose

1. Iniciar el Servicio con Docker Compose:
   docker-compose up
2. Detener el Servicio con Docker Compose:
   docker-compose down
   
### Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para sugerir cambios.
