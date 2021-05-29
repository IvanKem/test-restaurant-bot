from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import to_menu
from keyboards.inline.choice_button import choice
from loader import dp


@dp.message_handler(text="Смотреть меню")
@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Меню:")
    await message.answer("Выберите товар из меню ниже",reply_markup=choice)



@dp.message_handler(Text(equals=["Котлетки", "Макарошки", "Пюрешка"]))
async def get_food(message: Message):
    await message.answer(f"Вы выбрали {message.text}. Спасибо", reply_markup=ReplyKeyboardRemove())
