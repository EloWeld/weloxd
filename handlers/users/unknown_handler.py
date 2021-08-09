from aiogram import types
from loader import dp


@dp.message_handler()
async def cmd_zalgo(message: types.Message):
    await message.reply('Неизвестная команда, сорян')