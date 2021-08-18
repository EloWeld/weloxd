from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import InputFile, Message

import nav
from filters import IsAdmin, IsPrivate
from handlers.admin import ban_by_id
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

    user_turp = MainDB.userturple_by_id(str(message.from_user.id))
    user_bans = user_turp[0][3]
    if user_bans >= 5:
        await message.answer(
            f'Пхахах, чел, ты в муте :) Из деревни тебя депортировали на луну, потому что у тебя {user_bans} предупреждений')
        return

    await message.answer('Напиши, что ты хотел всем сказать, я слушаю...', reply_markup=nav.broadcasting_menu)
    await Broadcast.Enter.set()


@dp.message_handler(state=Broadcast.Enter)
async def broadcast(message: types.Message, state: FSMContext):
    users = MainDB.select_all_users()

    user_turp = MainDB.userturple_by_id(str(message.from_user.id))
    user_bans = user_turp[0][3]

    if message.text == '🌼 Закрыть варежку и сдохнуть 🌸':
        await message.answer('📞Поздравляю, твоё ебало сжато и скомпрессированно до минимума 🔇 \n'
                             'В деревне теперь тихо и спокойно без такого долбоёба как ты, который просто рот открыл '
                             'и закрыл, ну ты и попуск короче :/', reply_markup=nav.base_menu)
        await state.finish()
        return
    if message.text[0] == '/':
        ban_by_id(message.from_user.id)

        user_turp = MainDB.userturple_by_id(str(message.from_user.id))
        user_bans = user_turp[0][3]

        await message.answer(f'💢ಠ_ಠ💢\n'
                             f'😡Ага, Хацкер хуев, ещё раз так пошутишь я тебя пиздану и в бан отправлю!💢\n'
                             f'У тебя итак уже [{user_bans}/5] предупреждений! Аккуратней с языком!\n'
                             f'😝Команды будешь на рынке вводить, а тут деревня! Приличная община!😇', reply_markup=nav.base_menu)
        await state.finish()
        return
    print(users)
    for user_entity in users:
        await bot.send_message(chat_id=user_entity[0], text=f'Кот {message.from_user.full_name} прокричал на всю деревню: \n<b>{message.text}</b>')

    msg = await message.answer('Твоё сообщение разосланно этим никам: ' + ', '.join([f"@{x[1]}" for x in users]), reply_markup=nav.base_menu)
    await state.finish()

    await del_message(msg, 500)



