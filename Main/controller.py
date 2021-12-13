import telebot
from .tokens import *
from telebot import types
from .service import *

bot = telebot.TeleBot(tokenlist['uzbegim'])


class InlineController:
    def __init__(self, m, userid, messageid=None, call_data=None, chatid=None):
        self.userid = userid
        self.messageid = messageid
        self.call_data = call_data
        self.chatid = chatid
        self.m = m

    def category(self):
        category = get_category()
        ikey = types.InlineKeyboardMarkup(row_width=2)
        l = len(category)
        for i in range(0, l, 2):
            btn = types.InlineKeyboardButton(text=category[i].name_uz, callback_data=category[i].name_uz)
            if l % 2 == 1 and l-1 == i:
                ikey.add(btn)
            else:
                btn1 = types.InlineKeyboardButton(text=category[i + 1].name_uz, callback_data=category[i + 1].name_uz)
                ikey.add(btn, btn1)
        print(self.call_data)
        if self.call_data == None:
            bot.send_message(self.userid, text='Mahsulot Kategoriyasi', reply_markup=ikey)
        else:
            bot.delete_message(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id)
            bot.send_message(self.userid, text='Mahsulot Kategoriyasi', reply_markup=ikey)

    def products(self, cat_id):
        products = get_product(cat_id)
        ikey = types.InlineKeyboardMarkup(row_width=2)
        l = len(products)
        for i in range(0, l, 2):
            btn = types.InlineKeyboardButton(text=products[i].name_uz, callback_data=products[i].name_uz)
            if l % 2 == 1 and l-1 == i:
                ikey.add(btn)
            else:
                btn1 = types.InlineKeyboardButton(text=products[i + 1].name_uz, callback_data=products[i + 1].name_uz)
                ikey.add(btn, btn1)
        btn = types.InlineKeyboardButton(text="⬅️Ortga", callback_data='category')
        ikey.add(btn)
        try:
            bot.delete_message(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id)
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Products.objects.get(id=3).img, caption='Maxsulotlaaar', reply_markup=ikey)
        except:
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Products.objects.get(id=3).img, caption='Maxsulotlaaar', reply_markup=ikey)

            # bot.edit_message_text(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id, text='Mahsulotlaar', reply_markup=ikey)

    def product_item(self, pro_id):
        product_item = get_product_item(pro_id)
        ikey = types.InlineKeyboardMarkup(row_width=2)
        l = len(product_item)
        for i in range(0, l, 2):
            btn = types.InlineKeyboardButton(text=product_item[i].name_uz, callback_data=product_item[i].name_uz)
            if l % 2 == 1 and l-1 == i:
                ikey.add(btn)
            else:
                btn1 = types.InlineKeyboardButton(text=product_item[i + 1].name_uz, callback_data=product_item[i + 1].name_uz)
                ikey.add(btn, btn1)
        btn = types.InlineKeyboardButton(text="⬅️Ortga", callback_data=str(pro_id))
        ikey.add(btn)
        try:
            bot.delete_message(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id)
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Products.objects.get(id=3).img,   caption='Maxsulot itemlari', reply_markup=ikey)
        except:
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Products.objects.get(id=3).img,   caption='Maxsulot itemlari', reply_markup=ikey)

    def order_item(self, pro_id):
        orders = get_product_item()

