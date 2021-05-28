from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "В главное меню"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("menu", "Открыть меню"),

        ]
    )
