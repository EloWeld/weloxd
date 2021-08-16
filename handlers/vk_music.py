from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import dp
import vk_api

from states.states import VKMusic


@dp.message_handler(commands=['vkmusic'])
@dp.message_handler(Text(equals=['Музыка из вк']))
async def cmd_vk_music(message: types.Message):
    await message.answer('Окей, тогда введи сначала свой логин от вк: ', reply_markup=None)
    await VKMusic.Login.set()


@dp.message_handler(state=VKMusic.Login)
async def cmd_vk_music(message: types.Message, state: FSMContext):
    await state.update_data(login=message.text)
    await message.answer('Окей, теперь пароль от вк, не бойся: ', reply_markup=None)
    await VKMusic.Password.set()


@dp.message_handler(state=VKMusic.Password)
async def cmd_vk_music(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)

    try:
        data = await state.get_data()
        login, pass_ = data['login'], data['password']
        session = vk_api.VkApi(login=login, password=pass_)
        session.auth()
    except Exception as e:
        await VKMusic.Login.set()