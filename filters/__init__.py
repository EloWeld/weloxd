from aiogram import Dispatcher

from .private_chat import IsPrivate
from .groups import IsGroup
from .admins import IsAdmin


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsGroup)
    pass
