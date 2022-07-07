import logging

from telegram import Update
from telegram.ext import CallbackContext

from telegram_based_bot.env import EnvironmentConfig

from .utils import get_random_asset_chad

env_config = EnvironmentConfig()
log = logging.getLogger(__name__)


def update_handler(update: Update, _: CallbackContext):
    message = update.effective_message.text or update.message.caption
    if not message:
        log.debug("No message found in chat message...")
        return

    message = message.lower()
    if any(e in message for e in env_config.TELEGRAM_BOT_BASED_KEYWORDS):
        asset_chad = get_random_asset_chad()
        asset_chad.send(update.effective_message)
