from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text

import cmath, nav, os, requests

from loader import dp, bot
from states.states import Weather


@dp.message_handler(Command('weather'))
@dp.message_handler(Text(equals='Погода'))
async def cmd_weather(message: types.Message):
    await message.answer('Скажи город в котором хочешь узнать, сваляться ли лягухи с неба:',
                         reply_markup=nav.reply_markups.cities_menu)
    await Weather.City.set()


def get_weather_from_json(data):
    result = dict()
    result['description'] = data['weather'][0]['description']
    result['temp'] = data['main']['temp']
    result['temp_min'] = data['main']['temp_min']
    result['temp_max'] = data['main']['temp_max']
    result['humidity'] = data["main"]["humidity"]
    result['pressure'] = data["main"]["pressure"]
    result['wind'] = data["wind"]["speed"]
    result['sunrise'] = str(datetime.fromtimestamp(data["sys"]["sunrise"])).split(' ')[1]
    result['sunset'] = str(datetime.fromtimestamp(data["sys"]["sunset"])).split(' ')[1]
    result['length_of_the_day'] = datetime.fromtimestamp(
        data["sys"]["sunset"]) - datetime.fromtimestamp(
        data["sys"]["sunrise"])

    return result


@dp.message_handler(state=Weather.City)
async def state_weather(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(city=text)

    city = text
    appid = os.getenv("WEATHER_APPID")
    weather_req = requests.get(f'http://api.openweathermap.org/data/2.5/weather',
                               params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})

    weather = get_weather_from_json(weather_req.json())
    try:
        await message.answer(f'Итак, сегодня тебя ждёт погода:\n'
                             f'<b>{str(weather["description"]).capitalize()}</b>\n'
                             f'<b>Темпа {int(weather["temp"])}(От {weather["temp_min"]} до {weather["temp_max"]}</b>\n'
                             f'<b>Рассвет в {weather["sunrise"]}</b>\n'
                             f'<b>Закат в {weather["sunset"]}</b>\n'
                             f'<b>Ветерок {weather["wind"]}</b> м/с\n'
                             f'<b>Влажность {weather["humidity"]}</b> пох\n'
                             f'<b>Давление {weather["pressure"]}</b> атмосфер\n'
                             f'<b>Протяженность дня {weather["length_of_the_day"]}</b>\n')

        await message.answer(f'Тоби {cmath.pi}зда, сегодня в городе дождь из гробов с Hello Kitty',
                             reply_markup=nav.reply_markups.base_menu)
    except Exception as e:
        await message.answer(f'ЖАРКО КАК В АДУ!' + e)
    await state.finish()
