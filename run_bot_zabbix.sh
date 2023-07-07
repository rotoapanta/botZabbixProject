#!/bin/bash

# Define variables
CONDA_PATH="/home/rotoapanta/anaconda3/bin"
CONDA_ENV="bot_zabbix_env"
SCRIPT_PATH="/home/rotoapanta/script/digital_tiltmeter_zabbix"
PYTHON_SCRIPT="app.py"
CONFIG_FILE="config.ini"

# Carga el entorno de Conda dentro de la shell de bash
eval "$(${CONDA_PATH}/conda shell.bash hook)"

# Activa el ambiente Conda
conda activate ${CONDA_ENV}

# Navega hacia el directorio del script Python
# shellcheck disable=SC2164
cd ${SCRIPT_PATH}

# Ejecuta el script Python con el archivo de configuración y redirige la salida estándar a la salida de error
python ./${PYTHON_SCRIPT} ./${CONFIG_FILE} >&2