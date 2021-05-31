from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import to_menu
from keyboards.inline.choice_button import salad, soup, cancel
from loader import dp


@dp.message_handler(text="Смотреть меню")
@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Меню:")
    await message.answer("Выберите товар из меню ниже")
    await message.answer_photo(photo='https://kylinariya.ru/wp-content/uploads/2021/02/1-9-21.jpg',
                               caption='<b>Суп Lohikeitto</b>,\nон же уха по-фински, одно из самых нежных и вкусных '
                                       'первых блюд. Его ключевой ингредиент – мясо красной рыбы разных сортов. '
                                       'Традиционно используется форель, лосось, сёмга или кета. '
                                       'А нежирные сливки, которые добавляются в суп, делают его вкус мягким, '
                                       'а цвет приятно светлым.',
                               reply_markup=soup)

    await message.answer_photo(photo='http://only-holiday.ru/wp-content/uploads/2014/09/%D1%86%D0%B5%D0%B7%D0%B0%D1%80%D1%8C-%D1%81-%D1%87%D0%B5%D1%80%D1%80%D0%B8.jpg',
                               caption='<b>Салат Цезарь</b>,\nодин из самых популярных закусок в мире. Сочные салатные '
                                       'листья, ароматные кусочки куриной грудки и хрустящие сухарики делают его нежным'
                                       'и сытным. А пикантный соус добавляет блюду невероятный аромат и вкус.',
                               reply_markup=salad)

    await message.answer(reply_markup=cancel)


