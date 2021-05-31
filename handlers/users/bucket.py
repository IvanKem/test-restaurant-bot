from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.default import to_menu
from keyboards.inline import bucket_data, change_bucket
from loader import dp
import logging

from utils.db_api import DBCommands


@dp.message_handler(text="Корзина")
async def show_menu(message: Message):
    message_data = await message.answer("Корзина: ", reply_markup=to_menu)
    user = await DBCommands.get_user(DBCommands, message_data['chat']['id'], message_data['chat']['username'])
    await message.answer(f"Cуп * {user.soup} = {user.soup_price}")


@dp.callback_query_handler(text_contains="bucket")
async def show_menu_from_callback(call: CallbackQuery):
    await call.answer(cache_time=1)
    callback_data = call.data
    logging.info(f'call={callback_data}')

    message_data = await call.message.answer("Корзина: ", reply_markup=to_menu)
    user = await DBCommands.get_user(DBCommands, message_data['chat']['id'], message_data['chat']['username'])
    product_name = 'soup'
    markup = await bucket_data(message_data['chat']['id'], product_name)
    await call.message.answer(f'Суп * {user.soup} = {user.soup_price} руб.', reply_markup=markup)
    product_name = 'salad'
    markup = await bucket_data(message_data['chat']['id'], product_name)
    await call.message.answer(f'Салат* {user.salad} = {user.salad_price} руб.', reply_markup=markup)


@dp.callback_query_handler(change_bucket.filter(product_name='soup'))
async def change_bucket_soup(call: CallbackQuery, callback_data: dict):

    await call.answer(cache_time=1)

    logging.info(f'call={callback_data}')
    add = int(callback_data.get('add'))
    delete = int(callback_data.get('delete'))
    product_name = callback_data.get('product_name')
    message_data = int(callback_data.get('user_id'))
    markup = await bucket_data(message_data, product_name)
    if add == 1:
        await DBCommands.add_soup(DBCommands, message_data, 1, 400)
    if delete == 1:
        await DBCommands.add_soup(DBCommands, message_data, -1, -400)

    user = await DBCommands.get_user(DBCommands, message_data)

    await call.message.edit_text(f'Суп * {user.soup} = {user.soup_price} руб.', reply_markup=markup)


@dp.callback_query_handler(change_bucket.filter(product_name='salad'))
async def change_bucket_soup(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=1)

    logging.info(f'call={callback_data}')
    add = int(callback_data.get('add'))
    delete = int(callback_data.get('delete'))
    product_name = callback_data.get('product_name')
    message_data = int(callback_data.get('user_id'))
    markup = await bucket_data(message_data, product_name)
    if add == 1:
        await DBCommands.add_salad(DBCommands, message_data, 1, 350)
    if delete == 1:
        await DBCommands.add_salad(DBCommands, message_data, -1, -350)

    user = await DBCommands.get_user(DBCommands, message_data)

    await call.message.edit_text(f'Сaлат * {user.salad} = {user.salad_price} руб.', reply_markup=markup)
