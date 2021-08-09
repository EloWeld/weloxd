from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery, ContentType, InlineKeyboardMarkup, \
    InlineKeyboardButton, MessageEntity
from aiogram.utils.emoji import emojize
from data.phrases import ANIME_LIST

from loader import dp, bot
from states.states import Anime


@dp.message_handler(Text(equals='Аниме', ignore_case=True))
async def anime(message: types.Message):
    await message.answer(f'Enter your title number...')

    txt = ''
    for i in range(len(ANIME_LIST)):
        txt += f'<b>{str(i + 1)}</b> - {ANIME_LIST[i]["caption"]}\n'
    await message.answer(txt)

    await Anime.Anime.set()


@dp.message_handler(state=Anime.Anime)
async def anime_title(message: types.Message, state: FSMContext):
    msg = message.text
    await state.update_data(anime=int(msg) - 1)

    data = await state.get_data()

    try:
        if 'season' in ANIME_LIST[data["anime"]].keys():
            seasons_count = len(ANIME_LIST[data["anime"]]["season"])
            await message.answer(f'<b>{ANIME_LIST[data["anime"]]["caption"]}</b>\n'
                                 f'Now enter season...[Max - {seasons_count}]')
            await Anime.Season.set()
        elif 'link' in ANIME_LIST[data["anime"]].keys():
            await message.answer_photo(photo=ANIME_LIST[data['anime']]['photo'],
                                       caption=f"<b>{ANIME_LIST[data['anime']]['caption']}</b>\n"
                                               f"♥ Надеемся тебе зайдет ♥\n",
                                       reply_markup=
                                       InlineKeyboardMarkup(row_width=3, inline_keyboard=[
                                           [InlineKeyboardButton(text='Смотреть аниме',
                                                                 url=ANIME_LIST[data['anime']]['link'])]
                                       ]))
            await state.finish()
        elif 'episodes' in ANIME_LIST[data["anime"]].keys():
            title = ANIME_LIST[data["anime"]]["caption"]
            episodes_count = len(ANIME_LIST[data["anime"]]["episodes"])
            await message.answer(
                f'<b>{title}</b>\n'
                f'Now enter episode...[Max = {episodes_count}]')
            await Anime.Episode.set()
    except:
        await message.answer('Введи нормальный ответ!')
        await message.delete()


@dp.message_handler(state=Anime.Season)
async def anime_season(message: types.Message, state: FSMContext):
    msg = message.text
    await state.update_data(sez=msg)

    data = await state.get_data()

    try:
        title = ANIME_LIST[data["anime"]]["caption"]
        episodes_count = len(ANIME_LIST[data["anime"]]["season"][data["sez"]])
        await message.answer(
            f'<b>{title}</b>\n'
            f'Season: <b>{msg}</b>\n'
            f'Now enter episode...[Max = {episodes_count}]')

        await Anime.Episode.set()
    except:
        await message.answer('Введи нормальный ответ!')
        await message.delete()


@dp.message_handler(state=Anime.Episode)
async def anime_episode(message: types.Message, state: FSMContext):
    msg = message.text
    await state.update_data(ep=msg)

    data = await state.get_data()

    try:
        if 'season' in ANIME_LIST[data["anime"]].keys():
            await message.answer_photo(photo=ANIME_LIST[data['anime']]['photo'],
                                       caption=f"<b>{ANIME_LIST[data['anime']]['caption']}</b>\n"
                                               f"Season: <b>{data['sez']}</b>\n"
                                               f"Episode: <b>{data['ep']}</b>\n"
                                               f"♥ Смотри на здоровье ♥",
                                       reply_markup=
                                       InlineKeyboardMarkup(row_width=3, inline_keyboard=[
                                           [InlineKeyboardButton(text='Смотреть аниме',
                                                                 url=ANIME_LIST
                                                                 [data['anime']]
                                                                 ['season']
                                                                 [data['sez']]
                                                                 [int(data['ep']) - 1])]
                                       ]))
            await state.finish()
        elif 'episodes' in ANIME_LIST[data["anime"]].keys():
            await message.answer_photo(photo=ANIME_LIST[data['anime']]['photo'],
                                       caption=f"<b>{ANIME_LIST[data['anime']]['caption']}</b>\n"
                                               f"Episode: <b>{data['ep']}</b>\n"
                                               f"♥ Смотри на здоровье ♥",
                                       reply_markup=
                                       InlineKeyboardMarkup(row_width=3, inline_keyboard=[
                                           [InlineKeyboardButton(text='Смотреть аниме',
                                                                 url=ANIME_LIST
                                                                 [data['anime']]
                                                                 ['episodes']
                                                                 [int(data['ep']) - 1])]
                                       ]))
            await state.finish()
    except:
        await message.answer('Введи нормальный ответ!')
        await message.delete()


@dp.message_handler(Command('asdasd'))
async def anime_episodeas(message: types.Message, state: FSMContext):
    data = await state.get_data()
    try:
        await state.update_data(episode=data['episode'] + 1)
    except:
        await state.update_data(episode=1)
