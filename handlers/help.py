from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text

from loader import dp


@dp.message_handler(Command('help'))
@dp.message_handler(Text(equals='Помощь', ignore_case=True))
async def cmd_help(message: types.Message):
    text = [
        'Возможности: ',
        '/start - Главное меню',
        '/help - Получить справку',
        '/kitty - КОТИКИИИ!!! =^_^=',
        '/zalgo - Убей свой текст',
        '/topmusic - Ублажи свои ушные раковины',
        '/task - Получить задание',
    ]
    await message.answer('\n'.join(text))
