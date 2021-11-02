from telegram.ext import ConversationHandler
from telegram import InlineQueryResultMpeg4Gif, update

from views.bot_messages import View
from bot_models.bot_model import TelegramModel
from bot_models.db import Database

DOMAIN = "https://gif.revs.ir/"

class BotController:
    def __init__(self, update, context):
        self.update = update
        self.context = context
        self.admins = ["revisto"]
        self.db_channel_id = "-1001757428592"

    def cancel(self):
        self.update.message.reply_text(View.cancel())
        return ConversationHandler.END

    def get_gif(self):
        if (self.update.message["chat"]["username"]).lower() not in self.admins:
            self.update.message.reply_text(View.access_forbidden())            
            return ConversationHandler.END

        file_id = self.update.message.animation.file_id
        get_file = self.update.message.bot.get_file
        self.context.user_data["pending_gif"] = TelegramModel().save_pending_gif(get_file, file_id)
        self.update.message.reply_text(View.gif())
        return 1

    def get_gif_description_and_submit(self):
        pending_gif = self.context.user_data.get("pending_gif")
        description = self.update.message.text
        submit_gif_result = TelegramModel().submit_gif(pending_gif)
        gif_path = submit_gif_result["gif_path"]
        self.context.user_data.pop("pending_gif")
        if submit_gif_result["status"] == "exists":
            Database().update_gif(gif_path, description)
            self.update.message.reply_text(View.get_description_and_update())
        elif submit_gif_result["status"] == "new":
            self.context.bot.send_message(self.db_channel_id, f"{DOMAIN}{gif_path}")
            self.context.bot.send_animation(self.db_channel_id, open(gif_path, "rb"))
            Database().add_gif_to_db(gif_path, description)
            self.update.message.reply_text(View.get_description_and_submit())
        return ConversationHandler.END

    def start_and_help(self):
        welcome_message = View.welcome()
        self.update.message.reply_text(welcome_message)
        return True

    def inline_gif_query(self):
        query = self.update.inline_query.query
        results = list()
        related_gifs = TelegramModel().find_related_gifs(query)
        for similarity, gif in related_gifs:
            gif_url = f"{DOMAIN}{gif.gif_path}"
            print(gif_url)
            results.append(
                InlineQueryResultMpeg4Gif(
                    id=str(gif.id),
                    mpeg4_url=gif_url,
                    thumb_url=gif_url
                )
            )
        return results