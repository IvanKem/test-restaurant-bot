from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.default import to_menu
from keyboards.inline import bucket_data, change_bucket, update_bucket, order_approwing
from keyboards.inline.bucket_button import bucket_sum_update, order_approw
from loader import dp
import logging

from utils.db_api import database

db = database.DBCommands()


@dp.callback_query_handler(update_bucket.filter(update='clean_bucket'))
async def clean_bucket(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=1)
    logging.info(f'call={callback_data}')
    user_id = int(callback_data.get('user_id'))
    await db.clean_bucket(user_id)
    await call.message.answer(text='В вашей корзине пусто, закажите что-нибудь)')


@dp.message_handler(text="Корзина")
async def show_menu(message: Message):
    message_data = await message.answer("Корзина: ", reply_markup=to_menu)
    user = await db.get_user(message_data['chat']['id'], message_data['chat']['username'])

    if user.soup == 0 and user.salad == 0:
        await message.answer(text='В вашей корзине пусто, закажите что-нибудь)')
    else:
        product_name = 'soup'
        markup = await bucket_data(message_data['chat']['id'], product_name)
        if user.soup != 0:
            await message.answer(f'Суп * {user.soup} = {user.soup_price} руб.', reply_markup=markup)
        product_name = 'salad'
        markup = await bucket_data(message_data['chat']['id'], product_name)
        if user.salad != 0:
            await message.answer(f'Салат * {user.salad} = {user.salad_price} руб.', reply_markup=markup)
        sum_price = await db.bucket_sum_get(message_data['chat']['id'])
        markup = await bucket_sum_update(message_data['chat']['id'])
        await message.answer(f'Стоимость всего заказа {sum_price} руб.', reply_markup=markup)


@dp.callback_query_handler(order_approwing.filter(order='cancel_order'))
@dp.callback_query_handler(text_contains="bucket")
async def show_menu_from_callback(call: CallbackQuery):
    await call.answer(cache_time=1)
    callback_data = call.data
    logging.info(f'call={callback_data}')

    message_data = await call.message.answer("Корзина: ", reply_markup=to_menu)
    user = await db.get_user(message_data['chat']['id'], message_data['chat']['username'])

    if user.soup == 0 and user.salad == 0:
        await call.message.answer(text='В вашей корзине пусто, закажите что-нибудь)')
    else:
        product_name = 'soup'
        markup = await bucket_data(message_data['chat']['id'], product_name)
        if user.soup != 0:
            await call.message.answer(f'Суп * {user.soup} = {user.soup_price} руб.', reply_markup=markup)
        product_name = 'salad'
        markup = await bucket_data(message_data['chat']['id'], product_name)
        if user.salad != 0:
            await call.message.answer(f'Салат * {user.salad} = {user.salad_price} руб.', reply_markup=markup)

        sum_price = await db.bucket_sum_get(db, message_data['chat']['id'])
        markup = await bucket_sum_update(message_data['chat']['id'])
        await call.message.answer(f'Стоимость всего заказа {sum_price} руб.', reply_markup=markup)


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
        await db.add_soup(message_data, 1, 400)
    if delete == 1:
        await db.add_soup(message_data, -1, -400)

    user = await db.get_user(message_data)
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
        await db.add_salad(message_data, 1, 350)
    if delete == 1:
        await db.add_salad(message_data, -1, -350)

    user = await db.get_user(message_data)

    await call.message.edit_text(f'Сaлат * {user.salad} = {user.salad_price} руб.', reply_markup=markup)


@dp.callback_query_handler(update_bucket.filter(update='update'))
async def update_sum_bucket(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=1)
    logging.info(f'call={callback_data}')
    user_id = int(callback_data.get('user_id'))

    sum_price = await db.bucket_sum_get(user_id)
    markup = await bucket_sum_update(user_id)
    await call.message.edit_text(f'Стоимость всего заказа {sum_price} руб.', reply_markup=markup)


@dp.callback_query_handler(order_approwing.filter(order='order'))
async def update_sum_bucket(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=1)
    logging.info(f'call={callback_data}')
    user_id = int(callback_data.get('user_id'))
    await call.message.answer(text='Подтвердите данные о заказе:')
    user = await db.get_user(user_id)
    markup = await order_approw(user_id)
    await call.message.answer(
        f'Cуп по-фински (цена 400 руб за шт),\n количество {user.soup}, стоимостью {user.soup_price} руб.\n\n'
        f'Cалат цезарь (цена 350 руб за шт),\n количество {user.salad}, стоимостью {user.salad_price} руб.\n\n'
        f'Общая стоимость заказа - {user.sum_price} руб.',
        reply_markup=markup)


@dp.callback_query_handler(order_approwing.filter(order='approw_order'))
async def approw_order(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=1)
    logging.info(f'call={callback_data}')
    user_id = int(callback_data.get('user_id'))
    user = await db.get_user(user_id)
    await db.create_new_purchase(user.username, user.soup,  user.salad,
                                         user.salad_price, user.soup_price, user.sum_price)
    await call.message.answer(text='Новый заказ успешно создан и сохранен в базе данных')
    await db.clean_bucket(user_id)



