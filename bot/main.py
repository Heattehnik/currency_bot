import asyncio
import logging
import os
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
import markups as nav

load_dotenv()


logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!", reply_markup=nav.main_menu)

@dp.message()
async def bot_message(message: types.Message):
    if message.text == "Рандомное число":
        await bot.send_message(message.from_user.id, f"Your number {random.randint(0, 1000)}")
    elif message.text == "Подменю":
        await bot.send_message(message.from_user.id, f"Submenu", reply_markup=nav.other_menu)
    elif message.text == "Подменю":
        await bot.send_message(message.from_user.id, f"Submenu", reply_markup=nav.other_menu)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
