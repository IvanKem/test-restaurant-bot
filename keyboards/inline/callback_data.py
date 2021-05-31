from aiogram.utils.callback_data import CallbackData

buy_callback = CallbackData('buy', 'item_name', 'quantity', 'price')

change_bucket = CallbackData('change', 'user_id','product_name', 'add', 'delete')
