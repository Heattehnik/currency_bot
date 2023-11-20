import asyncio
import logging
import os
import random
from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
import markups as nav
from utils import register_client, get_currency, get_history, subscription

load_dotenv()


logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await register_client(
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name,
        message.from_user.last_name
    )
    await message.answer("Зарегистрирован!", reply_markup=nav.main_menu)


@dp.message()
async def bot_message(message: types.Message):
    if message.text == "Узнать курс доллара":
        currency = await get_currency(message.from_user.id)
        date = currency['date'].split('-')
        date = ".".join(reversed(date))
        await bot.send_message(message.from_user.id, f"Курс доллара на {date} - {currency['rate']} руб.", reply_markup=nav.main_menu)
    elif message.text == "История запросов":
        history = await get_history(message.from_user.id)
        history_text = "\n".join([f"{datetime.fromisoformat(request['created_at'][:-6]).strftime('%d.%m.%Y %H:%M:%S')} - {request['rate']} руб." for request in history])
        await bot.send_message(message.from_user.id,  f"Ваши последние 5 запросов: \n{history_text}", reply_markup=nav.main_menu)
    elif message.text == "Подписка":
        await bot.send_message(message.from_user.id, f"Вы можете подписаться на обновления.",
                               reply_markup=nav.subscription_menu)
    elif message.text == "Подписаться":
        if await subscription(message.from_user.id, True):
            await bot.send_message(message.from_user.id, "Вы подписались на обновления!")
    elif message.text == "Отписаться":
        if await subscription(message.from_user.id, False):
            await bot.send_message(message.from_user.id, "Вы отписались от обновлений!")
    elif message.text == "Назад":
        await bot.send_message(message.from_user.id, f"Главное меню", reply_markup=nav.main_menu)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
