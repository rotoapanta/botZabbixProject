import signal
import sys
import logging
from zbx_bot import zabbix
from zbx_bot.telegram_bot import main as telegram_main
from utils.config_reader import read_configuration_with_args
from utils.logging_utils import setup_logging

# Configurar el registro en el archivo .log
setup_logging()

# Obtener la configuración desde el archivo especificado
configuration = read_configuration_with_args()

# Conectarse a Zabbix utilizando la configuración proporcionada
zabbix_instance = zabbix.connect_to_zabbix(configuration)

bot_data = {
    'zabbix': zabbix_instance,
    'configuration': configuration
}

# Crear el objeto logger
logger = logging.getLogger(__name__)


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
