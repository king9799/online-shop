from .models import *


def ptoduct_item(name, price, desc, lan='uz'):
    if lan == 'ru':
        return f'<b>{name}</b>\n\n<b>Стоимость:</b> {price}\n\n<b><i>Описание:</i></b>\n{desc}\n'
    elif lan == 'en':
        return f'<b>{name}</b>\n\n<b>Price:</b> {price}\n\n<b><i>Description:</i></b>\n{desc}\n'
    else:
        return f'<b>{name}</b>\n\n<b>Narxi:</b> {price}\n\n<b><i>Tavsifi:</i></b>\n{desc}\n'


register_text = {1: {'uz': 'Ismingizni kiriting: ', 'ru': 'Введите ваше имя: ', 'en': 'Enter your name: '},
                 2: {'uz': 'Familiyangizni kiriting: ', 'ru': 'Введите вашу фамилию: ', 'en': 'Enter your last name: '},
                 3: {'uz': 'Telefon nomeringizni kiriting: ', 'ru': 'Введите свой номер телефона: ', 'en': 'Enter your phone number: '},
                 4: {'uz': 'Manzilingizni kiriting yoki rasmga olib tashlang: ', 'ru': 'Введите свое местоположение или сделайте снимок: ', 'en': 'Enter your location or take a picture: '}}

back_button = {'uz': "⬅️Ortga", 'en': "⬅️Back", 'ru': "⬅️Назад"}

base_btn_text = {
            'uz': ["💵 Valyuta kursi", "📑 Maxsulotlar", "🛒 Savatcha", "🛍 Buyurtmalarim", "👤 Profil", "💳 Hisob raqam", "🆘 Yordam", "⌛️Namoz vaqtlari", "🏘 Filiallar"],
            'en': ["💵 Currency rate", "📑 Products", "🛒 Box", "🛍 Orders", "👤 Profile", "💳 Bank account", "🆘 Help", "⌛️Prayer times", "🏘 Filiallar"],
            'ru': ["💵 Курс валюты", "📑 Продукты", "🛒 Карзинка", "🛍 Заказы", "👤 Профиль", "💳 Счет номер", "🆘 Помощь", "⌛️Время молитв", "🏘 Filiallar"]
            }


