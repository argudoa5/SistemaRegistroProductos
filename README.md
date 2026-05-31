# Programa para listar y registrar productos

## Descripción

La API de Gestión de Productos es una aplicación desarrollada en Python utilizando el framework FastAPI. Su objetivo es permitir el registro y consulta de productos mediante servicios web REST, facilitando la administración de información básica de inventario.

El sistema permite almacenar datos de productos como nombre, precio y stock disponible. Además, cuenta con documentación interactiva generada automáticamente mediante OpenAPI/Swagger, permitiendo probar los endpoints directamente desde el navegador.

Este proyecto utiliza GitHub para el control de versiones, Jira para la gestión de tareas y seguimiento del desarrollo, y Confluence para la documentación técnica y funcional.

## Características

- Registro de productos mediante solicitudes POST.
- Consulta de productos registrados mediante solicitudes GET.
- Documentación automática con Swagger UI.
- API REST desarrollada con FastAPI.
- Gestión del proyecto mediante Jira.
- Documentación colaborativa mediante Confluence.
- Control de versiones utilizando GitHub.

## Tecnologías Utilizadas

- Python 3.10+
- FastAPI
- Uvicorn
- OpenAPI
- Swagger UI
- GitHub
- Jira
- Confluence

## Estructura del Proyecto

```text
api-productos/
│
├── .gitignore
├── LICENSE
├── OpenAPI.yaml
├── README.md
└── app.py
```

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrese de tener instalado:

- Python 3.10 o superior
- Pip
- Git (opcional)
- Navegador web

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/api-productos.git
```

### 2. Acceder al directorio del proyecto

```bash
cd api-productos
```

### 3. Instalar dependencias

```bash
pip install fastapi uvicorn
```

### 4. Ejecutar la aplicación

```bash
uvicorn main:app --reload
```
