from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils import get_crypto_data
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from utils import save_chart


def start(update, context):
    # button_labels = ['BTC', 'ETH']
    # crypto_data = get_crypto_data()
    button_labels = [i["symbol"].upper() for i in crypto_data]
    keyboard = [
        [InlineKeyboardButton(label, callback_data=label)] for label in button_labels
    ]
    
    keyboard = [keyboard[i] + keyboard[i+1] + keyboard[i+2] for i in range(0, len(keyboard), 3)]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the message with the buttons
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to live crypto Data:')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Please choose an Symbol:',
                             reply_markup=reply_markup)



def start(update, context):
    button_labels = ['Text','Graph']
    keyboard = [
        [InlineKeyboardButton(label, callback_data=label)] for label in button_labels
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send the message with the buttons
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to live crypto Data:')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Please choose format to see results:',
                             reply_markup=reply_markup)



def button_callback(update, context):
    query = update.callback_query
    button_label = query.data
    context.bot.send_message(chat_id=query.message.chat_id, text=f'You selected: {button_label}')
    crypto_data = get_crypto_data()
    if button_label == "Text":
        button_labels = [i["symbol"].upper() for i in crypto_data]
        keyboard = [
            [InlineKeyboardButton(label, callback_data=label)] for label in button_labels
        ]
        keyboard = [keyboard[i] + keyboard[i+1] + keyboard[i+2] for i in range(0, len(keyboard), 3)]
        reply_markup = InlineKeyboardMarkup(keyboard)

        context.bot.send_message(chat_id=update.effective_chat.id, text='Please select crypto symbol to see data:',
                                reply_markup=reply_markup)

        # button_labels = [i["symbol"].upper() for i in crypto_data]
        # keyboard = [
        #     [InlineKeyboardButton(label, callback_data=label)] for label in button_labels
        # ]
        
        # keyboard = [keyboard[i] + keyboard[i+1] + keyboard[i+2] for i in range(0, len(keyboard), 3)]
        # reply_markup = InlineKeyboardMarkup(keyboard)
        # # Send the message with the buttons
        # context.bot.send_message(chat_id=update.effective_chat.id, text='Please choose an Symbol:',
        #                         reply_markup=reply_markup)

    elif button_label == "Graph":
        graph(update, context)

    else:
        for i in crypto_data:
            if i["symbol"].upper() == button_label:
                text = "||----------------------------------------\n"
                for key, value in i.items():
                    text+= f"||  <b>{key.capitalize()}</b> ==> <pre>{value}</pre> \n"
                text+= "||----------------------------------------"
                context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode="HTML")


def unknown_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'invalid command please enter valid command')


def graph(update, context):
    chat_id = update.effective_chat.id
    save_chart()
    context.bot.send_photo(chat_id, photo=open('images/graph.png', 'rb'))

def handle_unknown_message(update, context):
    chat_id = update.effective_chat.id
    response = "I don't understand. Please select valid data"
    context.bot.send_message(chat_id=chat_id, text=response)


################ Register Handlers ####################

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
graph_handler = CommandHandler('graph', graph)
button_callback_handler = CallbackQueryHandler(button_callback)
unknown_command_handler = (MessageHandler(Filters.command, unknown_command))
unknown_mesage_handler = MessageHandler(Filters.all, handle_unknown_message)
