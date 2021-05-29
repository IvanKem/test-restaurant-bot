from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.default import to_menu
from loader import dp
import logging

from utils.db_api import DBCommands


@dp.message_handler(text="Корзина")
async def show_menu(message: Message):
    await message.answer("Корзина: ", reply_markup=to_menu)


@dp.callback_query_handler(text_contains="bucket")
async def show_menu_from_callback(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f'call={callback_data}')

    message_data = await call.message.answer("Корзина: ", reply_markup=to_menu)
    #user = await DBCommands.get_user(DBCommands, message_data['chat']['id'], message_data['chat']['username'])
    #await call.message.answer(f"Cуп * {user.soup} = {user.soup_price}")