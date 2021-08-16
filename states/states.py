from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.callback_data import CallbackData


class StylistMode(StatesGroup):
    Mode = State()
    Text = State()


class Anime(StatesGroup):
    Anime = State()
    Season = State()
    Episode = State()


class Film(StatesGroup):
    Film = State()


class Broadcast(StatesGroup):
    Enter = State()


class Weather(StatesGroup):
    City = State()


class VKMusic(StatesGroup):
    Login = State()
    Password = State()
    Music = State()