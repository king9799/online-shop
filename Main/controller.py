import telebot
from .tokens import *
from telebot import types
from .service import *
from .text import *

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
            btn = types.InlineKeyboardButton(text=category[i].name_uz, callback_data=f'category_id_{category[i].id}')
            if l % 2 == 1 and l-1 == i:
                ikey.add(btn)
            else:
                btn1 = types.InlineKeyboardButton(text=category[i + 1].name_uz, callback_data=f'category_id_{category[i+1].id}')
                ikey.add(btn, btn1)
        if self.call_data == None:
            bot.send_message(self.userid, text='Mahsulot Kategoriyasi', reply_markup=ikey)
        else:
            bot.delete_message(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id)
            bot.send_message(self.userid, text='Mahsulot Kategoriyasi', reply_markup=ikey)

    def category_ru(self):
        category = get_category()
        ikey = types.InlineKeyboardMarkup(row_width=2)
        l = len(category)
        for i in range(0, l, 2):
            btn = types.InlineKeyboardButton(text=category[i].name_ru, callback_data=f'category_id_{category[i].id}')
            if l % 2 == 1 and l-1 == i:
                ikey.add(btn)
            else:
                btn1 = types.InlineKeyboardButton(text=category[i + 1].name_ru, callback_data=f'category_id_{category[i+1].id}')
                ikey.add(btn, btn1)
        if self.call_data == None:
            bot.send_message(self.userid, text='Категория продукта', reply_markup=ikey)
        else:
            bot.delete_message(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id)
            bot.send_message(self.userid, text='Категория продукта', reply_markup=ikey)

    def category_en(self):
        category = get_category()
        ikey = types.InlineKeyboardMarkup(row_width=2)
        l = len(category)
        for i in range(0, l, 2):
            btn = types.InlineKeyboardButton(text=category[i].name_en, callback_data=f'category_id_{category[i].id}')
            if l % 2 == 1 and l-1 == i:
                ikey.add(btn)
            else:
                btn1 = types.InlineKeyboardButton(text=category[i + 1].name_en, callback_data=f'category_id_{category[i+1].id}')
                ikey.add(btn, btn1)
        if self.call_data == None:
            bot.send_message(self.userid, text='Product Category', reply_markup=ikey)
        else:
            bot.delete_message(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id)
            bot.send_message(self.userid, text='Product Category', reply_markup=ikey)

    def products(self, cat_id):
        products = get_product(cat_id)
        ikey = types.InlineKeyboardMarkup(row_width=2)
        l = len(products)
        for i in range(0, l, 2):
            btn = types.InlineKeyboardButton(text=products[i].name_uz, callback_data=f'product_id_{products[i].id}')
            if l % 2 == 1 and l-1 == i:
                ikey.add(btn)
            else:
                btn1 = types.InlineKeyboardButton(text=products[i + 1].name_uz, callback_data=f'product_id_{products[i+1].id}')
                ikey.add(btn, btn1)
        btn = types.InlineKeyboardButton(text="⬅️Ortga", callback_data='category')
        ikey.add(btn)
        try:
            bot.delete_message(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id)
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Categories.objects.get(id=cat_id).img, caption='Maxsulotlaaar', reply_markup=ikey)
        except:
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Categories.objects.get(id=cat_id).img, caption='Maxsulotlaaar', reply_markup=ikey)

    def products_ru(self, cat_id):
        products = get_product(cat_id)
        ikey = types.InlineKeyboardMarkup(row_width=2)
        l = len(products)
        for i in range(0, l, 2):
            btn = types.InlineKeyboardButton(text=products[i].name_ru, callback_data=f'product_id_{products[i].id}')
            if l % 2 == 1 and l-1 == i:
                ikey.add(btn)
            else:
                btn1 = types.InlineKeyboardButton(text=products[i + 1].name_ru, callback_data=f'product_id_{products[i+1].id}')
                ikey.add(btn, btn1)
        btn = types.InlineKeyboardButton(text="⬅️Ortga", callback_data='category')
        ikey.add(btn)
        try:
            bot.delete_message(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id)
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Categories.objects.get(id=cat_id).img, caption='Продукты', reply_markup=ikey)
        except:
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Categories.objects.get(id=cat_id).img, caption='Продукты', reply_markup=ikey)

    def products_en(self, cat_id):
        products = get_product(cat_id)
        ikey = types.InlineKeyboardMarkup(row_width=2)
        l = len(products)
        for i in range(0, l, 2):
            btn = types.InlineKeyboardButton(text=products[i].name_en, callback_data=f'product_id_{products[i].id}')
            if l % 2 == 1 and l-1 == i:
                ikey.add(btn)
            else:
                btn1 = types.InlineKeyboardButton(text=products[i + 1].name_en, callback_data=f'product_id_{products[i+1].id}')
                ikey.add(btn, btn1)
        btn = types.InlineKeyboardButton(text="⬅️Ortga", callback_data='category')
        ikey.add(btn)
        try:
            bot.delete_message(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id)
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Categories.objects.get(id=cat_id).img, caption='Products', reply_markup=ikey)
        except:
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Categories.objects.get(id=cat_id).img, caption='Products', reply_markup=ikey)

    def product_item(self, pro_id):
        product_item = get_product_item(pro_id)
        ikey = types.InlineKeyboardMarkup(row_width=2)
        l = len(product_item)
        for i in range(0, l, 2):
            btn = types.InlineKeyboardButton(text=product_item[i].name_uz, callback_data=f'product_item_id_{product_item[i].id}')
            if l % 2 == 1 and l-1 == i:
                ikey.add(btn)
            else:
                btn1 = types.InlineKeyboardButton(text=product_item[i + 1].name_uz, callback_data=f'product_item_id_{product_item[i+1].id}')
                ikey.add(btn, btn1)
        btn = types.InlineKeyboardButton(text="⬅️Ortga", callback_data=str(pro_id))
        ikey.add(btn)
        try:
            bot.delete_message(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id)
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Products.objects.get(id=pro_id).img,   caption='Maxsulot itemlari', reply_markup=ikey, parse_mode='Markdown')
        except:
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Products.objects.get(id=pro_id).img,   caption='Maxsulot itemlari', reply_markup=ikey, parse_mode='Markdown')

    def product_item_ru(self, pro_id):
        product_item = get_product_item(pro_id)
        ikey = types.InlineKeyboardMarkup(row_width=2)
        l = len(product_item)
        for i in range(0, l, 2):
            btn = types.InlineKeyboardButton(text=product_item[i].name_ru, callback_data=f'product_item_id_{product_item[i].id}')
            if l % 2 == 1 and l-1 == i:
                ikey.add(btn)
            else:
                btn1 = types.InlineKeyboardButton(text=product_item[i + 1].name_ru, callback_data=f'product_item_id_{product_item[i+1].id}')
                ikey.add(btn, btn1)
        btn = types.InlineKeyboardButton(text="⬅️Ortga", callback_data=str(pro_id))
        ikey.add(btn)
        try:
            bot.delete_message(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id)
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Products.objects.get(id=pro_id).img,   caption='Товарные позиции', reply_markup=ikey, parse_mode='Markdown')
        except:
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Products.objects.get(id=pro_id).img,   caption='Товарные позиции', reply_markup=ikey, parse_mode='Markdown')

    def product_item_en(self, pro_id):
        product_item = get_product_item(pro_id)
        ikey = types.InlineKeyboardMarkup(row_width=2)
        l = len(product_item)
        for i in range(0, l, 2):
            btn = types.InlineKeyboardButton(text=product_item[i].name_en, callback_data=f'product_item_id_{product_item[i].id}')
            if l % 2 == 1 and l-1 == i:
                ikey.add(btn)
            else:
                btn1 = types.InlineKeyboardButton(text=product_item[i + 1].name_en, callback_data=f'product_item_id_{product_item[i+1].id}')
                ikey.add(btn, btn1)
        btn = types.InlineKeyboardButton(text="⬅️Ortga", callback_data=str(pro_id))
        ikey.add(btn)
        try:
            bot.delete_message(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id)
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Products.objects.get(id=pro_id).img,   caption='Product items', reply_markup=ikey, parse_mode='Markdown')
        except:
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=Products.objects.get(id=pro_id).img,   caption='Product items', reply_markup=ikey, parse_mode='Markdown')

    def item_info(self, pro_item_id):
        proi = ProductItem.objects.get(id=pro_item_id)
        ikey = types.InlineKeyboardMarkup(row_width=5)
        number = [[1,2,3,4,5],[6,7,8,9,10],[15,20,25,30,35]]
        for i in number:
            print('ii',i[0])
            btn = types.InlineKeyboardButton(text=f'{i[0]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[0]}')
            btn1 = types.InlineKeyboardButton(text=f'{i[1]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[1]}')
            btn2 = types.InlineKeyboardButton(text=f'{i[2]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[2]}')
            btn3 = types.InlineKeyboardButton(text=f'{i[3]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[3]}')
            btn4 = types.InlineKeyboardButton(text=f'{i[4]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[4]}')
            ikey.add(btn, btn1, btn2, btn3, btn4)
        btn = types.InlineKeyboardButton(text="⬅️Ortga", callback_data=str(pro_item_id))
        ikey.add(btn)
        try:
            bot.delete_message(chat_id=self.userid, message_id=self.call_data.message.message_id)
            text = ptoduct_item(proi.name_uz, proi.price, proi.desc_uz)
            print(text)
            bot.send_photo(chat_id=self.userid, photo=ProductItem.objects.get(id=pro_item_id).img,   caption=text, reply_markup=ikey, parse_mode='HTML')
        except:
            bot.send_photo(chat_id=self.userid, photo=Products.objects.get(id=pro_item_id).img,   caption='Maxsulot itemlari', reply_markup=ikey, parse_mode='HTML')

    def item_info_ru(self, pro_item_id):
        proi = ProductItem.objects.get(id=pro_item_id)
        ikey = types.InlineKeyboardMarkup(row_width=5)
        number = [[1,2,3,4,5],[6,7,8,9,10],[15,20,25,30,35]]
        for i in number:
            print('ii',i[0])
            btn = types.InlineKeyboardButton(text=f'{i[0]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[0]}')
            btn1 = types.InlineKeyboardButton(text=f'{i[1]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[1]}')
            btn2 = types.InlineKeyboardButton(text=f'{i[2]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[2]}')
            btn3 = types.InlineKeyboardButton(text=f'{i[3]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[3]}')
            btn4 = types.InlineKeyboardButton(text=f'{i[4]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[4]}')
            ikey.add(btn, btn1, btn2, btn3, btn4)
        btn = types.InlineKeyboardButton(text="⬅️Ortga", callback_data=str(pro_item_id))
        ikey.add(btn)
        try:
            bot.delete_message(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id)
            text = ptoduct_item(proi.name_ru, proi.price, proi.desc_ru, lan='ru')
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=proi.img,   caption=text, reply_markup=ikey, parse_mode='HTML')
        except:
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=proi.img,   caption='Maxsulot itemlari', reply_markup=ikey, parse_mode='HTML')

    def item_info_en(self, pro_item_id):
        proi = ProductItem.objects.get(id=pro_item_id)
        ikey = types.InlineKeyboardMarkup(row_width=5)
        number = [[1,2,3,4,5],[6,7,8,9,10],[15,20,25,30,35]]
        for i in number:
            print('ii',i[0])
            btn = types.InlineKeyboardButton(text=f'{i[0]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[0]}')
            btn1 = types.InlineKeyboardButton(text=f'{i[1]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[1]}')
            btn2 = types.InlineKeyboardButton(text=f'{i[2]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[2]}')
            btn3 = types.InlineKeyboardButton(text=f'{i[3]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[3]}')
            btn4 = types.InlineKeyboardButton(text=f'{i[4]} {proi.unit}', callback_data=f'id={pro_item_id}=amount={i[4]}')
            ikey.add(btn, btn1, btn2, btn3, btn4)
        btn = types.InlineKeyboardButton(text="⬅️Ortga", callback_data=str(pro_item_id))
        ikey.add(btn)
        try:
            bot.delete_message(chat_id=self.call_data.message.chat.id, message_id=self.call_data.message.message_id)
            text = ptoduct_item(proi.name_en, proi.price, proi.desc_en, lan='en')
            print(text)
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=proi.img,   caption=text, reply_markup=ikey, parse_mode='HTML')
        except:
            bot.send_photo(chat_id=self.call_data.message.chat.id, photo=proi.img,   caption='Maxsulot itemlari', reply_markup=ikey, parse_mode='HTML')

    def branch(self, lang='uz'):
        branch = Branches.objects.all()
        ikey = types.InlineKeyboardMarkup(row_width=2)
        l = len(branch)
        print(branch, l)
        for i in range(0, l, 2):
            if lang == 'ru':
                btn = types.InlineKeyboardButton(text=branch[i].name_ru, callback_data=f'branch_id_{branch[i].id}')
                if l % 2 == 1 and l-1 == i:
                    ikey.add(btn)
                else:
                    btn1 = types.InlineKeyboardButton(text=branch[i + 1].name_ru, callback_data=f'branch_id_{branch[i+1].id}')
                    ikey.add(btn, btn1)
            elif lang == 'en':
                btn = types.InlineKeyboardButton(text=branch[i].name_ru, callback_data=f'branch_id_{branch[i].id}')
                if l % 2 == 1 and l-1 == i:
                    ikey.add(btn)
                else:
                    btn1 = types.InlineKeyboardButton(text=branch[i + 1].name_ru, callback_data=f'branch_id_{branch[i+1].id}')
                    ikey.add(btn, btn1)
            else:
                btn = types.InlineKeyboardButton(text=branch[i].name_uz, callback_data=f'branch_id_{branch[i].id}')
                if l % 2 == 1 and l-1 == i:
                    ikey.add(btn)
                else:
                    btn1 = types.InlineKeyboardButton(text=branch[i + 1].name_uz, callback_data=f'branch_id_{branch[i+1].id}')
                    ikey.add(btn, btn1)
        bot.send_message(self.userid, '*Bizning filiallarimiz*', reply_markup=ikey, parse_mode='Markdown')






