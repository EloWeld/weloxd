from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import InputFile, Message

import nav
from filters import IsAdmin, IsPrivate
from loader import dp, bot
from aiogram import types

from middlewares.database import MainDB
from states.states import Broadcast
from backend.helpers import del_message


@dp.message_handler(Command('broadcast'), IsPrivate())
@dp.message_handler(Text(equals=['Кричать', 'Орать', 'Визжать', 'Пиздеть', 'Кричалка на юзеров']), IsPrivate())
async def broadcast(message: Message):
    if message.from_user.id not in MainDB.users_ids():
        await message.answer('Для того чтобы кричать, нужно сначала зарегаться в боте, просто пропиши:\n/start')
        return

    if message.from_user.id in MainDB.get_banned_users():
        await message.answer('Пхаха, чел, ты в муте, варешку свою будешь открывать на рынке')
        return

    await message.answer('Напиши, что ты хотел всем сказать, я слушаю...', reply_markup=nav.broadcasting_menu)
    await Broadcast.Enter.set()


@dp.message_handler(state=Broadcast.Enter)
async def broadcast(message: types.Message, state: FSMContext):
    users = MainDB.select_all_users()
    if message.text == '🌼 Закрыть варежку и сдохнуть 🌸':
        await message.answer('📞Поздравляю, твоё ебало сжато и скомпрессированно до минимума 🔇 \n'
                             'В деревне теперь тихо и спокойно без такого долбоёба как ты, который просто рот открыл '
                             'и закрыл, ну ты и попуск короче :/', reply_markup=nav.base_menu)
        await state.finish()
        return
    if message.text[0] == '/':
        await message.answer('💢ಠ_ಠ💢\n'
                             '😡Ага, Хацкер хуев, ещё раз так пошутишь я тебя пиздану и в бан отправлю!💢\n'
                             '😝Команды будешь на рынке вводить, а тут деревня! Приличная община!😇', reply_markup=nav.base_menu)
        await state.finish()
        return
    print(users)
    for user_entity in users:
        await bot.send_message(chat_id=user_entity[0], text=f'Кот {message.from_user.full_name} прокричал на всю деревню: \n<b>{message.text}</b>')

    msg = await message.answer('Твоё сообщение разосланно этим никам: ' + ', '.join([f"@{x[1]}" for x in users]), reply_markup=nav.base_menu)
    await state.finish()

    await del_message(msg, 500)



