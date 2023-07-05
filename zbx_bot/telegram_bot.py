import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from zbx_bot import zabbix

logger = logging.getLogger(__name__)


def ping_host(update: Update, context: CallbackContext):
    try:
        update.message.reply_text('Por favor, ingresa las palabras clave para la búsqueda del host:')
    except Exception as e:
        logger.exception("Error al responder al comando 'ping': %s", str(e))


def search_host(update: Update, context: CallbackContext):
    try:
        keywords = update.message.text
        zabbix_instance = context.bot_data.get('zabbix')

        if zabbix_instance is None:
            update.message.reply_text('No se encontró la instancia de Zabbix.')
            return

        hosts = zabbix.search_hosts_by_name(zabbix_instance, keywords)

        if not hosts:
            update.message.reply_text('No se encontraron hosts.')
            return

        keyboard = [[InlineKeyboardButton(host['name'], callback_data=host['hostid'])] for host in hosts]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Hosts encontrados:', reply_markup=reply_markup)
    except Exception as e:
        logger.exception("Error al buscar hosts: %s", str(e))


def get_ping(update: Update, context: CallbackContext):
    try:
        host_id = update.callback_query.data
        zabbix_instance = context.bot_data.get('zabbix')

        if zabbix_instance is None:
            update.callback_query.message.reply_text('No se encontró la instancia de Zabbix.')
            return

        host = zabbix.get_host_info(zabbix_instance, host_id)
        ip_address = zabbix.get_host_ip(zabbix_instance, host_id)

        if ip_address is None:
            update.callback_query.message.reply_text(f"No se pudo obtener la dirección IP del host {host[0]['host']}.")
            return

        respuesta_ping = zabbix.perform_ping(ip_address)

        update.callback_query.message.reply_text(
            f"Respuesta del ping para el host {host[0]['host']} ({ip_address}):\n\n{respuesta_ping}"
        )
    except Exception as e:
        logger.exception("Error al obtener la respuesta del ping: %s", str(e))


def main(bot_data):
    try:
        updater = Updater(bot_data['configuration']['telegram_token'])
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler('ping', ping_host))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, search_host))
        dispatcher.add_handler(CallbackQueryHandler(get_ping))

        # Pasar el bot_data al contexto
        dispatcher.bot_data['zabbix'] = bot_data['zabbix']

        updater.start_polling()
        updater.idle()
    except Exception as e:
        logger.exception("Error al iniciar el bot de Telegram: %s", str(e))