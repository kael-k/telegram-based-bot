import logging

from telegram.ext import Dispatcher, Filters, MessageHandler, Updater

from telegram_based_bot.bot.handlers import update_handler
from telegram_based_bot.env import EnvironmentConfig

log = logging.getLogger(__name__)
env_config = EnvironmentConfig()


def run_telegram_bot():
    updater = Updater(env_config.TELEGRAM_BOT_TOKEN)
    dispatcher: Dispatcher = updater.dispatcher

    filters = Filters.all
    if env_config.TELEGRAM_BOT_CHAT_IDS:
        filters &= Filters.chat(env_config.TELEGRAM_BOT_CHAT_IDS)

    dispatcher.add_handler(MessageHandler(filters=filters, callback=update_handler))
    updater.start_polling()
    updater.idle()


__all__ = ["run_telegram_bot"]
