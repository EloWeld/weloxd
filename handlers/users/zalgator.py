from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command, Text

from keyboards.reply_markups import reply_start_menu, zalgo_menu
from loader import dp
from states import ZalgoMode
from utils.misc.zalgo import get_zalgo
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton

import utils.set_bot_commands


@dp.message_handler(Command("zalgo"))
@dp.message_handler(Text(equals='Zalgo', ignore_case=True))
async def cmd_zalgo(message: types.Message):
    await utils.set_bot_commands.set_exit_commands(dp)
    await message.answer('Добро пожаловать в Zalgo-фикатор! Напишите степень изменения текста\nЧтобы выйти из режима - команда /stop', reply_markup=zalgo_menu)
    await ZalgoMode.Text.set()

@dp.message_handler(Text(equals=['1️⃣', '2️⃣', '3️⃣', '1', '2', '3']), state=ZalgoMode.Text)
async def zalgo_mode(message: types.Message, state: FSMContext):
    craziness = 1 if message.text in ['1️⃣', '1'] else 3 if message.text in ['2️⃣', '2'] else 5 if message.text in ['3️⃣', '3']else 0
    await state.update_data(craziness=craziness)
    await message.answer(f'Уровень безумия: {message.text}')


@dp.message_handler(Command('stop'), state=ZalgoMode.Text)
@dp.message_handler(Text(equals='🛑STOP🛑'), state=ZalgoMode.Text)
async def zalgo_stop(message: types.Message, state: FSMContext):
    await message.answer(text='Ты успешно покинул режим Zalgo-фикации', reply_markup=reply_start_menu)
    await utils.set_bot_commands.set_default_commands(dp)
    await state.finish()


@dp.message_handler(state=ZalgoMode.Text)
async def zalgo_reply(message: types.Message, state: FSMContext):
    text = message.text
    craziness = (await state.get_data())['craziness']
    await state.update_data(text=text)
    await message.answer(get_zalgo(craziness, text, use_super=True, use_sub=True))