from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить Велоксда"),
        types.BotCommand("task", "Получить задание"),
        types.BotCommand("zalgo", "Режим обработки текста в Zalgo"),
        types.BotCommand("kitty", "Получить картинку котика")
    ])


async def set_exit_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("stop", "Выйти из режима")
    ])
