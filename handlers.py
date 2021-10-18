
from telegram import Update
from telegram.ext import CallbackContext

from controllers.bot_controller import BotController


def start(update: Update, context: CallbackContext) -> int:
    return BotController(update, context).start()


def help_command(update: Update, context: CallbackContext) -> int:
    return BotController(update, context).help()

def inline_gif_query(update: Update, context: CallbackContext) -> int:
    return BotController(update, context).inline_gif_query()

def get_gif(update: Update, context: CallbackContext) -> int:
    return BotController(update, context).get_gif()

def get_gif_description(update: Update, context: CallbackContext) -> int:
    return BotController(update, context).get_gif_description_and_submit()

def cancel(update: Update, context: CallbackContext) -> int:
    return BotController(update, context).cancel()