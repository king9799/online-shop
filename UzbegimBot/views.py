import telebot
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from .models import User
# from .buttons import *
# from .text import *

bot = telebot.TeleBot("2102894205:AAE-qFT15tEykiaUuWCp79gxU9OMxKgsY_Y")


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse("<a href='http://t.me/dkarimoff96'>Created by</>")
    if request.method == 'POST':
        bot.process_new_updates([
            telebot.types.Update.de_json(
                request.body.decode("utf-8")
            )
        ])
        return HttpResponse(status=200)

# @bot.message_handlers
# def start(commands = start)