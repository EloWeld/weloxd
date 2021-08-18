from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import InlineKeyboardMarkup, \
    InlineKeyboardButton

import nav
from src.data.phrases import ANIME_LIST, FILM_LIST

from loader import dp
from states.states import Anime, Film


@dp.message_handler(Text(equals='🛑STOP🛑', ignore_case=True))
async def viewer_exit(message: types.Message):
    await message.answer('Вы вернулись в главное меню', reply_markup=nav.base_menu)


@dp.message_handler(Text(equals='🕶Смотрелка🎞', ignore_case=True))
async def viewer_menu(message: types.Message):
    await message.answer(f'Фильм или аниме?', reply_markup=nav.viewer_menu)


@dp.message_handler(Text(equals='😐Фильм😐', ignore_case=True))
async def viewer_film(message: types.Message):
    await message.answer(f'Введи название фильма')

    txt = ''
    for i in range(len(FILM_LIST)):
        txt += f'<b>{str(i + 1)}</b> - {FILM_LIST[i]["caption"]}\n'
    await message.answer(txt)

    await Film.Film.set()


@dp.message_handler(state=Film.Film)
async def film_title(message: types.Message, state: FSMContext):
    msg = message.text

    try:
        await state.update_data(film=int(msg) - 1)
        data = await state.get_data()
        if 'link' in FILM_LIST[data["film"]].keys():
            await message.answer_photo(photo=FILM_LIST[data['film']]['photo'],
                                       caption=f"<b>{FILM_LIST[data['film']]['caption']}</b>\n"
                                               f"♥ Надеемся тебе зайдет ♥\n",
                                       reply_markup=
                                       InlineKeyboardMarkup(row_width=3, inline_keyboard=[
                                           [InlineKeyboardButton(text='Смотреть фильм',
                                                                 url=FILM_LIST[data['film']]['link'])]
                                       ]))
            await state.finish()
    except:
        await message.answer('Введи нормальный ответ!')
        await message.delete()


@dp.message_handler(Text(equals='😎Аниме😎', ignore_case=True))
async def viewer_anime(message: types.Message):
    await message.answer(f'Введи название тайтла')

    txt = ''
    for i in range(len(ANIME_LIST)):
        txt += f'<b>{str(i + 1)}</b> - {ANIME_LIST[i]["caption"]}\n'
    await message.answer(txt, reply_markup=nav.exit_menu)

    await Anime.Anime.set()


@dp.message_handler(state=Anime.Anime)
async def anime_title(message: types.Message, state: FSMContext):
    msg = message.text

    if msg == '🛑STOP🛑':
        await message.answer('Вы вернулись в главное меню', reply_markup=nav.base_menu)
        await state.finish()
        return

    try:
        await state.update_data(anime=int(msg) - 1)
        data = await state.get_data()
        if 'season' in ANIME_LIST[data["anime"]].keys():
            seasons_count = len(ANIME_LIST[data["anime"]]["season"])
            films = [x for x in ANIME_LIST[data["anime"]]["season"] if not x.isdigit()]
            print(films)
            seasons_count -= len(films)
            films_msg = '\n'.join([f'Film - <b><u>{f}</u></b>' for f in films])
            answer = f'<b>{ANIME_LIST[data["anime"]]["caption"]}</b>\n' \
                     f'Теперь введи сезон...[Max - {seasons_count}]\n' + films_msg
            await message.answer(answer)
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
                f'Теперь введи эпизод...[Max = {episodes_count}]')
            await Anime.Episode.set()
    except:
        await message.answer('Введи нормальный ответ!')
        await message.delete()


@dp.message_handler(state=Anime.Season)
async def anime_season(message: types.Message, state: FSMContext):
    msg = message.text

    if msg == '🛑STOP🛑':
        await message.answer('Вы вернулись в главное меню', reply_markup=nav.base_menu)
        await state.finish()
        return

    try:
        await state.update_data(sez=msg)

        data = await state.get_data()
        title = ANIME_LIST[data["anime"]]["caption"]
        if isinstance(ANIME_LIST[data["anime"]]["season"][data["sez"]], type('')):
            await message.answer_photo(photo=ANIME_LIST[data['anime']]['photo'],
                                       caption=f"<b>{ANIME_LIST[data['anime']]['caption']}</b>\n"
                                               f"Фильм: <b>{data['sez']}</b>\n"
                                               f"♥ Смотри на здоровье ♥",
                                       reply_markup=
                                       InlineKeyboardMarkup(inline_keyboard=[
                                           [InlineKeyboardButton(text='Смотреть аниме',
                                                                 url=ANIME_LIST
                                                                 [data['anime']]
                                                                 ['season']
                                                                 [data['sez']])]
                                       ]))
            await state.finish()
            return
        episodes_count = len(ANIME_LIST[data["anime"]]["season"][data["sez"]])
        await message.answer(
            f'<b>{title}</b>\n'
            f'Сезон: <b>{msg}</b>\n'
            f'Теперь введи эпизод...[Max = {episodes_count}]', reply_markup=nav.exit_menu)

        await Anime.Episode.set()
    except:
        await message.answer('Введи нормальный ответ!')
        await message.delete()


@dp.message_handler(state=Anime.Episode)
async def anime_episode(message: types.Message, state: FSMContext):
    msg = message.text
    if msg == '🛑STOP🛑':
        await message.answer('Вы вернулись в главное меню', reply_markup=nav.base_menu)
        await state.finish()
        return

    await state.update_data(ep=msg)
    data = await state.get_data()

    try:
        if 'season' in ANIME_LIST[data["anime"]].keys():
            await message.answer_photo(photo=ANIME_LIST[data['anime']]['photo'],
                                       caption=f"<b>{ANIME_LIST[data['anime']]['caption']}</b>\n"
                                               f"Сезон: <b>{data['sez']}</b>\n"
                                               f"Эпизод: <b>{data['ep']}</b>\n"
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
                                               f"Эпизод: <b>{data['ep']}</b>\n"
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