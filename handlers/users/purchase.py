import logging

from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.default import to_menu
from keyboards.inline import buy_callback
from keyboards.inline.choice_button import choice, go_to_bucket
from loader import dp


@dp.callback_query_handler(buy_callback.filter(item_name='salad'))
async def buying_salad(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'call={callback_data}')
    quantity = callback_data.get('quantity')
    price = callback_data.get('price')

    await call.message.answer(f'Салат стоимостью {price}р, добавлен в корзину ({quantity})', reply_markup=go_to_bucket)


@dp.callback_query_handler(buy_callback.filter(item_name='soup'))
async def buying_soup(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'call={callback_data}')
    quantity = callback_data.get('quantity')
    price = callback_data.get('price')

    await call.message.answer(f'Суп, стоимостью {price}р, добавлен в корзину ({quantity}) ', reply_markup=go_to_bucket)


@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f'call={callback_data}')

    await call.message.answer("Вы в главном меню", reply_markup=to_menu)