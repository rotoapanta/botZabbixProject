from configparser import ConfigParser
import logging
import sys

logger = logging.getLogger(__name__)


def read_configuration(config_file):
    config = ConfigParser()
    config.read(config_file)

    configuration = {}

    if 'Zabbix' in config:
        # Leer la configuración de Zabbix
        zabbix_section = config['Zabbix']
        configuration['zabbix_url'] = zabbix_section.get('url')
        configuration['zabbix_user'] = zabbix_section.get('user')
        configuration['zabbix_password'] = zabbix_section.get('password')

    if 'Telegram' in config:
        telegram_section = config['Telegram']
        configuration['telegram_token'] = telegram_section.get('token')

    return configuration


def check_file(file_path):
    try:
        with open(file_path):
            return file_path
    except Exception as e:
        error_message = "Error: %s " % (str(e))
        logger.error(error_message)
        raise Exception(error_message)


def read_configuration_with_args():
    if len(sys.argv) < 2:
        error_message = "Se requiere el nombre del archivo de configuración como argumento."
        logger.error(error_message)
        sys.exit(1)

    config_file = sys.argv[1]
    check_file(config_file)
    return read_configuration(config_file)
