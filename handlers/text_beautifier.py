from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command, Text

import nav
from nav import tabs
from nav.reply_markups import base_menu
from loader import dp
from states import StylistMode

import backend.set_bot_commands


@dp.message_handler(Command(tabs.C_TEXT_BEAUTY))
@dp.message_handler(Text(equals=tabs.TEXT_BEAUTY, ignore_case=True))
async def cmd_text_stylist(message: types.Message):
    await backend.set_bot_commands.set_exit_commands(dp)
    await message.answer('Добро пожаловать в Стилизатор текста! Введите текст для стилизации\n'
                         'Чтобы выйти из режима - команда /stop', reply_markup=nav.exit_menu)
    await StylistMode.Text.set()


@dp.message_handler(state=StylistMode.Text)
async def stylist_mode(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    if message.text == '🛑STOP🛑':
        await state.finish()
        await message.answer('Вы вышли из стилизатора', reply_markup=nav.base_menu)
        return
    backend.Stylist.set_main_text(message.text)
    stylized_list = backend.Stylist.get_stylized()
    for style in stylized_list:
        await message.answer(style)
    await message.answer(f'Ваш текст в разных стилях.', reply_markup=nav.exit_menu)


@dp.message_handler(Command('stop'), state=StylistMode.Text)
@dp.message_handler(Text(equals='🛑STOP🛑'), state=StylistMode.Text)
async def zalgo_stop(message: types.Message, state: FSMContext):
    await message.answer(text='Ты успешно покинул режим Zalgo-фикации', reply_markup=base_menu)
    await backend.set_bot_commands.set_default_commands(dp)
    await state.finish()


@dp.message_handler(state=StylistMode.Text)
async def zalgo_reply(message: types.Message, state: FSMContext):
    text = message.text
    craziness = (await state.get_data())['craziness']
    await state.update_data(text=text)