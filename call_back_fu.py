from telegram import (Update)


from telegram.ext import CallbackContext


def start(update:Update,context:CallbackContext):

    first_name = update.message.chat.first_name
    update.message.reply_html(
        text = f"assalomu aleykum <i>{first_name}</i> bizning botimizga xush kelibsiz"
        
    )