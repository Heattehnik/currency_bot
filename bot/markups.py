from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = [KeyboardButton(text='Назад')]

# --- Main menu ---

btnRandom = [KeyboardButton(text='Рандомное число')]
btnOther = [KeyboardButton(text='Подменю')]
main_menu = ReplyKeyboardMarkup(keyboard=[btnRandom, btnOther])


# --- Sub menu ---

btnSome = [KeyboardButton(text='Some Text')]
btnSome2 = [KeyboardButton(text='Another text')]
other_menu = ReplyKeyboardMarkup(keyboard=[btnSome, btnSome2, btnMain], resize_keyboard=True)
