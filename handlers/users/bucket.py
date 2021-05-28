from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.default import to_menu
from loader import dp
import logging


@dp.message_handler(text="Корзина")
async def show_menu(message: Message):
    await message.answer("Корзина: ", reply_markup=to_menu)


@dp.callback_query_handler(text_contains="bucket")
async def show_menu_from_callback(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f'call={callback_data}')

    await call.message.answer("Корзина: ", reply_markup=to_menu)
