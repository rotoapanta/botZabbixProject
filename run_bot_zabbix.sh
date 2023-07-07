#!/bin/bash

# Define variables
ENV_NAME="bot_zabbix_env"
ENV_PATH="/home/rotoapanta/env/"
SCRIPT_PATH="/home/rotoapanta/script/bot_zabbix_project"
PYTHON_SCRIPT="app.py"
CONFIG_FILE="config.ini"

# Validar la existencia de rutas y archivos
if [ ! -d "${SCRIPT_PATH}" ]; then
    echo "El directorio del script no existe: ${SCRIPT_PATH}"
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

# Activar el entorno virtual
source ${ENV_PATH}/bin/activate

# Instalar las dependencias del archivo requirements.txt
pip install -r ${SCRIPT_PATH}/requirements.txt

# Navegar hacia el directorio del script Python
cd ${SCRIPT_PATH}

# Ejecutar el script Python con el archivo de configuración y redirigir la salida estándar a la salida de error
python ./${PYTHON_SCRIPT} ./${CONFIG_FILE} >&2
