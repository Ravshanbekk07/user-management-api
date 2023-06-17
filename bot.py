import os
from telegram.ext import (
    Updater,Commandhandler
)
from call_back_fu import (start)

TOKEN = os.environ.get('TOKEN')
update = Updater(token=TOKEN)
dispatcher = update.dispatcher()