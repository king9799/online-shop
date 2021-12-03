import datetime

from telebot import *
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .buttons import *
from .acts import *

bot = TeleBot("2102894205:AAE-qFT15tEykiaUuWCp79gxU9OMxKgsY_Y")


@csrf_exempt
def api(request):
    if request.method == 'GET':
        return HttpResponse("<a href='http://t.me/dkarimoff96'>Created by</>")
    if request.method == 'POST':
        bot.process_new_updates([
            telebot.types.Update.de_json(
                request.body.decode("utf-8")
            )
        ])
        return HttpResponse(status=200)


@bot.message_handler(commands=["start"])
def start(m):

    all_users = Users.objects.filter(user_id=m.chat.id, step=6)
    print(all_users)
    if len(all_users) > 0:
        markup = base_uz()
        bot.send_message(m.chat.id, "menu", reply_markup=markup)
    else:
        text = f'Assalomu alaykum hurmatli {m.from_user.first_name}.Bu Uzbegim online-market boti. \n\nBizning ' \
               f'xizmatlarimizdan foydalanish uchun avval ro`yhatdan o`ting. '
        bot.send_message(m.chat.id, text)
        text1 = "Muloqot tilini tanlang\nВыберите язык\nSelect Language"
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        btn = types.KeyboardButton("🇺🇿 O'zbek tili")
        btn1 = types.KeyboardButton("🇷🇺 Русский язык")
        btn2 = types.KeyboardButton("🇬🇧 English")
        btn3 = types.KeyboardButton("🆘 Yordam / Помощь / Help")
        markup.add(btn, btn1, btn2, btn3)
        bot.send_message(m.chat.id, text1, reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot_user = Users(user_id=message.chat.id)
    bot_user.save()
    if message.text == "🇺🇿 O'zbek tili":
        bot.send_message(message.chat.id, "Botdan foydalanish uchun avval ro`yhatdan o`ting.")
        bot_user.language = message.text
        bot_user.step = 1
        bot_user.save()
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        b = types.KeyboardButton("⬅️Ortga")
        markup.add(b)
        bot.send_message(message.chat.id, "Ismingizni kiriting: ", reply_markup=markup)
    elif bot_user.step == 1:
        bot_user.first_name = message.text
        bot_user.step += 1
        bot_user.save()
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        b = types.KeyboardButton("⬅️Ortga")
        markup.add(b)
        bot.send_message(message.chat.id, "Familyangizni kiriting: ", reply_markup=markup)
    elif bot_user.step == 2:
        bot_user.last_name = message.text
        bot_user.step += 1
        bot_user.save()
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        b = types.KeyboardButton("⬅️Ortga")
        markup.add(b)
        bot.send_message(message.chat.id, "Telefon nomeringizni kiriting: ", reply_markup=markup)
    elif bot_user.step == 3:
        bot_user.phone_number = message.text
        bot_user.step += 1
        bot_user.save()
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        b = types.KeyboardButton("⬅️Ortga")
        markup.add(b)
        bot.send_message(message.chat.id, "Manzilingizni kiriting: ", reply_markup=markup)
    elif bot_user.step == 4:
        bot_user.address = message.text
        bot_user.step += 1
        bot_user.save()
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        yes = types.KeyboardButton('✅ Ok')
        no = types.KeyboardButton('📝️️Tahrirlash')
        markup.add(yes, no)
        bot.send_message(message.chat.id, "Ro`yhatdan o`tish mufavaqqiyatli yakunlandi. ")
        bot.send_message(message.chat.id,
                         f"Sizning barcha ma`lumotlaringiz to`gri ko`rsatilganmi?\n\n🗂 Ism: {bot_user.first_name}\n📁 Familya: {bot_user.last_name}\n📱 Telefon nomer: {bot_user.phone_number}\n🏠 Manzil: {bot_user.address}",
                         reply_markup=markup)
    elif message.text == '✅ Ok':
        bot_user.active = True
        bot_user.step += 1
        bot_user.save()
        markup = base_uz()
        bot.send_message(message.chat.id, "MENU:", reply_markup=markup)
    elif message.text == "👤 Profil":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        e = types.KeyboardButton('📝️Tahrirlash')
        b5 = types.KeyboardButton("⬅️Ortga")
        markup.add(e, b5)
        bot.send_message(message.chat.id,
                         f"Sizning ma`lumotlaringiz:\n\n🗂Ism: {bot_user.first_name} \n📁Familiya: {bot_user.last_name} \n🏠Manzil: {bot_user.address} \n📱Nomer: {bot_user.phone_number} \n\nShaxsiy ma'lomatlarni o'zgartish uchun quyidagi "
                         "tugmalarda birini bosing", reply_markup=markup)

    elif message.text == '📝️️Tahrirlash':
        # bot_user.step = 6
        markup = types.InlineKeyboardMarkup(row_width=2)
        kmarkup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        b1 = types.InlineKeyboardButton("🗂 Ism", callback_data='first')
        b2 = types.InlineKeyboardButton("📁 Familya", callback_data='last')
        b3 = types.InlineKeyboardButton("🏠 Manzil", callback_data='address')
        b4 = types.InlineKeyboardButton("📱 Telefon nomer", callback_data='number')
        b5 = types.KeyboardButton("⬅️Ortga")
        markup.add(b1, b2, b3, b4)
        kmarkup.add(b5)
        bot.send_message(message.chat.id, "Shaxsiy ma'lomatlarni o'zgartish uchun quyidagi tugmalarda birini bosing", reply_markup=kmarkup)
        bot.send_message(message.chat.id, f"Sizning ma`lumotlaringiz:\n\n🗂Ism: {bot_user.first_name} \n📁Familiya: {bot_user.last_name} \n🏠Manzil: {bot_user.address} \n📱Nomer: {bot_user.phone_number} \n", reply_markup=markup)
    elif message.text == "⬅️Ortga":
        markup = base_uz()
        # bot_user.step -= 1
        bot.send_message(message.chat.id, "MENU:", reply_markup=markup)

    elif message.text == "🆘 Yordam / Помощь / Help":
        bot.send_message(message.chat.id,
                         "UZBEGIM halol go`sht mahsulotlari do`koni\n Ushbu bot orqali siz halol go`sht va Uzbegim do`konidagi barcha "
                         "maxsulotlarga buyurtma berishingiz mumkin. \n\n "
                         "\n ☎️Qo’shimcha ma’lumotlar uchun: 010-6363-9080")

    elif message.text == "📑 Maxsulotlar":
        markup = products()
        bot.send_message(message.chat.id, "Maxsulotni tanlang:", reply_markup=markup)

    elif message.text == "🛒 Savatcha":
        bot.send_message(message.chat.id, "Savatcha bo`sh!")

    elif message.text == "📦 Buyurtmalarim":
        bot.send_message(message.chat.id, "Buyurtmalar topilmadi")

    elif message.text == "💳 Hisob raqam":
        bot.send_message(message.chat.id, "Maxsus bank hisob raqami mahsulotga buyurtma berganingizdan so'ng "
                                          "beriladi.\n\n"
                                          " Конкретный номер банковского счета будет указан после заказа "
                                          "продуктов. \n\n "
                                          "The specific bank account number will be given after you "
                                          "order products.")
    # elif message.text == "📝 Manzilni o`zgartirish":
    #     markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    #     b1 = types.KeyboardButton("⬅️Ortga")
    #     markup.add(b1)
    #     bot.send_message(message.chat.id, "Manzilingizni rasm yoki text shaklda kiriting", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'first':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Ismingizni kiriting: ")
