from pyzabbix import ZabbixAPI
from pythonping import ping


def connect_to_zabbix(configuration):
    zabbix_url = configuration['zabbix_url']
    zabbix_user = configuration['zabbix_user']
    zabbix_password = configuration['zabbix_password']

    zabbix = ZabbixAPI(zabbix_url)
    zabbix.login(zabbix_user, zabbix_password)

    return zabbix


def search_hosts_by_name(zabbix, name):
    hosts = zabbix.host.get(search={'name': name}, output=['hostid', 'name'])
    return hosts


def get_host_info(zabbix, host_id):
    host = zabbix.host.get(hostids=host_id, output=['host'])
    return host


def get_host_ip(zabbix, host_id):
    host_interfaces = zabbix.hostinterface.get(hostids=host_id, output=['ip'])
    ip_address = host_interfaces[0]['ip'] if host_interfaces else None
    return ip_address


def perform_ping(ip_address):
    respuesta_ping = ping(ip_address, count=5)
    return str(respuesta_ping)
