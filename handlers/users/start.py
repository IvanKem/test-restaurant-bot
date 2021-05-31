from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import to_menu
from loader import dp
from utils.db_api import DBCommands


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    message_data = await message.answer(
        f"Привет, {message.from_user.first_name}! Я бот для заказа еды. Посмотри меню чтобы определиться с заказом)",
        reply_markup=to_menu)
    print(message_data)
    await DBCommands.get_user(DBCommands, message_data['chat']['id'], message_data['chat']['username'])
