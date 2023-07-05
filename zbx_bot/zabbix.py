import logging
from pyzabbix import ZabbixAPI
from pythonping import ping

logger = logging.getLogger(__name__)


def connect_to_zabbix(configuration):
    zabbix_url = configuration.get('zabbix_url')
    zabbix_user = configuration.get('zabbix_user')
    zabbix_password = configuration.get('zabbix_password')

    if not zabbix_url or not zabbix_user or not zabbix_password:
        logger.error("Configuración de Zabbix incompleta.")
        return None

    try:
        zabbix = ZabbixAPI(zabbix_url)
        zabbix.login(zabbix_user, zabbix_password)
        return zabbix
    except Exception as e:
        logger.exception("Error al conectar a Zabbix: %s", str(e))
        return None


def search_hosts_by_name(zabbix, name):
    try:
        hosts = zabbix.host.get(search={'name': name}, output=['hostid', 'name'])
        return hosts
    except Exception as e:
        logger.exception("Error al buscar hosts por nombre: %s", str(e))
        return []


def get_host_info(zabbix, host_id):
    try:
        host = zabbix.host.get(hostids=host_id, output=['host'])
        return host
    except Exception as e:
        logger.exception("Error al obtener información del host: %s", str(e))
        return []


def get_host_ip(zabbix, host_id):
    try:
        host_interfaces = zabbix.hostinterface.get(hostids=host_id, output=['ip'])
        ip_address = host_interfaces[0]['ip'] if host_interfaces else None
        return ip_address
    except Exception as e:
        logger.exception("Error al obtener la dirección IP del host: %s", str(e))
        return None


def perform_ping(ip_address):
    try:
        respuesta_ping = ping(ip_address, count=5)
        return str(respuesta_ping)
    except Exception as e:
        logger.exception("Error al realizar el ping: %s", str(e))
        return None