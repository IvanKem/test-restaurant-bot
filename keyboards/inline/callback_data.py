from aiogram.utils.callback_data import CallbackData

buy_callback = CallbackData('buy', 'item_name', 'quantity', 'price')

change_bucket = CallbackData('change', 'user_id', 'product_name', 'add', 'delete')

update_bucket = CallbackData('update', 'user_id', 'update')

order_approwing = CallbackData('order', 'user_id', 'order')