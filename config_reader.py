import configparser

def read_configuration():
    config = configparser.ConfigParser()
    config.read('config.ini')

    configuration = {
        'zabbix_url': config['Zabbix']['url'],
        'zabbix_user': config['Zabbix']['user'],
        'zabbix_password': config['Zabbix']['password'],
        'telegram_token': config['Telegram']['token']
    }

    return configuration

