# {{ cookiecutter.project_name }}

Proyecto ETL generado con Cookiecutter.

## Estructura

```text
{{ cookiecutter.project_slug }}/
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

## Uso
docker build -t {{ cookiecutter.project_slug }} .
docker run --rm -it {{ cookiecutter.project_slug }}

### 2.11 `.devcontainer/Dockerfile` (solo DEV)

`{{ cookiecutter.project_slug }}/.devcontainer/Dockerfile`:

```dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspaces