from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import change_bucket
from utils.db_api import DBCommands


def make_callback_data(user_id, product_name, add, delete):
    return change_bucket.new(user_id=user_id, product_name=product_name, add=add, delete=delete)


async def bucket_data(user_id, product_name):
    markup = InlineKeyboardMarkup()

    markup.row(
        InlineKeyboardButton(
            text='+1', callback_data=make_callback_data(user_id=user_id, product_name=product_name, add=1, delete=0)),
        InlineKeyboardButton(
            text='-1', callback_data=make_callback_data(user_id=user_id, product_name=product_name, add=0, delete=1)),
    )

    return markup
