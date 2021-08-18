from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import nav
from filters import IsAdmin
from middlewares.database import MainDB

from loader import dp


class BanMode(StatesGroup):
    User = State()


@dp.message_handler(Command('ban'))
async def cmd_ban(message: types.Message):
    users = [f'@{user[1]}' for user in MainDB.select_all_users()]

    users_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(user) for user in users]])
    users_keyboard.add(KeyboardButton('🛑STOP🛑'))

    await message.answer('Все юзеры: ' + ', '.join(users), reply_markup=users_keyboard)
    await BanMode.User.set()


@dp.message_handler(IsAdmin(), Text('🛑STOP🛑'), state=BanMode.User)
async def cmd_ban_input(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f'Вы вернулись в главное меню', reply_markup=nav.base_menu)


@dp.message_handler(IsAdmin(), state=BanMode.User)
async def cmd_ban_input(message: types.Message, state: FSMContext):
    admin_input = message.text

    if admin_input[1:] in [x[1] for x in MainDB.select_all_users()]:
        user = MainDB.userturple_by_username(admin_input[1:])
        user_bans = user[0][3]
        await message.reply(f'Этому юзверю начислено предупреждение, теперь у него [{user_bans + 1}/5]');
        MainDB.update_ban(user[0][0], user_bans + 1)
    await state.finish()


def ban_by_id(id):
    user = MainDB.userturple_by_id(id)
    user_bans = user[0][3]
    MainDB.update_ban(id, user_bans + 1)
