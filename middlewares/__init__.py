from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware
from .database import Database


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
