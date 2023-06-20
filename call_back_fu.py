import requests
from telegram import (
    Update
    
)
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
  
    first_name = update.message.chat.first_name
    last_name=update.message.chat.last_name
    username=update.message.chat.username
    doc_id=update.message.chat_id


    url = 'http://rramazonov.pythonanywhere.com/users/'
    requests.post(url,json={"firstname": first_name, "lastname": last_name, "username": username,"chat_id":doc_id})
    update.message.reply_html(
        text=f"Hello, <b>{first_name}</b>. Xush Kelibsiz "
        
    )
