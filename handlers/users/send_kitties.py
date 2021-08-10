import sqlite3

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp
from aiogram import types
import random
from data.phrases import KITTY_LIST
from middlewares.database import MainDB


@dp.message_handler(Command('kitty'))
@dp.message_handler(Text(equals='Котики', ignore_case=True))
async def cmd_kitty(message: types.Message):

    s = random.randrange(0, MainDB.count_all_kitty()[0][0] - 1)
    photo_url = MainDB.select_all_kitty()[s][0]
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo=photo_url,
                            caption=f"{random.choice(KITTY_LIST)}\n/kitty"
                            )
