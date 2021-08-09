import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery, Message

from filters import IsPrivate
from handlers.users.help import cmd_help
from handlers.users.send_kitties import cmd_kitty
from handlers.users.task import cmd_task
from handlers.users.zalgator import cmd_zalgo
from keyboards.inline_markups import inline_start_menu
from keyboards.reply_markups import reply_start_menu
from loader import dp, bot
from utils.db_api import User



@dp.message_handler(Command('start'), IsPrivate())
async def bot_start(message: Message):
    conn = sqlite3.connect('Data.db')
    cur = conn.cursor()
    cur.execute(f'INSERT INTO users VALUES("{message.from_user.id}", "@{message.from_user.username}")')
    conn.commit()

    bot_me = await bot.get_me()
    await message.answer(f'Эйчики, <b>{message.from_user.full_name}</b>, ты попал в ловушку под названием <b>{bot_me.full_name}</b>!\n\n'
                         f'Вот твои данные, отправленные в ФСБ: {message.from_user.full_name}, {message.from_user.id}\n\n'
                         f'Надеюсь ты не вражина буржуйская, кстати ниже мой список возможностей\n\n', reply_markup=inline_start_menu)
    await message.answer('...', reply_markup=reply_start_menu)


@dp.message_handler(Command('profile'))
async def get_profile(message: types.Message):
    conn = sqlite3.connect('Data.db')
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM users WHERE USER_ID = "{message.from_user.id}"')
    result = cur.fetchall()
    await message.answer(f'ID = {list(result[0])[0]}\nUserName = {[list(result[0])[1]][0]}')