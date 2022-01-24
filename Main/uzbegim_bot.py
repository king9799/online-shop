from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .buttons import *
from .tokens import *
from .controller import *
from telebot import types
import telebot
from .rate_prayertime import *
import requests
from .text import *
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from .imagestotext import *

bot = TeleBot(tokenlist['uzbegim'], parse_mode="HTML")


@csrf_exempt
def api(request):
    if request.method == 'GET':
        return HttpResponse("<h1>Bot Url</h1>")
    elif request.method == 'POST':
        bot.process_new_updates([
            telebot.types.Update.de_json(
                request.body.decode("utf-8")
            )
        ])
        return HttpResponse(status=200)


@bot.message_handler(commands=["start"])
def start(message):
    print(message)
    all_user = Users.objects.filter(user_id=message.from_user.id, step=6, active=True)
    if len(all_user) == 0:
        text = f'Assalomu alaykum {message.from_user.first_name}.\n\nBizning ' \
               f'xizmatlarimizdan foydalanish uchun avval ro`yhatdan o`ting. '
        bot.send_message(message.from_user.id, text)
        text1 = "Muloqot tilini tanlang\nВыберите язык\nSelect Language"
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        btn = types.KeyboardButton("🇺🇿 O'zbek tili")
        btn1 = types.KeyboardButton("🇷🇺 Русский язык")
        btn2 = types.KeyboardButton("🇬🇧 English")
        btn3 = types.KeyboardButton("🆘 Yordam / Помощь / Help")
        markup.add(btn, btn1, btn2, btn3)
        bot.send_message(message.from_user.id, text1, reply_markup=markup)
        user = Users.objects.filter(user_id=message.from_user.id)
        if len(user) == 0:
            user = Users.objects.create(
                user_id=message.from_user.id,
                step=0
            )
            user.save()
        else:
            user = user.get(user_id=message.from_user.id)
            user.step = 0
            user.save()
    elif all_user.get(user_id=message.from_user.id).language == "🇷🇺 Русский язык":
        markup = base_btn(base_btn_text['ru'])
        bot.send_message(message.from_user.id, "МЕНЮ:", reply_markup=markup)
    elif all_user.get(user_id=message.from_user.id).language == "🇬🇧 English":
        markup = base_btn(base_btn_text['en'])
        bot.send_message(message.from_user.id, "MENU:", reply_markup=markup)
    else:
        markup = base_btn(base_btn_text['uz'])
        bot.send_message(message.from_user.id, "MENYU:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def call_data(call):
    print(call, call.data)
    bot_user = Users.objects.get(user_id=call.from_user.id)
    btn = InlineController(call, call.from_user.id, call_data=call)
    if call.data in ['edit_uz', 'edit_ru', 'edit_en']:
        markup = types.InlineKeyboardMarkup(row_width=2)
        if call.data == "edit_uz":
            edit_btn = types.InlineKeyboardButton('🟢 ️Ism', callback_data='edit_fname')
            edit_btn1 = types.InlineKeyboardButton('🟠 ️Familiya', callback_data='edit_lname')
            edit_btn2 = types.InlineKeyboardButton('📱️Nomer', callback_data='edit_number')
            edit_btn3 = types.InlineKeyboardButton('🏠 Manzil', callback_data='edit_address')
            edit_btn4 = types.InlineKeyboardButton('🇺🇿 Bot tili', callback_data='edit_lang')
            markup.add(edit_btn, edit_btn1, edit_btn2, edit_btn3, edit_btn4)
            bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                  text=f"🔖 Sizning ma`lumotlaringiz:\n---------------------\n🟢 <b>Ism:</b> <i>{bot_user.first_name}</i>\n🟠 <b>Familiya:</b> <i>{bot_user.last_name}</i>\n📱 <b>Telefon nomer:</b> <i>{bot_user.phone_number}</i>\n🏠 <b>Manzil:</b> <i>{bot_user.address}</i>\n🇺🇿 <b>Bot Tili:</b> {bot_user.language}",
                                  reply_markup=markup)
        elif call.data == "edit_ru":
            edit_btn = types.InlineKeyboardButton('🟢 ️Имя', callback_data='edit_fname')
            edit_btn1 = types.InlineKeyboardButton('🟠 ️Фамилия', callback_data='edit_lname')
            edit_btn2 = types.InlineKeyboardButton('📱️Телефонный номер', callback_data='edit_number')
            edit_btn3 = types.InlineKeyboardButton('🏠 Адрес', callback_data='edit_address')
            edit_btn4 = types.InlineKeyboardButton('🇷🇺 Бoт Язык', callback_data='edit_lang')
            markup.add(edit_btn, edit_btn1, edit_btn2, edit_btn3, edit_btn4)
            bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                  text=f"🔖 <b>Ваша информация:</b>\n---------------------\n🟢 <b>Имя:</b> {bot_user.first_name}\n🟠 <b>Фамилия:</b> {bot_user.last_name}\n📱 <b>Телефонный номер:</b> {bot_user.phone_number}\n🏠 <b>Адрес:</b> {bot_user.address}\n🇷🇺 <b>Бoт Язык:</b> {bot_user.language}",
                                  reply_markup=markup)
        elif call.data == "edit_en":
            edit_btn = types.InlineKeyboardButton('🟢 First Name', callback_data='edit_fname')
            edit_btn1 = types.InlineKeyboardButton('🟠 Last Name', callback_data='edit_lname')
            edit_btn2 = types.InlineKeyboardButton('📱️Phone number', callback_data='edit_number')
            edit_btn3 = types.InlineKeyboardButton('🏠 Address', callback_data='edit_address')
            edit_btn4 = types.InlineKeyboardButton('🇺🇸 Bot Language', callback_data='edit_lang')
            markup.add(edit_btn, edit_btn1, edit_btn2, edit_btn3, edit_btn4)
            bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                  text=f"🔖 <b>Your information:</b>\n---------------------\n🟢 <b>Name:</b> {bot_user.first_name}\n🟠 <b>Last Name:</b> {bot_user.last_name}\n📱 <b>Phone number:</b> {bot_user.phone_number}\n🏠 <b>Address:</b> {bot_user.address}\n🇺🇸 <b>Bot Language:</b> {bot_user.language}",
                                  reply_markup=markup)
    elif call.data in ['busan', 'daegu', 'seoul', 'daejeon', 'changwon', 'gwangju', 'suwon', 'ulsan', 'jeonju-si',
                       'gimhae-si']:
        bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=pray_time(call.data))
    elif call.data in ['edit_fname', 'edit_lname', 'edit_number', 'edit_address', 'edit_lang']:
        if call.data == 'edit_fname':
            bot_user.step = 1
            bot_user.save()
            if bot_user.language == "🇺🇿 O'zbek tili":
                bot.send_message(call.from_user.id, "Ismingizni kiriting: ")
            elif bot_user.language == "🇷🇺 Русский язык":
                bot.send_message(call.from_user.id, "Введите ваше имя: ")
            elif bot_user.language == "🇬🇧 English":
                bot.send_message(call.from_user.id, "Enter your name: ")
        elif call.data == 'edit_lname':
            bot_user.step = 2
            bot_user.save()
            if bot_user.language == "🇺🇿 O'zbek tili":
                bot.send_message(call.from_user.id, "Familiyangizni kiriting: ")
            elif bot_user.language == "🇷🇺 Русский язык":
                bot.send_message(call.from_user.id, "Введите вашу фамилию: ")
            elif bot_user.language == "🇬🇧 English":
                bot.send_message(call.from_user.id, "Enter your last name: ")
        elif call.data == 'edit_number':
            bot_user.step = 3
            bot_user.save()
            if bot_user.language == "🇺🇿 O'zbek tili":
                bot.send_message(call.from_user.id, "Telefon nomeringizni kiriting:\nPS:01063639080 ")
            elif bot_user.language == "🇷🇺 Русский язык":
                bot.send_message(call.from_user.id, "Введите свой номер телефона:\nPS:01063639080 ")
            elif bot_user.language == "🇬🇧 English":
                bot.send_message(call.from_user.id, "Enter your phone number:\nPS:01063639080 ")
        elif call.data == 'edit_address':
            bot_user.step = 4
            bot_user.save()
            if bot_user.language == "🇺🇿 O'zbek tili":
                bot.send_message(call.from_user.id, "Manzilingizni bilan kiriting:\nP.S: ")
            elif bot_user.language == "🇷🇺 Русский язык":
                bot.send_message(call.from_user.id, "Введите свое местоположение: ")
            elif bot_user.language == "🇬🇧 English":
                bot.send_message(call.from_user.id, "Enter your location: ")
        elif call.data == 'edit_lang':
            text1 = "Muloqot tilini tanlang\nВыберите язык\nSelect Language"
            markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
            btn = types.KeyboardButton("🇺🇿 O'zbek tili")
            btn1 = types.KeyboardButton("🇷🇺 Русский язык")
            btn2 = types.KeyboardButton("🇬🇧 English")
            markup.add(btn, btn1, btn2)
            bot.send_message(call.from_user.id, text1, reply_markup=markup)
    elif 'category_id' in call.data and bot_user.language in lang_text:
        print(call.data)
        cat_id = str(call.data).split('_')
        if bot_user.language == lang_text[0]:
            btn.products(cat_id[2])
        elif bot_user.language == lang_text[1]:
            btn.products_ru(cat_id[2])
        elif bot_user.language == lang_text[2]:
            btn.products_en(cat_id[2])
    elif 'product_id' in call.data and bot_user.language in lang_text:
        pro_id = str(call.data).split('_')
        if bot_user.language == lang_text[0]:
            btn.product_item(pro_id[2])
        elif bot_user.language == lang_text[1]:
            btn.product_item_ru(pro_id[2])
        elif bot_user.language == lang_text[2]:
            btn.product_item_en(pro_id[2])
    elif 'product_item_id' in call.data and bot_user.language in lang_text:
        print('ff')
        pro_item_id = str(call.data).split('_')
        if bot_user.language == lang_text[0]:
            btn.item_info(pro_item_id[3])
        elif bot_user.language == lang_text[1]:
            btn.item_info_ru(pro_item_id[3])
        elif bot_user.language == lang_text[2]:
            btn.item_info_en(pro_item_id[3])
    elif call.data == "category":
        btn = InlineController(call, call.from_user.id, call_data=call)
        btn.category()
    elif 'id' and 'amount' in call.data:
        da = str(call.data)
        idamo = da.split("=")
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        pro_item = ProductItem.objects.get(id=int(idamo[1]))
        ikey = types.InlineKeyboardMarkup(row_width=1)
        btn = types.InlineKeyboardButton('➕ Qo`shish', callback_data=f'prduct={idamo[1]}=add={idamo[3]}')
        btn1 = types.InlineKeyboardButton(text="⬅️Ortga", callback_data=str(idamo[1]))
        ikey.add(btn, btn1)
        text = f'<b>🧾 Buyurtma tafsilotlari:</b>\n\n🛒 <i>{pro_item.desc_uz} x {idamo[3]} {pro_item.unit} = {int(idamo[3]) * int(pro_item.price)}</i> ₩'
        bot.send_message(call.from_user.id, text, reply_markup=ikey)
    elif 'product' and 'add' in call.data:
        print('ADDDD')
        product_id = str(call.data).split("=")
        product = ProductItem.objects.get(id=product_id[1])
        amount = product_id[3]
        client = Users.objects.get(user_id=call.from_user.id)
        order = Orders.objects.filter(client=client, active=True)
        print(product, amount, client, order)
        n = 0
        while True:
            print("hello")
            if order.exists():
                print('Good')
                order_item = OrderItem.objects.create(
                    order=order.get(),
                    product_item=product,
                    amount=amount,
                    summa=int(amount) * int(product.price)
                )
                order_item.save()
                summa = 0
                order_sums = OrderItem.objects.filter(order=order.get())
                print(order_sums)
                for i in order_sums:
                    summa += int(i.summa)
                order = order.get()
                order.summa = summa
                order.l_order_item = len(order_sums)
                order.save()
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='✔️<b>Mahsulot savatchaga qo`shildi:</b>')
                text = f'❇️(<i>{product.name_uz} x {amount} {product.unit}</i>)'
                bot.send_message(call.from_user.id, text)
                break
            else:
                order_n = f'A{n}'
                print(n)
                print(Orders.objects.filter(order_n=order_n).exists())
                if Orders.objects.filter(order_n=order_n).exists():
                    n += 1
                else:
                    Orders.objects.create(
                        order_n=order_n,
                        client=client,
                    ).save()
    elif 'delete' in call.data:
        data = str(call.data).split('_')
        or_it = OrderItem.objects.get(id=data[1])
        print(or_it.order.l_order_item)
        or_it.order.l_order_item -= 1
        or_it.order.summa -= or_it.summa
        or_it.order.save()
        or_it.delete()
        orders = OrderItem.objects.filter(order__client=bot_user, order__active=True)
        if orders.exists():
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Buyurtma berish 🟢', callback_data=f'getorder_{orders.last().order.id}')
            markup.add(btn)
            text = '🛒 <b>Sizning savatchangiz:</b>\n\n'
            n = 1
            for i in orders:
                btn = types.InlineKeyboardButton(f'{i.product_item.name_uz} | {i.amount} {i.product_item.unit} ❌',
                                                 callback_data=f'delete_{i.id}')
                markup.add(btn)
                text += f'<b>{n}:</b> {i.product_item.name_uz} | <i>{i.amount} {i.product_item.unit} x {i.product_item.price} ₩ = {int(i.amount) * int(i.product_item.price)}</i> ₩\n'
                n += 1
            order = Orders.objects.get(client=bot_user, active=True)
            delivery = Extra.objects.get(name="Delivery").quantity
            bonus = Extra.objects.get(name="bonus").quantity
            text += f'\n🚚 <b>Pochta narxi:</b> <i>{delivery}</i> ₩ \n📦 <b>Jami mahsulot:</b> <i>{order.l_order_item}|{order.summa}</i> ₩\n💸 <b>Bonus:</b> <i>{order.summa / 100 * bonus}</i> ₩\n💳 <b>Jami:</b> <i>{order.summa + delivery - (order.summa / 100 * bonus)}</i> ₩'
            bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=text,
                                  reply_markup=markup)
        else:
            bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                  text="Savatchamizda Mahsulotlar yuq")
    elif 'getorder' in call.data:
        data = str(call.data).split('_')
        order = Orders.objects.get(id=data[1])
        order.active = False
        order.save()
        or_it = OrderItem.objects.filter(order__id=order.id)
        send_text = send_order(or_it)
        bot.send_message(-1001559083213, send_text)
        if bot_user.language == lang_text[1]:
            text = order_text(or_it, lan='ru')
            bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=text['text'])
            bot.send_message(call.from_user.id, text['text1'])
        elif bot_user.language == lang_text[2]:
            text = order_text(or_it, lan='en')
            bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=text['text'])
            bot.send_message(call.from_user.id, text['text1'])
        else:
            text = order_text(or_it)
            bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=text['text'])
            bot.send_message(call.from_user.id, text['text1'])
    elif call.data == 'history':
        or_it = OrderItem.objects.filter(order__client=bot_user, order__active=False)
        or_id = Orders.objects.filter(client=bot_user, active=False)
        if bot_user.language == lang_text[1]:
            text = my_order(or_it,or_id, last=False, lang='ru')
            print(text)
            bot.edit_message_text(chat_id=call.from_user.id, text=text, message_id=call.message.message_id)
        elif bot_user.language == lang_text[2]:
            text = my_order(or_it, or_id, last=False, lang='en')
            bot.edit_message_text(chat_id=call.from_user.id, text=text, message_id=call.message.message_id)
        else:
            text = my_order(or_it, or_id, last=False)
            bot.edit_message_text(chat_id=call.from_user.id, text=text, message_id=call.message.message_id)
    elif ProductItem.objects.filter(id=call.data).exists():
        proitem = ProductItem.objects.get(id=call.data).product_name.category.id
        print("sss", proitem)
        btn = InlineController(call, call.from_user.id, call_data=call)
        btn.products(proitem)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message.text)
    bot_user = Users.objects.get(user_id=message.from_user.id)
    if message.text in ["⬅️Ortga", "⬅️Назад", "⬅️Back"]:
        bot_user.step -= 1
        bot_user.save()
        if bot_user.step in [1, 2, 3, 4] and bot_user.language == "🇺🇿 O'zbek tili":
            if bot_user.step == 1:
                markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                b = types.KeyboardButton(f"{message.from_user.first_name}")
                markup.add(b)
                bot.send_message(message.from_user.id, register_text[bot_user.step]['uz'], reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                b = types.KeyboardButton("⬅️Ortga")
                markup.add(b)
                bot.send_message(message.from_user.id, register_text[bot_user.step]['uz'], reply_markup=markup)
        elif bot_user.step in [1, 2, 3, 4] and bot_user.language == "🇷🇺 Русский язык":
            if bot_user.step == 1:
                markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                b = types.KeyboardButton(f"{message.from_user.first_name}")
                markup.add(b)
                bot.send_message(message.from_user.id, register_text[bot_user.step]['ru'], reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                b = types.KeyboardButton("⬅️Назад")
                markup.add(b)
                bot.send_message(message.from_user.id, register_text[bot_user.step]['ru'], reply_markup=markup)
        elif bot_user.step in [1, 2, 3, 4] and bot_user.language == "🇬🇧 English":
            if bot_user.step == 1:
                markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                b = types.KeyboardButton(f"{message.chat.first_name}")
                markup.add(b)
                bot.send_message(message.from_user.id, register_text[bot_user.step]['en'], reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                b = types.KeyboardButton("⬅️Back")
                markup.add(b)
                bot.send_message(message.from_user.id, register_text[bot_user.step]['en'], reply_markup=markup)
    elif message.text in ["🇺🇿 O'zbek tili", "🇷🇺 Русский язык", "🇬🇧 English"]:
        print('djhhgdjh')
        if message.text == "🇺🇿 O'zbek tili":
            if bot_user.active == True:
                # markup = types.InlineKeyboardMarkup(row_width=1)
                bot_user.language = message.text
                bot_user.save()
                lang(message, bot_user)
            else:
                bot.send_message(message.from_user.id, "Botdan foydalanish uchun avval ro`yhatdan o`ting.")
                bot_user.language = message.text
                bot_user.step = 1
                bot_user.save()
                markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                b = types.KeyboardButton(f"{message.from_user.first_name}")
                markup.add(b)
                bot.send_message(message.from_user.id, "Ismingizni kiriting: ", reply_markup=markup)
        elif message.text == "🇷🇺 Русский язык":
            if bot_user.active == True:
                # markup = types.InlineKeyboardMarkup(row_width=1)
                bot_user.language = message.text
                bot_user.save()
                lang(message, bot_user)

            else:
                bot.send_message(message.from_user.id, "Чтобы подписаться на бота, сначала зарегистрируйтесь")
                bot_user.language = message.text
                bot_user.step = 1
                bot_user.save()
                markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                b = types.KeyboardButton(f"{message.from_user.first_name}")
                markup.add(b)
                bot.send_message(message.from_user.id, "Введите ваше имя: ", reply_markup=markup)
        elif message.text == "🇬🇧 English":
            if bot_user.active == True:
                # markup = types.InlineKeyboardMarkup(row_width=1)
                bot_user.language = message.text
                bot_user.save()
                lang(message, bot_user)
            else:
                bot.send_message(message.from_user.id, "Sign up for using the bot")
                bot_user = Users.objects.get(user_id=message.from_user.id)
                bot_user.language = message.text
                bot_user.step = 1
                bot_user.save()
                markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                b = types.KeyboardButton(f"{message.from_user.first_name}")
                markup.add(b)
                bot.send_message(message.from_user.id, "Enter your name: ", reply_markup=markup)
                print(bot_user.language)
    elif bot_user.step == 1 and bot_user.language in ["🇺🇿 O'zbek tili", "🇷🇺 Русский язык", "🇬🇧 English"]:
        bot_user.first_name = message.text
        bot_user.step += 1
        bot_user.save()
        if bot_user.active == True:
            markup = types.InlineKeyboardMarkup(row_width=1)
            bot_user.step = 6
            bot_user.save()
            if bot_user.language == "🇺🇿 O'zbek tili":
                bot.send_message(message.from_user.id, "Sizning ma'lumotlaringiz muvaffaqiyatli o'zgartirildi.")
                edit_btn = types.InlineKeyboardButton('✏️Tahrirlash', callback_data='edit_uz')
                markup.add(edit_btn)
                bot.send_message(message.from_user.id,
                                 f"🔖 <b>Sizning ma`lumotlaringiz:</b\n---------------------\n🟢 <b>Ism</b>: <i>{bot_user.first_name}</i>\n🟠 <b>Familiya:</b> <i>{bot_user.last_name}</i>\n📱 <b>Telefon nomer:</b> <i>{bot_user.phone_number}</i>\n🏠 <b>Manzil:</b> <i>{bot_user.address}</i>\n🇺🇿 <b>Bot tili:</b> {bot_user.language}",
                                 reply_markup=markup)
            elif bot_user.language == "🇷🇺 Русский язык":
                bot.send_message(message.from_user.id, "Ваша информация была успешно изменена.")
                edit_btn = types.InlineKeyboardButton('✏️Редактировать', callback_data='edit_ru')
                markup.add(edit_btn)
                bot.send_message(message.from_user.id,
                                 f"🔖 <b>Ваша информация:</b>\n---------------------\n🟢 <b>Имя:</b> {bot_user.first_name}\n🟠 <b>Фамилия:</b> {bot_user.last_name}\n📱 <b>Телефонный номер:</b> {bot_user.phone_number}\n🏠 <b>Адрес:</b> {bot_user.address}\n🇷🇺 <b>Бoт Язык:</b> {bot_user.language}",
                                 reply_markup=markup)
            elif bot_user.language == "🇬🇧 English":
                bot.send_message(message.from_user.id, "Your information has been successfully modified.")
                edit_btn = types.InlineKeyboardButton('✏️Edit', callback_data='edit_en')
                markup.add(edit_btn)
                bot.send_message(message.from_user.id,
                                 f"🔖 <b>Your information:</b>\n---------------------\n🟢 <b>Name:</b> <i>{bot_user.first_name}</i>\n🟠 <b>Last name:</b> <i>{bot_user.last_name}</i>\n📱 <b>Phone number:</b> <i>{bot_user.phone_number}</i>\n🏠 <b>Address:</b> <i>{bot_user.address}</i>\n🇺🇸 <b>Bot Language:</b> {bot_user.language}",
                                 reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            if bot_user.language == "🇺🇿 O'zbek tili":
                b = types.KeyboardButton("⬅️Ortga")
                markup.add(b)
                bot.send_message(message.from_user.id, "Familiyangizni kiriting: ", reply_markup=markup)
            elif bot_user.language == "🇷🇺 Русский язык":
                b = types.KeyboardButton("⬅️Назад")
                markup.add(b)
                bot.send_message(message.from_user.id, "Введите вашу фамилию: ", reply_markup=markup)
            elif bot_user.language == "🇬🇧 English":
                b = types.KeyboardButton("⬅️Back")
                markup.add(b)
                bot.send_message(message.from_user.id, "Enter your last name: ", reply_markup=markup)
    elif bot_user.step == 2 and bot_user.language in ["🇺🇿 O'zbek tili", "🇷🇺 Русский язык", "🇬🇧 English"]:
        bot_user.last_name = message.text
        bot_user.step += 1
        bot_user.save()
        if bot_user.active == True:
            markup = types.InlineKeyboardMarkup(row_width=1)
            bot_user.step = 6
            bot_user.save()
            if bot_user.language == "🇺🇿 O'zbek tili":
                bot.send_message(message.from_user.id, "Sizning ma'lumotlaringiz muvaffaqiyatli o'zgartirildi.")
                edit_btn = types.InlineKeyboardButton('✏️Tahrirlash', callback_data='edit_uz')
                markup.add(edit_btn)
                bot.send_message(message.from_user.id,
                                 f"🔖 <b>Sizning ma`lumotlaringiz:</b>\n---------------------\n🟢 <b>Ism:</b> <i>{bot_user.first_name}</i>\n🟠 <b>Familiya:</b> <i>{bot_user.last_name}</i>\n📱 <b>Telefon nomer:</b> <i>{bot_user.phone_number}</i>\n🏠 <b>Manzil:</b> <i>{bot_user.address}</i>\n🇺🇿 <b>Bot tili:</b> {bot_user.language}",
                                 reply_markup=markup)
            elif bot_user.language == "🇷🇺 Русский язык":
                bot.send_message(message.from_user.id, "Ваша информация была успешно изменена.")
                edit_btn = types.InlineKeyboardButton('✏️Редактировать', callback_data='edit_ru')
                markup.add(edit_btn)
                bot.send_message(message.from_user.id,
                                 f"🔖 <b>Ваша информация:</b>\n---------------------\n🟢 <b>Имя:</b> {bot_user.first_name}\n🟠 <b>Фамилия:</b> {bot_user.last_name}\n📱 <b>Телефонный номер:</b> {bot_user.phone_number}\n🏠 <b>Адрес:</b> {bot_user.address}\n🇷🇺 <b>Бoт Язык:</b> {bot_user.language}",
                                 reply_markup=markup)
            elif bot_user.language == "🇬🇧 English":
                bot.send_message(message.from_user.id, "Your information has been successfully modified.")
                edit_btn = types.InlineKeyboardButton('✏️Edit', callback_data='edit_en')
                markup.add(edit_btn)
                bot.send_message(message.from_user.id,
                                 f"🔖 <b>Your information:</b>\n---------------------\n🟢 <b>Name:</b> {bot_user.first_name}\n🟠 <b>Last Name:</b> {bot_user.last_name}\n📱 <b>Phone number:</b> {bot_user.phone_number}\n🏠 <b>Address:</b> {bot_user.address}\n🇺🇸 <b>Bot Language:</b> {bot_user.language}",
                                 reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            if bot_user.language == "🇺🇿 O'zbek tili":
                b = types.KeyboardButton("⬅️Ortga")
                markup.add(b)
                bot.send_message(message.from_user.id, "Telefon nomeringizni kiriting: ", reply_markup=markup)
            elif bot_user.language == "🇷🇺 Русский язык":
                b = types.KeyboardButton("⬅️Назад")
                markup.add(b)
                bot.send_message(message.from_user.id, "Введите свой номер телефона: ", reply_markup=markup)
            elif bot_user.language == "🇬🇧 English":
                b = types.KeyboardButton("⬅️Back")
                markup.add(b)
                bot.send_message(message.from_user.id, "Enter your phone number: ", reply_markup=markup)
    elif bot_user.step == 3 and bot_user.language in lang_text:
        if str(message.text).isdigit():
            bot_user.phone_number = message.text
            bot_user.step += 1
            bot_user.save()
            if bot_user.active == True:
                markup = types.InlineKeyboardMarkup(row_width=1)
                bot_user.step = 6
                bot_user.save()
                if bot_user.language == "🇺🇿 O'zbek tili":
                    bot.send_message(message.from_user.id, "Sizning ma'lumotlaringiz muvaffaqiyatli o'zgartirildi.")
                    edit_btn = types.InlineKeyboardButton('✏️Tahrirlash', callback_data='edit_uz')
                    markup.add(edit_btn)
                    bot.send_message(message.from_user.id,
                                     f"🔖 <b>Sizning ma`lumotlaringiz:</b>\n---------------------\n🟢 <b>Ism:</b> <i>{bot_user.first_name}</i>\n🟠 <b>Familiya:</b> <i>{bot_user.last_name}</i>\n📱 <b>Telefon nomer:</b> <i>{bot_user.phone_number}</i>\n🏠 <b>Manzil:</b> <i>{bot_user.address}</i>\n🇺🇿 <b>Bot tili:</b> {bot_user.language}",
                                     reply_markup=markup)
                elif bot_user.language == "🇷🇺 Русский язык":
                    bot.send_message(message.from_user.id, "Ваша информация была успешно изменена.")
                    edit_btn = types.InlineKeyboardButton('✏️Редактировать', callback_data='edit_ru')
                    markup.add(edit_btn)
                    bot.send_message(message.from_user.id,
                                     f"🔖 <b>Ваша информация:</b>\n---------------------\n🟢 <b>Имя:</b> {bot_user.first_name}\n🟠 <b>Фамилия:</b> {bot_user.last_name}\n📱 <b>Телефонный номер:</b> {bot_user.phone_number}\n🏠 <b>Адрес:</b> {bot_user.address}\n🇷🇺 <b>Бoт Язык:</b> {bot_user.language}",
                                     reply_markup=markup)
                elif bot_user.language == "🇬🇧 English":
                    bot.send_message(message.from_user.id, "Your information has been successfully modified.")
                    edit_btn = types.InlineKeyboardButton('✏️Edit', callback_data='edit_en')
                    markup.add(edit_btn)
                    bot.send_message(message.from_user.id,
                                     f"🔖 <b>Your information:</b>\n---------------------\n🟢 <b>Name:</b> {bot_user.first_name}\n🟠 <b>Last Name:</b> {bot_user.last_name}\n📱 <b>Phone number:</b> {bot_user.phone_number}\n🏠 <b>Address:</b> {bot_user.address}\n🇺🇸 <b>Bot Language:</b> {bot_user.language}",
                                     reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                if bot_user.language == "🇺🇿 O'zbek tili":
                    b = types.KeyboardButton("⬅️Ortga")
                    markup.add(b)
                    bot.send_message(message.from_user.id, "Manzilingizni kiriting: ", reply_markup=markup)
                elif bot_user.language == "🇷🇺 Русский язык":
                    b = types.KeyboardButton("⬅️Назад")
                    markup.add(b)
                    bot.send_message(message.from_user.id, "Введите свое местоположение: ", reply_markup=markup)
                elif bot_user.language == "🇬🇧 English":
                    b = types.KeyboardButton("⬅️Back")
                    markup.add(b)
                    bot.send_message(message.from_user.id, "Enter your location: ", reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            if bot_user.language == "🇺🇿 O'zbek tili":
                b = types.KeyboardButton("⬅️Ortga")
                markup.add(b)
                bot.send_message(message.from_user.id, "Telefon nomeringizni kiriting: ", reply_markup=markup)
            elif bot_user.language == "🇷🇺 Русский язык":
                b = types.KeyboardButton("⬅️Назад")
                markup.add(b)
                bot.send_message(message.from_user.id, "Введите свой номер телефона: ", reply_markup=markup)
            elif bot_user.language == "🇬🇧 English":
                b = types.KeyboardButton("⬅️Back")
                markup.add(b)
                bot.send_message(message.from_user.id, "Enter your phone number: ", reply_markup=markup)
    elif bot_user.step == 4 and bot_user.language in ["🇺🇿 O'zbek tili", "🇷🇺 Русский язык", "🇬🇧 English"]:
        print(message.from_user.id, ':', message)
        bot_user.address = message.text
        bot_user.step += 1
        bot_user.save()
        if bot_user.active == True:
            markup = types.InlineKeyboardMarkup(row_width=1)
            bot_user.step = 6
            bot_user.save()
            if bot_user.language == "🇺🇿 O'zbek tili":
                bot.send_message(message.from_user.id, "Sizning ma'lumotlaringiz muvaffaqiyatli o'zgartirildi.")
                edit_btn = types.InlineKeyboardButton('✏️Tahrirlash', callback_data='edit_uz')
                markup.add(edit_btn)
                bot.send_message(message.from_user.id,
                                 f"🔖 <b>Sizning ma`lumotlaringiz:</b>\n---------------------\n🟢 <b>Ism:</b> <i>{bot_user.first_name}</i>\n🟠 <b>Familiya:</b> <i>{bot_user.last_name}</i>\n📱 <b>Telefon nomer:</b> <i>{bot_user.phone_number}</i>\n🏠 <b>Manzil:</b> <i>{bot_user.address}</i>\n🇺🇿 <b>Bot tili:</b> {bot_user.language}",
                                 reply_markup=markup)
            elif bot_user.language == "🇷🇺 Русский язык":
                bot.send_message(message.from_user.id, "Ваша информация была успешно изменена.")
                edit_btn = types.InlineKeyboardButton('✏️Редактировать', callback_data='edit_ru')
                markup.add(edit_btn)
                bot.send_message(message.from_user.id,
                                 f"🔖 <b>Ваша информация:</b>\n---------------------\n🟢 <b>Имя:</b> {bot_user.first_name}\n🟠 <b>Фамилия:</b> {bot_user.last_name}\n📱 <b>Телефонный номер:</b> {bot_user.phone_number}\n🏠 <b>Адрес:</b> {bot_user.address}\n🇷🇺 <b>Бoт Язык:</b> {bot_user.language}",
                                 reply_markup=markup)
            elif bot_user.language == "🇬🇧 English":
                bot.send_message(message.from_user.id, "Your information has been successfully modified.")
                edit_btn = types.InlineKeyboardButton('✏️Edit', callback_data='edit_en')
                markup.add(edit_btn)
                bot.send_message(message.from_user.id,
                                 f"🔖 <b>Your information:</b>\n---------------------\n🟢 <b>Name:</b> {bot_user.first_name}\n🟠 <b>Last Name:</b> {bot_user.last_name}\n📱 <b>Phone number:</b> {bot_user.phone_number}\n🏠 <b>Address:</b> {bot_user.address}\n🇺🇸 <b>Bot Language:</b> {bot_user.language}",
                                 reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            if bot_user.language == "🇺🇿 O'zbek tili":
                yes = types.KeyboardButton('✅ Ok')
                no = types.KeyboardButton('🚫 ️Bekor qilish')
                back = types.KeyboardButton("⬅️Ortga")
                markup.add(yes, no, back)
                text = f"<b>Sizning barcha ma`lumotlaringiz to`gri ko`rsatilganmi?:</b>\n---------------------\n🟢 <b>Ism:</b> <i>{bot_user.first_name}</i>\n🟠 <b>Familiya:</b> <i>{bot_user.last_name}</i>\n📱 <b>Telefon nomer:</b> <i>{bot_user.phone_number}</i>\n🏠 <b>Manzil:</b> <i>{bot_user.address}</i>\n🇺🇿 <b>Bot tili:</b> <i>{bot_user.language}</i>"
                print(text)
                bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=markup)
            elif bot_user.language == "🇷🇺 Русский язык":
                yes = types.KeyboardButton('✅ Ok')
                no = types.KeyboardButton('🚫 ️Отменить')
                back = types.KeyboardButton("⬅️Назад")
                markup.add(yes, no, back)
                bot.send_message(message.from_user.id,
                                 f"<b>Правильно ли отображается вся ваша информация?:</b>\n---------------------\n🟢 <b>Имя:<b> <i>{bot_user.first_name}</i>\n🟠 <b>Фамилия:</b> <i>{bot_user.last_name}</i>\n📱 <b>Телефонный номер:</b> <i>{bot_user.phone_number}</i>\n🏠 <b>Адрес:</b> <i>{bot_user.address}</i>\n🇷🇺 </b>Бoт Язык:</b> <i>{bot_user.language}</i>",
                                 reply_markup=markup)
            elif bot_user.language == "🇬🇧 English":
                yes = types.KeyboardButton('✅ Ok')
                no = types.KeyboardButton('🚫 ️Cancel')
                back = types.KeyboardButton("⬅️Back")
                markup.add(yes, no, back)
                bot.send_message(message.from_user.id,
                                 f"<b>Is all your information displayed correctly?:</b>\n---------------------\n🟢 <b>Name:</b> <i>{bot_user.first_name}</i>\n🟠 <b>Last Name:</b> <i>{bot_user.last_name}</i>\n📱 <b>Phone number:</b> <i>{bot_user.phone_number}</i>\n🏠 <b>Address:</b> <i>{bot_user.address}</i>\n🇺🇸 <b>Bot Language:</b> <i>{bot_user.language}</i>",
                                 reply_markup=markup, )
    elif bot_user.step == 5 and message.text == '✅ Ok':
        bot_user.step += 1
        bot_user.active = True
        bot_user.save()
        if bot_user.language == "🇷🇺 Русский язык":
            bot.send_message(message.from_user.id, "Регистрация прошла успешно. ")
            markup = base_btn(base_btn_text['ru'])
            bot.send_message(message.from_user.id, "МЕНЮ:", reply_markup=markup)
        elif bot_user.language == "🇬🇧 English":
            bot.send_message(message.from_user.id, "The registration was completed successfully. ")
            markup = base_btn(base_btn_text['en'])
            bot.send_message(message.from_user.id, "MENU:", reply_markup=markup)
        else:
            bot.send_message(message.from_user.id, "Ro`yhatdan o`tish mufavaqqiyatli yakunlandi. ")
            markup = base_btn(base_btn_text['uz'])
            bot.send_message(message.from_user.id, "MENYU:", reply_markup=markup)
    elif bot_user.step == 5 and message.text in ['🚫 ️Cancel', '🚫 ️Отменить', '🚫 ️Bekor qilish']:
        print('dd')
        bot_user.delete()
        text = f'Assalomu alaykum {message.from_user.first_name}.\nBizning ' \
               f'xizmatlarimizdan foydalanish uchun avval ro`yhatdan o`ting. '
        bot.send_message(message.from_user.id, text)
        text1 = "Muloqot tilini tanlang\nВыберите язык\nSelect Language"
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        btn = types.KeyboardButton("🇺🇿 O'zbek tili")
        btn1 = types.KeyboardButton("🇷🇺 Русский язык")
        btn2 = types.KeyboardButton("🇬🇧 English")
        btn3 = types.KeyboardButton("🆘 Yordam / Помощь / Help")
        markup.add(btn, btn1, btn2, btn3)
        bot.send_message(message.from_user.id, text1, reply_markup=markup)
        user = Users.objects.create(
            user_id=message.from_user.id,
            step=0
        )
        user.save()
    elif message.text in ["👤 Profil", "👤 Profile", "👤 Профиль"] and bot_user.step == 6:
        markup = types.InlineKeyboardMarkup(row_width=1)
        if bot_user.language == "🇺🇿 O'zbek tili":
            edit_btn = types.InlineKeyboardButton('✏️Tahrirlash', callback_data='edit_uz')
            markup.add(edit_btn)
            bot.send_message(message.from_user.id,
                             f"🔖 <b>Sizning ma`lumotlaringiz:</b>\n---------------------\n🟢 <b>Ism:</b> <i>{bot_user.first_name}</i>\n🟠 <b>Familiya:</b> <i>{bot_user.last_name}</i>\n📱 <b>Telefon nomer:</b> <i>{bot_user.phone_number}</i>\n🏠 <b>Manzil:</b> <i>{bot_user.address}</i>\n🇺🇿 <b>Bot tili:</b> {bot_user.language}",
                             reply_markup=markup)
        elif bot_user.language == "🇷🇺 Русский язык":
            edit_btn = types.InlineKeyboardButton('✏️Редактировать', callback_data='edit_ru')
            markup.add(edit_btn)
            bot.send_message(message.from_user.id,
                             f"🔖 <b>Ваша информация:</b>\n---------------------\n🟢 <b>Имя:</b> {bot_user.first_name}\n🟠 <b>Фамилия:</b> {bot_user.last_name}\n📱 <b>Телефонный номер:</b> {bot_user.phone_number}\n🏠 <b>Адрес:</b> {bot_user.address}\n🇷🇺 <b>Бoт Язык:</b> {bot_user.language}",
                             reply_markup=markup)
        elif bot_user.language == "🇬🇧 English":
            edit_btn = types.InlineKeyboardButton('✏️Edit', callback_data='edit_en')
            markup.add(edit_btn)
            bot.send_message(message.from_user.id,
                             f"🔖 <b>Your information:</b>\n---------------------\n🟢 <b>Name:</b> {bot_user.first_name}\n🟠 <b>Last Name:</b> {bot_user.last_name}\n📱 <b>Phone number:</b> {bot_user.phone_number}\n🏠 <b>Address:</b> {bot_user.address}\n🇺🇸 <b>Bot Language:</b> {bot_user.language}",
                             reply_markup=markup)
    elif message.text in ["📑 Maxsulotlar", "📑 Products", "📑 Продукты"] and bot_user.step == 6:
        if bot_user.language == "🇺🇿 O'zbek tili":
            InlineController(m=message, userid=message.from_user.id).category()
        elif bot_user.language == "🇷🇺 Русский язык":
            InlineController(m=message, userid=message.from_user.id).category_ru()
        elif bot_user.language == "🇬🇧 English":
            InlineController(m=message, userid=message.from_user.id).category_en()
    elif message.text in ["🆘 Yordam", "🆘 Help", "🆘 Помощь"] or message.text == "🆘 Yordam / Помощь / Help" :
        if bot_user.language == "🇺🇿 O'zbek tili":
            bot.send_message(message.from_user.id,
                             "UZBEGIM halol go`sht mahsulotlari do`koni\nUshbu bot orqali siz halol go`sht va Uzbegim do`konidagi barcha "
                             "maxsulotlarga buyurtma berishingiz mumkin. \n\n "
                             "\n ☎️Qo’shimcha ma’lumotlar uchun: 010-6363-9080")
        elif bot_user.language == "🇷🇺 Русский язык":
            bot.send_message(message.from_user.id,
                             "UZBEGIM halol go`sht mahsulotlari do`koni\nUshbu bot orqali siz halol go`sht va Uzbegim do`konidagi barcha "
                             "maxsulotlarga buyurtma berishingiz mumkin. \n\n "
                             "\n ☎️Qo’shimcha ma’lumotlar uchun: 010-6363-9080")
        elif bot_user.language == "🇬🇧 English":
            bot.send_message(message.from_user.id,
                             "UZBEGIM halol go`sht mahsulotlari do`koni\nUshbu bot orqali siz halol go`sht va Uzbegim do`konidagi barcha "
                             "maxsulotlarga buyurtma berishingiz mumkin. \n\n "
                             "\n ☎️Qo’shimcha ma’lumotlar uchun: 010-6363-9080")
        else:
            bot.send_message(message.from_user.id,
                         "UZBEGIM halol go`sht mahsulotlari do`koni\nUshbu bot orqali siz halol go`sht va Uzbegim do`konidagi barcha "
                         "maxsulotlarga buyurtma berishingiz mumkin. \n\n "
                         "\n ☎️Qo’shimcha ma’lumotlar uchun: 010-6363-9080")
    elif message.text in ["⌛️Namoz vaqtlari", "⌛️Prayer times", "⌛️Время намаза"] and bot_user.step == 6:
        markup = types.InlineKeyboardMarkup(row_width=2)
        b = types.InlineKeyboardButton('Busan', callback_data='busan')
        b1 = types.InlineKeyboardButton('Daegu', callback_data='daegu')
        b2 = types.InlineKeyboardButton('Seoul', callback_data='seoul')
        b3 = types.InlineKeyboardButton('Daejeon', callback_data='daejeon')
        b4 = types.InlineKeyboardButton('Changwon', callback_data='changwon')
        b5 = types.InlineKeyboardButton('Gwangju', callback_data='gwangju')
        b6 = types.InlineKeyboardButton('Suwon', callback_data='suwon')
        b7 = types.InlineKeyboardButton('Ulsan', callback_data='ulsan')
        b8 = types.InlineKeyboardButton('Jeonju', callback_data='jeonju-si')
        b9 = types.InlineKeyboardButton('Gimhae', callback_data='gimhae-si')
        markup.add(b, b1, b2, b3, b4, b5, b6, b7, b8, b9)
        if bot_user.language == "🇺🇿 O'zbek tili":
            bot.send_message(message.from_user.id, "Namoz vaqtlarini bilish uchun hududingizni tanlang:",
                             reply_markup=markup)
        elif bot_user.language == "🇷🇺 Русский язык":
            bot.send_message(message.from_user.id, "Выберите свой регион, чтобы узнать время намаза:",
                             reply_markup=markup)
        elif bot_user.language == "🇬🇧 English":
            bot.send_message(message.from_user.id, "Select your region to know the prayer times:",
                             reply_markup=markup)
    elif message.text in ["💵 Valyuta kursi", "💵 Currency rate", "💵 Курс валюты"] and bot_user.step == 6:
        r = requests.get('https://cbu.uz/oz/arkhiv-kursov-valyut/json/')
        a = r.json()[0]['Date']
        if bot_user.language == "🇺🇿 O'zbek tili":
            bot.send_message(message.from_user.id,
                             f"O`zbekiston Markaziy Bank ma`lumotlariga ko`ra:\n\n🇺🇿 {rates()[6]}\n🇰🇷 {rates()[4]}\n🇷🇺 {rates()[0]}\n🇰🇬 {rates()[3]}\n🇮🇩 {rates()[1]}\n🇰🇿 {rates()[5]}\n🇮🇳 {rates()[2]}\n\n Sana: {a}")
        elif bot_user.language == "🇷🇺 Русский язык":
            bot.send_message(message.from_user.id,
                             f"По данным Центрального банка Узбекистана:\n\n🇺🇿 {rates()[6]}\n🇰🇷 {rates()[4]}\n🇷🇺 {rates()[0]}\n🇰🇬 {rates()[3]}\n🇮🇩 {rates()[1]}\n🇰🇿 {rates()[5]}\n🇮🇳 {rates()[2]}\n\n Дата: {a}")
        elif bot_user.language == "🇬🇧 English":
            bot.send_message(message.from_user.id,
                             f"According to the Central Bank of Uzbekistan:\n\n🇺🇿 {rates()[6]}\n🇰🇷 {rates()[4]}\n🇷🇺 {rates()[0]}\n🇰🇬 {rates()[3]}\n🇮🇩 {rates()[1]}\n🇰🇿 {rates()[5]}\n🇮🇳 {rates()[2]}\n\n Date: {a}")
    elif message.text in ["🛒 Savatcha", "🛒 Box", "🛒 Карзинка"] and bot_user.step == 6:
        orders = OrderItem.objects.filter(order__client=bot_user, order__active=True)
        if orders.exists():
            markup = types.InlineKeyboardMarkup(row_width=1)
            if bot_user.language == lang_text[1]:  # ru version
                btn = types.InlineKeyboardButton('Заказ 🟢', callback_data=f'getorder_{orders.last().order.id}')
                markup.add(btn)
                text = '🛒 <b>Ваша корзина:</b>\n\n'
                n = 1
                for i in orders:
                    btn = types.InlineKeyboardButton(f'{i.product_item.name_ru} | {i.amount} {i.product_item.unit} ❌',
                                                     callback_data=f'delete_{i.id}')
                    markup.add(btn)
                    text += f'<b>{n}:</b> {i.product_item.name_ru} | <i>{i.amount} {i.product_item.unit} x {i.product_item.price} ₩ = {round(int(i.amount) * int(i.product_item.price), -2)}</i> ₩\n'
                    n += 1
                order = Orders.objects.get(client=bot_user, active=True)
                delivery = Extra.objects.get(name="Delivery").quantity
                bonus = Extra.objects.get(name="bonus").quantity
                text += f'\n-------------------\n📦 <b>Общий продукт:</b> <i>{round(order.summa, -2)}</i> ₩\n💸 <b>Возврат наличных:</b> <i>{round(order.summa / 100 * bonus, -2)}</i> ₩\n-------------------\n🚚 <b>Стоимость доставки:</b> <i>{delivery}</i> ₩ \n-------------------\n💳 <b>Общая сумма:</b> <i>{round(order.summa + delivery - (order.summa / 100 * bonus), -2)}</i> ₩'
                bot.send_message(message.from_user.id, text, reply_markup=markup)
            elif bot_user.language == lang_text[2]:  # en verssion
                btn = types.InlineKeyboardButton('Ordering 🟢', callback_data=f'getorder_{orders.last().order.id}')
                markup.add(btn)
                text = '🛒 <b>Your cart:</b>\n\n'
                n = 1
                for i in orders:
                    btn = types.InlineKeyboardButton(f'{i.product_item.name_en} | {i.amount} {i.product_item.unit} ❌',
                                                     callback_data=f'delete_{i.id}')
                    markup.add(btn)
                    text += f'<b>{n}:</b> {i.product_item.name_en} | <i>{i.amount} {i.product_item.unit} x {i.product_item.price} ₩ = {round(int(i.amount) * int(i.product_item.price), -2)}</i> ₩\n'
                    n += 1
                order = Orders.objects.get(client=bot_user, active=True)
                delivery = Extra.objects.get(name="Delivery").quantity
                bonus = Extra.objects.get(name="bonus").quantity
                text += f'\n-------------------\n📦 <b>Total product:</b> <i>{round(order.summa, -2)}</i> ₩\n💸 <b>Cashback:</b> <i>{round(order.summa / 100 * bonus, -2)}</i> ₩\n-------------------\n🚚 <b>Delivery price:</b> <i>{delivery}</i> ₩ \n-------------------\n💳 <b>Total:</b> <i>{round(order.summa + delivery - (order.summa / 100 * bonus), -2)}</i> ₩'
                bot.send_message(message.from_user.id, text, reply_markup=markup)
            else:
                btn = types.InlineKeyboardButton('Buyurtma berish 🟢',
                                                 callback_data=f'getorder_{orders.last().order.id}')
                markup.add(btn)
                text = '🛒 <b>Sizning savatchangiz:</b>\n\n'
                n = 1
                for i in orders:
                    btn = types.InlineKeyboardButton(f'{i.product_item.name_uz} | {i.amount} {i.product_item.unit} ❌',
                                                     callback_data=f'delete_{i.id}')
                    markup.add(btn)
                    text += f'<b>{n}:</b> {i.product_item.name_uz} | <i>{i.amount} {i.product_item.unit} x {i.product_item.price} ₩ = {round(int(i.amount) * int(i.product_item.price), -2)}</i> ₩\n'
                    n += 1
                order = Orders.objects.get(client=bot_user, active=True)
                delivery = Extra.objects.get(name="Delivery").quantity
                bonus = Extra.objects.get(name="bonus").quantity
                text += f'\n-------------------\n📦 <b>Jami mahsulot:</b> <i>{round(order.summa, -2)}</i> ₩\n💸 <b>Sizning Bonusingiz:</b> <i>{round(order.summa / 100 * bonus, -2)}</i> ₩\n-------------------\n🚚 <b>Yetkazib berish narxi:</b> <i>{delivery}</i> ₩ \n-------------------\n💳 <b>Jami:</b> <i>{round(order.summa + delivery - (order.summa / 100 * bonus), -2)}</i> ₩'
                bot.send_message(message.from_user.id, text, reply_markup=markup)
        else:
            if bot_user.language == lang_text[1]:
                bot.send_message(message.from_user.id, '🛒 В вашей корзине нет товаров')
            elif bot_user.language == lang_text[2]:
                bot.send_message(message.from_user.id, '🛒 There are no products in your cart')
            else:
                bot.send_message(message.from_user.id, '🛒 Savatingizda mahsulotlar yo‘q')
    elif message.text in ["🛍 Buyurtmalarim", "🛍 Orders", "🛍 Заказы"] and bot_user.step == 6:
        orders = Orders.objects.filter(client=bot_user, active=False)
        or_it = OrderItem.objects.filter(order__id=orders.last().id)
        if orders.exists():
            markup = types.InlineKeyboardMarkup(row_width=1)
            if bot_user.language == lang_text[1]:
                text = my_order(or_it, lang='ru')
                btn = types.InlineKeyboardButton('История заказов 📗', callback_data=f'history')
                markup.add(btn)
                bot.send_message(message.from_user.id, text, reply_markup=markup)
            elif bot_user.language == lang_text[2]:
                text = my_order(or_it, lang='en')
                btn = types.InlineKeyboardButton('Order history 📗', callback_data=f'history')
                markup.add(btn)
                bot.send_message(message.from_user.id, text, reply_markup=markup)
            else:
                text = my_order(or_it)
                btn = types.InlineKeyboardButton('Buyurtma tarixi 📗', callback_data=f'history')
                markup.add(btn)
                bot.send_message(message.from_user.id, text, reply_markup=markup)
        else:
            if bot_user.language == lang_text[1]:
                bot.send_message(message.from_user.id, '🛍 У вас пока нет заказов')
            elif bot_user.language == lang_text[2]:
                bot.send_message(message.from_user.id, '🛍 You don\'t have any orders yet')
            else:
                bot.send_message(message.from_user.id, '🛍 Buyurtmalaringiz hozircha yo‘q')
    elif message.text in ["🏘 Filiallar"] and bot_user.step == 6:
        InlineController(m=message, userid=message.from_user.id).branch()
    elif message.text in ["💳 Hisob raqam", "💳 Счет номер", "💳 Bank account"] and bot_user.step == 6:
        if bot_user.language == "🇺🇿 O'zbek tili":
            bot.send_message(message.from_user.id,
                             '🏦 Bank: KEB HANA\n💳 Hisob: 630-005487-942\n👤 Karta egasi: MURODQULOV \n🔒 Kod: 081')
        elif bot_user.language == "🇷🇺 Русский язык":
            bot.send_message(message.from_user.id,
                             '🏦 Банк: КЕБ ХАНА\n💳 Счёт:630-005487-942\n👤 Владелец карты:MURODQULOV\n🔒 Код:081')
        elif bot_user.language == "🇬🇧 English":
            bot.send_message(message.from_user.id,
                             '🏦 Bank: KEB HANA\n💳 Holder:630-005487-942\n👤 Card holder:MURODQULOV\n🔒 Code:081')
    # elif message.text == "📝 Manzilni o`zgartirish":
    #     markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    #     b1 = types.KeyboardButton("⬅️Ortga")
    #     markup.add(b1)
    #     bot.send_message(message.from_user.id, "Manzilingizni rasm yoki text shaklda kiriting", reply_markup=markup)
    else:
        if bot_user.language in lang_text and bot_user.active == True:
            bot.send_message(message.from_user.id, 'Please Enter True 😁😁😁')
        else:
            bot.send_message(message.from_user.id, 'Please Enter True 😁😁😁')


def lang(message, bot_user):
    if bot_user.language == "🇺🇿 O'zbek tili":
        markup1 = base_btn(base_btn_text['uz'])
        bot.send_message(message.from_user.id, "Sizning ma'lumotlaringiz muvaffaqiyatli o'zgartirildi.",
                         reply_markup=markup1)
    elif bot_user.language == "🇷🇺 Русский язык":
        markup1 = base_btn(base_btn_text['ru'])
        bot.send_message(message.from_user.id, "Ваша информация была успешно изменена.", reply_markup=markup1)
    elif bot_user.language == "🇬🇧 English":
        markup1 = base_btn(base_btn_text['en'])
        bot.send_message(message.from_user.id, "Your information has been successfully modified.", reply_markup=markup1)

# @bot.message_handler(content_types=['photo'])
# def photo_handler(message):
#     user = Users.objects.get(user_id=message.from_user.id)
#     images = Images(user=user)
#     images.save()
#     raw = message.photo[1].file_id
#     path = raw + ".jpg"
#     file_info = bot.get_file(raw)
#     downloaded_file = bot.download_file(file_info.file_path)
#     content = ContentFile(downloaded_file)
#     images.image.save(path, content, save=True)
#     images.save()
#     bot.send_message(message.from_user.id, str(img_to_text(images.image)))
