import logging
from config_reader import read_configuration
from zbx_bot import zabbix
from zbx_bot.telegram_bot import main
import signal

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Obtener la configuración
configuration = read_configuration()

# Conectarse a Zabbix utilizando el token de acceso
zabbix_instance = zabbix.connect_to_zabbix(configuration)

logger = logging.getLogger('telegram')
logger.setLevel(logging.INFO)

bot_data = {
    'zabbix': zabbix_instance,
    'configuration': configuration
}

main(bot_data)
