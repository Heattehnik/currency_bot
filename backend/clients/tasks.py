import telebot
from celery import shared_task
from clients.models import Client
from currency.models import Currency
import os

bot = telebot.TeleBot(token=os.getenv('BOT_TOKEN'))


@shared_task
def send_currency_rate():
    try:
        currency_rate = Currency.objects.latest('date')
        subscribed_users = Client.objects.filter(is_subscribed=True)
        for user in subscribed_users:
            chat_id = user.user_id
            message = f"{currency_rate}"
            bot.send_message(chat_id, message)
    except Currency.DoesNotExist:
        return 'Нет курса валют'
    return "Курс доллара отправлен подписчикам"
