from telegram.ext import Updater, Filters, InlineQueryHandler, CommandHandler, ConversationHandler, CallbackContext, MessageHandler
from config import Config

from handlers import *


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(Config.token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    submit_gif_converstation = ConversationHandler(
        entry_points=[MessageHandler(Filters.animation, get_gif)],
        states={
            1: [
                MessageHandler(Filters.text, get_gif_description),
                CommandHandler("cancel", cancel),
            ]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    dispatcher.add_handler(submit_gif_converstation)

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(InlineQueryHandler(inline_gif_query))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()