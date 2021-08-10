from datetime import datetime

from aiogram import types
from loader import dp
from middlewares.database import MainDB


@dp.message_handler()
async def cmd_zalgo(message: types.Message):
    await message.reply('Неизвестная команда, сорян')
    MainDB.add_message(message)