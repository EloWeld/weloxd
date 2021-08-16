from aiogram.types import BotCommand

import nav


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        BotCommand("start", "Запустить Велоксда"),
        BotCommand("task", "Получить задание"),
        BotCommand(nav.C_TEXT_BEAUTY, "Режим обработки текста в Zalgo"),
        BotCommand("anime", "Найти аниме себе на вечерок"),
        BotCommand("weather", "Узнать погоду"),
        BotCommand("topmusic", "Найти музыку по душе"),
        BotCommand("unikum", "Погладить ворчунью"),
        BotCommand("donate", "Задонатить на лечение психики"),
        BotCommand("broadcast", "Кричалка на юзеров"),
        BotCommand("help", "Помощь, не скорая, но тоже неплохая")
    ])


async def set_exit_commands(dp):
    await dp.bot.set_my_commands([
        BotCommand("stop", "Выйти из режима")
    ])
