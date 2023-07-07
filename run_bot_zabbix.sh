#!/bin/bash

# Define variables
CONDA_PATH="/home/rotoapanta/anaconda3/bin"
CONDA_ENV="bot_zabbix_env"
SCRIPT_PATH="/home/rotoapanta/script/bot_zabbix_project"
PYTHON_SCRIPT="app.py"
CONFIG_FILE="config.ini"

# Validar la existencia de rutas y archivos
if [ ! -d "${CONDA_PATH}" ]; then
    echo "La ruta de Conda no existe: ${CONDA_PATH}"
    exit 1
fi

if [ ! -f "${SCRIPT_PATH}/${PYTHON_SCRIPT}" ]; then
    echo "El script Python no existe: ${SCRIPT_PATH}/${PYTHON_SCRIPT}"
    exit 1
fi

if [ ! -f "${SCRIPT_PATH}/${CONFIG_FILE}" ]; then
    echo "El archivo de configuración no existe: ${SCRIPT_PATH}/${CONFIG_FILE}"
    exit 1
fi

# Carga el entorno de Conda dentro de la shell de bash
eval "$(${CONDA_PATH}/conda shell.bash hook)"

# Activa el ambiente Conda
conda activate ${CONDA_ENV}

# Navega hacia el directorio del script Python
cd ${SCRIPT_PATH}

# Ejecuta el script Python con el archivo de configuración y redirige la salida estándar a la salida de error
python ./${PYTHON_SCRIPT} ./${CONFIG_FILE} >&2
