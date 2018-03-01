import yaml
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from database import *

TOKEN = '503377124:AAGoehZa_dEnCG5ZBb0evPXxXoGShn4hlHE'

texts = yaml.safe_load(open('texts.yaml'))
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

del_mes = []

def start_handler(bot, update):
    chat_id = update.message.chat_id
    if not user_exist(chat_id):
        username = update.message.from_user.username
        insert_user(chat_id, username)
    buttons = [[KeyboardButton(text=texts['start_btn'])]]
    keyboard = ReplyKeyboardMarkup(keyboard= buttons, resize_keyboard=True)
    bot.send_message(chat_id = chat_id, text= texts['start_msg'], reply_markup=keyboard, one_time_keyboard= True)

def msg_handler(bot, update):
    chat_id = update.message.chat_id
    msg = update.message.text
    if msg == texts['start_btn']:
        set_status(chat_id, 0)
        test(chat_id, bot, update, "")
    if msg == texts['ans_exit']:

        start_handler(bot, update)

def test(user, bot, update, answer):
    if answer == 'cancel':
        set_status(user, 0)
        buttons = [[KeyboardButton(text=texts['start_btn'])]]
        keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard= True)
        bot.send_message(chat_id=user, text=texts['start_msg'], reply_markup=keyboard)
    elif get_status(user) == 0:
            set_status(user, 1)
            buttons = [[InlineKeyboardButton(texts['ans_1_1'], callback_data='yes'), InlineKeyboardButton(texts['ans_1_2'], callback_data='no')],
                   [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            msg = bot.send_message(chat_id=user, text= texts['msg_1'], reply_markup= keyboard)
            del_mes.append(msg.message_id)
    elif get_status(user) == 1:
            set_status(user, 2)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard= True)
            if answer == 'yes':
                bot.send_message(chat_id=user, text=texts['msg_2'], reply_markup= keyboard)
            else:
                bot.send_message(chat_id=user, text=texts['msg_3'], reply_markup=keyboard)



def callback_handler(bot, update):
    chat_id = update.callback_query.message.chat_id
    query_data = update.callback_query.data
    print(query_data)
    bot.delete_message(chat_id = chat_id, message_id=del_mes.pop())
    test(chat_id, bot, update, query_data)



def main():
    create_tables()
    print('database created')
    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(MessageHandler(Filters.text, msg_handler))
    dispatcher.add_handler(CallbackQueryHandler(callback_handler))
    updater.start_polling()

if __name__ == '__main__':
    print('start')
    main()