def order_text(pro_item, lan='uz'):
    delivery = Extra.objects.get(name="Delivery").quantity
    bonus = Extra.objects.get(name="bonus").quantity
    if lan == 'en':
        text = f'<b>📦 Order Number:</b> #{pro_item.last().order.order_n} \nProducts:\n\n'
        text1 = f'<b>Thank you for your order!</b>\n\n🏦 Bank: КЕБ ХАНА\n💳 Account:630-005487-942\n👤 Holder: MURODQULOV SH\n🔒Code: 081\n\n💸 Total payment: {round(pro_item.last().order.summa + delivery - (pro_item.last().order.summa / 100 * bonus), -2):,} ₩\n\n➡️Please transfer the specified amount of money to the given bank account.\n📱 For more information: 010-6363-9080'
        n = 1
        for i in pro_item:
            text += f'{n}. <b>{i.product_item.name_ru}</b>\n   <b>Price:</b> {round(i.product_item.price, -2)} ₩\n   <b>Amount:</b> {i.amount}\n   <b>Total price:</b> {i.summa} ₩\n\n'
            n += 1
        text += f'\n----------------\n📦 <b>Total product:</b> <i> {round(i.order.summa, -2):,}</i> ₩\n----------------\n💸 <b>Cashback:</b> <i>{round(i.order.summa / 100 * bonus, -2):,}</i> ₩\n----------------\n🚚 <b>Delivery price::</b> <i>{delivery:,}</i> ₩ \n----------------\n💳 <b>Total:</b> <strong>{round(i.order.summa + delivery - (i.order.summa / 100 * bonus), -2):,}</strong> ₩\n\n{i.order.cr_on}'
    elif lan == 'ru':
        text = f'<b>📦 Номер заказа:</b> #{pro_item.last().order.order_n} \nПродукты:\n\n'
        text1 = f'<b>Благодарим за покупку!</b>\n\n🏦 Банк: КЕБ ХАНА\n💳 Счёт:630-005487-942\n👤 Владелец карты: MURODQULOV SH\n🔒Код: 081\n\n💸 Сумма платежа: {round(pro_item.last().order.summa + delivery - (pro_item.last().order.summa / 100 * bonus), -2):,} ₩\n\n➡️Просим вас переведите данную сумму денег на указанный выше банковский счет.\n📱 Подробно связитесь: 010-6363-9080'
        n = 1
        for i in pro_item:
            text += f'{n}. <b>{i.product_item.name_ru}</b>\n   <b>Стоимость:</b> {round(i.product_item.price, -2)}\n   <b>Kоличество:</b> {i.amount}\n   <b>Итоговая цена:</b> {i.summa} ₩\n\n'
            n += 1
        text += f'\n----------------\n📦 <b>Общий продукт:</b> <i> {round(i.order.summa, -2):,}</i> ₩\n----------------\n💸 <b>Возврат наличных:</b> <i>{round(i.order.summa / 100 * bonus, -2):,}</i> ₩\n----------------\n🚚 <b>Доставка:</b> <i>{delivery:,}</i> ₩ \n----------------\n💳 <b>Общая сумма:</b> <strong>{round(i.order.summa + delivery - (i.order.summa / 100 * bonus), -2):,}</strong> ₩\n\n{i.order.cr_on}'
    else:
        text = f'<b>📦 Buyurtma raqami:</b> #{pro_item.last().order.order_n} \nMaxsulotlar:\n\n'
        text1 = f'<b>Buyurtmangiz uchun raxmat!</b>\n\n🏦 Bank: KEB HANA \n💳 Hisob: 630-005487-942\n👤 Karta egasi: MURODQULOV SH\nKod: 081 \n\n💸 Tolov summasi: {round(pro_item.last().order.summa + delivery - (pro_item.last().order.summa / 100 * bonus)):,} ￦\n\n➡️Ko\'rsatilgan miqdordagi pulni yuqoridagi bank hisob raqamga o\'tkazishingizni so`raymiz\n📱 Qo\'shimcha ma\'lumot uchun: 010-6363-9080'
        n = 1
        for i in pro_item:
            text += f'{n}. <b>{i.product_item.name_uz}</b>\n   <b>Narxi:</b> {round(i.product_item.price, -2)} ₩\n   *Miqdori:* {i.amount} kg\n   *Umumiy narxi:* {i.summa} ₩\n\n'
            n += 1
        text += f'\n----------------\n📦 <b>Jami mahsulot:</b> <i> {round(i.order.summa, -2):,}</i> ₩\n----------------\n💸 <b>Xaridingiz uchun bonus:</b> <i>{round(i.order.summa / 100 * bonus, -2):,}</i> ₩\n----------------\n🚚 <b>Yetkazib berish xizmati:</b> <i>{delivery:,}</i> ₩ \n----------------\n💳 <b>Jami:</b> <strong>{round(i.order.summa + delivery - (i.order.summa / 100 * bonus), -2):,}</strong> ₩\n\n{i.order.cr_on}'
    return {'text': text, 'text1': text1}


def send_order(or_it_id):
    text = f'✅ Yangi buyurtma {or_it_id.last().order.cr_on} \n#️⃣ Buyurtma raqami: #{or_it_id.last().order.order_n}\n🙍‍♂️ Mijoz: {or_it_id.last().order.client.first_name} {or_it_id.last().order.client.last_name}\n🏠 Manzil: {or_it_id.last().order.client.address}\n🏠 Qo\'shimcha:\n☎  Telefon: {or_it_id.last().order.client.phone_number}\n🛒  Buyurtmalar:\n'
    text += '----------------\n'
    for i in or_it_id:
        text += f'📜 <code>Nomi: {i.product_item.name_uz} \n💰 Narxi: {i.product_item.price:,} ₩ \n🔢 Soni: {i.amount} {i.product_item.unit} \n🧾 To\'lov: {i.summa:,} ₩</code> \n----------------\n'
    delivery = Extra.objects.get(name="Delivery").quantity
    bonus = Extra.objects.get(name="bonus").quantity
    text += f'\n----------------\n💸 <b>Bonus:</b> <i>{round(i.order.summa / 100 * bonus, -2):,}</i> ₩\n----------------\n🚚 <b>Pochta narxi:</b> <i>{delivery:,}</i> ₩\n----------------\n💳 <b>Jami:</b> <strong>{round(i.order.summa + delivery - (i.order.summa / 100 * bonus), -2):,}</strong> ₩'
    return text


