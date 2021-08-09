import sqlite3

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp
from aiogram import types
import random
from data.phrases import KITTY_LIST


@dp.message_handler(Command('kitty'))
@dp.message_handler(Text(equals='Котики', ignore_case=True))
async def cmd_kitty(message: types.Message):
    
    photo_url = f'https://chance2.ru/photo/img/skachat-foto-kotiat-{random.randrange(1, 22)}.jpg'
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo=photo_url,
                            caption=f"{random.choice(KITTY_LIST)}\n/kitty"
                            )
