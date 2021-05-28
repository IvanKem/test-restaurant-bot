from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import buy_callback

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Салат 350р', callback_data=buy_callback.new(
                item_name='salad', quantity='1', price='350'
            )),
            InlineKeyboardButton(text='Cуп 400р', callback_data=buy_callback.new(
                item_name='soup', quantity='1', price='400'
            )),

        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='cancel'),
        ]
    ]

)

go_to_bucket = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Перейти в корзину', callback_data='bucket')
        ]
    ]
)
