from os import stat
from random import choice

class View:
    @staticmethod
    def cancel():
        messages = ["باش!", "باشه!", "حله!", "اوکی!",]
        message = choice(messages)
        return message

    @staticmethod
    def gif():
        adverbs = ["باش!", "باشه!", "حله!", "اوکی!",]
        adverb = choice(adverbs)
        message = f"{adverb} حالا توضیحات گیف رو بفرست."
        return message

    @staticmethod
    def get_description_and_submit():
        messages = ["اضافه شد!", "اوکی شد!", "با موفقیت اضافه شد!"]
        message = choice(messages)
        return message

    @staticmethod
    def get_description_and_update():
        message = "گیف وجود داشت. توضیحات گیف آپدیت شد."
        return message

    @staticmethod
    def access_forbidden():
        message = (
            "متاسفانه شما جزو اشخاص معتمد ما نیستید."
            "\n"        
            "اگر اصرار دارید که به دیتابیس گیف ما کمک کنید به @revisto پیام بدید."
        )
        return message

    @staticmethod
    def welcome():
        message = (
            "سلام, من ربات RevGif هستم که میشه ترکیب @Revisto و Gif!"
            "\n"
            "\nبه من گیف ارسال میشه با توضیحات مربوط بهش و من اونارو سیو میکنم. بعدش میتونید توی چت هاتون من رو صدا بزنید و بهتون گیف های مرتبط رو نشون بدم."
            "\n"
            "\nیه سری افراد خاص و مطمین میتونن گیف ثبت کنن و اگه میخواین بهشون اضافه بشی به سازنده بات پیام بده @Revisto :)"
            "\n"
            "\nو حالا چجوری توی چتتون من رو صدا بزنید:"
            "\n"
            "\nاول آی‌دی من یعنی @RevGifBot رو بزنید و جلوش توضیحات مربوط به گیفی که دنبالش هستید رو بفرستید, یعنی یه چیزی تو, این مایه‌ها:"
            "\n"
            "\n@RevGifBot داداش گلمی خلسه"
            "\n"
            "\n"
            "\nهمین دیگه. خوش باشید :)"
        )
        return message