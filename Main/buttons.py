from telebot import *
def base_uz():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn = types.KeyboardButton("💵 Valyuta kursi")
    btn1 = types.KeyboardButton("📑 Maxsulotlar")
    btn2 = types.KeyboardButton("🛒 Savatcha")
    btn3 = types.KeyboardButton("📦 Buyurtmalarim")
    btn4 = types.KeyboardButton("👤 Profil")
    btn5 = types.KeyboardButton("💳 Hisob raqam")
    btn6 = types.KeyboardButton("🆘 Yordam")
    btn7 = types.KeyboardButton("⌛️Namoz vaqtlari")

    markup.add(btn1, btn2, btn3)
    markup.add(btn4, btn5, btn6)
    markup.add(btn, btn7)
    return markup
def base_ru():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn = types.KeyboardButton("💵 Курс валюты")
    btn1 = types.KeyboardButton("📑 Продукты")
    btn2 = types.KeyboardButton("🛒 Карзинка")
    btn3 = types.KeyboardButton("📦 Заказы")
    btn4 = types.KeyboardButton("👤 Профиль")
    btn5 = types.KeyboardButton("💳 Счет номер")
    btn6 = types.KeyboardButton("🆘 Помощь")

    markup.add(btn)
    markup.add(btn1, btn2, btn3)
    markup.add(btn4, btn5, btn6)
    return markup

def base_en():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn = types.KeyboardButton("💵 Currency rate")
    btn1 = types.KeyboardButton("📑 Products")
    btn2 = types.KeyboardButton("🛒 Box")
    btn3 = types.KeyboardButton("📦 Orders")
    btn4 = types.KeyboardButton("👤 Profile")
    btn5 = types.KeyboardButton("💳 Bank account")
    btn6 = types.KeyboardButton("🆘 Help")

    markup.add(btn)
    markup.add(btn1, btn2, btn3)
    markup.add(btn4, btn5, btn6)
    return markup

def products():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn = types.InlineKeyboardButton(" Mol go`shti", callback_data="0")
    btn1 = types.InlineKeyboardButton(" Qo`y go`shti", callback_data="1")
    btn2 = types.InlineKeyboardButton(" Tovuq go`shti", callback_data="2")
    btn3 = types.InlineKeyboardButton("Kitoblar", callback_data="3")
    btn4 = types.InlineKeyboardButton("Oziq-ovat", callback_data="4")
    btn5 = types.InlineKeyboardButton("Konserva", callback_data="5")
    btn6 = types.InlineKeyboardButton("Kalbasa maxsulotlari", callback_data="6")
    btn7 = types.InlineKeyboardButton("Shirinliklar", callback_data="7")
    btn8 = types.InlineKeyboardButton("Tuzlamalar", callback_data="8")
    btn9 = types.InlineKeyboardButton("Yarim tayyor", callback_data="9")
    btn10 = types.InlineKeyboardButton("Ichimliklar", callback_data="10")
    btn11 = types.InlineKeyboardButton("Ziravorlar", callback_data="11")
    btn12 = types.InlineKeyboardButton("CHEGIRMALAR", callback_data="12")
    btn13 = types.InlineKeyboardButton("Palov maxsulotlari", callback_data="13")
    markup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13)
    return markup

def beef():
    markup = types.InlineKeyboardMarkup(row_width=2)
    b = types.InlineKeyboardButton("Mol bo`yin", callback_data="m")
    b1 = types.InlineKeyboardButton("Mol dum", callback_data="m1")
    b2 = types.InlineKeyboardButton("Mol jigar", callback_data="m2")
    b3 = types.InlineKeyboardButton("Mol qiyma", callback_data="m3")
    b4 = types.InlineKeyboardButton("Mol oldi son", callback_data="m4")
    b5 = types.InlineKeyboardButton("Mol orqa son", callback_data="m5")
    b6 = types.InlineKeyboardButton("Mol ichki son", callback_data="m6")
    b7 = types.InlineKeyboardButton("Mol qovurg`a", callback_data="m7")
    b8 = types.InlineKeyboardButton("Mol til", callback_data="m8")
    b9 = types.InlineKeyboardButton("Mol tuyoq", callback_data="m9")
    b10 = types.InlineKeyboardButton("Mol yog`i", callback_data="m10")
    markup.add(b, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10)

    return markup

def lamb():
    markup = types.InlineKeyboardMarkup(row_width=2)
    b = types.InlineKeyboardButton("Qo`y mushak", callback_data="q")
    b1 = types.InlineKeyboardButton("Qo`y bo`yin", callback_data="q1")
    b2 = types.InlineKeyboardButton("Qo`y yelka qovurg`a", callback_data="q2")
    b3 = types.InlineKeyboardButton("Qoy yelka lahm", callback_data="q3")
    b4 = types.InlineKeyboardButton("Qo`y orqa son lahm", callback_data="q4")
    b5 = types.InlineKeyboardButton("Qo`y qo`l butun", callback_data="q5")
    b6 = types.InlineKeyboardButton("Qo`y son butun", callback_data="q6")
    b7 = types.InlineKeyboardButton("Qo`y ilik suyak", callback_data="q7")
    b8 = types.InlineKeyboardButton("Qo`y umurtqa suyak", callback_data="q8")
    b9 = types.InlineKeyboardButton("Qo`y tuyoq", callback_data="q9")
    b10 = types.InlineKeyboardButton("Qo`y mayda qovurg`a", callback_data="q10")
    b11 = types.InlineKeyboardButton("Qo`y yog`i", callback_data="q11")
    markup.add(b, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11)
    return markup

