from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_button = [KeyboardButton(text='Назад')]

# --- Main menu ---

currency_button = [KeyboardButton(text='Узнать курс доллара')]
history_button = [KeyboardButton(text='История запросов')]
subscription_button = [KeyboardButton(text='Подписка')]
main_menu = ReplyKeyboardMarkup(keyboard=[currency_button, history_button, subscription_button], resize_keyboard=True)

# --- Sub menu ---

subscribe_button = [KeyboardButton(text='Подписаться')]
unsubscribe_button = [KeyboardButton(text='Отписаться')]
subscription_menu = ReplyKeyboardMarkup(keyboard=[subscribe_button, unsubscribe_button, main_menu_button], resize_keyboard=True)