def my_order(or_it_id, or_id=0, last=True, lang='uz'):
    if last == True:
        if lang == 'ru':
            text = f'#️⃣ Номер заказа: #{or_it_id.last().order.order_n}\n🛒  Заказы:\n'
            text += '----------------\n'
            for i in or_it_id:
                text += f'📜 <code>Товара: {i.product_item.name_ru} \n💰 Цена: {i.product_item.price:,} ₩ \n🔢 Количество: {i.amount} {i.product_item.unit} \n🧾 Оплата: {i.summa:,} ₩</code> \n----------------\n'
            delivery = Extra.objects.get(name="Delivery").quantity
            bonus = Extra.objects.get(name="bonus").quantity
            text += f'\n📦 <b>Общий продукт:</b> <i>{i.order.summa:,}</i> ₩\n----------------\n💸 <b>Возврат наличных:</b> <i>{round(i.order.summa / 100 * bonus, -2):,}</i> ₩\n----------------\n🚚 <b>Доставка:</b> <i>{delivery:,}</i> ₩ \n----------------\n💳 <b>Общая сумма:</b> <strong>{round(i.order.summa + delivery - (i.order.summa / 100 * bonus), -2):,}</strong> ₩\n\n{i.order.cr_on}'
            return text
        elif lang == 'en':
            text = f'#️⃣ Order number: #{or_it_id.last().order.order_n}\n🛒  Orders:\n'
            text += '----------------\n'
            for i in or_it_id:
                text += f'📜 <code>Product: {i.product_item.name_uz} \n💰 Summa: {i.product_item.price:,} ₩ \n🔢 Amount: {i.amount} {i.product_item.unit} \n🧾 Payment: {i.summa:,} ₩</code> \n----------------\n'
            delivery = Extra.objects.get(name="Delivery").quantity
            bonus = Extra.objects.get(name="bonus").quantity
            text += f'\n📦 <b>Total product:</b> <i>{i.order.summa:,}</i> ₩\n----------------\n💸 <b>Cashback:</b> <i>{round(i.order.summa / 100 * bonus, -2):,}</i> ₩\n----------------\n🚚 <b>Delivery price:</b> <i>{delivery:,}</i> ₩ \n----------------\n💳 <b>Total:</b> <strong>{round(i.order.summa + delivery - (i.order.summa / 100 * bonus), -2):,}</strong> ₩\n\n{i.order.cr_on}'
            return text
        else:
            text = f'#️⃣ Buyurtma raqami: #{or_it_id.last().order.order_n}\n🛒  Buyurtmalar:\n'
            text += '----------------\n'
            for i in or_it_id:
                text += f'📜 <code>Nomi: {i.product_item.name_uz} \n💰 Narxi: {i.product_item.price:,} ₩ \n🔢 Soni: {i.amount} {i.product_item.unit} \n🧾 Harid narxi:: {i.summa:,} ₩</code> \n----------------\n'
            delivery = Extra.objects.get(name="Delivery").quantity
            bonus = Extra.objects.get(name="bonus").quantity
            text += f'\n📦 <b>Jami haridlar qiymati:</b> <i>{i.order.summa:,}</i> ₩\n----------------\n💸 <b>Harid uchun bonus:</b> <i>{round(i.order.summa / 100 * bonus, -2):,}</i> ₩\n----------------\n🚚 <b>Pochta narxi:</b> <i>{delivery:,}</i> ₩ \n----------------\n💳 <b>Jami:</b> <strong>{round(i.order.summa + delivery - (i.order.summa / 100 * bonus), -2):,}</strong> ₩\n\n{i.order.cr_on}'
            return text
    else:
        print('jjj')
        text = ''
        if lang == 'ru':
            for order in or_id:
                text += f'#️⃣ Номер заказа: #{order.order_n}\n🛒  Заказы:\n'
                text += '----------------\n'
                for pro_item in or_it_id:
                    if order.order_n == pro_item.order.order_n:
                        text += f'📜 <code>Товара: {pro_item.product_item.name_ru} \n💰 Цена: {pro_item.product_item.price:,} ₩ \n🔢 Количество: {pro_item.amount} {pro_item.product_item.unit} \n🧾 Оплата: {pro_item.summa:,} ₩</code> \n----------------\n'
                delivery = Extra.objects.get(name="Delivery").quantity
                bonus = Extra.objects.get(name="bonus").quantity
                text += f'\n📦 <b>Общий продукт:</b> <i>{round(order.summa, -2):,}</i> ₩\n----------------\n💸 <b>Возврат наличных:</b> <i>{round(pro_item.order.summa / 100 * bonus, -2):,}</i> ₩\n----------------\n🚚 <b>Доставка:</b> <i>{delivery:,}</i> ₩ \n----------------\n💳 <b>Общая сумма:</b> <strong>{round(pro_item.order.summa + delivery - (pro_item.order.summa / 100 * bonus), -2):,}</strong> ₩\n\n{pro_item.order.cr_on}\n\n--------------------------------------\n\n'
            return text
        elif lang == 'en':
            for order in or_id:
                text += f'#️⃣ Order number: #{order.order_n}\n🛒  Orders:\n'
                text += '----------------\n'
                for pro_item in or_it_id:
                    if order.order_n == pro_item.order.order_n:
                        text += f'📜 <code>Product: {pro_item.product_item.name_en} \n💰 Summa: {pro_item.product_item.price:,} ₩ \n🔢 Amount: {pro_item.amount} {pro_item.product_item.unit} \n🧾 Payment: {pro_item.summa:,} ₩</code> \n----------------\n'
                delivery = Extra.objects.get(name="Delivery").quantity
                bonus = Extra.objects.get(name="bonus").quantity
                text += f'\n📦 <b>Total product:</b> <i>{round(order.summa, -2):,}</i> ₩\n----------------\n💸 <b>Cashback:</b> <i>{round(pro_item.order.summa / 100 * bonus, -2):,}</i> ₩\n----------------\n🚚 <b>Delivery price:</b> <i>{delivery:,}</i> ₩ \n----------------\n💳 <b>Total:</b> <strong>{round(pro_item.order.summa + delivery - (pro_item.order.summa / 100 * bonus), -2):,}</strong> ₩\n\n{pro_item.order.cr_on}\n\n--------------------------------------\n\n'
            return text
        else:
            print(or_it_id)
            for order in or_id:
                text += f'#️⃣ Buyurtma raqami: #{order.order_n}\n🛒  Buyurtmalar:\n'
                text += '----------------\n'
                for pro_item in or_it_id:
                    if order.order_n == pro_item.order.order_n:
                        text += f'📜 <code>Nomi: {pro_item.product_item.name_uz} \n💰 Narxi: {pro_item.product_item.price:,} ₩ \n🔢 Soni: {pro_item.amount} {pro_item.product_item.unit} \n🧾 Harid narxi: {pro_item.summa:,} ₩</code> \n----------------\n'
                delivery = Extra.objects.get(name="Delivery").quantity
                bonus = Extra.objects.get(name="bonus").quantity
                text += f'\n📦 <b>Jami haridlar qiymati:</b> <i>{round(order.summa, -2):,}</i> ₩\n----------------\n💸 <b>Harid uchun bonus:</b> <i>{round(order.summa / 100 * bonus, -2):,}</i> ₩\n----------------\n🚚 <b>Pochta narxi:</b> <i>{delivery:,}</i> ₩ \n----------------\n💳 <b>Jami:</b> <strong>{round(order.summa + delivery - (order.summa / 100 * bonus), -2):,}</strong> ₩\n\n{order.cr_on}\n\n--------------------------------------\n\n'
            return text








lang_text = ["🇺🇿 O'zbek tili", "🇷🇺 Русский язык", "🇬🇧 English"]