def chicken():
    markup = types.InlineKeyboardMarkup(row_width=2)
    b = types.InlineKeyboardButton("Tovuq ko`krak lahm (2kg)", callback_data="t")
    b1 = types.InlineKeyboardButton("Tovuq oyoq lahm (2kg)", callback_data="t1")
    b2 = types.InlineKeyboardButton("Tovuq butun", callback_data="t2")
    b3 = types.InlineKeyboardButton("Okorachka (2.5kg)", callback_data="t3")
    b4 = types.InlineKeyboardButton("Tovuq oyoqchalari (2.5kg)", callback_data="t4")
    b5 = types.InlineKeyboardButton("Tovuq qanot (2.5kg)", callback_data="t5")
    b6 = types.InlineKeyboardButton("Butun tovuq kesilgan", callback_data="t6")
    markup.add(b, b1, b2, b3, b4, b5, b6)
    return markup

def books():
    markup = types.InlineKeyboardMarkup(row_width=2)
    b = types.InlineKeyboardButton("Ruchkali Qur`on kitob", callback_data="q")
    b1 = types.InlineKeyboardButton("Ruchkali Qur`on kitob (katta)", callback_data="q1")
    markup.add(b, b1)
    return markup

def food():
    markup = types.InlineKeyboardMarkup(row_width=2)
    b = types.InlineKeyboardButton("Non (tandir)", callback_data="q")
    b1 = types.InlineKeyboardButton("Non (katta)", callback_data="q1")
    b2 = types.InlineKeyboardButton("Semichka yog` (1L)", callback_data="q2")
    b3 = types.InlineKeyboardButton("Semichka yog` (5L)", callback_data="q3")
    b4 = types.InlineKeyboardButton("Anchor saryog` (454 gr)", callback_data="q4")
    b5 = types.InlineKeyboardButton("Hurmo KHALAS", callback_data="q5")
    b6 = types.InlineKeyboardButton("Lipton qora choy", callback_data="q6")
    b7 = types.InlineKeyboardButton("Chedder pishloq", callback_data="q7")
    b8 = types.InlineKeyboardButton("Noxot", callback_data="q8")
    b9 = types.InlineKeyboardButton("Bobo guruch", callback_data="q9")
    b10 = types.InlineKeyboardButton("Basmati guruch", callback_data="q10")
    b11 = types.InlineKeyboardButton("Ko`k choy 95 (400gr)", callback_data="q11")
    b12 = types.InlineKeyboardButton("Ko`k choy 110 (400gr)", callback_data="q12")
    b13 = types.InlineKeyboardButton("California asali (500gr)", callback_data="q13")
    b14 = types.InlineKeyboardButton("California asali (3kg)", callback_data="q14")
    b15 = types.InlineKeyboardButton("Qaymoq", callback_data="q15")
    b16 = types.InlineKeyboardButton("Qurt ermak", callback_data="q16")
    b17 = types.InlineKeyboardButton("Amerika pistasi", callback_data="q17")
    b18 = types.InlineKeyboardButton("Grechka", callback_data="q18")
    b19 = types.InlineKeyboardButton("Mosh", callback_data="q19")
    b20 = types.InlineKeyboardButton("Bodom", callback_data="q20")
    markup.add(b, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20)
    return markup

def can():
    markup = types.InlineKeyboardMarkup(row_width=2)
    b = types.InlineKeyboardButton("Qo`y tushonka", callback_data="c")
    b1 = types.InlineKeyboardButton("Mol tushonka", callback_data="c1")
    b2 = types.InlineKeyboardButton("Tovuq tushonka", callback_data="c2")
    b3 = types.InlineKeyboardButton("Perlovka", callback_data="c3")
    b4 = types.InlineKeyboardButton("Moshkichri", callback_data="c4")
    b5 = types.InlineKeyboardButton("Grechka", callback_data="c5")
    b6 = types.InlineKeyboardButton("Osh", callback_data="c6")
    markup.add(b, b1, b2, b3, b4, b5, b6)
    return markup

def kalbasa():
    markup = types.InlineKeyboardMarkup(row_width=2)
    b = types.InlineKeyboardButton("Doktorskaya", callback_data="c")
    b1 = types.InlineKeyboardButton("Minskaya", callback_data="c1")
    b2 = types.InlineKeyboardButton("Moskovskaya", callback_data="c2")
    b3 = types.InlineKeyboardButton("Vetchina", callback_data="c3")
    b4 = types.InlineKeyboardButton("Indeyka", callback_data="c4")
    b5 = types.InlineKeyboardButton("Servelat", callback_data="c5")
    b6 = types.InlineKeyboardButton("Lyubitelskaya", callback_data="c6")
    b7 = types.InlineKeyboardButton("Mol go`shtli sasiska", callback_data="c7")
    b8 = types.InlineKeyboardButton("Tovuq go`shtli sasiska", callback_data="c8")
    b9 = types.InlineKeyboardButton("Yegerskaya sasiska", callback_data="c9")
    markup.add(b, b1, b2, b3, b4, b5, b6, b7, b8, b9)
    return markup

def sweets():
    pass

def salty():
    pass

def half():
    pass
def bavarage():
    pass
def spice():
    pass
def discount():
    pass
def palov():
    pass



















