import random

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import InputFile
from loader import dp
from aiogram import types
from middlewares.database import MainDB


@dp.message_handler(Command('topmusic'), )
@dp.message_handler(Text(equals='Музло', ignore_case=True))
async def cmd_task(message: types.Message):
    tracks = MainDB.select_all_tracks()
    random_track_id = random.randrange(0, MainDB.count_all_tracks()[0][0])
    random_track = {'audio': tracks[random_track_id][0],
                    'img': tracks[random_track_id][1],
                    'title': tracks[random_track_id][2],
                    'local': tracks[random_track_id][3] is not None,}
    if random_track['local']:
        print(random_track)
        await message.answer_audio(audio=open(random_track['audio'], "r"),
                                   caption='Услада для ушей ♥',
                                   title=random_track['title'],
                                   thumb=None,
                                   )
    else:
        await message.answer_audio(audio=random_track['audio'],
                                   caption='Услада для ушей ♥',
                                   title=random_track['title'],
                                   thumb=random_track['img'],
                                   )


@dp.message_handler(Command('unikum'))
@dp.message_handler(Text(equals=['Кто молодец?', 'Кто', 'молодец', 'Кто тут у нас умница?'], ignore_case=True))
async def cmd_task(message: types.Message):
    await message.answer_document(document=InputFile('photos/alien.gif'),
                               caption='Вот вверху - умница!',
                               )


@dp.message_handler(Command('unikum'))
@dp.message_handler(Text(equals=['Кто молодец?', 'Кто', 'молодец', 'Кто тут у нас умница?'], ignore_case=True))
async def cmd_task(message: types.Message):
    print()
    place = 57
    await message.answer(f'{place}')