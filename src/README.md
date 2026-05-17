# Mortalidad en Colombia 2019

## Introducción del proyecto
Este proyecto consiste en una aplicación web interactiva desarrollada con Dash y Plotly para visualizar estadísticas de mortalidad en Colombia durante el año 2019.

## Objetivo
Analizar la distribución de mortalidad en Colombia mediante gráficos interactivos y filtros por departamento, sexo y grupos de edad.

## Estructura del proyecto

src/

- app.py
- requirements.txt
- render.yaml
- data/
  - Nuevo_anexo.csv
  - Divipola.csv

## Requisitos

- Python 3.11
- Dash
- Pandas
- Plotly
- Gunicorn

## Despliegue en Render

1. Subir el proyecto a GitHub.
2. Crear un nuevo Web Service en Render.
3. Conectar el repositorio.
4. Configurar:
   - Build Command:
     pip install -r src/requirements.txt

   - Start Command:
     gunicorn src.app:server

## Software utilizado

- Python
- Dash
- Plotly
- Pandas
- Visual Studio Code
- Render
- GitHub

## Instalación local

git clone URL_DEL_REPOSITORIO

cd mortalidad_colombia

pip install -r src/requirements.txt

python src/app.py

## Visualizaciones

La aplicación incluye:

- Indicadores generales de mortalidad.
- Gráfico circular de mortalidad por sexo.
- Gráfico de barras por departamento.
- Histograma de distribución por edad.
- Filtros interactivos por departamento.

## Resultados

La aplicación permite identificar patrones de mortalidad en Colombia y comparar datos demográficos de forma visual e interactiva.