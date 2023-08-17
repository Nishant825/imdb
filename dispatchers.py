from telegram.ext import Updater
from config import TOKEN
from handlers import *


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# command dispatchers

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(graph_handler)
dispatcher.add_handler(button_callback_handler)

# Message dispathers
dispatcher.add_handler(unknown_command_handler)
dispatcher.add_handler(unknown_mesage_handler)