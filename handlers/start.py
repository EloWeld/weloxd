from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import Message

from filters import IsPrivate
from nav.inline_markups import inline_start_menu
from nav.reply_markups import base_menu
from loader import dp, bot
from middlewares.database import MainDB


@dp.message_handler(Command('start'), IsPrivate())
async def bot_start(message: Message):
    bot_me = await bot.get_me()
    try:
        MainDB.add_user(message.from_user)
    except Exception as e:
        print(e)
    await message.answer(
        f'Эйчики, <b>{message.from_user.full_name}</b>, ты попал в ловушку под названием <b>{bot_me.full_name}</b>!\n\n'
        f'Вот твои данные, отправленные в ФСБ: {message.from_user.full_name}, {message.from_user.id}\n\n'
        f'Надеюсь ты не вражина буржуйская, кстати ниже мой список возможностей\n\n', reply_markup=inline_start_menu)
    await message.answer('...', reply_markup=base_menu)


@dp.message_handler(Command('profiles'))
async def get_profile(message: types.Message):
    users = MainDB.select_all_users()
    print(users)
    answer = ''
    for user_entity in users:
        answer += f'-{users.index(user_entity) + 1}-\n'\
                  f'ID = {user_entity[0]}\n' + \
                  f'UserName = {user_entity[1]}\n' + \
                  f'Subscription = {user_entity[2]}\n\n'
    await message.answer(answer)
