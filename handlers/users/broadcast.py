import random

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import InputFile, Message

from data.phrases import TASK_LIST
from filters import IsAdmin, IsPrivate
from keyboards.reply_markups import reply_start_menu
from loader import dp, bot
from aiogram import types

from middlewares.database import MainDB
from states.states import Broadcast


@dp.message_handler(Command('broadcast'), IsPrivate())
@dp.message_handler(Text(equals=['Кричать', 'Орать', 'Визжать', 'Пиздеть', 'Покричать на всех']), IsPrivate())
async def broadcast(message: Message):
    if message.from_user.id in MainDB.get_banned_users():
        await message.answer('Пхаха, чел, ты в муте, варешку свою будешь открывать на рынке')
        return

    await message.answer('Напиши, что ты хотел всем сказать, я слушаю...', reply_markup=None)
    await Broadcast.Enter.set()


@dp.message_handler(state=Broadcast.Enter)
async def broadcast(message: types.Message, state: FSMContext):
    users = MainDB.select_all_users()

    for user_entity in users:
        await bot.send_message(chat_id=user_entity[0], text=f'Кот {message.from_user.full_name} прокричал на всю деревню: \n<b>{message.text}</b>')

    await message.answer('Твоё сообщение разосланно этим никам: ' + ', '.join([x[1] for x in users]), reply_markup=reply_start_menu)

    await state.finish()



