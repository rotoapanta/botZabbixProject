import logging
import signal
import sys
from config_reader import read_configuration
from zbx_bot import zabbix
from zbx_bot.telegram_bot import main as telegram_main

# Obtener el nombre del archivo de configuración desde los argumentos de línea de comandos
if len(sys.argv) < 2:
    print("Se requiere el nombre del archivo de configuración como argumento.")
    sys.exit(1)

config_file = sys.argv[1]

# Obtener la configuración desde el archivo especificado
configuration = read_configuration(config_file)

# Configurar el registro en el archivo .log
logging.basicConfig(
    filename='app.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Conectarse a Zabbix utilizando la configuración proporcionada
zabbix_instance = zabbix.connect_to_zabbix(configuration)

bot_data = {
    'zabbix': zabbix_instance,
    'configuration': configuration
}

# Función para manejar señales y finalizar la aplicación adecuadamente
def handle_exit(signum, frame):
    logger.info("Finalizando la aplicación...")
    # Agregar aquí cualquier código adicional para limpiar recursos, guardar datos, etc.
    sys.exit(0)

# Registrar la función de manejo de señales para SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, handle_exit)

# Iniciar la aplicación del bot de Telegram
try:
    telegram_main(bot_data)
except Exception as e:
    logger.exception("Error durante la ejecución del bot de Telegram: %s", str(e))