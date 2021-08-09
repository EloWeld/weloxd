import random

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import InputFile

from data.phrases import TASK_LIST
from loader import dp
from aiogram import types


@dp.message_handler(Command('topmusic'), )
@dp.message_handler(Text(equals='Музло', ignore_case=True))
async def cmd_task(message: types.Message):
    await message.answer_audio(audio=InputFile('music/mur.mp3'),
                               caption='Услада для ушей ♥',
                               title='Мурчание серокрылого',
                               thumb=InputFile('photos/cat.jpg'))