from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

to_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Смотреть меню"),
        ],
        [
            KeyboardButton(text="Корзина"),
            KeyboardButton(text="Помощь"),
        ],
    ],
    resize_keyboard=True
)