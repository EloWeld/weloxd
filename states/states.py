from aiogram.dispatcher.filters.state import StatesGroup, State


class ZalgoMode(StatesGroup):
    Mode = State()
    Text = State()

class Anime(StatesGroup):
    Anime = State()
    Season = State()
    Episode = State()