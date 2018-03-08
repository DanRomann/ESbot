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
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    bot.send_message(chat_id=chat_id, text=texts['start_msg'], reply_markup=keyboard, one_time_keyboard=True)


def msg_handler(bot, update):
    chat_id = update.message.chat_id
    msg = update.message.text
    if msg == texts['start_btn']:
        set_status(chat_id, '0')
        test(chat_id, bot, update, "")
    if msg == texts['ans_exit']:
        start_handler(bot, update)


def test(user, bot, update, answer):
    if answer == 'cancel':
        set_status(user, '0')
        buttons = [[KeyboardButton(text=texts['start_btn'])]]
        keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True)
        bot.send_message(chat_id=user, text=texts['start_msg'], reply_markup=keyboard)
    elif get_status(user) == '0':
        set_status(user, '1')
        buttons = [[InlineKeyboardButton(texts['ans_1_1'], callback_data='m'),
                    InlineKeyboardButton(texts['ans_1_2'], callback_data='w')],
                   [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]
                   ]
        keyboard = InlineKeyboardMarkup(buttons)
        msg = bot.send_message(chat_id=user, text=texts['msg_1'], reply_markup=keyboard)
        del_mes.append(msg.message_id)
    elif get_status(user) == '1':
        # buttons = [[KeyboardButton(texts['ans_exit'])]]
        # keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard= True)
        if answer == 'm':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['ans_2_1'], callback_data='km')],
                       [InlineKeyboardButton(texts['ans_2_2'], callback_data='kitm')],
                       [InlineKeyboardButton(texts['ans_2_3'], callback_data='egim')],
                       [InlineKeyboardButton(texts['ans_2_4'], callback_data='grm')],
                       [InlineKeyboardButton(texts['ans_2_5'], callback_data='im')],
                       [InlineKeyboardButton(texts['ans_2_6'], callback_data='yam')],
                       [InlineKeyboardButton(texts['ans_2_7'], callback_data='mm')],
                       [InlineKeyboardButton(texts['ans_2_8'], callback_data='sm')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_2'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        else:
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['ans_2_1'], callback_data='kw')],
                       [InlineKeyboardButton(texts['ans_2_2'], callback_data='kitw')],
                       [InlineKeyboardButton(texts['ans_2_3'], callback_data='egiw')],
                       [InlineKeyboardButton(texts['ans_2_4'], callback_data='grw')],
                       [InlineKeyboardButton(texts['ans_2_5'], callback_data='iw')],
                       [InlineKeyboardButton(texts['ans_2_6'], callback_data='yaw')],
                       [InlineKeyboardButton(texts['ans_2_7'], callback_data='mw')],
                       [InlineKeyboardButton(texts['ans_2_8'], callback_data='sw')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_2'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'm':
        if answer == 'km':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['warrior'], callback_data='wkm')],
                       [InlineKeyboardButton(texts['hunter'], callback_data='hkm')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'kitm':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['mage'], callback_data='mkitm')],
                       [InlineKeyboardButton(texts['warrior'], callback_data='wkitm')],
                       [InlineKeyboardButton(texts['hunter'], callback_data='hkitm')],
                       [InlineKeyboardButton(texts['defender'], callback_data='dkitm')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'egim':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['mage'], callback_data='megim')],
                       [InlineKeyboardButton(texts['warrior'], callback_data='wegim')],
                       [InlineKeyboardButton(texts['hunter'], callback_data='hegim')],
                       [InlineKeyboardButton(texts['defender'], callback_data='degim')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'grm':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['mage'], callback_data='mgrm')],
                       [InlineKeyboardButton(texts['warrior'], callback_data='wgrm')],
                       [InlineKeyboardButton(texts['hunter'], callback_data='hgrm')],
                       [InlineKeyboardButton(texts['defender'], callback_data='dgrm')],
                       [InlineKeyboardButton(texts['assasin'], callback_data='agrm')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'im':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['mage'], callback_data='mim')],
                       [InlineKeyboardButton(texts['warrior'], callback_data='wim')],
                       [InlineKeyboardButton(texts['hunter'], callback_data='him')],
                       [InlineKeyboardButton(texts['defender'], callback_data='dim')],
                       [InlineKeyboardButton(texts['assasin'], callback_data='aim')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'yam':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['mage'], callback_data='myam')],
                       [InlineKeyboardButton(texts['hunter'], callback_data='hyam')],
                       [InlineKeyboardButton(texts['defender'], callback_data='dyam')],
                       [InlineKeyboardButton(texts['assasin'], callback_data='ayam')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'mm':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['mage'], callback_data='mmm')],
                       [InlineKeyboardButton(texts['warrior'], callback_data='wmm')],
                       [InlineKeyboardButton(texts['hunter'], callback_data='hmm')],
                       [InlineKeyboardButton(texts['defender'], callback_data='dmm')],
                       [InlineKeyboardButton(texts['assasin'], callback_data='amm')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'sm':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['warrior'], callback_data='wsm')],
                       [InlineKeyboardButton(texts['hunter'], callback_data='hsm')],
                       [InlineKeyboardButton(texts['defender'], callback_data='dsm')],
                       [InlineKeyboardButton(texts['assasin'], callback_data='asm')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    # women
    elif get_status(user) == 'w':
        if answer == 'kw':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['mage'], callback_data='mkw')],
                       [InlineKeyboardButton(texts['defender'], callback_data='dkw')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'kitw':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['mage'], callback_data='mkitw')],
                       [InlineKeyboardButton(texts['hunter'], callback_data='hkitw')],
                       [InlineKeyboardButton(texts['assasin'], callback_data='akitw')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'egiw':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['mage'], callback_data='megiw')],
                       [InlineKeyboardButton(texts['hunter'], callback_data='hegiw')],
                       [InlineKeyboardButton(texts['assasin'], callback_data='aegiw')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'grw':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['mage'], callback_data='mgrw')],
                       [InlineKeyboardButton(texts['warrior'], callback_data='wgrw')],
                       [InlineKeyboardButton(texts['hunter'], callback_data='hgrw')],
                       [InlineKeyboardButton(texts['defender'], callback_data='dgrw')],
                       [InlineKeyboardButton(texts['assasin'], callback_data='agrw')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'iw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'yaw':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['warrior'], callback_data='wyaw')],
                       [InlineKeyboardButton(texts['hunter'], callback_data='hyaw')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'mw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['awilix'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'sw':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['mage'], callback_data='msw')],
                       [InlineKeyboardButton(texts['hunter'], callback_data='hsw')],
                       [InlineKeyboardButton(texts['ans_exit'], callback_data='cancel')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_class'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'km':
        if answer == 'wkm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['cuchulainn'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'hkm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['cernunnos'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'kitm':
        if answer == 'mkitm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['aokuang'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'wkitm':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['high_alive'], callback_data='wkitm1')],
                       [InlineKeyboardButton(texts['support_team'], callback_data='wkitm2')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_choose'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'hkitm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['houyi'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'dkitm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['xingtian'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'egim':
        if answer == 'megim':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['damage'], callback_data='megim1')],
                       [InlineKeyboardButton(texts['support_friend'], callback_data='megim2')], ]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_choose'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'wegim':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['osiris'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'hegim':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['anhur'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'degim':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['help_friends'], callback_data='degim1')],
                       [InlineKeyboardButton(texts['center_battle'], callback_data='degim2')], ]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_choose'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'grm':
        if answer == 'mgrm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['zeus'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'wgrm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['achilles'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'hgrm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['chiron'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'dgrm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['ares'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'agrm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['thanatos'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'im':
        if answer == 'mim':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['agni'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'wim':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['mobile'], callback_data='wim1')],
                       [InlineKeyboardButton(texts['damage'], callback_data='wim2')], ]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_choose'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'him':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['rama'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'dim':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['support'], callback_data='dim1')],
                       [InlineKeyboardButton(texts['init'], callback_data='dim2')], ]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_choose'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'aim':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['bakasura'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'yam':
        if answer == 'myam':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['raijin'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'hyam':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['hachiman'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'dyam':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['kuzenbo'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'ayam':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['raijin'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'mm':
        if answer == 'mmm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['ahpuch'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'wmm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['chaac'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'hmm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['ahmuzencab'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'dmm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['cabrakan'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'amm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['hunbatz'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'sm':
        if answer == 'wsm':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['eye'], callback_data='wsm1')],
                       [InlineKeyboardButton(texts['hand'], callback_data='wsm2')], ]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_victim'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'hsm':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['ullr'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'dsm':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['fire'], callback_data='dsm1')],
                       [InlineKeyboardButton(texts['ice'], callback_data='dsm2')], ]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_choose'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'asm':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['rat'], callback_data='asm1')],
                       [InlineKeyboardButton(texts['rat_son'], callback_data='asm2')],
                       [InlineKeyboardButton(texts['father_son'], callback_data='asm3')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_become'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'kw':
        if answer == 'mkw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['morrigan'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'dkw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['artio'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'kitw':
        if answer == 'mkitw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['nuwa'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'hkitw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['jingwei'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'akitw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['daji'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'egiw':
        if answer == 'megiw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['isis'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'hegiw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['neith'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'aegiw':
            set_status(user, answer)
            buttons = [[InlineKeyboardButton(texts['easy'], callback_data='aegiw1')],
                       [InlineKeyboardButton(texts['hard'], callback_data='aegiw2')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['msg_choose'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'grw':
        if answer == 'mgrw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['aphrodite'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'wgrw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['nike'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'hgrw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['medusa'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'dgrw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['athena'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'agrw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['nemesis'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'yaw':
        if answer == 'wyaw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['amaterasu'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'hyaw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['izanami'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'sw':
        if answer == 'msw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['sol'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'hsw':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['skadi'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'wkitm':
        if answer == 'wkitm1':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['sunwukong'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        if answer == 'wkitm2':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['guanyu'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'megim':
        if answer == 'megim1':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['anubis'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'megim2':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['ra'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'degim':
        if answer == 'degim1':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['khepri'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'degim2':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['sobek'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'wim':
        if answer == 'wim1':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['vamana'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'wim2':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['ravana'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'dim':
        if answer == 'dim1':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['ganesha'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'dim2':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['kumbhakarna'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'wsm':
        if answer == 'wsm1':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['odin'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'wsm2':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['tyr'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'dsm':
        if answer == 'dsm1':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['fafnir'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'dsm2':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['ymir'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'asm':
        if answer == 'asm1':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['loki'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'asm2':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['fenrir'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'asm3':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['thor'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
    elif get_status(user) == 'aegiw':
        if answer == 'aegiw1':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['bastet'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)
        elif answer == 'aegiw2':
            set_status(user, answer)
            buttons = [[KeyboardButton(texts['ans_exit'])]]
            keyboard = ReplyKeyboardMarkup(buttons)
            bot.edit_message_text(chat_id=user, message_id=del_mes[-1], text=texts['serqet'])
            bot.edit_message_reply_markup(chat_id=user, message_id=del_mes[-1], reply_markup=keyboard)


def callback_handler(bot, update):
    chat_id = update.callback_query.message.chat_id
    query_data = update.callback_query.data
    print(query_data)
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
