# 🍪 Cookiecutter Python ETL Template

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)
![DevContainer](https://img.shields.io/badge/VSCode-DevContainer-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Plantilla profesional para crear proyectos de **Ingeniería de Datos /
ETL en Python**, con:

✅ Arquitectura modular (Extract / Transform / Load)\
✅ Docker para ejecución\
✅ Dev Containers para desarrollo\
✅ Tests con pytest\
✅ Git listo desde el día 1

------------------------------------------------------------------------

## 🚀 Uso

Instala Cookiecutter (una sola vez):

``` bash
pip install cookiecutter
```

Crea un nuevo proyecto a partir del template:

``` bash
cookiecutter gh:TU_USUARIO/cookiecutter-python-etl
```

Luego responde las preguntas:

``` text
project_name: Mi Proyecto ETL
project_slug: mi_proyecto_etl
author_name: Tu Nombre
```

------------------------------------------------------------------------

## 📂 Estructura generada

``` text
project/
├── src/
│   ├── main.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── tests/
│   └── test_etl.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── README.md
└── .devcontainer/
    ├── devcontainer.json
    └── Dockerfile
```

------------------------------------------------------------------------

## 🐳 Uso con Docker

Construir la imagen:

``` bash
docker build -t my_etl .
```

Ejecutar el contenedor:

``` bash
docker run --rm -it my_etl
```

------------------------------------------------------------------------

## 🧪 Ejecutar tests

``` bash
pytest
```

------------------------------------------------------------------------

## 🛠 Desarrollo con VS Code (Dev Containers)

1.  Abre el proyecto generado en VS Code
2.  Presiona `Ctrl + Shift + P`
3.  Selecciona **Dev Containers: Reopen in Container**
4.  Espera a que se instalen las dependencias automáticamente
5.  Comienza a desarrollar dentro del contenedor

------------------------------------------------------------------------

## 📜 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.
