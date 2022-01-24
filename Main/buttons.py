from telebot import *


def base_btn(*args):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn = types.KeyboardButton(args[0][0])
    btn1 = types.KeyboardButton(args[0][1])
    btn2 = types.KeyboardButton(args[0][2])
    btn3 = types.KeyboardButton(args[0][3])
    btn4 = types.KeyboardButton(args[0][4])
    btn5 = types.KeyboardButton(args[0][5])
    btn6 = types.KeyboardButton(args[0][6])
    btn7 = types.KeyboardButton(args[0][7])
    btn8 = types.KeyboardButton(args[0][8])
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn, btn7, btn8)
    return markup


def branch(arg, lang='uz'):
    if lang == 'ru':
        pass
    elif lang == 'en':
        pass
    else:
        pass














