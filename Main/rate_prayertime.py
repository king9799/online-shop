import requests
from telebot import *


def rates():
    re = []
    r = requests.get('https://cbu.uz/oz/arkhiv-kursov-valyut/json/')
    a = r.json()[0]
    for i in r.json():
        if i['id'] in [38, 36, 34, 28, 26, 57]:
            re.append(f'1 $ = {round(float(a["Rate"]) / float(i["Rate"]), 2)} {i["Ccy"]}')
    re.append(f'1 $ = {a["Rate"]} UZS')
    return re


def pray_time(a):
    b = requests.get(f'https://api.pray.zone/v2/times/today.json?city={a}').json()['results']['datetime'][0]
    c = b["date"]["gregorian"]
    r = b["times"]
    return f'⌛️Namoz vaqtlari {a.upper()} shahri bo`yicha:\n\nImsak: {r["Imsak"]} \nFajr: {r["Fajr"]}\nDhuhr: {r["Dhuhr"]}\nAsr: {r["Asr"]}\nMaghrib: {r["Maghrib"]}\nIsha: {r["Isha"]}\n\n📅 Sana: {c}\nManbaa: PrayerTimes.date'

