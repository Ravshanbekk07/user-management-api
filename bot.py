import os
from telegram.ext import (
    Updater,Commandhandler
)
from call_back_fu import (start)

TOKEN = os.environ.get('TOKEN')
def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher()
    dispatcher.add_handler(handler=Commandhandler('start', start))
   







    updater.start_polling()
    updater.idle()


main()