from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
@dp.message_handler(text='Помощь')
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Вернуться в главное меню",
            "/help - Получить справку",
            "/menu - Посмотреть меню",
            "",
            "Если что-то не понятно или ",
            "есть какие-то вопросы пишите ",
            "на почту: example@mail.ru",

            )
    
    await message.answer("\n".join(text))
