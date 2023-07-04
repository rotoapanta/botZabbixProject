import configparser
import logging

logger = logging.getLogger(__name__)

def read_configuration(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    configuration = {}

    if 'Zabbix' in config:
        zabbix_section = config['Zabbix']
        configuration['zabbix_url'] = zabbix_section.get('url')
        configuration['zabbix_user'] = zabbix_section.get('user')
        configuration['zabbix_password'] = zabbix_section.get('password')

    if 'Telegram' in config:
        telegram_section = config['Telegram']
        configuration['telegram_token'] = telegram_section.get('token')

    return configuration
