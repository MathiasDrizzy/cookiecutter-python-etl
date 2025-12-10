# 🍪 Cookiecutter Python ETL Template

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)
![DevContainer](https://img.shields.io/badge/VSCode-DevContainer-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Plantilla profesional para crear proyectos de **Ingeniería de Datos / ETL en Python**, con:

✅ Arquitectura modular (Extract / Transform / Load)  
✅ Docker para ejecución  
✅ Dev Containers para desarrollo  
✅ Tests con pytest  
✅ Git listo desde el día 1  

---

## 🚀 Uso

```bash
pip install cookiecutter
cookiecutter gh:TU_USUARIO/cookiecutter-python-etl

## 📂 Estructura generada

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
└── .devcontainer/
    ├── devcontainer.json
    └── Dockerfile

## 🐳 Uso con Docker
docker build -t my_etl .
docker run --rm -it my_etl

## 📜 Licencia

Este proyecto se distribuye bajo la licencia MIT.