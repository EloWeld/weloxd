import random

from aiogram.dispatcher.filters import Command, Text

from src.data.phrases import TASK_LIST
from loader import dp
from aiogram import types


@dp.message_handler(Command('task'), )
@dp.message_handler(Text(equals='Задание', ignore_case=True))
async def cmd_task(message: types.Message):
    await message.answer(random.choice(TASK_LIST) + '\n/task')